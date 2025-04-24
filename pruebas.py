#Programa utilizado para calcular el costo de una compra
# nombre producto, precio unitario, cantidad de productos adquiridos, porcentaje de descuento que se aplicará si es que existe alguno.

#Se imprime un mensaje de bienvenidad
print("Bienvenido al super de RIWI")
# Bucle infinito para mantener el menú activo hasta que el usuario decida salir

while True:
# Muestra el menú de opciones
    print("      Menú Principal \n" 
    " 1. Registrar una compra \n" 
    " 2. Salir")
    # Solicita al usuario que seleccione una opción
    menu_option = input("Selecciona una opción. ")

    # Si el usuario elige registrar una compra
    if menu_option == "1" :
        # Solicita el nombre del producto

        name_product = (input("Ingresa el nombre de tu producto: "))
        # Solicita el precio unitario y valida que sea mayor a 0

        unity_price = float (input ("Ingresa el precio unitario de tu producto: "))
        if unity_price < 0:
            unity_price = float(input("Ingresa el precio unitario de tu producto, recuerda que debe ser mayor que cero: "))

        # Solicita la cantidad de productos y valida que sea al menos 1
        cant_product = int( input("Ingresa la cantidad a llevar de tu producto: "))
        if cant_product <= 0:
            cant_product = int(input("Ingrese nuevamente un valor mayor que cero, recuerda que debes llevar al menos un producto: "))

        # Solicita el descuento y verifica que esté en el rango correcto (0-100)
        discount_product = int (input("Ingresa el descuento de tu producto: "))
        if discount_product < 0 or discount_product > 100:
            discount_product = int(input("Ingrese nuevamente un valor de descuento válido, " \
                "recuerdad que los descuentos de RIWI están comprendidos entre 0% y 100%; Ingresa nuevamente el valor de tu descuento "))
        #Calcula el descuento aplicado
        parcial_price = unity_price * (discount_product / 100) # Valor del descuento sobre el precio unitario
        price_discount = unity_price - parcial_price # Precio unitario con descuento aplicado
        total = price_discount * cant_product # Precio total con descuento
        total_base = unity_price * cant_product # Precio total sin descuento
        print(f"El/la, {name_product}, tiene un valor total sin descuentos de: {total_base: .2f} con un descuento del {discount_product},%, ")
        print(f"Por ende el valor total de la compra con el descuento aplicado es de: {total: .2f} .")

    # Si el usuario elige salir    
    else:
        print(" Nos veremos en una futura compra. ")
        break # Sale del bucle y termina la ejecución del programa