from twilio.rest import Client

account_SID = 'AC691ab11264f4b2d6d3309ba8b811d205'
auth_token = '5dddd0020a17adcd7953d1ee436c3924'
twilio_number = '+14253812300'

twilio_cli = Client(account_SID, auth_token)

message = twilio_cli.messages.create(
    body='Hello from the other side', from_=twilio_number, to='+79773571157')

updated_message = twilio_cli.messages.get(message.sid)

print(message.status, message.date_created,
      message.date_updated, message.date_sent)
