import Email
from VerificationMessage import message



class User:
    def __init__(self, email, phone_number, max_desired_price, stub_hub_link):
        self.email = email
        self.phone_number = phone_number
        self.max_desired_price = max_desired_price
        Email.send_email(email, message)

    