
alumnos = []
profesores = []
cursos = {}

# Agregar un curso
def agregar_curso():
    codigo = input("Ingrese el código del curso: ")
    nombre = input("Ingrese el nombre del curso: ")
    cursos[codigo] = nombre
    print(f"Curso '{nombre}' agregado exitosamente.\n")

# Agregar un alumno
def agregar_alumno():
    nombre = input("Ingrese el nombre del alumno: ")
    cedula = input("Ingrese la cédula del alumno: ")
    curso = input("Ingrese el código del curso: ")
    
    if curso not in cursos:
        print(f"Error: El curso '{curso}' no existe.\n")
        return
    
    try:
        nota = float(input("Ingrese la nota del alumno: "))
    except ValueError:
        print("Error: La nota debe ser un número.\n")
        return
    
    alumno = {
        'nombre': nombre,
        'cedula': cedula,
        'curso': curso,
        'nota': nota
    }
    alumnos.append(alumno)
    print(f"Alumno '{nombre}' agregado exitosamente.\n")

# Agregar un profesor
def agregar_profesor():
    nombre = input("Ingrese el nombre del profesor: ")
    cedula = input("Ingrese la cédula del profesor: ")
    curso = input("Ingrese el código del curso: ")
    
    if curso not in cursos:
        print(f"Error: El curso '{curso}' no existe.\n")
        return
    
    profesor = {
        'nombre': nombre,
        'cedula': cedula,
        'curso': curso
    }
    profesores.append(profesor)
    print(f"Profesor '{nombre}' agregado exitosamente.\n")

# Promedio de notas
def promedio_notas():
    if not alumnos:
        return 0
    total_notas = sum(alumno['nota'] for alumno in alumnos)
    return total_notas / len(alumnos)

# Rendimiento académico
def clasificar_alumnos():
    clasificacion = {'aprobados': [], 'aplazados': [], 'reprobados': []}
    
    for alumno in alumnos:
        if alumno['nota'] > 70:
            clasificacion['aprobados'].append(alumno)
        elif 60 <= alumno['nota'] <= 69:
            clasificacion['aplazados'].append(alumno)
        else:
            clasificacion['reprobados'].append(alumno)
    
    return clasificacion

# Nota por encima del promedio
def alumnos_sobre_promedio():
    promedio = promedio_notas()
    return len([alumno for alumno in alumnos if alumno['nota'] > promedio])

# Menú 
while True:
    print("\nMenú:")
    print("1. Agregar curso")
    print("2. Agregar alumno")
    print("3. Agregar profesor")
    print("4. Mostrar lista de alumnos")
    print("5. Mostrar promedio de notas")
    print("6. Mostrar clasificación de alumnos")
    print("7. Mostrar alumnos sobre el promedio")
    print("8. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        agregar_curso()
    elif opcion == "2":
        agregar_alumno()
    elif opcion == "3":
        agregar_profesor()
    elif opcion == "4":
        print("Lista de alumnos:", alumnos)
    elif opcion == "5":
        print("Promedio de notas:", promedio_notas())
    elif opcion == "6":
        print("Clasificación de alumnos:", clasificar_alumnos())
    elif opcion == "7":
        print("Alumnos con nota sobre el promedio:", alumnos_sobre_promedio())
    elif opcion == "8":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida, intente nuevamente.")
