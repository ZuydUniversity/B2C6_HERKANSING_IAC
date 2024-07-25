from flask import request
from flask_restplus import Api, Resource, fields
from . import app, db
from .models import Gold, Pickaxe

api = Api(app)

gold_model = api.model('Gold', {
    'id': fields.Integer(readOnly=True),
    'amount': fields.Integer(required=True, description='The amount of gold')
})

pickaxe_model = api.model('Pickaxe', {
    'id': fields.Integer(readOnly=True),
    'strength': fields.Integer(required=True, description='The strength of the pickaxe')
})

@api.route('/gold')
class GoldList(Resource):
    @api.marshal_with(gold_model, envelope='resource')
    def get(self):
        return Gold.query.all()

    @api.expect(gold_model)
    @api.marshal_with(gold_model, envelope='resource')
    def post(self):
        new_gold = Gold(amount=api.payload['amount'])
        db.session.add(new_gold)
        db.session.commit()
        return new_gold, 201

@api.route('/pickaxe')
class PickaxeList(Resource):
    @api.marshal_with(pickaxe_model, envelope='resource')
    def get(self):
        return Pickaxe.query.all()

    @api.expect(pickaxe_model)
    @api.marshal_with(pickaxe_model, envelope='resource')
    def post(self):
        new_pickaxe = Pickaxe(strength=api.payload['strength'])
        db.session.add(new_pickaxe)
        db.session.commit()
        return new_pickaxe, 201