# Crear un Diccionario
informacion_personal = {
    "nombre": "Andrés Shigui",
    "edad": 29,
    "ciudad": "Santiago de Píllaro",
    "profesion": "Ingeniero"
}

# Acceder y Modificar Valores
# Acceder al valor asociado con la clave "ciudad"
ciudad_actual = informacion_personal["ciudad"]
print("Ciudad actual:", ciudad_actual)

# Modificar el valor de la clave "ciudad"
informacion_personal["ciudad"] = "Ambato"
print("Ciudad modificada:", informacion_personal["ciudad"])

# Agregar una nueva clave-valor al diccionario
informacion_personal["profesion"] = "Desarrollador de software"
print("Profesión agregada:", informacion_personal["profesion"])

# Verificar Existencia de Claves
# Verificar si la clave "telefono" existe en el diccionario
if "telefono" not in informacion_personal:
    # Agregar la clave "telefono" con un número de teléfono ficticio
    informacion_personal["telefono"] = "555-1234"
    print("Teléfono agregado:", informacion_personal["telefono"])
else:
    print("La clave 'telefono' ya existe en el diccionario")

# Eliminar una Clave
# Eliminar la clave "edad" del diccionario
del informacion_personal["edad"]
print("Edad eliminada del diccionario")

# Imprimir el Diccionario Final
print("Diccionario final:")
print(informacion_personal)