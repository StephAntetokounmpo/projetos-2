pontos = int(input("Quantos pontos você fez nessa partida? "))
assistencias = int(input("Quantas assistencias você fez nessa partida? "))
rebotes = int(input("Quantos rebotes você fez nessa partida? "))
idade = int(input("Qual sua Idade? "))
if not (pontos >= 5 and assistencias >= 5 and rebotes >= 5 and pontos <= 100 and assistencias <= 100 and rebotes <= 100):
    print("Valores de pontos, assistências ou rebotes fora do intervalo esperado.")
elif idade >= 19:
    print("Seja Bem vindo a NBA!")
elif not idade >= 19:
    print("Você não pode Entrar na NBA.")
if pontos <= 5 or assistencias <= 5 or rebotes <= 5:
    print("Não está muito bom, Continue treinando")
elif pontos >= 5 and pontos <= 10 or assistencias >= 5 and assistencias <= 10 or rebotes >= 5 and rebotes <= 10:
    print("está aceitavel, Mais pode melhorar, continue treinando!")
elif pontos >= 10 and pontos <= 20 or assistencias >= 10 and assistencias <= 15 or rebotes >= 10 and rebotes <= 15:
    print("Caramba um triplo duplo , Muito bom! Continue Treinando!")
elif pontos >= 15 and pontos <= 30 or assistencias >= 10 and assistencias <= 20 or rebotes >= 10 and rebotes <= 20:
    print("Muito bom, Rumo a MVP!!")
elif pontos >= 30 and pontos <= 100 and assistencias >= 20 and assistencias <= 100 or rebotes >= 20 and rebotes <= 100:
    print("Você está pegando fogo, Novo MVP!! #ONFIRE")
else:
    print("Tente de novo.")