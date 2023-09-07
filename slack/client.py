# This file will contain the WebClient initialization and the loading of secrets.

from slack_sdk import WebClient
import streamlit as st

# Load secrets
SLACK_USER_TOKEN = st.secrets["slack"]["SLACK_USER_TOKEN"]
BOT_USER_ID = st.secrets["slack"]["BOT_USER_ID"]

client = WebClient(token=SLACK_USER_TOKEN)
