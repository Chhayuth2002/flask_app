import pdfkit
import os
from datetime import datetime
from app import app, render_template, text, engine, request, Response, Sale, SaleDetail
from sqlalchemy import insert
import json


@app.route('/pos')
def pos_index():
    return render_template('pos_screen.html')


@app.route("/pdf")
def index_pdf():
    sale_id = request.args.get('sale_id')

    directory = os.path.join(os.getcwd(), 'pdf')

    file_path = os.path.join(directory, 'invoice.pdf')

    with engine.connect() as con:
        sale_list = con.execute(
            text(f"""
                SELECT sd.*, p.product_name, s.date as sale_date
                FROM sale_detail sd
                JOIN product p ON sd.product_id = p.product_id
                JOIN sale s ON sd.sale_id = s.sale_id
                WHERE sd.sale_id = 16;
            """))
        con.commit
    now = datetime.now()
    created_at = now.strftime("%Y-%m-%d %H:%M")
    server_url = request.url_root
    html = render_template("invoice.html", data=sale_list,
                           now=created_at, server_url=server_url)
    options = {
        'page-height': '10in',
        'page-width': '3in',
        'margin-top': '0.1in',
        'margin-right': '0in',
        'margin-bottom': '0.1in',
        'margin-left': '0in',
    }

    config = pdfkit.configuration(
        wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')

    pdf = pdfkit.from_string(
        html, file_path, options, configuration=config)
    pdf_preview = pdfkit.from_string(
        html, '', options, configuration=config)
    return Response(pdf_preview, mimetype="application/pdf")


@app.route('/pos/createSale', methods=['post'])
def createSale():
    total_price = request.form.get('total_price')
    received_amount = request.form.get('received_amount')
    selected_product = request.form.get('selected_product')

    selected_product_obj = json.loads(selected_product)

    with engine.connect() as con:
        # result = con.execute(query, total_price=total_price)
        stmt = insert(Sale).values(date=datetime.now(),
                                   customer_id=1, price=total_price)
        saleRes = con.execute(stmt)
        sale_id = saleRes.lastrowid
        con.commit()
        for item in selected_product_obj:
            product_id = item['product_id']
            qty = item['qty']
            price = item['price']

            stmtS = insert(SaleDetail).values(sale_id=sale_id,
                                              product_id=product_id, qty=qty, price=price)
            con.execute(stmtS)
            con.commit()

        current_sale = con.execute(
            text(f"select * from sale where sale_id={sale_id}"))

        current_sale_detail = con.execute(text(
            f"select sale_detail.* , product.product_name from sale_detail join product on sale_detail.product_id = product.product_id where sale_detail.sale_id={
                sale_id};"
        ))

        print(current_sale)
        print(current_sale_detail)

        con.commit

        html = (
            "<strong>"
        )

    return [{'status': 'success', 'sale_id': sale_id}]


@app.route('/getAllProduct')
def getAllProduct():
    try:
        con = engine.connect()

        products = con.execute(text(
            'SELECT product.*, category.* FROM product JOIN category ON product.category_id = category.category_id ;'))
        categories = con.execute(text('SELECT * from category;'))
        con.commit()
        category_list = [{'id': category.category_id,
                          'name': category.category_name} for category in categories]

        product_list = []
        for product in products:
            product_list.append(
                {
                    'product_id': product.product_id,
                    'name': product.product_name,
                    'discount': product.discount,
                    'price': product.price,
                    'image': product.image,
                    'category_name': product.category_name,
                    'category_id': product.category_id,
                }
            )

        result = [
            product_list,
            category_list
        ]

        return result
    except Exception as e:
        return f'Error: {str(e)}', 500
    finally:
        con.close()
