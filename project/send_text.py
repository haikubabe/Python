from twilio import rest 
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACbf723a183dc441b706952e91a1a4801f"
auth_token  = "faabe9da555c20f7744233b7bc942ccf"
client = rest.TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="I love Brandy<3",
    to="+919051456362",    # Replace with your phone number
    from_="+12562704903") # Replace with your Twilio number
print message.sid
