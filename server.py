import telebot
import smtplib
from email.mime.text import MIMEText

# Замените значения переменных ниже на ваши данные
bot_token = "5951331406:AAEuHqCUMVje6xUtXYA07JUPD21Gz-lB2As"
email_address = "workoutvirtualenv@gmail.com"
email_password = "gsbpuysnhyhddphz"
smtp_server = "smtp.gmail.com"
smtp_port = 587

bot = telebot.TeleBot(bot_token)

first_run = True


@bot.message_handler(commands=["start"])
def handle_start(message):
    global first_run
    if first_run:
        reply_text = "Здравствуйте! Если вам требуется помощь от технического отдела, пожалуйста, напишите свое имя и отдел, где вам нужна помощь."
        bot.reply_to(message, reply_text)
        first_run = False


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text
    userid = message.chat.username

    print(str(message.contact))
    send_email(str(userid) + "\n" + text)
    bot.reply_to(message, "Сообщение отправлено на почту")


def send_email(text):
    msg = MIMEText(text)
    msg["From"] = email_address
    msg["To"] = email_address
    msg["Subject"] = "Новое сообщение"
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(email_address, email_password)
        server.send_message(msg)
        server.quit()
        print("Почта успешно отправлена")
    except Exception as e:
        print("Ошибка отправки почты:", str(e))


try:
    bot.polling()
except Exception as e:
    print("Произошла ошибка в работе бота:", str(e))
