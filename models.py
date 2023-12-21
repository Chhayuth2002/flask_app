from sqlalchemy import  Column, Integer, Text, ForeignKey, Float, DateTime
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customer'
    customer_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text, nullable=False)
    image = Column(Text)
    phone = Column(Text)
    email = Column(Text)
    status = Column(Text)
    
    sales = relationship("Sale", back_populates="customer")
    
class Sale(Base):
    __tablename__ = 'sale'
    sale_id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(DateTime, nullable=False, default=datetime.utcnow)
    price = Column(Float, nullable=False)
    customer_id = Column(Integer, ForeignKey('customer.customer_id'))
    
    customer = relationship("Customer", back_populates="sales")
    
class Category(Base):
    __tablename__ = 'category'
    category_id = Column(Integer, primary_key=True, autoincrement=True)
    category_name = Column(Text)
    status = Column(Text)
        
    products = relationship("Product", back_populates="category")
    
class Product(Base):
    __tablename__ = 'product'
    product_id = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(Text)
    price = Column(Float(10, 2))    
    discount = Column(Float(10, 2))
    image = Column(Text)
    status = Column(Text)
    category_id = Column(Integer, ForeignKey('category.category_id'))
    
    category = relationship("Category", back_populates="products")
    
