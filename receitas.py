import os
from groq import Groq

def space():
    print("\n")

os.environ["GROQ_API_KEY"] = "Insira a sua própria chave API"

client = Groq(api_key = os.environ.get("GROQ_API_KEY"),)

messages = []
usuario = "Escreva uma receita (de uma forma breve que seja composta pelo nome, ingredientes e modo de preparo), utilizando a linha mais recente e contendo apenas os seguintes ingredientes: "

while True:
    space()
    text = input("Liste alguns ingredientes para obter uma receita completa ou 'sair' para cancelar: ")
    usuario += text

    if text == "sair":
        space()
        print("Você fechou o programa.")
        break

    messages.append({"role": "user", "content": usuario})
    space()

    chat_completion = client.chat.completions.create(
        messages = messages,
        model = "llama-3.1-70b-versatile",
    )

    resposta = chat_completion.choices[0].message.content
    print("Receita: \n \n", resposta)

    messages.append({"role": "assistant", "content": resposta})
