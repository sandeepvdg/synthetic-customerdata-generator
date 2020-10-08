from flask import Flask
import random
from customermodel import Customer
import names
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/customer', defaults={'gender':''})
@app.route('/customer/<string:gender>')
def get_rnd_customer(gender):
    gender_list = ['male', 'female', 'none']
    city_list = ['Wolfsburg', 'Hannover', 'Hamburg', 'Stuttgart', 'Dresden', 'Berlin']
    street_list = ['School Street', 'Village Street', 'Garden Street', 'Station Street', 'Main Street', 'Market Street']
    postalcode_list = [10115, 10117, 10120, 10215, 10251, 10200, 10532, 20211, 20116, 50817, 50125, 50126, 50241]
    title_list=['Doctor', 'President', 'Professor','Major','Director']
    gendername=''
    customer = Customer()
    if gender=="":
        gender=random.choice(['M','F'])
    if gender.upper()=='M':
        gendername='male'
        customer.salutation='Mr.'
    elif gender.upper()=='F':
        gendername='female'
        customer.salutation='Ms.'
    elif gender.upper()=='O':
        gendername='None'
        customer.salutation='Mx.'
    customer.lastname = names.get_last_name()
    customer.firstName=names.get_first_name(gender=gendername)
    customer.fullName = customer.firstName +' ' + customer.lastname
    customer.personalEmail=customer.firstName.lower()+'.'+customer.lastname.lower()+'@personaemail.com'
    customer.serviceEmail=customer.firstName.lower()+'.'+customer.lastname.lower()+'@officeemail.com'

    customer.personalTelephone = '+4900000000000'
    customer.serviceTelephone='+491111111111111'
    yyyy=random.randrange(1970,1999)
    mm=random.randrange(1,12)
    dd=random.randrange(1,30)
    customer.dateOfBirth=yyyy.__str__()+'-'+mm.__str__()+'-'+dd.__str__()
    customer.place=random.choice(city_list)
    customer.street=random.choice(street_list)
    customer.postalCode=random.choice(postalcode_list)
    customer.title=random.choice(title_list)
    return customer.toJson()
if __name__ == '__main__':
    app.run()
