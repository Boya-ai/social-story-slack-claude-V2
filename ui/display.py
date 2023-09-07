# This file will contain functions to display data on Streamlit, such as the formatted story.

import streamlit as st

def format_story(new_message):
    # Split the story into parts
    parts = new_message.split('\n')

    # Create an HTML string to format the story
    story_html = "<div style='text-align: right; direction: rtl; font-family: Arial, sans-serif; border: 2px solid #e3e3e3; padding: 20px; border-radius: 10px;'>"
    story_html += "<h2 style='color: #4a90e2;'>Claude's Social Story:</h2>"

    for part in parts:
        if part.startswith('- '):
            story_html += f"<h3 style='color: #333;'>{part[2:]}</h3>"
        else:
            story_html += f"<p>{part}</p>"

    story_html += "</div>"

    return story_html

def display_story(story):
    # Replacing newline characters with HTML line breaks
    story_html = story.replace("\n", "<br>")

    # Formatting the output with HTML
    story_output = f"<div style='text-align: right; direction: rtl; border: 2px solid #f0f0f0; padding: 15px; border-radius: 10px; font-family: Arial; font-size: 14px;'>\
                    <h2>Claude's Social Story:</h2><br>{story_html}\
                    </div>"

    st.markdown(story_output, unsafe_allow_html=True)
