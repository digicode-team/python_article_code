"""
Este módulo explica como crear y manipular cadenas de texto

Para ejecutarlo, abre un terminal python3 (recomendamos ipython3) y
copia cada linea o cada grupo según te convenga
"""

# Las cadenas de texto se definen entre comillas de 4 formas
#   comillas dobles
text1 = "mi texto y una comilla simple (')"
#   simples
text2= 'mi texto y una comilla doble (")'
#   3 dobles
text3 = """mi texto con "comillas" de dos 'tipos'"""
#   3 simples
text4 ='''mi texto con caracteres de escape: \" o \' '''

print(text1, text2, text3, text4, sep="\n")


# Caracteres de escape
text5 = "Usa \" para escapar comillas dobles entre comillas dobles"
print(text5)


# Interpolar variables
number = 5
num_dict = {"num1": 3, "num2": 9}

text6 = "Interpola un número aquí %d y otro aquí %d." % (number, 6)
text7 = "Interpola aquí {} y otro aquí ({}).".format(number, 7)
text8 = "Interpola aquí {num1} y aquí ({num2}) otro.".format(num2=number, num1=8)
text9 = "Ahora {numo1} y ({num2}).".format(**num_dict)
text10 = f"Interpola números aquí {number} y aquí ({num_dict['numero2']})."

print(text5, text6, text7, text8, text9, text10, sep="\n")


# Manipular cadenas
base_text = "Python es un lenguaje de propósito general"

first_parte = base_text[:10]
second_parte = base_text[10:]
final = base_text[-5:]
middle_part = base_text[13:24]

print(first_part, second_part, final, middle_part, sep="\n")


# Algunas funciones propias de las cadenas de texto
base_text = "Python es un lenguaje de propósito general"

base_text.upper()  # Pasar a mayúsculas
base_text.title()  # Pasar a mayúsculas la primer letra de cada palabra
base_text.startswith("P")  # El texto empieza por P??


# Usa la ayuda (help) directamente en la terminal
help(str)
help(str.startswith)
help(base_text.startswith)
