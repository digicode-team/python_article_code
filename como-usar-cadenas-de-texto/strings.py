"""
Este módulo explica como crear y manipular cadenas de texto

Para ejecutarlo, abre un terminal python3 (recomendamos ipython3) y
copia cada linea o cada grupo según te convenga
"""

# Las cadenas de texto se definen entre comillas de 4 formas
#   comillas dobles
texto2 = "mi texto y una comilla simple (')"
#   simples
texto1 = 'mi texto y una comilla doble (")'
#   3 dobles
texto3 = """mi texto con "comillas" de dos 'tipos'"""
#   3 simples
texto4 ='''mi texto con caracteres de escape: \" o \' '''

print(texto1, texto2, texto3, texto4, sep="\n")


# Caracteres de escape
texto5 = "Usa \" para escapar comillas dobles entre comillas dobles"
print(texto5)


# Interpolar variables
numero = 5
num_dict = {"numero1": 3, "numero2": 9}

texto6 = "Interpola un número aquí %d y otro aquí %d." % (numero, 6)
texto7 = "Interpola aquí {} y otro aquí ({}).".format(numero, 7)
texto8 = "Interpola aquí {num1} y aquí ({num2}) otro.".format(num2=numero, num1=8)
texto9 = "Ahora {numero1} y ({numero2}).".format(**num_dict)
texto10 = f"Interpola números aquí {numero} y aquí ({num_dict['numero2']})."

print(texto5, texto6, texto7, texto8, texto9, texto10, sep="\n")


# Manipular cadenas
texto_base = "Python es un lenguaje de propósito general"

primera_parte = texto_base[:10]
segunda_parte = texto_base[10:]
final = segunda_parte = texto_base[-5:]
medio = texto_base[13:24]

print(primera_parte, segunda_parte, final, medio, sep="\n")


# Algunas funciones propias de las cadenas de texto
texto_base = "Python es un lenguaje de propósito general"

texto_base.upper()  # Pasar a mayúsculas
texto_base.title()  # Pasar a mayúsculas la primer letra de cada palabra
texto_base.startswith("P")  # El texto empieza por P??


# Usa la ayuda (help) directamente en la terminal
help(str)
help(str.startswith)
help(texto_base.startswith)
