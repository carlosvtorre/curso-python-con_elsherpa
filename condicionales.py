#declaralos la variable 
# con el input lo que lee lo guarda en String 
calificacion = input ("Introduce tu calificación de la AZ-900: ")

# convertimos la variable calificacion que esta en String a int
calificacion = int (calificacion)

if calificacion < 700 :
    print ("Vees, por no estudiar") # Si la calificaion es menor a 700 imprime esto 
elif calificacion > 1000:
    print ("MIENTESS!!!, No puedes sacar mas de mil")
else :
    print ("felicidades pasa por tu certificado")


# Verificador de mayoria de edad
edad = input("Ingrese su edad: ")
edad = int (edad)

if edad >= 18 and edad <= 100 :
    print ("Bienvenido al mamitas puebla")
elif edad > 100 :
    print("Si vienes acompañado de tus abuelitos si te podemos fiar")
elif edad < 0 : 
    print ("ni que fueras viajero del tiempo")
else :
    print ("no puedes llevarte esos cigarros")