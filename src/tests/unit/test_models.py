from flaskdr.models import Customer

def test_new_customer():
    new_customer=Customer("Kevin","Smith","test@gmail.com","123 elmo street","Durham","NC",12345,"applesAndoranges","test1234")
    assert(new_customer.first_name=="Kevin")
    assert(new_customer.zip==12345)