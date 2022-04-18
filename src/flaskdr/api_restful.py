from flask_restful import Api, Resource
from flask import jsonify, request
from src.flaskdr import create_app
from src.flaskdr.models import Customer,Order,Art,db
import hashlib
import secrets

app=create_app()
api=Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

def scramble(password: str):
    """Hash and salt the given password"""
    salt = secrets.token_hex(16)
    return hashlib.sha512((password + salt).encode('utf-8')).hexdigest()



class all_customers(Resource):
    def get(self):
        customer_records=Customer.query.all()
        arr=[Customer.serialize(record) for record in customer_records] #fancy for loop
        return jsonify(arr)

class get_customer_by_id(Resource):
    def get(self,c_id):
        customer_records=Customer.query.get_or_404(c_id)
        return jsonify({"customer":customer_records.serialize()})

class del_customer_by_id(Resource):
    def delete(self,c_id):
        customer_records=Customer.query.get_or_404(c_id)
        try:
            db.session.delete(customer_records) # prepare DELETE statement
            db.session.commit() # execute DELETE statement
            return jsonify(True)
        except:
            # something went wrong :(
            return jsonify(False)

class add_customers(Resource):
    def post(self):
        # if 'username' not in request.json and 'password' not in request.json or len(request.json["username"])< 3 and len(request.json['password'])<8:
        #     return abort(400)
        c=Customer(
            first_name=request.json['First_Name'],
            last_name=request.json['Last_Name'],
            email=request.json['Email'],
            address=request.json['Street_Address'],
            city=request.json['City'],
            state=request.json['State'],
            zip=request.json['Zip'],
            username=request.json['Username'],
            password=scramble(request.json['Password'])
        )
        db.session.add(c)
        db.session.commit()
        return jsonify(c.serialize())
        



class all_orders(Resource):
    def get(self):
        order_records=Order.query.all()
        arr_o=[Order.serialize(record) for record in order_records] 
        return jsonify(arr_o)

class all_art(Resource):
    def get(self):
        art_records=Art.query.all()
        arr_a=[Art.serialize(records) for records in art_records]
        return jsonify(arr_a)


class get_artwork_by_id(Resource):
    def get(self,c_id):
        art_record=Art.query.get_or_404(c_id)
        return jsonify({"artwork":art_record.serialize()})



class del_artwork_by_id(Resource):
    def delete(self,c_id):
        art_record=Art.query.get_or_404(c_id)
        try:
            db.session.delete(art_record) # prepare DELETE statement
            db.session.commit() # execute DELETE statement
            return jsonify(True)
        except:
            # something went wrong :(
            return jsonify(False)
    

api.add_resource(HelloWorld, '/')
api.add_resource(all_customers, '/customers')
api.add_resource(get_customer_by_id, '/customers/<int:c_id>')
api.add_resource(all_orders, '/orders')
api.add_resource(all_art, '/artwork')
api.add_resource(get_artwork_by_id,  '/artwork/<int:c_id>')
api.add_resource(del_artwork_by_id,  '/artwork/<int:c_id>')
api.add_resource(del_customer_by_id, '/customers/<int:c_id>')
api.add_resource(add_customers, '/customers')



    
