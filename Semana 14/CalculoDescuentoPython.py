def calcular_descuento(monto_compra, descuento=10):
    """Calcula el descuento según el monto total de la compra y una tasa de descuento.

    Parámetros:
        monto_compra (float): El monto total de la compra.
        descuento (float): La tasa de descuento como porcentaje. Predeterminado en 10%.

    Retorna:
        float: El monto del descuento.
    """
    # Calcula el descuento
    monto_descuento = monto_compra * (descuento / 100)

    # Retorna el monto del descuento
    return monto_descuento

# Llama a la función dos veces
monto_compra1 = 100
descuento1 = calcular_descuento(monto_compra1)
monto_final1 = monto_compra1 - descuento1

monto_compra2 = 200
descuento2 = calcular_descuento(monto_compra2, 20)
monto_final2 = monto_compra2 - descuento2

# Imprime los resultados
print(f"Para una compra de ${monto_compra1}, el descuento es ${descuento1:.2f},"
      f" y el monto final es ${monto_final1:.2f}.")
print(f"Para una compra de ${monto_compra2}, el descuento es ${descuento2:.2f},"
      f" y el monto final es ${monto_final2:.2f}.")