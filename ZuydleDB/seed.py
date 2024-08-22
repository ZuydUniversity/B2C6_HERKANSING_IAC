from app import app
from models import db, User

with app.app_context():
    db.create_all()

  
    user1 = User(username='admin', password='admin')
    user2 = User(username='Dakka', password='Dakka')
    user3 = User(username='Kevin', password='password')

 
    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)
    db.session.commit()

    print("Database gevuld met testgegevens.")