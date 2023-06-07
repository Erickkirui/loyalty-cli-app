import os
import sys

sys.path.append(os.getcwd)

from sqlalchemy import (create_engine, PrimaryKeyConstraint, Column, String,Integer, ForeignKey)
# from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship



Base = declarative_base()
engine = create_engine('sqlite:///database/loyalty.db', echo=True)

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    transactions = relationship("Transaction", back_populates="customer")


class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    point = Column(Integer)
    
    customer = relationship("Customer", back_populates="transactions")

class Loyaltypoints(Base):
    __tablename__ = 'loyaltypoints'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    point = Column(Integer)





Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()