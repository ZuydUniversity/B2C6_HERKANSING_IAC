from flask import Flask, jsonify, request, session, make_response
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_cors import CORS

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

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    user = User.query.filter_by(username=username).first()

    if user and user.password == password:
        return jsonify({"success": True, "message": "Login successful!"}), 200
    else:
        return jsonify({"success": False, "message": "Invalid username or password"}), 401


if __name__ == '__main__':
    app.run(port=5000, debug=True)
    