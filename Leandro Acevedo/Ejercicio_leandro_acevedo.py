# Mamma Mia Pizzeria ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
# Los ingredientes para cada tipo de pizza aparecen a continuación.

# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no y en función de su respuesta le 
# muestre un menú con los ingredientes disponibles para que elija.

# Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas.

# Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.


# 1. Mostrar menú de bienvenida
print("Bienvenido a Mamma Mia Pizzeria\n")

# 2. Preguntar al usuario el tipo de pizza que desea.
print("Que tipo de pizza desea?\n \n1. Vegetariana\n2. No vegetariana\n")

# 3. Leer la opción del usuario
tipo_pizza = int(input("Ingrese el numero correspondiente a su eleccion: (1 o 2): "))

# 4. deffinir ingredientes base
ingredientes_base = ["mozzarella", "tomate"]

# 5. opcion 1: pizza vegetariana
if tipo_pizza == 1:
    print("\nUsted ha elegido una pizza vegetariana.\n")
    ingredientes_vegetarianos = ["Pimiento", "Tofu"]
    print("Ingredientes disponibles:")
    for i, ingrediente in enumerate(ingredientes_vegetarianos, start=1):
        print(f"{i}. {ingrediente}")
    
    opcion_ingrediente = int(input("\nSeleccione un ingrediente adicional (1 o 2): "))
    ingrediente_seleccionado = ingredientes_vegetarianos[opcion_ingrediente - 1]
    
    # Mostrar resultado
    print(f"\nSu pizza vegetariana lleva: {', '.join(ingredientes_base + [ingrediente_seleccionado])}")

# 6. opcion 2: pizza no vegetariana
elif tipo_pizza == 2:
    print("\nUsted ha elegido una pizza no vegetariana.\n")
    ingredientes_no_vegetarianos = ["Peperoni", "Jamón", "Salmón"]
    print("Ingredientes disponibles:")
    for i, ingrediente in enumerate(ingredientes_no_vegetarianos, start=1):
        print(f"{i}. {ingrediente}")
    
    opcion_ingrediente = int(input("\nSeleccione un ingrediente adicional (1, 2 o 3): "))
    ingrediente_seleccionado = ingredientes_no_vegetarianos[opcion_ingrediente - 1]
    
    # Mostrar resultado
    print(f"\nSu pizza no vegetariana lleva: {', '.join(ingredientes_base + [ingrediente_seleccionado])}")
    print("\n¡Buen provecho!")
else:
    print("\nOpción no válida. Por favor, elija 1 o 2 para seleccionar el tipo de pizza.")



