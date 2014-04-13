from flask import Flask, request, redirect
import twilio.twiml
import os
import urllib
import mechanize
import re

app = Flask(__name__)
 
# @app.route("/")
# def hello():
#     return "Hello World! haoiehfoaehf"

# callers = {
# 	"+18122363915": "Vismay is good!",
# 	"+14158675310": "Boots",
# 	"+14158675311": "Virgil",
# }
 
@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
	"""Respond and greet the caller by name."""
 	message = "Query not found. Please send in this format: first two character represent airline and four digits flight number put a space in between. e.g:DL 1234"

	# from_number = request.values.get('From', None)
	# city = request.values.get('FromCity', None)
	body = request.values.get('Body', None)
	airline = ""
	number = ""
	array = body.split(' ')
	

	if (len(array) <=1):
		resp = twilio.twiml.Response()
		resp.message(message)
	 	return str(resp)
	else:
		airline = array[0]
		number = array[1]
		if len(airline)!=2 or len(number)>4 or len(number)<3:
			resp = twilio.twiml.Response()
			resp.message(message)
			return str(resp)
	
	# airline = ""
	# number = ""
	# for i in range(6):
	# 	if i < 2:
	# 		if body[i].isalpha():
	# 			airline = airline + body[i]
	# 	else:
	# 		if body[i].isdigit():
	# 			number = number + str(body[i])

	# if from_number in callers:
	# 	message = callers[from_number] + ", thanks for the message!"
	# else:
	# 	message = "Monkey, thanks for the message!"
 	
	br = mechanize.Browser()
	br.set_handle_robots(False)
	br.addheaders=[('User-agent','chrome')]

	# airline = body
	# number = "5349"

	query = "https://www.google.com/search?q="+airline+"+"+number+"&oq="+airline+"+"+number

	htmltext = br.open(query).read()

	regex = '</b></td></tr></table></div><div><table cellspacing="0"><tr><td colspan="2" style="height:1.2em;color:#093;padding: 4px 0">(.+?)</td>'
	pattern = re.compile(regex)
	status = re.findall(pattern, htmltext)
	if status :
		message = airline + number + ' is ' + status[0]
	else:
		message = airline + number + ' is delayed' 
	
	# print airline + number + ' is ' + status[0]
	
	# message = body
	resp = twilio.twiml.Response()
	resp.message(message)
 
	return str(resp)
 
if __name__ == "__main__":
	# app.run(debug=True,host='0.0.0.0')
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)