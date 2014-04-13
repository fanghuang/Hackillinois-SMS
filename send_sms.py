# from twilio.rest import TwilioRestClient
 
# # Your Account Sid and Auth Token from twilio.com/user/account
# account_sid = "PN3516502740c1f1bdfad4d56e7d7474e9"
# auth_token  = "e7bd7f97aa4b0858d8c5bd09732d2511"
# client = TwilioRestClient(account_sid, auth_token)
 
# message = client.sms.messages.create(body="Jenny please?! I love you <3",
#     to="+18122363915",    # Replace with your phone number
#     from_="+18128644782") # Replace with your Twilio number
# print message.sid

import twilio
from twilio.rest import TwilioRestClient
try:
	account_sid = "ACedfb08c8d4d265990a4ab42477e2e52a"
	auth_token  = "e7bd7f97aa4b0858d8c5bd09732d2511"
	client = twilio.rest.TwilioRestClient(account_sid, auth_token)
	message = client.sms.messages.create(body="Jfor taylorou <3",
	to="+18122363915",    # Replace with your phone number
	from_="+18128644782")
except twilio.TwilioRestException as e:
	print e