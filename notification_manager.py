import smtplib

my_email = "REPLACE"
password = "REPLACE"


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def send_email(self, emails, message , google_flight_link):
        with smtplib.SMTP("smtp.gmail.com") as self.connection:
            self.connection.starttls()
            self.connection.login(user=my_email, password=password)
            for email in emails:
                self.connection.sendmail(
                    from_addr=my_email,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )
