from src.lul import tempmail

# create mail istance
mail = tempmail(sleep_time=4, timeout=None)
# create and get temp-mail.org mail token
get_mail = mail.get_token()
print(f"Email: {get_mail['email']}")

# fetch new messages
while True:
  for ok in mail.get_messages(get_mail['token']):
    print(f"New message: {ok['from']} | {ok['subject']}")

