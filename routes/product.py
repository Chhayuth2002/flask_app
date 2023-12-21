from app import app, request, engine,jsonify, Product
from sqlalchemy.orm import sessionmaker



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
    
    session.close()
    
    return jsonify([product_to_json(product) for product in products])

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

    return jsonify(product_to_json(new_product)), 201

@app.route('/api/product/<int:product_id>', methods=['GET'])
def get_product(id):
    Session = sessionmaker(bind=engine)
    session = Session()
    
    product = session.query(Product).filter_by(product_id=id).first()
    
    session.close()
    
    if product:
        return jsonify(product_to_json(product))
    else:
        return jsonify({'message': 'Product not found'}), 404

@app.route('/api/product/<int:product_id>', methods=['PUT'])
def edit_product(id):
    data = request.json
    
    Session = sessionmaker(bind=engine)
    
    with Session() as session:
        product = session.query(Product).filter_by(product_id=id).first()
        
        if product:
            product.product_name = data['product_name']
            product.price = data['price']
            product.discount = data['discount']
            product.image = data['image']
            product.status = data['status']
            product.category_id = data['category_id']
            session.commit()
            session.refresh(product)
            
            return jsonify(product_to_json(product))
        else:
            return jsonify({'message': 'Product not found'}), 404

@app.route('/api/product/<int:product_id>', methods=['DELETE'])
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