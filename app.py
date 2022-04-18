import random
import string
import hashlib
import secrets
from faker import Faker
from src.flaskdr.models import Customer,Order,Order_Art,Art,db
from src.flaskdr.api_restful import app
from imgs.imag_paths import paths,price,titles
from datetime import date, datetime


customer_count=50
order_count=100
art_work=len(paths)

def random_passhash():
    """Get hashed and salted password of length N | 8 <= N <= 15"""
    raw = ''.join(
        random.choices(
            string.ascii_letters + string.digits + '!@#$%&', # valid pw characters
            k=random.randint(8, 10) # length of pw
        )
    )

    salt = secrets.token_hex(12)

    return hashlib.sha512((raw + salt).encode('utf-8')).hexdigest()



def main():
    """Main driver function"""
    app.app_context().push()
    db.drop_all()
    db.create_all()
    fake = Faker()
    last_customer=None
    for i in range(customer_count):
        last_customer=Customer(fake.first_name(),fake.last_name(),fake.email(),fake.street_address(),fake.state_abbr(),fake.state_abbr(),fake.zipcode(),fake.user_name(),password=random_passhash())
        db.session.add(last_customer)


    db.session.commit()

    last_order=None
    for j in range(order_count):
        last_order=Order(
            customer_id=random.randint(1,50),
            order_date=date(2021,random.randint(1,4),random.randint(1,11)),
            ship_date=date(2021,random.randint(5,8),random.randint(3,11)),
            ship_street=fake.street_address(),
            ship_city=fake.city(),
            ship_state=fake.state_abbr(),
            ship_zip=fake.zipcode()

        )
        db.session.add(last_order)
    db.session.commit()

    last_art=None
    for l in range(art_work):
        last_art=Art(
            title=titles[l],
            cost=price[l],
            image=paths[l]
        )
        db.session.add(last_art)
    db.session.commit()
    
    order_and_art=set()

### new_likes = [{"user_id": pair[0], "tweet_id": pair[1]} for pair in list(user_tweet_pairs)]
    #insert_likes_query = likes_table.insert().values(new_likes)
    #db.session.execute(insert_likes_query)
    #how to populate data into the order_artwork table , create a set for the pairs, then create a while or for loop to store the pairs in a tuple  then inser that tuple into the 
    #the order_art table 

    

    while len(order_and_art)<order_count:
        purchases=(
            random.randint(last_order.id - order_count+ 1, last_order.id),
            random.randint(last_art.id - art_work + 1, last_art.id)
            )
        
        if purchases in order_and_art:
            continue  
        order_and_art.add(purchases)
    transactions=[{"order_id": pair[0],"art_id":pair[1]} for pair in list(order_and_art)]
    insertQuery=Order_Art.insert().values(transactions)
    db.session.execute(insertQuery)
    db.session.commit()



main()
   