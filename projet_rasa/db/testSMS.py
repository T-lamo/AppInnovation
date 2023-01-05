from twilio.rest import Client

# Remplacez les valeurs ci-dessous par votre SID, votre auth token et votre numéro de téléphone Twilio
account_sid = "AC64c34eb4c59c3febc79e26819d37a1df"
auth_token = "ad15ba5285d7f558cd87cc5a5ef9b60d"
twilio_phone_number = "+15153688407"

client = Client(account_sid, auth_token)

client.messages.create(
    from_=twilio_phone_number,
    to="+33680596882",
    body="Hello, world!"
)