from mailjet_rest import Client
import os
api_key = '8aaa900f8f8c702c54e1f6458db7da19'
api_secret = 'c19ee7876ad58889106135aeb7ff73d2'
mailjet = Client(auth=(api_key, api_secret), version='v3.1')
data = {
  'Messages': [
    {
      "From": {
        "Email": "sidhu1397@gmail.com",
        "Name": "Sidharth"
      },
      "To": [
        {
          "Email": "ragavendrach13@gmail.com",
          "Name": "Muthuraghavendran"
        }
      ],
      "Subject": "CPU Usage Warning",
      "TextPart": """Dear subscriber,
                      Your cpu usage is currently above the threshold limit.Please close non-imperative programs to maintain system stability.
       This is a system generated mail do not reply.""",
      # "HTMLPart": "<h3>Dear passenger 1, welcome to <a href='https://www.mailjet.com/'>Mailjet</a>!</h3><br />May the delivery force be with you!",
      "CustomID": "AppGettingStartedTest"
    }
  ]
}
result = mailjet.send.create(data=data)
print(result.status_code)
print(result.json())
