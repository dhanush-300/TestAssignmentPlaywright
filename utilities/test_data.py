# Placeholder for future test data
from faker import Faker

fake = Faker()

def random_email():
    return fake.email()

def random_password():
    return fake.password()

def random_name():
    return fake.first_name()

def random_surname():
    return fake.last_name()