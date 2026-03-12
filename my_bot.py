import secret
from openai import OpenAI
import os
import random
my_openai_key = secret.my_openai_key
desired_words = 2000
max_token_limit = int(desired_words * 1.4)

jokes = [
    "why did the chicken cross the road? It wanted to go to the other side",
    "why was the math book sad? Because it had too many problems."
]
def tell_joke():
    return random.choice(jokes)
def random_number():
    return str(random.randint(1,100))
def roll_dice():
    return str(random.randint(1,6))
def count_vowels(text):
    vowels = "aeiou"
    count = 0

    for char in text.lower():
        if char in vowels:
            count += 1

    return count
def replace_vowels(text):
    vowels = "aieouAIEOU"
    new_text = ""

    for char in text:
        if char in vowels:
            if char.isupper():
                new_text += "U"
            else:
                new_text += "u"
        else:
            new_text += char

    return new_text


client = OpenAI(api_key=my_openai_key)

def get_ai_response(user_message, user_name):
    try:
        response = client.responses.create(
            model="gpt-4.1-mini", 
            input=f"{user_name} says: {user_message}",
            max_tokens=max_token_limit
    
        )
        return (response.output_text).strip()
        
            

    except Exception as e:
        print("OpenAI error:", repr(e))
        return "invalid"
    

def respond(user_message, user_name):
    msg = user_message.lower()
    if "hello" in msg:
      return "Hello!"
    if "please replace all the vowels in this sentence with the letter u" in user_message:
      return replace_vowels(user_message)
    if "number" in user_message:
      return random_number()
    if "dice" in user_message:
       return roll_dice()
    if "joke" in user_message:
       return tell_joke()
    if "bye" in user_message:
       return "bye"
    if "how are you" in user_message:
        return "I am your chatbot"
    if "what do you do" in user_message:
        return "I can give you answers for anything, tell you a joke, give you a random number betwen 1 and 100, roll a dice for you, and more"
    return get_ai_response(user_message, user_name)
def should_i_respond(user_message, user_name):

    return True  
