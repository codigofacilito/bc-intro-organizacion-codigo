nombre = "Cody" 

def saludar():
  global nombre
  nombre = "Uriel" 
  print("Hola", nombre)

saludar() 
print(nombre)