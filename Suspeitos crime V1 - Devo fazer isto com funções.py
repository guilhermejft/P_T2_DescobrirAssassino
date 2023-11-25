GrauDeSuspeito = 5

Q1 = input("Telefonou para a vítima? (s/n)")
if Q1.lower() != "s":
    GrauDeSuspeito -= 1
Q2 = input("Esteve no local do crime? (s/n)")
if Q2.lower() != "s":
    GrauDeSuspeito -= 1
Q3 = input("Mora perto da vítima? (s/n)")
if Q3.lower() != "s":
    GrauDeSuspeito -= 1
Q4 = input("Devia para a vítima? (s/n)")
if Q4.lower() != "s":
    GrauDeSuspeito -= 1
Q5 = input("Já trabalhou com a vítima? (s/n)")
if Q5.lower() != "s":
    GrauDeSuspeito -= 1

if GrauDeSuspeito == 3:
    print("Foi declarado suspeito")
elif 5 > GrauDeSuspeito > 3:
    print("Foi declarado cúmplice")
elif GrauDeSuspeito > 5:
    print("Foi declarado culpado")
else:
    print("Foi declarado inocente")