from models import Base , User , Comment
from sqlalchemy.orm import Session
from connect import engine

session = Session(bind=engine)

user1 = User(
        username = 'kumar',
        email_address = 'kumar@org.com',
        comments = [
            Comment(text="Hello World"),
            Comment(text="Hello Please Enroll"),
            ]
        )


user2 = User(
        username = 'Ram',
        email_address = 'ram@gmail.com',
        comments = [
            Comment(text="Nice Content"),
            Comment(text="Please create more example on AI ML"),
            ]
        )


user3 = User(
        username = 'Cassie',
        email_address = 'cassie@hotmail.com',
        )


session.add_all([user1,user2,user3])
session.commit()
session.close()