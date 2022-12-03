import httpx
import json
import time


class tempmail:
   def __init__(self, sleep_time: int=10, timeout: int=60):
     self.endpoint = "https://web2.temp-mail.org"
     self.client = httpx.Client(http2=False, verify=False, timeout=timeout)
     self.time = sleep_time

   def get_token(self):
    response = self.client.post(f'{self.endpoint}/mailbox', headers={
       'authority': 'web2.temp-mail.org',
       'accept': 'application/json',
       'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
       'origin': 'https://temp-mail.org',
       'referer': 'https://temp-mail.org/',
       'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
       'sec-ch-ua-mobile': '?0',
       'sec-ch-ua-platform': '"Windows"',
       'sec-fetch-dest': 'empty',
       'sec-fetch-mode': 'cors',
       'sec-fetch-site': 'same-site',
       'user-agent': 'Swaps/1.337',
      }).json()

    if "token" in response:
        data = {"status": "CREATED", "email": response["mailbox"], "token": response["token"]}
        return data
    else:
        data = {"status": "FAILED", "message": response}
        return data

   def get_messages(self, token):
        time.sleep(self.time)
        response = self.client.get(f'{self.endpoint}/messages', headers={
           'authority': 'web2.temp-mail.org',
           'accept': 'application/json',
           'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
           'origin': 'https://temp-mail.org',
           'referer': 'https://temp-mail.org/',
           'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
           'sec-ch-ua-mobile': '?0',
           'authorization': f"Bearer {token}",
           'sec-ch-ua-platform': '"Windows"',
           'sec-fetch-dest': 'empty',
           'sec-fetch-mode': 'cors',
           'sec-fetch-site': 'same-site',
           'user-agent': 'Swaps/1.337',
         })  
        if response.status_code == 200:
           return response.json()['messages']
        else:
            data = {"status": "FAILED", "message": response}
            return data

if __name__ == '__main__':
    input("> github.com/3ut")
