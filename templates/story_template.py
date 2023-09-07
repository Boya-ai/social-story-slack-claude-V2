# This file will contain the predefined prompt for the social story.

def generate_story_prompt(gender, name, age, situation):
    prompt = f"""
    As an AI language model embodying the roles of Carol Gray, Psychologist, Therapist, Special Education Teacher, Speech and Language Therapist, Occupational Therapist, Autism Specialist, and Behavior Analyst, your task is to create a social story strictly in the first-person perspective for a {gender} child named {name}, who is {age} years old, about {situation}. 
    Do not invent or introduce fictitious names of places or people in the story.
    The story must be written in correct Hebrew language suitable for kids. It must adhere to Carol Gray's Social Stories 10.2 criteria and be age-appropriate. It should use a positive and patient tone, provide clear guidance on social cues and appropriate responses, and be reassuring and supportive. The story should describe more than it directs, and it should answer relevant 'wh' questions that describe context, including WHERE, WHEN, WHO, WHAT, HOW, and WHY.

    Ensure the language, sentence length, and complexity of the story are suitable for a {age}-year-old child. If {age} is between 2 and 4, use simple sentences (1-3 per page) with basic vocabulary. The directives should be clear, concrete actions. Familiar scenarios or elements should be included. If {age} is between 5 and 7, use 3-5 sentences per page with expanded vocabulary. Introduce a wider range of situations. If {age} is over 8, use detailed paragraphs with advanced vocabulary and descriptions. Discuss abstract thoughts and emotions.

    Here's the structure you should follow:

    - Title: A clear title that reflects the content of the story. For example, 'Going to the Dentist'.
    - Introduction: The introduction should introduce the topic. For example, 'I sometimes need to go to the dentist to keep my teeth healthy.'
        The introduction should follow these guidelines:
        - Do not include any identifying details about a specific character or their age - this is a social story.
        - Start with a general sentence introducing the topic, such as 'Sometimes it's hard to focus in class when there's a lot of noise.'
        - Briefly describe the challenge or problem the story will address.
        - Use concise, simple sentences.
        - Make sure the introduction directly relates to the topic and content of the story.
    - Body: The body should describe the situation in detail, including:
        - Descriptive sentences: These should state facts or set the scene. For example, 'The dentist's office is a place where I go to keep my teeth clean and healthy.'
        - Perspective sentences: These should describe my reactions, feelings, or thoughts. For example, 'I feel happy when I sit still in the chair.'
        - Problem sentences: These should identify the problem or challenge. For example, 'Sometimes, I might feel scared when the dentist is checking my teeth.'
        - Coping sentences: These should suggest coping strategies or positive affirmations. For example, 'I can squeeze my toy when I feel scared.'
        - Directive sentences: These should suggest appropriate responses or behaviors. For example, 'I can try to sit still and open my mouth wide when the dentist asks me to.'
        - Affirmative sentences: These should reinforce a key point or express a shared value or belief. For example, 'Going to the dentist is important because it helps keep my teeth clean and healthy.'
    - Conclusion: The conclusion should summarize the story and reinforce the desired behavior. For example, 'Even though going to the dentist can be scary, I know it's important for keeping my teeth healthy. I can do it!'

    Please format the output story as follows:
    - Title: [Title of the story]
    - Introduction: [Introduction of the story]
    - Body: 
        - Descriptive sentences: [Descriptive sentences]
        - Perspective sentences: [Perspective sentences]
        - Problem sentences: [Problem sentences]
        - Coping sentences: [Coping sentences]
        - Directive sentences: [Directive sentences]
        - Affirmative sentences: [Affirmative sentences]
    - Conclusion: [Conclusion of the story]
    """
    return prompt



def analysis_prompt(story):
    return f"""
    Claude, perform a detailed analysis and revision of the following story considering the Social Stories 10.2 criteria and age-specific guidelines:

    1. **The Social Story Goal**: Ensure the story shares accurate information with content, format, and voice that is descriptive, meaningful, and safe for the audience.
    2. **Two-Step Discovery**: Check if the story gathers relevant information to improve understanding and identify specific topics.
    3. **Three-Parts & a Title**: Confirm the story has a clear title, introduction, body, and conclusion.
    4. **Four·mat Makes it Mine!**: Verify the format is tailored to the individual's abilities, attention span, learning style, and interests.
    5. **Five Factors Define Voice & Vocabulary**: Ensure the story has a supportive voice and vocabulary, using first/third person, correct tense, a positive tone, literal accuracy, and clear meaning.
    6. **Six Questions Guide Story Development**: Does the story answer 'WH' questions like WHERE, WHEN, WHO, WHAT, HOW, and WHY?
    7. **Seven is About Sentences**: Confirm it consists of Descriptive Sentences and potentially Coaching Sentences.
    8. **A Gr·eight! Formula**: Check if the story describes more than it directs.
    9. **Nine to Refine**: Ensure the story has been reviewed and revised to meet the criteria.
    10. **Ten Guides to Editing and Implementation**: Confirm the story is introduced and reviewed correctly with the audience.
    11. **First-Person Perspective**: Ensure the story is written strictly in the first-person perspective.

    **Age-specific Guidelines**:
    - For **2-4 age group**: Ensure the story is simple, concise, relates to familiar settings, uses repetitive phrasing, and provides tangible examples.
    - For **5-7 age group**: The story should have incremental complexity, introduce basic emotions, have interactive components, address real-life school scenarios.
    - For **over 8 age group**: Use advanced language, delve into diverse emotions, introduce problem-solving scenarios, address real-world situations, and encourage feedback or discussions.

    Additionally, ensure that the story writen in hebrew text that adheres to proper grammar and syntax rules.

    example:
    - Title: A clear title that reflects the content of the story. For example, 'Going to the Dentist'.
    - Introduction: The introduction should introduce the topic. For example, 'I sometimes need to go to the dentist to keep my teeth healthy.'
        The introduction should follow these guidelines:
        - Do not include any identifying details about a specific character or their age - this is a social story.
        - Start with a general sentence introducing the topic, such as 'Sometimes it's hard to focus in class when there's a lot of noise.'
        - Briefly describe the challenge or problem the story will address.
        - Use concise, simple sentences.
        - Make sure the introduction directly relates to the topic and content of the story.
    - Body: The body should describe the situation in detail, including:
        - Descriptive sentences: These should state facts or set the scene. For example, 'The dentist's office is a place where I go to keep my teeth clean and healthy.'
        - Perspective sentences: These should describe my reactions, feelings, or thoughts. For example, 'I feel happy when I sit still in the chair.'
        - Problem sentences: These should identify the problem or challenge. For example, 'Sometimes, I might feel scared when the dentist is checking my teeth.'
        - Coping sentences: These should suggest coping strategies or positive affirmations. For example, 'I can squeeze my toy when I feel scared.'
        - Directive sentences: These should suggest appropriate responses or behaviors. For example, 'I can try to sit still and open my mouth wide when the dentist asks me to.'
        - Affirmative sentences: These should reinforce a key point or express a shared value or belief. For example, 'Going to the dentist is important because it helps keep my teeth clean and healthy.'
    - Conclusion: The conclusion should summarize the story and reinforce the desired behavior. For example, 'Even though going to the dentist can be scary, I know it's important for keeping my teeth healthy. I can do it!'
    
    
     
    Analyze and provide a revised version of the story that meets all these standards:

    {story}

    Please format the revised output story as follows:
    - Title: [Title of the story]
    - Introduction: [Introduction of the story]
    - Body:
        - Descriptive sentences: [Descriptive sentences]
        - Perspective sentences: [Perspective sentences]
        - Problem sentences: [Problem sentences]
        - Coping sentences: [Coping sentences]
        - Directive sentences: [Directive sentences]
        - Affirmative sentences: [Affirmative sentences]
    - Conclusion: [Conclusion of the story]
    """
