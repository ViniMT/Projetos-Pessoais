hellos = "Hello World\nHello World\nHello World"
print(hellos)

with open("hello3.txt", "w") as file:
    file.write("Hello World")

lista = ["Ludimilo", "Catarino", " Goiano", "Goiabado"]
with open("hello.txt", "w") as file:
    file.write(str(lista))

text = "MEU TEXTO"
with open("hello.txt", "w") as file:
    for pos in range(10):
        file.write(text + " PELA :"+ str(pos) + " VEZ\n")


