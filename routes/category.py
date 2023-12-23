from app import app, request, engine, jsonify, Category
from sqlalchemy.orm import sessionmaker


# Function to convert Category object to JSON
def category_to_json(category):
    return {
        'category_id': category.category_id,
        'category_name': category.category_name,
        'status': category.status
    }

# Routes

@app.route('/api/category', methods=['GET'])
def get_categories():
    Session = sessionmaker(bind=engine)
    session = Session()
    
    categories = session.query(Category).all()
    
    session.close()
    
    return jsonify([category_to_json(category) for category in categories])

@app.route('/api/category/<int:id>', methods=['GET'])
def get_category(id):
    Session = sessionmaker(bind=engine)
    session = Session()
    
    category = session.query(Category).filter_by(category_id=id).first()
    
    session.close()
    
    if category:
        return jsonify(category_to_json(category))
    else:
        return jsonify({'message': 'Category not found'}), 404

@app.route('/api/category', methods=['POST'])
def add_category():
    data = request.json
    new_category = Category(category_name=data['category_name'], status=data['status'])
    
    Session = sessionmaker(bind=engine)
    
    with Session() as session:
        session.add(new_category)
        session.commit()
        
        session.refresh(new_category)

    return jsonify(category_to_json(new_category)), 201


@app.route('/api/category', methods=['PUT'])
def edit_category():
    data = request.json
    category_id = data['category_id']
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    with Session() as session:
        category = session.query(Category).filter_by(category_id=category_id).first()
        
        if category:
            category.category_name = data['category_name']
            category.status = data['status']
            session.commit()
            session.refresh(category)
            
            return jsonify(category_to_json(category))
        else:
            return jsonify({'message': 'Category not found'}), 404

@app.route('/api/category/<int:id>', methods=['DELETE'])
def delete_category(id):
    Session = sessionmaker(bind=engine)
    
    with Session() as session:
        category = session.query(Category).filter_by(category_id=id).first()

        if category:
            session.delete(category)
            session.commit()
            
            return jsonify({'message': 'Category deleted successfully'})
        else:
            return jsonify({'message': 'Category not found'}), 404
    


    

    