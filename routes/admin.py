from app import app, render_template, request, text


@app.route('/admin')
def admin():
    return render_template('admin/dashboard/index.html')

@app.route('/admin/product')
def product():
    return render_template('admin/product/index.html')

@app.route('/admin/product_form')
def product_form():
    return render_template('admin/product/form.html')

@app.route('/admin/category')
def category():
    return render_template('admin/category/index.html')

@app.route('/admin/category_form')
def category_form():
    return render_template('admin/category/form.html')


@app.route('/admin/sale')
def sale():
    return render_template('admin/sale/index.html')


