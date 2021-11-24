# 2. Crear un array con los siguientes datos "perro", "gato", 1, 100
print("2. Crear un array con los siguientes datos ""perro"", ""gato"", 1, 100")
valores = ["perro", "gato", 1, 100]

# 3. Mostrar de la segunda a la cuarta letra de la primera palabra del array anterior.
print("\n3. Mostrar de la segunda a la cuarta letra de la primera palabra del array anterior.")
print("\n", valores[0][1:4])

# 4. Mostrar la penultima letra de la segunda palabra
print("\n4. Mostrar la penultima letra de la segunda palabra")
print("\n", valores[1][-2])

# 5. En la tercera posición del array guardar el siguiente texto con este formato:
# "En un 
#    lugar de 
# la mancha..."
print("\n5. En la tercera posición del array guardar el siguiente texto con este formato:")
valores = """En un
    lugar de
  la mancha..."""
print("\n", valores[2])

# 6. Sumar al contenido de la cuarta posición la primera cifra de esta misma posición.
print("\n6. Sumar al contenido de la cuarta posición la primera cifra de esta misma posición.")
valores = ["gato", "perro", 1, 100]
numeros = str(valores[3])
suma = valores[3] + int(numeros[0])
print("\n", suma)

# 7. Agregar al final del array otro array: "tortuga", 200.
print("\n7. Agregar al final del array otro array: ""tortuga"", 200.")
valores.extend([["tortuga", 200]])
# valores += [["tortuga", 200]]
# valores.append(["tortuga", 200])
print("\n", valores)

