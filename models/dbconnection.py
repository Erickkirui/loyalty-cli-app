from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database/loyalty.db')
Session = sessionmaker(bind=engine)
session = Session()
