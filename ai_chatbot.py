import openai
import gradio

openai.api_base = "https://api.pawan.krd/cosmosrp/v1"
openai.api_key = "pk-pROKjkbQgvQMghKAWjjchiENXCaEEgzakjBUwjOlMdGiMCCS"

his = []
first_message = True
file_name = "Defalut"
def chat_bot(message):
        global first_message,file_name
        if first_message:
            file_name = message[:20]
            first_message = False
        his.append({"role": "user", "content": message})
        chat_completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=his
        )
        response = chat_completion.choices[0].message.content
        his.append({"role": "assistant", "content": response})
        with open(f"{file_name}.txt",'a',encoding="utf-8") as f:
            f.write(f"Message: {message}\n")
            f.write(f"Response: {response}\n")
        conversation = [(his[i]["content"],his[i+1]["content"]) for i in range(0,len(his)-1,2)]
        return "",conversation

with gradio.Blocks() as chatbot_ui:
    gradio.Markdown("""<h1><center> My Chatbot </center></h1>""")
    chatbot = gradio.Chatbot()
    txt = gradio.Textbox(show_label = False, placeholder="Enter text!!")
    submit = gradio.Button("Send")
    submit.click(chat_bot,inputs=txt,outputs=[txt,chatbot])

chatbot_ui.launch(share=True)