# Seguimiento de las subidas del conector

**Tareas Background > Subidas conector** muestra qué ocurrió en cada ejecución de subida automática.

## Cómo revisar una ejecución

1. Filtra por fuente, regla, ejecución, estado o rango de fechas. Al entrar se muestran los últimos 30 días.
2. Revisa cada fila: audio, fuente, ruta y formulario de la regla, fecha, duración, estado, motivo y ejecución.
3. Distingue entre **Subido**, descarte por duración mínima, reintentos agotados, error de subida, error de metadatos y error al leer la duración. Cualquier estado no reconocido se muestra como **Desconocido**; consulta el motivo de la fila.
4. Si existe un error, revisa el motivo antes de repetir o modificar la regla.
5. Utiliza la paginación para recorrer el resultado.
6. Pulsa **Descargar CSV** para exportar todos los resultados que cumplen los filtros, no solo la página visible. La exportación admite un rango máximo de 90 días.

Un fichero puede omitirse porque ya se había tratado, no cumple un filtro o supera un límite configurado. Omitido no significa necesariamente error.

## Antes de reintentar

- Comprueba que la fuente sigue conectada.
- Revisa ruta, filtros y periodo de búsqueda.
- Confirma que el formulario continúa activo.
- Evita lanzar de nuevo una ejecución que todavía esté en curso.
