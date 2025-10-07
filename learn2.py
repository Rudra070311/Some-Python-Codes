import json
import os
from datetime import datetime
import difflib

s = "Messiah: "
print("Hi! My name is Messiah, your personal AI in development.")
print("Enter 'bye' to exit.")
print("You can teach me too by:")
print("teach: your question -- my expected reply\n")

base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "chat.json")

if os.path.exists(file_path):
    try:
        with open(file_path, "r") as mem:
            memory = json.load(mem)
    except json.JSONDecodeError:
        print("Warning: Memory file was empty or broken. Starting fresh.")
        memory = {}
else:
    memory = {}

while True:
    userInp = input("User: ").lower().strip()

    if userInp == "bye":
        print(s, "I will remember you and your teachings. Bye!")    
        break

    elif userInp.startswith("teach:"):
        try:
            Part = userInp.replace("teach:", "").split("--")
            Ques = Part[0].strip()
            Ans = Part[1].strip()
            memory[Ques] = Ans
            print(s, f"Got it! When you ask '{Ques}', I'll answer '{Ans}'.")
            
            with open(file_path, "w") as mem:
                json.dump(memory, mem, indent=2)
        except:
            print(s, "Format error! Use:")
            print("teach: your question -- my expected reply")

    bestMatch = difflib.get_close_matches(userInp, memory.keys(), n=1, cutoff=0.8)
    
    if bestMatch:
        key = bestMatch[0]
        print(s, memory[key])
    elif "hi" in userInp or "hello" in userInp:
        print(s, "Hi!")
    elif "how are you" in userInp or "how you doing" in userInp:
        print(s, "I'm great. How are you?")
    elif "i am fine" in userInp:
        print(s, "Nice to hear that! Ask your question.")
    elif "your name" in userInp:
        print(s, "My name is Europa, your personal AI.")
    elif "time" in userInp:
        print(s, "The time is", datetime.now().strftime("%H:%M:%S"))
    elif "date" in userInp:
        print(s, "Today's date is", datetime.now().strftime("%d-%m-%Y"))
    else:
        print(s, "I don’t know that yet. You can teach me using:")
        print("teach: your question -- my expected reply")

with open(file_path, "w") as mem:
    json.dump(memory, mem, indent=2)