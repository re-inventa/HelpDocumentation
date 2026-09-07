# Seguimiento y resultados

## Historial

La pantalla **Runs** permite filtrar por solución, workflow, estado, usuario y fechas. La lista está ordenada por las ejecuciones más recientes y permite abrir el detalle.

## Estados

| Estado | Significado |
| --- | --- |
| Creada | Registrada, todavía sin despacho confirmado. |
| En cola | Aceptada para ejecución. |
| En curso | Tiene trabajo activo. |
| Esperando entrada | Necesita una condición o entrada antes de continuar. |
| Cancelando | La intención está registrada y se está confirmando la detención. |
| Correcta | Terminó satisfactoriamente. |
| Fallida | Terminó con un error. |
| Cancelada | La detención quedó confirmada. |
| Caducada | Superó el tiempo permitido. |

El detalle se actualiza en tiempo real cuando es posible y usa refresco periódico como respaldo. Incluye resumen, items, pasos, eventos y artifacts.

## Descargar resultados

- Usa la descarga individual para revisar un artifact concreto.
- Usa la descarga ZIP para recoger los resultados disponibles de la ejecución.
- Un resultado puede dejar de estar disponible al terminar su periodo de retención.
- La ausencia de descarga no cambia el estado histórico de la ejecución.

## Acciones de recuperación

- **Reintentar despacho** recupera una ejecución creada que no llegó a activarse; no crea una segunda ejecución.
- **Cancelar** registra primero la intención y después solicita la detención.
- **Relanzar** crea una ejecución nueva a partir de una anterior finalizada, conservando trazabilidad entre ambas.
