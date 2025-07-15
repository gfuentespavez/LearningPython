def calcular_ingredientes(base_peso, proporcion):
    return round(base_peso * proporcion, 1)

def receta_pan_normal(peso_pan, tipo):
    proporciones = {
        'agua': 330 / 900,
        'aceite': 36 / 900,
        'sal': 10 / 900,
        'azúcar': 24 / 900 if tipo == 'aireado' else 12 / 900,
        'harina': 560 / 900,
        'levadura': 4 / 900 if tipo == 'aireado' else 2.5 / 900
    }

    print(f"\n🧾 Receta de Pan Normal ({tipo}) para {peso_pan:.0f}g:")
    for k, v in proporciones.items():
        print(f"{k.capitalize()}: {calcular_ingredientes(peso_pan, v)} g")
    print("\n📟 Programa sugerido: Pan blanco/francés | Tiempo: 3h50 | Corteza: media")

def receta_pan_cerveza(peso_pan, alcohol):
    proporciones = {
        'cerveza': 330 / 900,
        'aceite': 36 / 900,
        'sal': 10 / 900,
        'azúcar': 12 / 900 if alcohol == 'sin' else 0,
        'harina': 560 / 900,
        'levadura': 4 / 900
    }

    print(f"\n🧾 Receta de Pan con Cerveza ({'sin alcohol' if alcohol == 'sin' else 'con alcohol'}) para {peso_pan:.0f}g:")
    for k, v in proporciones.items():
        if v > 0:
            print(f"{k.capitalize()}: {calcular_ingredientes(peso_pan, v)} g")
    print("\n📟 Programa sugerido: Pan blanco/francés | Tiempo: 3h50 | Corteza: media u oscura")

def receta_ciabatta(peso_pan, metodo):
    # Receta base para 900 g
    proporciones = {
        'harina': 500 / 900,
        'agua': 375 / 900,
        'sal': 10 / 900,
        'levadura': 3 / 900,
        'aceite': 20 / 900,
        'azúcar': 5 / 900
    }

    print(f"\n🧾 Receta de Ciabatta ({metodo}) para {peso_pan:.0f}g:")
    for k, v in proporciones.items():
        print(f"{k.capitalize()}: {calcular_ingredientes(peso_pan, v)} g")

    if metodo == "panificadora":
        print("\n📟 Programa sugerido: Pan blanco o francés | Tiempo: 3h50 | Corteza: media")
        print("⚠️ Masa muy pegajosa. No agregar harina extra. Dejar que la máquina trabaje.")
    else:
        print("\n🔧 Procedimiento artesanal:")
        print("1. Usa la panificadora solo en modo AMASADO (1er ciclo).")
        print("2. Saca la masa, deja fermentar 1–2h en bowl aceitado.")
        print("3. Dobla la masa sobre sí misma con espátula aceitada.")
        print("4. Deja reposar 30 min más. No formes con fuerza.")
        print("5. Hornea en horno muy caliente (230 °C) con vapor 20–25 min sobre piedra o bandeja pre-calentada.")
        print("🔥 Resultado: corteza crujiente, miga alveolada, puro pan rústico.")

def main():
    print("🍞 Panificador Pro v2.0 🍺")
    print("1. Pan normal")
    print("2. Pan con cerveza")
    print("3. Pan tipo ciabatta")
    opcion = input("Selecciona tipo de pan (1, 2 o 3): ").strip()

    try:
        peso_pan = int(input("Ingresa el peso del pan deseado (ej: 900): ").strip())
    except ValueError:
        print("❌ Error: Debes ingresar un número válido.")
        return

    if opcion == "1":
        print("\n¿Prefieres un pan más aireado o con más sabor?")
        print("1. Más aireado")
        print("2. Más sabor")
        tipo = input("Selecciona (1 o 2): ").strip()
        tipo = "aireado" if tipo == "1" else "sabor"
        receta_pan_normal(peso_pan, tipo)

    elif opcion == "2":
        print("\n¿Usarás cerveza con o sin alcohol?")
        print("1. Con alcohol")
        print("2. Sin alcohol")
        tipo_cerveza = input("Selecciona (1 o 2): ").strip()
        alcohol = "con" if tipo_cerveza == "1" else "sin"
        receta_pan_cerveza(peso_pan, alcohol)

    elif opcion == "3":
        print("\n¿Quieres hacerla completa en panificadora o usar horno?")
        print("1. Completa en panificadora")
        print("2. Solo amasado, horneado artesanal")
        metodo = input("Selecciona (1 o 2): ").strip()
        metodo = "panificadora" if metodo == "1" else "artesanal"
        receta_ciabatta(peso_pan, metodo)

    else:
        print("❌ Opción no válida.")

if __name__ == "__main__":
    main()
