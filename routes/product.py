from app import app, request, engine, jsonify, Product, Category
from sqlalchemy.orm import sessionmaker
from routes.category import category_to_json


# Function to convert Product object to JSON
def product_to_json(product):
    return {
        'product_id': product.product_id,
        'product_name': product.product_name,
        'price': float(product.price),
        'discount': float(product.discount),
        'image': product.image,
        'status': product.status,
        'category_id': product.category_id
    }


# Routes
@app.route('/api/product', methods=['GET'])
def get_products():
    Session = sessionmaker(bind=engine)
    session = Session()

    products = session.query(Product).all()

    product_list = []

    for product in products:
        product_json = product_to_json(product)

        product_json['category'] = product.category.category_name if product.category else None
        product_list.append(product_json)

    session.close()

    return jsonify(product_list)


@app.route('/api/product', methods=['POST'])
def add_product():
    data = request.json
    new_product = Product(
        product_name=data['product_name'],
        price=data['price'],
        discount=data['discount'],
        image=data['image'],
        status=data['status'],
        category_id=data['category_id']
    )

    Session = sessionmaker(bind=engine)

    with Session() as session:
        session.add(new_product)
        session.commit()
        session.refresh(new_product)

        new_json = product_to_json(new_product)
        category = session.query(Category).filter_by(
            category_id=new_product.category_id).first()

        new_json['category'] = category.category_name if new_product.category else None

    return jsonify(new_json), 201


@app.route('/api/product/<int:id>', methods=['GET'])
def get_product(id):
    Session = sessionmaker(bind=engine)
    session = Session()

    product = session.query(Product).filter_by(product_id=id).first()

    session.close()

    if product:
        return jsonify(product_to_json(product))
    else:
        return jsonify({'message': 'Product not found'}), 404


@app.route('/api/product', methods=['PUT'])
def edit_product():
    data = request.json
    product_id = data['product_id']

    Session = sessionmaker(bind=engine)

    with Session() as session:
        product = session.query(Product).filter_by(
            product_id=product_id).first()

        category = session.query(Category).filter_by(
            category_id=data['category_id']).first()

        if product:
            product.product_name = data['product_name']
            product.price = data['price']
            product.discount = data['discount']
            product.image = data['image']
            product.status = data['status']
            product.category_id = data['category_id']
            session.commit()
            session.refresh(product)

            new_json = product_to_json(product)
            new_json['category'] = category.category_name if product.category else None

            return jsonify(new_json), 201
        else:
            return jsonify({'message': 'Product not found'}), 404


@app.route('/api/product/<int:id>', methods=['DELETE'])
def delete_product(id):
    Session = sessionmaker(bind=engine)

    with Session() as session:
        product = session.query(Product).filter_by(product_id=id).first()

        if product:
            session.delete(product)
            session.commit()

            return jsonify({'message': 'Product deleted successfully'})
        else:
            return jsonify({'message': 'Product not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
