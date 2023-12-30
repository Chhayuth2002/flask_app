from app import app, render_template, request, text


@app.route('/admin')
def dashboard():
    return render_template('admin/dashboard.html')


@app.route('/admin/product')
def product():
    return render_template('admin/product.html')


@app.route('/admin/category')
def category():
    return render_template('admin/category.html')


@app.route('/admin/sale')
def sale():
    return render_template('admin/sale.html')


@app.route('/admin/customer')
def customer():
    return render_template('admin/customer.html')
