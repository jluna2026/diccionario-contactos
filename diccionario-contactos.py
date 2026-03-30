# Crear un diccionario para almacenar contactos
contactos = {}

# Agregar datos
contactos["Ana"] = "0991234567"
contactos["Luis"] = "0987654321"
contactos["María"] = "0971112233"

# Mostrar la información almacenada
print("Lista de contactos:")
for nombre, telefono in contactos.items():
    print(f"{nombre}: {telefono}")

# Operación básica: buscar un contacto
buscar = "Luis"
if buscar in contactos:
    print(f"\nTeléfono de {buscar}: {contactos[buscar]}")
else:
    print(f"\n{buscar} no está en la lista de contactos.")

# Operación básica: eliminar un contacto
eliminar = "Ana"
if eliminar in contactos:
    del contactos[eliminar]
    print(f"\n{eliminar} ha sido eliminado de la lista.")
else:
    print(f"\n{eliminar} no está en la lista.")

# Mostrar la lista actualizada
print("\nLista actualizada de contactos:")
for nombre, telefono in contactos.items():
    print(f"{nombre}: {telefono}")