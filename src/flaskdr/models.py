
from flask_sqlalchemy import SQLAlchemy


db= SQLAlchemy()

Order_Art=db.Table(
    'orders_artwork',
    db.Column('order_id',db.Integer,db.ForeignKey('orders.id'),primary_key=True),
    db.Column('art_id',db.Integer,db.ForeignKey('artwork.id'),primary_key=True),
    #artwork_rel= db.relationship("Art", backref=db.backref("orders", cascade="all, delete-orphan")),
    #order_rel= db.relationship("Order", backref=db.backref("orders", cascade="all, delete-orphan"))
 )

class Customer(db.Model):
    __tablename__='customers'
    id= db.Column(db.Integer,primary_key=True,autoincrement=True)
    first_name= db.Column(db.String(50),nullable=False)
    last_name=db.Column(db.String(50),nullable=False)
    email=db.Column(db.String(225),nullable=False)
    address=db.Column(db.String(300),nullable=False)
    city=db.Column(db.String(70),nullable=False)
    state=db.Column(db.String(10),nullable=False)
    zip=db.Column(db.String(10),nullable=False)
    username=db.Column(db.String(100),nullable=False)
    password=db.Column(db.String(140),nullable=False)
    ordering=db.relationship('Order', backref="ordering")

    def __init__(self,first_name,last_name,email,address,city,state,zip,username,password):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.address=address
        self.city=city
        self.state=state
        self.zip=zip
        self.username=username
        self.password=password

    def serialize(self):
        return{
            "ID:":self.id,
            "First_Name":self.first_name,
            "Last_Name":self.last_name,
            "Email":self.email,
            "Street_Address":self.address,
            "City":self.city,
            "State":self.state,
            "Zip":self.zip,
            "Username":self.username,
            "Password":self.password
        }




class Order(db.Model):
    __tablename__='orders'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    customer_id=db.Column(db.Integer,db.ForeignKey('customers.id'),nullable=False)
    order_date=db.Column(db.Date,nullable=False)
    ship_date=db.Column(db.Date,nullable=True)
    ship_street=db.Column(db.String(300),nullable=False)
    ship_city=db.Column(db.String(50),nullable=False)
    ship_state=db.Column(db.String(2),nullable=False)
    ship_zip=db.Column(db.String(5),nullable=False)
    


    
    def __init__(self,customer_id,order_date,ship_date,ship_street,ship_city,ship_state,ship_zip):
        self.customer_id=customer_id
        self.order_date=order_date
        self.ship_date=ship_date
        self.ship_street=ship_street
        self.ship_city=ship_city
        self.ship_state=ship_state
        self.ship_zip=ship_zip
        
    def serialize(self):
        return{
            "ID:":self.id,
            "Customer_ID":self.customer_id,
            "Order_Date":self.order_date,
            "Ship_Date":self.ship_date,
            "Street_Address":self.ship_street,
            "City":self.ship_city,
            "State":self.ship_state,
            "Zip":self.ship_zip,
        }
       


class Art(db.Model):
    __tablename__='artwork'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    title=db.Column(db.String(300),nullable=False)
    cost=db.Column(db.Numeric,nullable=False)
    image_path=db.Column(db.String(300),nullable=True)
    ordering=db.relationship('Order', secondary=Order_Art,lazy='subquery',backref=db.backref('Order_Art', lazy=True))


    def __init__(self,title,cost,image):
        self.title=title
        self.cost=cost
        self.image_path=image

    def serialize(self):
        return{
           "Title":self.title,
           "Price":self.cost,
           "URL":self.image_path
        }
       





   