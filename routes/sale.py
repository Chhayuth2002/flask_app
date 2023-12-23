from app import app, engine, jsonify, Sale
from sqlalchemy.orm import sessionmaker


def sale_to_json(sale):
    return {
        'sale_id': sale.sale_id,
        'date': sale.date.strftime('%Y-%m-%d %H:%M:%S'),
        'price': float(sale.price),
        'customer_id': sale.customer_id,
    }

@app.route('/api/sale', methods=['GET'])
def get_sales():
    Session = sessionmaker(bind=engine)
    session = Session()
    
    sales = session.query(Sale).all()
    
    session.close()
    
    return jsonify([sale_to_json(sale) for sale in sales])