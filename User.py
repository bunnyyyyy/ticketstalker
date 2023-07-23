import Email
from Show import Show
import time



class User:
    def __init__(self, email, max_desired_price, artist, date, stub_hub_link):
        self.artist = artist
        self.date = date
        self.email = email
        self.max_desired_price = max_desired_price
        message = f"""\
        Subject: Verifying Your Ticket Updater

        Hello. Thank you for giving us your event details. You will be notified whenever a ticket is listed below ${max_desired_price} for {self.artist}'s show on {self.date}. To stop receiving notifications for this event, please go to LINK HERE and delete your event or email sanya.badhe@gmail.com.
        """
        Email.send_email(email, message)
        self.show = Show(stub_hub_link)

    def start_checking(self):
        self.deleted = False

        while self.deleted == False:
            minPrice = float(self.show.get_stubhub_price())
            if (minPrice <= self.max_desired_price):
                price_found_message = f"""\
                Subject: TICKETS FOR ${minPrice} FOUND

                A listing has been made for ${minPrice} on Stubhub for {self.artist}'s show on {self.date}. To stop receiving notifications for this event, please go to LINK HERE and delete your event or email sanya.badhe@gmail.com.
                """

                Email.send_email(self.email, price_found_message)
                time.sleep(60*20)

    def delete(self):
        self.deleted = True
    
test = User("michelleypink28@gmail.com", 999.99, "Taylor Swift", "7/28/23", "https://www.stubhub.com/taylor-swift-santa-clara-tickets-7-28-2023/event/151197002/")
test.start_checking()