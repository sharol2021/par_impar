# Programa para saber si un numero es impar o par

print("------------------------------------------")
print("------------EL RESULTADO ES:--------------")
print("------------------------------------------")
# input
x = int(input("Digite el valor de X: "))

# processing  
r= x%2 
if r==0:
    msj="PAR"
else:
    msj="IMPAR"    

# output
print("el numero " + str (r)+ " es " + msj)
print("---------------------")
print("-----RESULTADOS------")
print("---------------------")