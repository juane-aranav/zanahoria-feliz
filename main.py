#cuando yo tenía XXV años y mi madre L, mi primo felipe tenía XIV, mi primo esteban XVIII y mi tía XLIII

solicitud="Ingrese un texto el cual incluya números romanos en mayúsculas:\n "

numeros_romanos={"I":"1","V":"5","X":"10","L":"50","C":"100","D":"500","M":"1000"}

entrada=input(solicitud) #variable con la asignación del texto ingresado

separador=entrada.split() #lista con los strings de la entrada separados en los espacios

salida=[] #lista con los strings de "separador" pero con los números romanos traducidos

def traductor(n):


    """
    Traduce cadenas con números romanos en cadenas con números arábigos.

    n: str

    traductor("IX")
    >>> "9"
    """


    signos=0 #variable de tipo int que se encarga de determinar que signo gramatical está en un string

    if "," in n:
        n=n.replace(",","")
        signos=1

    if "." in n:
        n=n.replace(".","")
        signos=2

    if ";" in n:
        n=n.replace(";","")
        signos=3


    arabn=0 #variable de tipo int a la cual se le asignan los números romanos traducidos

    invhor=n[::-1] #variable que invierte horizontalmente los carácteres del string n

    pren=eval(numeros_romanos[invhor[0]]) #variable que identifica el valor anterior al ciclo actual de "i"
    

    for i in invhor:
        posi=eval(numeros_romanos[i])
        if pren>posi:
            arabn-=eval(numeros_romanos[i])
        else:
            arabn+=eval(numeros_romanos[i])
        pren=posi

    if signos==1:
        arabn=str(arabn)+","

    elif signos==2:
        arabn=str(arabn)+"."

    elif signos==3:
        arabn=str(arabn)+";"

    else:
        arabn=str(arabn)

    return arabn

for i in separador:
    try:
        salida.append(traductor(i))

    except:
        salida.append(i)


textra=" ".join(salida) #variable que añade a un string los valores de la lista "salida"

print(textra)