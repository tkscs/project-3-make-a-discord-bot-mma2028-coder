from secret import my_username

"""
**Do NOT change the name of this function.**

This function will be called every time anyone says anything on a channel where the bot lives.

* It returns `True` if the bot notices something it wants to repond to.
* You can have certain words or patterns in the messages trigger the bot.
* You can have the bot respond differently to different users
"""
def should_i_respond(user_message, user_name):
    if "please replace all the vowels in this sentence with the letter u" in user_message:
      return True
    if "please replace all the vowels in this sentence with the letter a" in user_message:
        return True
    if "1234567890" in user_message:
        return True

def recite_pi():
   print(3.1415)
def roll_dice():
   return str(random.radint(1,6))

"""
**Do NOT change the name of this function.**

This function will be called every time the `should_i_respond` function returns `True`.

* This function returns a string.
* The bot will post the returned string on the channel where the original message was sent.
* You can have the bot respond differently to different messages and users
"""
import random
def shuffle_numbers(text):
    numbers = "1234567890"
    random.shuffle(numbers)
    shuffled = "".join(numbers)
    return shuffled
   




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


def respond(user_message, user_name):
    if "please replace all the vowels in this sentence with the letter u" in user_message:
      return replace_vowels(user_message)
    if "please replace all the vowels in this sentence with the letter a" in user_message:
      return replace_vowels(user_message)
    if "1234567890" in user_message:
      return shuffle_numbers(user_message)
    if "dice" in user_message:
       return roll_dice
    if "recite pi" in user_message:
       return recite_pi
