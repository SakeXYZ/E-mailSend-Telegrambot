# HelpDeskBot With E-Mail
# ENG
This code is a simple telegram bot that accepts messages from users and sends their contents to the specified mail. It uses the telebot libraries to work with Telegram and smtplib to send email. When a user sends a message to the bot, the message content is saved to the text variable, and then sent to the specified mail using the send_email() function.

The send_email() function creates a MIMEText object, fills in its headers and contents, connects to the SMTP server using the specified parameters (server address, port, email address and password), and sends a message. If the sending is successful, the message "Mail has been sent successfully" is displayed. If an error occurs, an error message is displayed.

The bot is launched using bot.polling(), which allows it to receive and process messages from users. The /start command calls the handle_start function, which sends a welcome message. All other messages are processed by the handle_message function, which calls the send_email() function and sends a response message to the user.

Please note that for this code to work successfully, you need to have the correct email credentials and a configured SMTP server.

# RU
Данный код представляет собой простого телеграм-бота, который принимает сообщения от пользователей и отправляет их содержимое на указанную почту. Он использует библиотеки telebot для работы с Телеграмом и smtplib для отправки электронной почты. Когда пользователь отправляет сообщение боту, содержимое сообщения сохраняется в переменную text, а затем отправляется на указанную почту с помощью функции send_email().

Функция send_email() создает объект MIMEText, заполняет его заголовки и содержимое, подключается к серверу SMTP с помощью указанных параметров (адрес сервера, порт, адрес и пароль электронной почты), и отправляет сообщение. Если отправка проходит успешно, выводится сообщение "Почта успешно отправлена". В случае возникновения ошибки, выводится сообщение об ошибке.

Бот запускается с помощью bot.polling(), что позволяет ему получать и обрабатывать сообщения от пользователей. Команда /start вызывает функцию handle_start, которая отправляет приветственное сообщение. Все остальные сообщения обрабатываются функцией handle_message, которая вызывает функцию send_email() и отправляет ответное сообщение пользователю.

Обратите внимание, что для успешной работы этого кода необходимо иметь правильные учетные данные электронной почты и настроенный сервер SMTP.

# Library
- telebot : pip3 install telebot
- smtblib : pip3 install smtblib
