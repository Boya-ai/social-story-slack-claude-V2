# This function takes in the story and an optional filename (defaulting to claude-story.txt).
# It then writes the story to the file using UTF-8 encoding.

def save_story_to_file(story, filename="claude-story.txt"):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(story)



