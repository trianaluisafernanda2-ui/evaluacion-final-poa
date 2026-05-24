# ============================================================
#  AUDITORÍA DE HORAS SEMANALES - Control de Jornada Laboral
# ============================================================

from horas_data import equipo, UMBRAL_HORAS, DIAS

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


# --- Funcion que ejecutara  ---
def imprimir_reporte(reporte, umbral):
    """Imprime el reporte de jornada laboral por recurso."""
    sep = "=" * 68

    print(sep)
    print("          REPORTE DE HORAS SEMANALES DEL EQUIPO")
    print(f"          Umbral estándar: {umbral} horas semanales")
    print(sep)
    print(f"  {'Recurso':<18} {'L':>4} {'M':>4} {'X':>4} {'J':>4} {'V':>4}  {'Total':>6}  Jornada")
    print("-" * 68)

    for r in reporte:
        d = r["horas_por_dia"]
        marca = "⚠" if r["clasificacion"] == "Sobretiempo" else " "
        print(
            f"  {r['nombre']:<18}"
            f" {d['lunes']:>4} {d['martes']:>4} {d['miercoles']:>4}"
            f" {d['jueves']:>4} {d['viernes']:>4}"
            f"  {r['total']:>6}  {marca} {r['clasificacion']}"
        )

    print("-" * 68)

    sobretiempos = [r for r in reporte if r["clasificacion"] == "Sobretiempo"]
    print(f"  Recursos en sobretiempo: {len(sobretiempos)} de {len(reporte)}")
    print(sep)


# --- PUNTO DE ENTRADA ---
if __name__ == "__main__":
    reporte = auditar_equipo(equipo, UMBRAL_HORAS)
    imprimir_reporte(reporte, UMBRAL_HORAS)