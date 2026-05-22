# ============================================================
#  AUDITORÍA DE HORAS SEMANALES - Control de Jornada Laboral
# ============================================================

from horas_data import equipo, UMBRAL_HORAS,DIAS




# --- Funcion para analizar al recurso o empleado ---
def analizar_recurso(recurso, umbral):
    
    # calculo total de horas trabajadas por el recurso
    total = sum(recurso[dia] for dia in DIAS)
    
    #  determinar si el recurso está en sobretiempo o no
    clasificacion = "Sobretiempo" if total > umbral else "Horario Estándar"
    return total, clasificacion


# --- funcion para auditar al equipo completo ---
def auditar_equipo(equipo, umbral):
    
    # creamos el espacio para almacenar el reporte de cada recurso
    reporte = []

    for recurso in equipo:
        total, clasificacion = analizar_recurso(recurso, umbral)
        reporte.append({
            "nombre":        recurso["nombre"],
            "horas_por_dia": {dia: recurso[dia] for dia in DIAS},
            "total":         total,
            "clasificacion": clasificacion,
        })
    return reporte