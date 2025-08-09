def inventarios():
    inventario_productos= {}
    
    print("Bienvenido al inventario: \n por favor seleccione una opcion\n\n")    
    
    while True:
        opcion = int(input("Opción 1: Agregar producto\n Opción 2 : Actualizar producto \n Opción 3 : Eliminar producto \n Opción 4: Mostrar Inventario\n Opción 5: Salir del inventario \n Escriba su opción : "))
    
        if opcion == 1:
           while True:
                    print("\n--- Agregar producto ---")
                    producto = input("Nombre del producto: ").strip().lower()
                    cantidad = int(input("Cantidad: "))
                    inventario_productos[producto] = cantidad
                    continuar = input("¿Agregar más productos? (si/no): ").strip().lower()
                    if continuar == 'no':
                        break
            
        elif opcion == 2:
            print("Actualizar Productos")
            producto_actualizar = input("Ingrese el nombre del producto que quiere actualizar: ")
            if producto_actualizar in inventario_productos:
                cantidad_actualizar = int(input("Ingrese la nueva cantidad: "))
                
                inventario_productos.update({producto_actualizar: cantidad_actualizar})
            else:
                print("El producto no existe en la lista")
        elif opcion == 3:
            print("Eliminar productos")
            eliminar_producto= input("Escriba el productos que quiere eliminar del inventario: ")
            if producto in inventario_productos:
                del inventario_productos[eliminar_producto]
                print(f"✅ '{producto}' eliminado.")
            else:
                print(f"⚠️ El producto '{producto}' no está en el inventario.")
        elif opcion == 4:
            print("\n--- Inventario actual ---")
            if  not inventario_productos:
                print("⚠️ El inventario está vacío.\n")
            else:
                for producto, cantidad in inventario_productos.items():
                    print(f"📦 {producto}: {cantidad}") 
        elif opcion == 5:
            print(f"Saliendo del inventario")
            break
inventarios()