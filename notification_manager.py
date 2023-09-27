class NotificationManager:
    from twilio.rest import Client

    TWILIO_SID = "XYZ"
    TWILIO_AUTH_TOKEN = "XYZ"
    TWILIO_VIRTUAL_NUMBER = "+1234567890"
    TWILIO_VERIFIED_NUMBER = "+1234567898"

    class NotificationManager:

        def __init__(self):
            self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

        def send_sms(self, message):
            message = self.client.messages.create(
                body=message,
                from_=TWILIO_VIRTUAL_NUMBER,
                to=TWILIO_VERIFIED_NUMBER,
            )
            # Prints if successfully sent.
            print(message.sid)