# This file will be the main entry point for the Streamlit app, integrating all the modules we've created.

import streamlit as st
from slack.client import BOT_USER_ID
from slack.utils import send_message, find_direct_message_channel, get_new_messages
from templates.story_template import generate_story_prompt, analysis_prompt
from ui.components import get_user_inputs, display_header
from ui.display import format_story, display_story
from utils.file_handler import save_story_to_file

def main():
    # Display the header and model name
    display_header()
    
    # Collect user inputs
    gender, name, age, situation = get_user_inputs()

    # Generate the story prompt
    prompt = generate_story_prompt(gender, name, age, situation)

    # Send the prompt to Claude and display the generated story
    if st.button('Create Social Story'):
        # Spinner to show while waiting for Claude's response
        with st.spinner("Generating Social Story..."):
            dm_channel_id = find_direct_message_channel(BOT_USER_ID)
            if not dm_channel_id:
                st.error("Could not find DM channel with the bot.")
                return

            last_message_timestamp = send_message(dm_channel_id, prompt)
            new_message = get_new_messages(dm_channel_id, last_message_timestamp)

            # Save the initial story to a file
            save_story_to_file(new_message)
            
            # Send another prompt to Claude for analysis and revision
            analysis_text = analysis_prompt(new_message)
            last_analysis_timestamp = send_message(dm_channel_id, analysis_text)
            
            # Wait for Claude's revised response
            revised_message = get_new_messages(dm_channel_id, last_analysis_timestamp)

            # Save the revised story to a file named revised-story.txt
            save_story_to_file(revised_message, filename="revised-story.txt")

            # Format and display the revised story
            formatted_story = format_story(revised_message)
            display_story(formatted_story)

if __name__ == "__main__":
    main()
