from flask import Flask, jsonify, request, session, make_response
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask import request\

from models import db, User, Gold, Pickaxe

app = Flask(__name__)
app.secret_key = b'***************************************'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)

migrate = Migrate(app, db)

db.init_app(app)

bcrypt = Bcrypt(app)

@app.route('/api/users', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        # Implement logic to fetch users from the database
        pass
    elif request.method == 'POST':
        # Implement logic to create a new user in the database
        pass

if __name__ == '__main__':
    app.run(port=5555, debug=True)
    