import os
import sys

sys.path.append(os.getcwd)

from sqlalchemy import (create_engine, PrimaryKeyConstraint,UniqueConstraint,CheckConstraint, Column, String,Integer, ForeignKey, DateTime)
# from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship



Base = declarative_base()
engine = create_engine('sqlite:///database/loyalty.db', echo=True)

class Customer(Base):
    __tablename__ = 'customers'
    __table_args__ = (
        PrimaryKeyConstraint(
            'id',
            name='id_pk'),
        
        UniqueConstraint(
            'email','name',
            name='uix_1'),
        

    )
    

    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone_number = Column(Integer)
    email = Column(String)
    transactions = relationship("Transaction", back_populates="customer")


class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    point = Column(Integer)
    amount = Column(Integer)
    transaction_date= Column(DateTime)
    customer = relationship("Customer", back_populates="transactions")

class Loyaltypoints(Base):
    __tablename__ = 'loyaltypoints'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    point = Column(Integer)


#delete tables
#Base.metadata.drop_all(engine)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()