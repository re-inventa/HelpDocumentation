# Incidencias y recuperación

## Chat web público

Si la pantalla de administración rechaza un origen, revisa que sea una URL HTTPS
completa sin ruta, por ejemplo `https://chat.example.invalid`, y que se haya
introducido uno por línea. HTTP solo sirve para pruebas locales en localhost,
`127.0.0.1` o `[::1]`. La
**Prueba controlada** exige al menos un origen y se admiten como máximo 50. Si
la creación de una integración indica que el canal no está listo, comprueba que
el estado guardado sea **Activo** y el modo **Prueba controlada**, dentro de una
ventana autorizada. Un error de permisos requiere que la persona responsable
revise tu rol; un conflicto puede indicar una clave ya utilizada o una integración
revocada. Si falla la custodia al crear o rotar, consulta el estado actualizado
antes de volver a intentarlo y solicita apoyo operativo. La credencial nueva aparece
una sola vez tras crear o rotar. Si se cierra el aviso o se pierde la respuesta,
actualiza el estado: rota una integración existente para recibir otra credencial, o
repite el alta si no aparece. Una versión anterior nunca puede recuperarse.

Si el asistente insertado muestra **Reintentar apertura**, úsalo desde la misma
pestaña. Si el intento ya no puede completarse, utiliza **Solicitar nuevo inicio**
y completa la comprobación que ofrezca el sitio. Si el asistente ni siquiera carga,
recarga la página o usa el contacto alternativo del sitio. El código que gestiona
la integración caduca a los 2 minutos, pero no se muestra a la persona visitante
ni requiere copiar un enlace. El navegador puede recuperar la misma conversación
sin ampliar su caducidad.

Una sesión caduca 30 minutos después de su primera apertura. Recargar o enviar mensajes no
reinicia el plazo. Si se borran los datos del sitio, se cierra la pestaña o se cambia de
navegador, la sesión puede dejar de ser recuperable.
La conservación posterior del historial no amplía ese acceso. La
[política de conservación](chat-web-publico.md#conservacion-de-conversaciones)
distingue el almacenamiento principal de las copias del proveedor y los respaldos.

**La sesión ha caducado. Solicita un nuevo inicio al sitio.** indica que terminó su
plazo. **El acceso a esta conversación ha sido revocado.** indica que se retiró el
acceso de la sesión o de su integración. **El canal no está disponible.** indica que
se deshabilitó el canal o su acceso público. **La sesión no es válida. Solicita un
nuevo inicio al sitio.** puede aparecer si se perdió el acceso guardado en la
pestaña. **El chat no está disponible temporalmente.** señala una indisponibilidad
temporal. Dentro de una conversación abierta el aviso de sesión puede abreviarse a
**La sesión no es válida.**, y al enviar un mensaje puede aparecer **El servicio de
chat no está disponible temporalmente.** Si el acceso se retiró, utiliza el contacto
alternativo del sitio.

**El canal no está disponible en este sitio.** puede indicar que el asistente se
abrió sin su página anfitriona o que la prueba no está habilitada allí. Vuelve al
sitio que ofrece el chat; si el aviso persiste, usa su contacto alternativo.

Al deshabilitar el canal o revocar una integración, no se aceptan nuevos mensajes ni
renovaciones en las sesiones afectadas. Una respuesta que ya había comenzado puede
terminar y mostrarse después, con consumo dentro de los límites configurados. Espera a
que se cierre antes de interpretar su contenido como definitivo. La desactivación no
elimina automáticamente el historial ni retira texto que ya se mostró.

Si el asistente insertado indica que el almacenamiento de la pestaña está bloqueado,
puedes continuar en esa página, pero la recarga impedirá recuperar la sesión. No se
abrirá otra conversación automáticamente: solicita un inicio nuevo al sitio si lo
necesitas. Si se agota un límite o el servicio no está disponible, utiliza el contacto
alternativo publicado por el sitio.

Si aparece **No se pudo confirmar la conversación. Reintenta desde esta pestaña o
utiliza el contacto alternativo.**, usa primero **Reintentar apertura** desde la misma
pestaña. El asistente conserva el intento pendiente. **Solicitar nuevo inicio** pide
otra comprobación al sitio cuando el intento anterior ya no sirve.

Si aparece **No se pudo verificar el inicio. Completa de nuevo la comprobación en el
sitio.**, repite la comprobación Turnstile. Si el rechazo se repite, pide al
responsable del sitio que revise la configuración. La integración debe gestionar
por su cuenta los reintentos técnicos del inicio sin pedir al visitante un código.
Desde una misma conexión se pueden obtener como máximo 10 inicios para un canal en
60 minutos; varias personas que comparten esa conexión pueden consumir el cupo.
Las respuestas técnicas de la petición de inicio, incluidas **Inicio no disponible.**
y **El token Turnstile ya fue utilizado por otro inicio.**, corresponden al servidor
del sitio. La especificación técnica de integración del canal documenta la petición,
su idempotencia y las condiciones para repetir el mismo intento; no son mensajes
que deba buscar la persona visitante en el asistente insertado.

**Se ha alcanzado el límite temporal de uso.** corresponde al ritmo de 6 mensajes
en 60 segundos; espera antes de reintentar. **Se ha alcanzado el límite de mensajes.**
indica que se agotaron los 20 mensajes de la sesión y requiere un inicio nuevo cuando
esté disponible. **Se ha alcanzado el presupuesto de uso del chat.** indica que se
agotó el presupuesto de la conversación o el diario compartido. Si el aviso persiste,
usa el contacto alternativo del sitio. Durante la apertura también puede aparecer
**Se ha alcanzado el límite de mensajes de la sesión.**

Si aparece **Hay otra respuesta en curso o se alcanzó la concurrencia del canal.**, espera
a que termine la respuesta actual. Cada conversación admite una respuesta en curso y cada
canal hasta 5. Durante la apertura, el aviso puede decir **Hay otra respuesta en curso o
se alcanzó el límite de respuestas simultáneas.** No repitas el mensaje mientras siga
activa la respuesta anterior.

Si aparece **No se pudo enviar el mensaje. Crea un nuevo envío para reintentarlo.**, el
intento fue rechazado: envía el texto otra vez como un mensaje nuevo cuando el chat vuelva a
estar disponible. Si aparece **Comprueba el historial y reintenta el mismo mensaje desde
esta pestaña.**, revisa primero el historial. La confirmación puede llegar después; si
el mensaje no aparece tras recuperar la conexión, vuelve a intentarlo en esa conversación.
Si aparece **Hay un envío sin confirmar. Reintenta primero el mismo mensaje o recarga la
conversación.**, conserva ese texto y comprueba el historial antes de enviar otro.
**No se pudo renovar la lectura. Vuelve a intentarlo más tarde.** indica que no se
pudo recuperar el acceso temporal a la respuesta; mantén la pestaña y reintenta después.

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
