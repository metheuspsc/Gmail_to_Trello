from imbox import Imbox
import html2text
import requests

API_KEY='Your api key'
OAUTH_TOKEN='Your token'
subjects = ["List of subjects to search"]
print (assunto)

def get_mail_send_trello(x):

    with Imbox('imap.gmail.com',
            username='Your Usename',
            password='Your Password',
            ssl=True,
            ssl_context=None,
            starttls=False) as imbox:

        desired_mail = imbox.messages(unread=True,label='',subject=x,raw='Raw Gmail search syntax')
        for uid, message in mails_desejados:

            desc = message.subject
            html= (str(message.body))
            betterHTML= html2text.html2text(html)
            start = "html': ['"
            end = ']}'
            texto = betterHTML[betterHTML.find(start) + len(start):betterHTML.rfind(end)]
            imbox.mark_seen(uid)

            if x == 'Subject that goes to this board/list':
                list_id = '' 
                r = requests.post("https://api.trello.com/1/cards?key=" + \
                              API_KEY + "&token=" + OAUTH_TOKEN + \
                              "&name=" + desc + "&idList=" + \
                              list_id + "&desc=" + \
                              texto)

            elif x == 'Subject that goes to this board/list':

                list_id = ''
                r = requests.post("https://api.trello.com/1/cards?key=" + \
                              API_KEY + "&token=" + OAUTH_TOKEN + \
                              "&name=" + desc + "&idList=" + \
                              list_id + "&desc=" + \
                              texto)

[get_mail_send_trello(x) for x in subjects]
