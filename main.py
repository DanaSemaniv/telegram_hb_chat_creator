import random

from telethon.sync import TelegramClient
from telethon.tl import functions
from telethon.tl.functions.messages import CreateChatRequest
from telethon.tl.types import InputMediaPoll, Poll, PollAnswer

from settings import *


def get_password():
    return input('Enter your password ')


input('Are you sure?')

with TelegramClient('chat_creating', api_id, api_hash).start(phone, password=get_password) as client:
    # create new chat
    result = client(CreateChatRequest(
        users=chat_users,
        title=chat_name
    ))

    chat_id = result.chats[0].id
    print('Chat was created with chat id', chat_id)

    if chat_photo_path:
        client(functions.messages.EditChatPhotoRequest(
            chat_id=chat_id,
            photo=client.upload_file(chat_photo_path)
        ))
        print('Chat photo edited')

    if description:
        client(functions.messages.EditChatAboutRequest(
            peer=chat_id,
            about=description
        ))
        print('Description edited')

    if greeting_text:
        message = client.send_message(chat_id, greeting_text)
        print('Greeting sent')

        if pin_greeting_message:
            client.pin_message(chat_id, message, notify=False)
            print('Greeting pinned')

    if poll_question:
        message = client.send_message(chat_id, file=InputMediaPoll(
            poll=Poll(
                id=random.randint(1, 1000000),
                question="Закинув:",
                answers=[PollAnswer(answer, bytes(id_)) for id_, answer in enumerate(poll_answers)],
                public_voters=poll_public
            )
        ))
        print('Poll sent')

        if pin_poll:
            client.pin_message(chat_id, message, notify=False)
            print('Poll pinned')

    print('The End')
