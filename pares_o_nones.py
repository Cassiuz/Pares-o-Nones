import random

print("Modificacion de juego \'Pares o Nones\'")

ordenador = random.randint(1, 2)
eleccion = input('¿Serán \'Pares\' o \'Nones\'?\n>>> ').lower()

if eleccion != 'pares' and eleccion != 'nones':
    print(f'Error: Tu eleccion debe ser \'pares\' o \'nones\'. Escribiste {eleccion}')

else:
    try:
        jugador = int(input('Ingrese su elecion(1 o 2)\n>>> '))

        if jugador != 1 and jugador != 2:
            print(f'Error: Solo 1 o 2 como datos válidos. Ingresaste {jugador}')
        else:
            suma = ordenador + jugador

            # determinar es pares o nones
            if suma % 2 == 0:
                resultado_int = 'pares'
            else:
                resultado_int = 'nones'
            
            # Comprobar si acertó
            if eleccion == resultado_int:
                resultado_str = 'Has acertado!\n'
            else:
                resultado_str = 'Has fallado.\n'

            # --- Mostrar resultados ---
            print(f'\n--- Resultados ---')
            print(f'La computadora eligió: {ordenador}')
            print(f'El usuario eligió: {jugador}')
            print(f'La suma es {suma}, que es \'{resultado_int}\'')
            print(f'Tú habias elegido: \'{eleccion}\'')
            print(resultado_str)

    except ValueError:
        print(f'Error: Debes ingresar un número (1 o 2)')
