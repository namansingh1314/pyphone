import schedule
import time

from twilio.rest import Client 
account_naman = 'AC5172480e9728c5273d6591605ca07275'
auth_token ='8584b077cff8d48108fa03f22e1ae615'
Client = Client(account_naman,auth_token)

call = Client.calls.create(
                       twiml='<Response><Say>uth ja bhai</Say><Response>',
                       to='+917460851024',
                       from_='+17624222334'
                    )

print(call.sid)