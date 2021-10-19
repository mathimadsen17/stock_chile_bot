import requests

def telegram_bot_sendtext_checker(bot_message):
    
    bot_token = '2084668302:AAEOofnAmhtYnMe6Qy-5U9OELEJRDmjuqe8'
    bot_chatID = '1346710969'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()