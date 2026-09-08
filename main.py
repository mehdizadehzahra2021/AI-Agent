import ollama
from datetime import datetime
def get_time():
    return datetime.now().strftime("%H:%M:%S")
messages =[{"role":"user","content":"hello! introduce yourself in one sentence"}]
messages.insert(0,{"role":"system","content":"you have a tool called get_time that returns the current time."})
response= ollama.chat(
    model="gemma3:4b", 
    messages =messages
)

messages.append(response["message"])
print (response["message"],["content"])
messages.append({"role":"user","content":"say in one sentence what do you do now"})

response= ollama.chat(
    model="gemma3:4b", 
    messages =messages
)
messages.append(response["message"])
print (response["message"],["content"])
while True:
    user_input = input ("you:")
    if "time" in user_input.lower():
        tool_result = get_time()
        messages.append({"role":"user","content":f"The current time is {tool_result}"})
        print("TOOL result:",tool_result)
        continue
    messages.append({"role":"user","content":user_input})
    response= ollama.chat(
        model="gemma3:4b", 
        messages =messages
    )
    print (response["message"],["content"])
    messages.append(response["message"])


