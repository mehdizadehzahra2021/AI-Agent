import ollama
response= ollama.chat(
    model="qwen3:4b",
    messages=[{"role":"user","content":"Say hello in exactly one sentence."}],
    think=False,
    )
print(response.message.content)
