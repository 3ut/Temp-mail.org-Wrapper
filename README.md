<div id="top"></div>
<p align="center">

  <br/>
<div align="center">
  <a href="https://github.com/3ut/Temp-mail.org-Wrapper">
    <img src="https://scontent.fcta2-2.fna.fbcdn.net/v/t39.30808-6/300376967_448925583960488_4556548013530860200_n.png?_nc_cat=100&ccb=1-7&_nc_sid=09cbfe&_nc_ohc=QHLKCKT7xRwAX8aG1nk&_nc_ht=scontent.fcta2-2.fna&oh=00_AfBvrkGAIBEY6_lXBS2NZulICea2NqxH2yn0mRgMsEFFsg&oe=63904C2F" alt="Logo" width="120" height="120">
  </a>
  
  
  <h2 align="center">temp-mail.org wrapper</h3>

  <p align="center">
    A simple wrapper capable of generating emails using the temp-mail.org API.
    <br />
    <br />
    <a href="https://github.com/3ut/Temp-mail.org-Wrapper/issues">Report Bug</a>
    ·
    <a href="https://github.com/3ut/Temp-mail.org-Wrapper/issues">Request Feature</a>
  </p>
</div>
  
---------------------------------------

### Features
* Symple Sintax
* API key not required


---------------------------------------

### Usage

```py
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
````
---------------------------------------

### Output
![a307ngws](https://user-images.githubusercontent.com/84240761/205456587-3629efbf-a1e6-4482-9ac1-cee788a2037f.png)
---------------------------------------
### Contact
[Telegram](https://t.me/swaps1337)
[Discord](https://discord.com/users/853374852559274014)
