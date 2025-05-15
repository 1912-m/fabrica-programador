def banco():
    saldo=int(input("digite o saldo bancário"))
    saque= int( input("digite o valor de saque"))
    if saldo >= saque:
        saldo=saldo-saque
        print ("voce realizou um saque comsucesso. seu saldo é:", saldo)
    else:
        print("voce não possui saldo suficiente para realizar essa operação.")

def mediaaluno():
   
    nota1=int(input("digite a primeira nota"))
    nota2=int(input("digite a segunda nota"))
    media=(nota1+nota2)/2
    if media>=6:
        print("aprovado") 

    else:
        print("reprovado")
mediaaluno()