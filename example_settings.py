# settings
# Login to https://my.telegram.org/ choose API development tools and create new App
# then copy App api_id and App api_hash
api_id = 1234567
api_hash = 'your api hash'

phone = '+380123456789'  # your phone connected to telegram account

chat_name = 'New chat name'
chat_users = [
    'me',
    'username',
]

chat_photo_path = '/path/to/photo.png'  # leave blank and photo would not be set

description = 'Chat description'  # leave blank for empty description

greeting_text = f'First message to the group'  # leave blank and no message would be sent
pin_greeting_message = False

poll_question = 'Question'  # leave blank and no poll would be created
poll_answers = ['Yes', 'No']  # up to 10 answers
poll_public = True
pin_poll = True
