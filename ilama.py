import os
import openai

openai.api_base = "https://api.llama-api.com"

# supply your API key however you choose
openai.api_key = os.getenv('api_key')
functions = [
    {'name': 'information_extraction',
     'description': 'Extracts the relevant information from the passage.',
     'parameters': {
             'type': 'object',
             'properties': {
                 'sentiment': {'title': 'sentiment', 'type': 'string', 'description': 'the sentiment encountered in the passage'},
                 'aggressiveness': {'title': 'aggressiveness', 'type': 'integer', 'description': 'a 0-10 score of how aggressive the passage is'},
                 'language': {'title': 'language', 'type': 'string', 'description': 'the language of the passage'},
             }, 'required': []
     }
     }
]

completion = openai.ChatCompletion.create(model="llama-13b-chat",
                                          messages=[
                                              {"role": "user", "content": "Extract the desired information from the following passage.:\n\nI love you, but not so much!"}],
                                          functions=functions,
                                          function_call={
                                              "name": "information_extraction"}
                                          )
print(completion)
