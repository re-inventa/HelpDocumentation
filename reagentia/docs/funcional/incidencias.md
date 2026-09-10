# Incidencias y recuperación

## La conversación está recuperando la conexión

Espera a que el estado deje de mostrar **Sin conexión**, **Recuperando conexión** o **Intentando recuperarla**. El chat trata de reconectarse automáticamente. Antes de repetir un mensaje, comprueba si aparece en el historial recuperado.

## La conversación está conciliando el último turno

La pantalla muestra el contenido durable disponible mientras comprueba el último turno. Espera a que finalice la conciliación antes de considerar completa una respuesta que estaba en curso. Cerrar y volver a abrir el navegador no elimina el historial guardado.

## La respuesta se interrumpe o no se detiene

El texto parcial recibido se conserva. Puedes enviar otro mensaje cuando la conversación vuelva a estar disponible.

Si aparece **No se pudo confirmar la parada**, vuelve a pulsar **Detener**. Si el aviso persiste, anota la hora aproximada y el estado mostrado para solicitar soporte; no repitas el mensaje mientras siga activa la respuesta anterior.

## No puedes abrir o continuar una conversación

Comprueba la organización activa, que exista un asistente habilitado y que tu rol permita utilizar conversaciones. Un observador puede consultar un asistente, pero no abrir ni continuar conversaciones con la configuración inicial.

Si la pantalla indica que se alcanzó el límite, no se pueden enviar más mensajes en esa conversación. El historial ya guardado permanece visible.

## La ejecución sigue creada

Espera el umbral que indique la interfaz. Si aparece **Reintentar lanzamiento**, úsalo una vez y vuelve al detalle. No crees otro lanzamiento salvo que el sistema confirme que el anterior no existe.

## La cancelación no termina

Una cancelación puede permanecer en **Cancelando** mientras se confirma el estado. Si aparece **Reintentar cancelación**, úsalo y conserva el identificador de la ejecución para soporte.

## La ejecución falla o caduca

1. Revisa el evento y el paso que falló.
2. Comprueba conexión LLM, recursos y archivos de entrada.
3. Corrige la causa fuera de la ejecución terminada.
4. Usa **Relanzar** para crear una ejecución trazable con la configuración permitida.

## No hay resultados descargables

Comprueba que el paso productor terminó correctamente y que el artifact no está eliminado o fuera de retención. Una ejecución puede tener resultados parciales; revisa cada item y paso.

## Acceso denegado

Verifica organización activa y rol. No compartas una sesión ni pidas que se amplíen permisos por tanteo: indica la acción concreta que necesitas realizar.

## Qué incluir al pedir soporte

- identificador visible de la ejecución;
- fecha y hora aproximadas;
- organización, sin datos personales;
- estado mostrado y acción intentada;
- texto del error saneado;
- si el problema se repite en un lanzamiento nuevo.

No incluyas documentos, claves, tokens, enlaces temporales de descarga ni capturas con información sensible.
