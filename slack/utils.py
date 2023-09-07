# This file will contain utility functions related to Slack operations.

from slack_sdk.errors import SlackApiError
import streamlit as st
from .client import client
import time
from .client import BOT_USER_ID


def send_message(channel, text):
    try:
        response = client.chat_postMessage(channel=channel, text=text)
        return response['ts']
    except SlackApiError as e:
        st.error(f"Error sending message: {e}")

def fetch_messages(channel, last_message_timestamp):
    response = client.conversations_history(channel=channel, oldest=last_message_timestamp)
    return [msg['text'] for msg in response['messages'] if msg['user'] == BOT_USER_ID]

def get_new_messages(channel, last_message_timestamp):
    while True:
        messages = fetch_messages(channel, last_message_timestamp)
        if messages and not messages[-1].endswith('Typing…_'):
            return messages[-1]
        time.sleep(5)

def find_direct_message_channel(user_id):
    try:
        response = client.conversations_open(users=user_id)
        return response['channel']['id']
    except SlackApiError as e:
        st.error(f"Error opening DM channel: {e}")
