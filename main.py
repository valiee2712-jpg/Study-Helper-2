import questionary

def main():
    while True:
        nombre = input("¿Cómo te llamas? ")
        print("\nHola " + nombre + "," + " estoy aquí para ayudarte a estudiar ✨")

        nivel = questionary.select(
            "Selecciona tu nivel de estudios:",
            choices=[
                "1° de primaria",
                "2° de primaria",
                "3° de primaria",
                "4° de primaria",
                "5° de primaria",
                "6° de primaria",
                "1° de secundaria",
                "2° de secundaria",
                "3° de secundaria",
                "4° de secundaria",
                "5° de secundaria",
                "Universidad"
            ]
        ).ask()

        print(f"\nHas seleccionado: {nivel}. ¡A darle con todo al estudio! 🚀\n")

        facilidad = questionary.select(
          "¿Qué tan fácil memorizas/aprendes un tema?",
          choices=[
            "Muy fácil",
            "Normal",
            "Medio dificil",
            "Dificil",
            "Se me dificulta mucho"
          ]
        ).ask()

        if facilidad == "Muy fácil":
            print("\n¡Increíble! Tienes una mente muy ágil. ✨ Aprovecha esa velocidad para aprender cosas nuevas cada día.")
        elif facilidad == "Normal":
            print("\n¡Muy bien! Tienes un ritmo equilibrado. 📚 Con organización, no habrá tema que se te resista.")
        elif facilidad == "Medio dificil":
            print("\n¡Ánimo! El aprendizaje es un proceso. 🧠 A veces solo hace falta encontrar la técnica adecuada.")
        elif facilidad == "Dificil":
            print("\n¡No te rindas! Los temas difíciles son los que más nos hacen crecer. 💪 La constancia es tu mejor aliada.")
        elif facilidad == "Se me dificulta mucho":
            print("\n¡Eres un valiente! 🛡️ Estudiar algo que te cuesta requiere mucho coraje. Estoy aquí para apoyarte en el camino.")

        while True:
            # Nueva sección de cursos y notas con validación
            print("\n--- Registro de Cursos y Notas ---")
            cursos_y_notas = []

            while True:
                nombre_curso = input("\nNombre del curso (o escribe 'fin' para terminar): ").strip()
                
                if nombre_curso.lower() == 'fin':
                    break
                    
                if not nombre_curso:
                    print("❌ Error: El nombre del curso no puede estar vacío. Por favor, escribe un nombre.")
                    continue
                
                tipo_sistema = questionary.select(
                    f"¿Qué sistema de notas usas en {nombre_curso}?",
                    choices=[
                        "Letras (AD, A, B, C)",
                        "Números (0 al 20)",
                        "Números (0 al 100)"
                    ]
                ).ask()
                
                nota_final = ""
                if tipo_sistema == "Letras (AD, A, B, C)":
                    nota_final = questionary.select(
                        f"Selecciona tu nota para {nombre_curso}:",
                        choices=["AD", "A", "B", "C"]
                    ).ask()
                elif tipo_sistema == "Números (0 al 20)":
                    while True:
                        entrada = input(f"Escribe tu nota para {nombre_curso} (0-20): ")
                        if entrada.isdigit() and 0 <= int(entrada) <= 20:
                            nota_final = int(entrada)
                            break
                        else:
                            print("❌ Error: Por favor ingresa un número válido entre 0 y 20.")
                elif tipo_sistema == "Números (0 al 100)":
                    while True:
                        entrada = input(f"Escribe tu nota para {nombre_curso} (0-100): ")
                        if entrada.isdigit() and 0 <= int(entrada) <= 100:
                            nota_final = int(entrada)
                            break
                        else:
                            print("❌ Error: Por favor ingresa un número válido entre 0 y 100.")
                
                cursos_y_notas.append({
                    "curso": nombre_curso, 
                    "nota": nota_final,
                    "sistema": tipo_sistema
                })

            print("\n--- Tu Resumen de Notas y Recomendaciones ---")
            for item in cursos_y_notas:
                curso = item["curso"]
                nota = item["nota"]
                sistema = item["sistema"]
                letra_final = ""

                # Lógica de conversión adaptada
                if sistema == "Letras (AD, A, B, C)":
                    letra_final = nota
                elif sistema == "Números (0 al 20)":
                    if 18 <= nota <= 20:
                        letra_final = "AD"
                    elif 14 <= nota <= 17:
                        letra_final = "A"
                    elif 10 <= nota <= 13:
                        letra_final = "B"
                    else:
                        letra_final = "C"
                elif sistema == "Números (0 al 100)":
                    if 90 <= nota <= 100:
                        letra_final = "AD"
                    elif 80 <= nota <= 89:
                        letra_final = "A"
                    elif 70 <= nota <= 79:
                        letra_final = "B"
                    else:
                        letra_final = "C"

                # Mostrar resultado y mensaje motivacional
                print(f"\n📚 {curso}: {nota} ({letra_final})")
                
                if letra_final == "AD":
                    print("   ✨ Muy bien, estás en el logro destacado. Te ayudaremos a mantener y reforzar este nivel.")
                elif letra_final == "A":
                    print("   ✅ Buen trabajo, alcanzaste el logro esperado. Te ayudaremos a mejorar aún más.")
                elif letra_final == "B":
                    print("   🟡 Estás en proceso. Te ayudaremos a reforzar los temas para que subas.")
                elif letra_final == "C":
                    print("   💪 No te preocupes, estás comenzando. Te ayudaremos paso a paso.")

            input("\nPresiona Enter para continuar...")

            while True:
                # Menú principal de estudio
                estudiar = questionary.select(
                  "¿Necesitas estudiar?",
                  choices=[
                    "Ir",
                    "Editar perfil",
                    "Salir"
                  ]
                ).ask()

                if estudiar == "Editar perfil":
                    break # Rompe el ciclo de estudio para volver a preguntar el nombre
                elif estudiar == "Salir":
                    print(f"✨ ¡Hasta pronto, {nombre}! Mucho éxito en tus estudios.")
                    return # Sale completamente del programa

                if estudiar == "Ir":
                    actividades = questionary.checkbox(
                        "¿Qué necesitas estudiar?",
                        choices=[
                            "Tarea",
                            "Examen",
                            "Exposición",
                            "Solo quiero repasar"
                        ]
                    ).ask()

                    # Extraemos los nombres de los cursos registrados
                    nombres_cursos = [item["curso"] for item in cursos_y_notas]
                    datos_plan = []
                    
                    if actividades:
                        for actividad in actividades:
                            cursos_seleccionados = questionary.checkbox(
                                f"¿En qué cursos tienes {actividad}?",
                                choices=nombres_cursos
                            ).ask()
                            
                            if cursos_seleccionados:
                                for curso in cursos_seleccionados:
                                    detalle = ""
                                    if actividad == "Tarea":
                                        detalle = questionary.select(
                                            f"¿Qué tipo de tarea tienes en {curso}?",
                                            choices=[
                                                "Investigación",
                                                "Ejercicios / problemas",
                                                "Preguntas teóricas"
                                            ]
                                        ).ask()
                                    elif actividad == "Examen":
                                        detalle = questionary.select(
                                            f"¿Qué dificultad tiene el examen de {curso}?",
                                            choices=[
                                                "Fácil",
                                                "Media",
                                                "Difícil"
                                            ]
                                        ).ask()
                                    elif actividad == "Exposición":
                                        detalle = questionary.select(
                                            f"¿Qué duración tiene la exposición de {curso}?",
                                            choices=[
                                                "Corta",
                                                "Media",
                                                "Larga"
                                            ]
                                        ).ask()
                                    elif actividad == "Solo quiero repasar":
                                        detalle = "Repaso general"
                                    
                                    datos_plan.append({
                                        "curso": curso,
                                        "actividad": actividad,
                                        "detalle": detalle
                                    })
                            else:
                                print(f"⚠️ No seleccionaste ningún curso para {actividad}.")

                    # Preguntar por el tiempo disponible
                    tiempo = questionary.select(
                        "¿Cuánto tiempo tienes para estudiar hoy?",
                        choices=[
                            "30 minutos",
                            "1 hora",
                            "2 horas",
                            "3 horas",
                            "Más de 3 horas"
                        ]
                    ).ask()

                    # Mostrar el Plan de Estudio
                    print(f"\n--- 📝 TU PLAN DE ESTUDIO ({tiempo}) ---")
                    
                    if not datos_plan:
                        print("No hay actividades registradas para hoy.")
                    else:
                        # Ordenar: Exámenes primero
                        datos_plan.sort(key=lambda x: 0 if x["actividad"] == "Examen" else 1)

                        for item in datos_plan:
                            # Buscar la nota del curso
                            nota_actual = "Desconocida"
                            for c in cursos_y_notas:
                                if c["curso"] == item["curso"]:
                                    nota = c["nota"]
                                    sistema = c["sistema"]
                                    if sistema == "Letras (AD, A, B, C)":
                                        nota_actual = nota
                                    elif sistema == "Números (0 al 20)":
                                        if 18 <= nota: nota_actual = "AD"
                                        elif 14 <= nota: nota_actual = "A"
                                        elif 10 <= nota: nota_actual = "B"
                                        else: nota_actual = "C"
                                    elif sistema == "Números (0 al 100)":
                                        if 90 <= nota: nota_actual = "AD"
                                        elif 80 <= nota: nota_actual = "A"
                                        elif 70 <= nota: nota_actual = "B"
                                        else: nota_actual = "C"
                                    break

                            # Determinar prioridad y tiempo basado en nota y tiempo total
                            prioridad = "ALTA 🔥" if item["actividad"] == "Examen" else "Media 📝"
                            info_tiempo = ""
                            
                            # Reglas de flujo
                            if nota_actual in ["B", "C"]:
                                info_tiempo = "Más tiempo asignado (Refuerzo)"
                            elif nota_actual == "AD":
                                info_tiempo = "Repaso corto"

                            # Ajuste por tiempo total
                            metodo_base = ""
                            if "30 minutos" in tiempo or "1 hora" in tiempo:
                                metodo_base = "Microestudio"
                            else:
                                metodo_base = "Técnica Pomodoro"

                            print(f"\n📌 {item['curso']} - {item['actividad']} ({prioridad})")
                            if info_tiempo:
                                print(f"   ⏳ Gestión: {info_tiempo}")
                            
                            # Lógica de recomendaciones
                            recomendacion = ""
                            if item["actividad"] == "Tarea":
                                if "Investigación" in item["detalle"]:
                                    recomendacion = "Lectura guiada + resúmenes + mapas mentales"
                                elif "Ejercicios" in item["detalle"]:
                                    recomendacion = "Práctica intensiva + repaso activo"
                                else:
                                    recomendacion = "Repaso activo + método Feynman"
                            
                            elif item["actividad"] == "Exposición":
                                recomendacion = "Esquema + ensayo oral + práctica visual"
                            
                            elif item["actividad"] == "Examen":
                                if item["detalle"] == "Difícil" or nota_actual in ["B", "C"]:
                                    recomendacion = f"{metodo_base} + repaso activo + práctica intensiva"
                                else:
                                    recomendacion = f"{metodo_base} + repaso ligero + ejercicios"

                            elif item["actividad"] == "Solo quiero repasar":
                                recomendacion = "Flashcards + Repaso espaciado"
                            
                            else:
                                recomendacion = "Repaso general con técnica Pomodoro"

                            print(f"   💡 Método: {recomendacion}")

                    print(f"\n✨ ¡Mucho éxito, {nombre}! Confía en tu proceso y dale con todo. 🚀")
                    input("\nPresiona Enter para volver al menú...")

            if estudiar == "Editar perfil":
                break # Sale del bucle de estudio para volver a preguntar el nombre

if __name__ == "__main__":
    main()


 


