import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="Study Helper", page_icon="✨")

def main():
    st.title("✨ Study Helper")
    
    # Inicializar estado de la sesión para guardar datos del perfil y notas
    if 'nombre' not in st.session_state:
        st.session_state.nombre = ""
    if 'nivel' not in st.session_state:
        st.session_state.nivel = ""
    if 'cursos_y_notas' not in st.session_state:
        st.session_state.cursos_y_notas = []
    if 'etapa' not in st.session_state:
        st.session_state.etapa = "perfil"

    # --- BARRA LATERAL (Perfil) ---
    with st.sidebar:
        st.header("👤 Perfil")
        if st.session_state.nombre:
            st.write(f"**Usuario:** {st.session_state.nombre}")
        if st.session_state.nivel:
            st.write(f"**Nivel:** {st.session_state.nivel}")
        
        if st.button("🔄 Editar Perfil"):
            st.session_state.etapa = "perfil"
            st.rerun()

    # --- ETAPA 1: CONFIGURACIÓN DE PERFIL ---
    if st.session_state.etapa == "perfil":
        st.header("Configura tu perfil")
        nombre = st.text_input("¿Cómo te llamas?", value=st.session_state.nombre)
        nivel = st.selectbox("Selecciona tu nivel de estudios:", [
            "1° de primaria", "2° de primaria", "3° de primaria", "4° de primaria", "5° de primaria", "6° de primaria",
            "1° de secundaria", "2° de secundaria", "3° de secundaria", "4° de secundaria", "5° de secundaria", "Universidad"
        ], index=0 if not st.session_state.nivel else ["1° de primaria", "2° de primaria", "3° de primaria", "4° de primaria", "5° de primaria", "6° de primaria", "1° de secundaria", "2° de secundaria", "3° de secundaria", "4° de secundaria", "5° de secundaria", "Universidad"].index(st.session_state.nivel))
        
        facilidad = st.select_slider("¿Qué tan fácil memorizas/aprendes un tema?", 
            options=["Se me dificulta mucho", "Dificil", "Medio dificil", "Normal", "Muy fácil"])

        if st.button("Guardar Perfil y Continuar"):
            if nombre:
                st.session_state.nombre = nombre
                st.session_state.nivel = nivel
                st.session_state.etapa = "notas"
                st.rerun()
            else:
                st.error("Por favor, ingresa tu nombre.")

    # --- ETAPA 2: REGISTRO DE CURSOS Y NOTAS ---
    elif st.session_state.etapa == "notas":
        st.header(f"📚 Registro de Cursos para {st.session_state.nombre}")
        
        with st.form("form_cursos"):
            col1, col2, col3 = st.columns(3)
            with col1:
                nuevo_curso = st.text_input("Nombre del curso")
            with col2:
                sistema = st.selectbox("Sistema de notas", ["Letras (AD, A, B, C)", "Números (0-20)", "Números (0-100)"])
            with col3:
                if sistema == "Letras (AD, A, B, C)":
                    nota = st.selectbox("Nota", ["AD", "A", "B", "C"])
                elif sistema == "Números (0-20)":
                    nota = st.number_input("Nota", 0, 20, 10)
                else:
                    nota = st.number_input("Nota", 0, 100, 50)
            
            submit_curso = st.form_submit_button("Añadir Curso")
            if submit_curso and nuevo_curso:
                st.session_state.cursos_y_notas.append({
                    "curso": nuevo_curso,
                    "nota": nota,
                    "sistema": sistema
                })

        if st.session_state.cursos_y_notas:
            st.subheader("Tus Cursos Registrados")
            for i, item in enumerate(st.session_state.cursos_y_notas):
                st.write(f"- **{item['curso']}**: {item['nota']} ({item['sistema']})")
            
            if st.button("Generar Plan de Estudio 🚀"):
                st.session_state.etapa = "estudio"
                st.rerun()

    # --- ETAPA 3: PLAN DE ESTUDIO ---
    elif st.session_state.etapa == "estudio":
        st.header("📝 Plan de Estudio Inteligente")
        
        actividades = st.multiselect("¿Qué necesitas estudiar hoy?", 
                                    ["Tarea", "Examen", "Exposición", "Repaso"])
        
        tiempo_total = st.selectbox("¿Cuánto tiempo tienes?", 
                                   ["30 minutos", "1 hora", "2 horas", "3 horas", "Más de 3 horas"])

        if actividades:
            datos_plan = []
            for act in actividades:
                st.subheader(f"Configuración para {act}")
                cursos_act = st.multiselect(f"¿En qué cursos tienes {act}?", 
                                          [c['curso'] for c in st.session_state.cursos_y_notas],
                                          key=f"cursos_{act}")
                
                for curso in cursos_act:
                    if act == "Tarea":
                        detalle = st.selectbox(f"Tipo de tarea en {curso}", ["Investigación", "Ejercicios", "Teoría"], key=f"det_{act}_{curso}")
                    elif act == "Examen":
                        detalle = st.selectbox(f"Dificultad en {curso}", ["Fácil", "Media", "Difícil"], key=f"det_{act}_{curso}")
                    elif act == "Exposición":
                        detalle = st.selectbox(f"Duración en {curso}", ["Corta", "Media", "Larga"], key=f"det_{act}_{curso}")
                    else:
                        detalle = "General"
                    
                    datos_plan.append({"curso": curso, "actividad": act, "detalle": detalle})

            if st.button("Ver Plan Final"):
                st.divider()
                st.subheader(f"📋 TU PLAN PARA HOY ({tiempo_total})")
                
                # Ordenar Exámenes primero
                datos_plan.sort(key=lambda x: 0 if x["actividad"] == "Examen" else 1)
                
                for item in datos_plan:
                    # Buscar la nota del curso para lógica de refuerzo
                    info_curso = next((c for c in st.session_state.cursos_y_notas if c["curso"] == item["curso"]), None)
                    letra_final = "C" # Default
                    
                    if info_curso:
                        nota = info_curso["nota"]
                        sistema = info_curso["sistema"]
                        if sistema == "Letras (AD, A, B, C)":
                            letra_final = nota
                        elif sistema == "Números (0-20)":
                            if nota >= 18: letra_final = "AD"
                            elif nota >= 14: letra_final = "A"
                            elif nota >= 10: letra_final = "B"
                            else: letra_final = "C"
                        else: # 0-100
                            if nota >= 90: letra_final = "AD"
                            elif nota >= 80: letra_final = "A"
                            elif nota >= 70: letra_final = "B"
                            else: letra_final = "C"

                    # Determinar prioridad y método base
                    prioridad = "ALTA 🔥" if item["actividad"] == "Examen" else "Media 📝"
                    metodo_base = "Microestudio" if "30 minutos" in tiempo_total or "1 hora" in tiempo_total else "Técnica Pomodoro"
                    
                    # Contenedor visual organizado
                    with st.expander(f"📌 {item['curso']} - {item['actividad']} ({prioridad})", expanded=True):
                        col_a, col_b = st.columns([1, 2])
                        with col_a:
                            st.write(f"**Nota actual:** {letra_final}")
                            if letra_final in ["B", "C"]:
                                st.warning("⚠️ REFUERZO NECESARIO")
                            elif letra_final == "AD":
                                st.success("✅ REPASO CORTO")
                        
                        with col_b:
                            # Lógica de recomendaciones coherente
                            recomendacion = ""
                            if item["actividad"] == "Tarea":
                                if item["detalle"] == "Investigación":
                                    recomendacion = "Lectura guiada + resúmenes + mapas mentales"
                                elif item["detalle"] == "Ejercicios":
                                    recomendacion = "Práctica intensiva + repaso activo"
                                else:
                                    recomendacion = "Repaso activo + método Feynman"
                            elif item["actividad"] == "Exposición":
                                recomendacion = "Esquema + ensayo oral + práctica visual"
                            elif item["actividad"] == "Examen":
                                if item["detalle"] == "Difícil" or letra_final in ["B", "C"]:
                                    recomendacion = f"{metodo_base} + repaso activo + práctica intensiva"
                                else:
                                    recomendacion = f"{metodo_base} + repaso ligero + ejercicios"
                            else:
                                recomendacion = "Flashcards + Repaso espaciado"
                                
                            st.write(f"💡 **Método:** {recomendacion}")
                            st.write(f"🕒 **Gestión:** {'Más tiempo (Refuerzo)' if letra_final in ['B', 'C'] else 'Tiempo estándar'}")

                st.success(f"✨ ¡Mucho éxito, {st.session_state.nombre}! Confía en tu proceso. 🚀")
                if st.button("Nueva Sesión"):
                    st.session_state.etapa = "estudio"
                    st.rerun()


if __name__ == "__main__":
    main()
