import ollama
from datetime import datetime
def get_time():
    """Get the current local time.
    Returns:
    The current local time.
    """
    return datetime.now().strftime("%H:%M:%S")
def calculator (a:float,b:float)->float:
    """Calculate the sum of tow numbers."""
    return a+b
messages =[{"role":"user","content":"hello! introduce yourself in one sentence"}]
messages.insert(0,{"role":"system","content":"you are a helpful assistant."
                   "Answer the user directly and conciesly."
                   "do not describe your reasoning or internal process."
                   "Do not mention tools unless necessary."
                   "Use the get_time tool only when the user ask for the current time."})
response= ollama.chat(
    model="qwen3:4b", 
    messages =messages, tools=[get_time,calculator],
    think=False
)
print(response.message)

messages.append(response["message"])
print (response["message"].content)
messages.append({"role":"user","content":"say in one sentence what do you do now"})

response= ollama.chat(
    model="qwen3:4b", 
    messages =messages,
    think=False
)
messages.append(response["message"])
print (response["message"].content)
while True:
    user_input = input ("you:")
    messages.append({"role":"user","content":user_input})
        #tool_result = get_time()
        #print("TOOL result:",tool_result)
        #messages.append({"role":"tool","content":tool_result})
    response= ollama.chat(
                model="qwen3:4b", 
                messages =messages
                ,tools=[get_time,calculator]
                ,think=False
                )
    
    messages.append(response.message)
    if response.message.tool_calls:
        for call in response.message.tool_calls:
            print("CALL:",call)
            if call.function.name=="get_time":
                result=get_time()
            elif call.function.name =="calculator":
                result=calculator(**call.function.arguments)
                print("TOOL:",call.function.name)
                print("ARGS:",call.function.arguments)
                print("result:",result)
            messages.append({
                    "role":"tool",
                    "tool_name":call.function.name,
                    "content":str(result)
                })
            print("TOOL RESULT:",result)
            #after tool only one time call model
    final_response=ollama.chat(
        model="qwen3:4b", 
         messages =messages,
         think=False
    )
    messages.append(final_response.message)
    print(final_response.message.content)
   
else:
    print(response.message.content)
    
    


