import sys
import requests

#this function helps to send email and mails can be in form of list if we want
def send():
    """
        all required details are passed into variable below 
        e.g mail,api_base_url and api_key(gotten from mailgun),till messages.
    """
    mails = ['']
    api_base_url = "https://api.mailgun.net/v3/#/messages"
    api_key = ""
    from_email = "# <#.com>"
    to_email_list = mails
    subject = "FROM PYTHON"
    messages = "data scrapped sucessful"
# this return help to post  auth and data to api_base_url
    return requests.post(
    api_base_url,
    auth=("api", api_key),
    data={"from": from_email, "to": to_email_list, "subject": subject, "text": messages})

send()
print("Done!")



