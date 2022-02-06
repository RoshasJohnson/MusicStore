# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

def otpverification(id):

    account_sid = os.environ['AC0eb31c976dfd6b92c07d3e35d715b3f8']
    auth_token = os.environ['c0fb01106cb0736e0ed0e14354817fd8']
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            messaging_service_sid='MG9752274e9e519418a7406176694466fa',
            body='body',
            to='+917012598205'
        )
    print(message.sid)
       