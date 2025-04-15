from openai import OpenAI
import streamlit as st
open_api_key = st.secrets["openai_api_key"]

client = OpenAI(api_key=open_api_key)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": "Write a one-sentence bedtime story about a unicorn."
        }
    ]
)

print(completion.choices[0].message.content)
st.write('Enter a text prompt, and the model will generate a completion.')
st.write(completion.choices[0].message.content)
# import openai
# import streamlit as st

# # Set up your OpenAI API key
# openai.api_key = st.secrets["openai_api_key"]

# # Function to get completion from OpenAI API
# def generate_completion(prompt):
#     response = openai.Completion.create(
#         model="text-davinci-003",  # You can use "gpt-4" or another model
#         prompt=prompt,
#         max_tokens=100,
#         temperature=0.7,
#         top_p=1,
#         frequency_penalty=0,
#         presence_penalty=0
#     )
#     return response.choices[0].text.strip()

# # Streamlit app UI
# st.title('OpenAI Text Completion App')
# st.write('Enter a text prompt, and the model will generate a completion.')

# # Input for user to enter a prompt
# user_input = st.text_area("Enter your prompt here:")

# if st.button('Generate Completion'):
#     if user_input:
#         # Call the OpenAI API to generate a completion
#         completion = generate_completion(user_input)
#         st.subheader('Generated Text:')
#         st.write(completion)
#     else:
#         st.error('Please enter a prompt before clicking "Generate Completion".')
