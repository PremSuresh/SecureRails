from twilio.rest import Client

def SMS(message, sent):
    sent = "+91"+sent
    account_sid = "AC3b2934c77e97340c066e2b5788e35c79"
    auth_token = "ce9149d72ee792312a694ed5be660302"
    client = Client(account_sid, auth_token)
    client.messages.create(to=sent,from_="+12566175880",body=message)
