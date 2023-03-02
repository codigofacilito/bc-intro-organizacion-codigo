def clearTerminal():
  # Hay mejores formas pero por ahora usemos esta
  saltosDeLinea = "\n" * 100
  print(saltosDeLinea)

preguntas = [
    "¿Cuál es tu nombre?",
    "¿Cuál es tu edad?",
    "¿Cuál es tu nacionalidad?",
]
respuestas = []
print("Hola, y bienvenido a la encuesta \n Contesta las siguientes preguntas:")

for pregunta in preguntas:
    print(pregunta)
    respuestas.append(input())
    clearTerminal()

print("Estas fueron tus respuestas: ")
for respuesta in respuestas:
    print(respuesta)

