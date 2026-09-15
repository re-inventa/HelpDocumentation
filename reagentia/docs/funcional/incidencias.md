# Incidencias y recuperación

## La conversación está recuperando la conexión

Espera a que el estado deje de mostrar **Sin conexión**, **Recuperando conexión** o **Intentando recuperarla**. El chat trata de reconectarse automáticamente. Antes de repetir un mensaje, comprueba si aparece en el historial recuperado.

## La conversación está conciliando el último turno

La pantalla muestra el contenido durable disponible mientras comprueba el último turno. Espera a que finalice la conciliación antes de considerar completa una respuesta que estaba en curso. Cerrar y volver a abrir el navegador no elimina el historial guardado.

## La respuesta se interrumpe o no se detiene

El texto parcial recibido se conserva. Puedes enviar otro mensaje cuando la conversación vuelva a estar disponible.

Si aparece **No se pudo confirmar la parada**, vuelve a pulsar **Detener**. Si el aviso persiste, anota la hora aproximada y el estado mostrado para solicitar soporte; no repitas el mensaje mientras siga activa la respuesta anterior.

## La actividad de herramientas no termina correctamente

Consulta el estado del bloque **Herramientas**. Si muestra **En curso**, espera a que finalice la respuesta antes de enviar otro mensaje. Si muestra **Resultado parcial**, **Fallida** o **Cancelada**, despliega el bloque para identificar qué ejecución produjo información y cuál no terminó.

Una herramienta fallida no implica que se haya perdido el historial. Conserva la conversación y vuelve a formular la consulta cuando la respuesta haya alcanzado un estado final. Si el fallo se repite, anota la hora aproximada, el nombre visible de la herramienta y el estado mostrado, sin copiar documentos ni datos sensibles.

## El asistente no puede continuar por el contexto disponible

El historial visible permanece guardado aunque el asistente necesite trabajar con una representación resumida o acotada de la conversación.

- Si aparece **Esta conversación ha alcanzado su límite de contexto. Inicia otra conversación para continuar.**, abre una conversación nueva. El aviso significa que la conversación actual ya no puede continuar con la información que cabe incluso después de usar una representación resumida o acotada del historial.
- Si aparece **El modelo del asistente no tiene un perfil de contexto válido. Contacta con un administrador.**, pide a una persona administradora que revise la configuración del agente antes de volver a intentarlo.

No repitas indefinidamente el mismo mensaje. Una conversación nueva comienza sin los mensajes, resúmenes ni resultados de herramientas de la anterior.

## No puedes abrir o continuar una conversación

Comprueba la organización activa, que exista un asistente habilitado y que tu rol permita utilizar conversaciones. Un observador puede consultar un asistente, pero no abrir ni continuar conversaciones con la configuración inicial.

Si la pantalla indica que se alcanzó el límite, no se pueden enviar más mensajes en esa conversación. El historial ya guardado permanece visible.

## Una herramienta asignada no está disponible

Revisa la causa indicada junto a la herramienta. Su asignación al agente no basta para utilizarla: debe admitir conversaciones, estar habilitada para la organización y disponer del contexto o los recursos que exige.

Si falta una configuración o un recurso, pide a una persona con los permisos correspondientes que lo revise. La lista de disponibilidad para conversaciones nuevas no implica que el cambio se aplique a una conversación existente; comprueba la configuración conservada por esa conversación.

Por ejemplo, **Buscar en la base reguladora** requiere un documento autorizado, publicado e indexado. Una conversación iniciada sin ese documento fijado no adquiere acceso aunque se configure después; en ese caso hay que preparar el recurso y abrir una conversación nueva. Consulta el [ejemplo de búsqueda documental](asistentes.md#ejemplo-una-herramienta-de-busqueda-documental).

## No puedes cerrar una conversación

Si el asistente está respondiendo, espera a que termine o pulsa **Detener respuesta** y vuelve a intentar **Cerrar conversación**. Una conversación cerrada permanece en el listado para consulta, pero ya no acepta mensajes. Crear otra no altera ese historial.

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
