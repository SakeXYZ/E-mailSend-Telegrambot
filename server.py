import telebot
import smtplib
from email.mime.text import MIMEText

# Замените значения переменных ниже на ваши данные
bot_token = "your TelegramBot API-Token"
email_address = "your address"
email_password = "you password"
smtp_server = "smtp.gmail.com"
smtp_port = 587

bot = telebot.TeleBot(bot_token)

first_run = True


@bot.message_handler(commands=["start"])
def handle_start(message):
    global first_run
    if first_run:
        reply_text = "Welcome"
        bot.reply_to(message, reply_text)
        first_run = False

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text
    userid = message.chat.username

    print(str(message.contact))
    send_email(str(userid) + "\n" + text)
    bot.reply_to(message, "Message send in email")


def send_email(text):
    msg = MIMEText(text)
    msg["From"] = email_address
    msg["To"] = email_address
    msg["Subject"] = "New message"
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(email_address, email_password)
        server.send_message(msg)
        server.quit()
        print("Mail send succesfull")
    except Exception as e:
        print("Send is Failed", str(e))


try:
    bot.polling()
except Exception as e:
    print(":", str(e))
