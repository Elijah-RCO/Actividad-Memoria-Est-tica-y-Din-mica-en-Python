# src/main.py
"""
Mini-Sistema de Registro de Calificaciones (Un estudiante fijo)
Autor: Esteban
"""

# -------------------------------
# Memoria Estática (Inmutable)
# -------------------------------
cursos = ("Matemáticas", "Física", "Programación", "Inglés")  # tupla fija
estudiante = "Juan Pérez"  # nombre fijo

# -------------------------------
# Memoria Dinámica (Mutable)
# -------------------------------
calificaciones = [None] * len(cursos)  # lista con un espacio para cada curso

# -------------------------------
# Funciones
# -------------------------------
def mostrar_menu():
    print("\n=== Registro de Calificaciones ===")
    print(f"👤 Estudiante: {estudiante}")
    print("1. Agregar/Modificar calificación")
    print("2. Eliminar calificación")
    print("3. Mostrar calificaciones")
    print("4. Calcular promedio final")
    print("5. Salir")

def agregar_modificar():
    print("Cursos disponibles:")
    for i, curso in enumerate(cursos, 1):
        print(f"{i}. {curso}")

    try:
        idx = int(input("Seleccione el curso (número): ")) - 1
        if idx < 0 or idx >= len(cursos):
            print("❌ Opción inválida.")
            return
        nota = float(input(f"Ingrese la calificación para {cursos[idx]}: "))
        calificaciones[idx] = nota
        print(f"✅ Calificación guardada: {cursos[idx]} → {nota}")
    except ValueError:
        print("❌ Entrada inválida.")

def eliminar():
    print("Cursos disponibles:")
    for i, curso in enumerate(cursos, 1):
        print(f"{i}. {curso}")
    try:
        idx = int(input("Seleccione el curso (número): ")) - 1
        if idx < 0 or idx >= len(cursos):
            print("❌ Opción inválida.")
            return
        calificaciones[idx] = None
        print(f"🗑️ Calificación eliminada para {cursos[idx]}.")
    except ValueError:
        print("❌ Entrada inválida.")

def mostrar():
    print(f"\n📘 Calificaciones de {estudiante}:")
    for curso, nota in zip(cursos, calificaciones):
        if nota is None:
            print(f" - {curso}: ❌ Sin calificación")
        else:
            print(f" - {curso}: {nota}")

def promedio():
    notas = [n for n in calificaciones if n is not None]
    if notas:
        prom = sum(notas) / len(notas)
        print(f"📊 Promedio final: {prom:.2f}")
    else:
        print("⚠️ No hay calificaciones registradas.")

# -------------------------------
# Programa principal
# -------------------------------
def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_modificar()
        elif opcion == "2":
            eliminar()
        elif opcion == "3":
            mostrar()
        elif opcion == "4":
            promedio()
        elif opcion == "5":
            print("👋 Saliendo del sistema...")
            break
        else:
            print("❌ Opción inválida.")

if __name__ == "__main__":
    main()

