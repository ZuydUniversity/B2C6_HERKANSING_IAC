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

@app.route('/api/users', methods=['GET'])
def get_user():
    username = request.args.get('username')
    if username:
        user = User.query.filter_by(username=username).first()
        if user:
            return jsonify({"exists": True}), 200
        else:
            return jsonify({"exists": False}), 404
    else:
        users = User.query.all()
        user_list = []
        for user in users:
            user_data = {
                'id': user.id,
                'username': user.username,
                'password': user.password
            }
            user_list.append(user_data)
        return jsonify(user_list)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
    