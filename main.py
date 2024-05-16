from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import time

chatbot = ChatBot('Bot')

matematica = [
    "Quanto é 2 + 2?",
    "4",
    "Qual a raiz quadrada de 9?"
    "3",
    "Quanto é 3 elevado ao quadrado",
    "9"
]

geografia = [
    "Qual a capital de Santa Catarina",
    "Florianópolis",
    "Qual a capital do Brasil",
    "Brasília",
    "Em qual região está localizado o estado de São Paulo?",
    "Região Sudeste"
]

historia = [
    "Quem descobriu o Brasil?",
    "Pedro Alvares Cabral",
    "Em que ano Cristóvão Colombo chegou às Américas?",
    "1492",
    "Quem foi o primeiro presidente do Brasil?",
    "Marechal Deodoro da Fonseca"
]

trainer = ListTrainer(chatbot)

def chatbot_response(text):
    if text:
        response = chatbot.get_response(text)

        return response.text
    else:
        return "Desculpe, não entendi. Pode repetir, por favor?"

def solicita_disciplina():
    disciplina_escolhida = input("Bot: Por favor selecione uma das matérias disponíveis \n[1] - Matemática\n[2] - Geografia\n[3] - História\n ")

    disciplinas = {
        '1': matematica,
        '2': geografia,
        '3': historia
    }

    if disciplina_escolhida in disciplinas:
        trainer.train(disciplinas[disciplina_escolhida])
        return True
    else:
        return False

print("Bot: Boa tarde sou um bot que irá auxiliar nos seus estudos: ")
disciplina_escolhida = solicita_disciplina()
while True:
    if disciplina_escolhida:
        texto_usuario = input("Bot: Faça a sua pergunta: ")
        if texto_usuario == 'finalizar':
            print(f"Bot: Tchau! Até logo.")
            break

        start_time = time.time()
        chatbot_response_text = chatbot_response(texto_usuario)

        print(f"Bot: {chatbot_response_text}")

        end_time = time.time()
        response_time = end_time - start_time
        print(f"Tempo de resposta do bot: {response_time:.2f} segundos")
    else:
        disciplina_escolhida = solicita_disciplina()
