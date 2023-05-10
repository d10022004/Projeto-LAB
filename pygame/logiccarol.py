import random
random.seed()

bastão=0
ladobranco=0
ladomadeira=0

for i in range(1,5,1):
    bastão=random.randint(0,2)
    if(bastão == 1):
        print("bastão", i, "->Lado branco")
        ladobranco=ladobranco+1
    else:
        print("bastão", i, "->Lado de madeira")
        ladomadeira=ladomadeira+1

if(ladobranco == 0):
    print("Mova 5 quadrados e ganha uma jogada extra")
elif(ladobranco == 1):
    print("Mova 1 quadrado e ganha uma jogada extra")
elif(ladobranco == 2):
    print("Mova 2 quadrados ")
elif(ladobranco == 3):
    print("Mova 3 quadrados ")
elif(ladobranco == 4):
    print("Mova 4 quadrados e ganha uma jogada extra")