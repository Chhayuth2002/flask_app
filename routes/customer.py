from app import app, request, engine, jsonify, Customer
from sqlalchemy.orm import sessionmaker

# Function to convert Customer object to JSON


def customer_to_json(customer):
    return {
        'customer_id': customer.customer_id,
        'name': customer.name,
        'image': customer.image,
        'status': customer.status,
        'phone': customer.phone,
        'email': customer.email,
    }

# CRUD Operations


@app.route('/api/customer', methods=['GET'])
def get_customers():
    Session = sessionmaker(bind=engine)
    session = Session()

    customers = session.query(Customer).all()

    session.close()

    return jsonify([customer_to_json(customer) for customer in customers])


@app.route('/api/customer/<int:id>', methods=['GET'])
def get_customer(id):
    Session = sessionmaker(bind=engine)
    session = Session()

    customer = session.query(Customer).filter_by(
        customer_id=id).first()

    session.close()

    if customer:
        return jsonify(customer_to_json(customer))
    else:
        return jsonify({'message': 'Customer not found'}), 404


@app.route('/api/customer', methods=['POST'])
def create_customer():
    data = request.json

    new_customer = Customer(
        name=data['name'],
        image=data.get('image', ''),
        status=data.get('status', ''),
        phone=data.get('phone', ''),
        email=data.get('email', '')
    )

    Session = sessionmaker(bind=engine)

    with Session() as session:
        session.add(new_customer)
        session.commit()

        session.refresh(new_customer)

    return jsonify(customer_to_json(new_customer)), 201


@app.route('/api/customer', methods=['PUT'])
def update_customer():
    data = request.json
    customer_id = data['customer_id']
    Session = sessionmaker(bind=engine)

    with Session() as session:
        customer = session.query(Customer).filter_by(
            customer_id=customer_id).first()

        if customer:
            customer.name = data.get('name', customer.name)
            customer.image = data.get('image', customer.image)
            customer.status = data.get('status', customer.status)
            customer.phone = data.get('phone', customer.phone)
            customer.email = data.get('email', customer.email)

            session.commit()
            session.refresh(customer)

            return jsonify(customer_to_json(customer))
        else:
            session.close()
            return jsonify({'message': 'Customer not found'}), 404


@app.route('/api/customer/<int:id>', methods=['DELETE'])
def delete_customer(id):
    Session = sessionmaker(bind=engine)
    session = Session()

    customer = session.query(Customer).filter_by(
        customer_id=id).first()

    if customer:
        session.delete(customer)
        session.commit()
        session.close()

        return jsonify({'message': 'Customer deleted successfully'})
    else:
        session.close()
        return jsonify({'message': 'Customer not found'}), 404
