import os
from groq import Groq

os.environ["GROQ_API_KEY"] = "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"

client = Groq(api_key = os.environ.get("GROQ_API_KEY"),)

messages = []
usuario = "Escreva uma receita (de uma forma breve que seja composta pelo nome, ingredientes e modo de preparo) que contenha apenas os seguintes ingredientes: "

while True:
    usuario += input("Liste alguns ingredientes para obter uma receita completa ou 'sair' para cancelar: ")

    if usuario.lower() == 'sair':
        print("Você fechou o programa.")
        break

    messages.append({"role": "user", "content": usuario})

    chat_completion = client.chat.completions.create(
        messages = messages,
        model = "llama-3.1-70b-versatile",
    )

    resposta = chat_completion.choices[0].message.content
    print("Receita: \n \n", resposta)

    messages.append({"role": "assistant", "content": resposta})