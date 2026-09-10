# Asistentes y conversaciones

La sección **Asistentes** permite conversar dentro de Reagentia con un asistente habilitado para la organización activa. Una conversación mantiene su propio historial y puede retomarse después de cerrar el navegador.

Un asistente no es una configuración editable desde esta pantalla. Utiliza una versión publicada de un agente y ofrece un punto de acceso conversacional para las personas autorizadas.

!!! note "Disponibilidad"
    La sección muestra únicamente los asistentes habilitados para la organización activa. La pantalla y los permisos efectivos determinan si puedes consultar un asistente, abrir una conversación o continuarla.

## Abrir o continuar una conversación

1. Accede a **Asistentes** con la organización correcta seleccionada.
2. Revisa el nombre y la descripción del asistente mostrado.
3. Pulsa **Abrir conversación** para empezar o **Continuar conversación** para recuperar la conversación activa.
4. Escribe el mensaje y pulsa **Enviar mensaje**. También puedes pulsar `Intro`; utiliza `Mayús+Intro` para añadir una línea nueva.
5. Consulta el estado situado bajo el historial mientras se prepara y recibe la respuesta.

Los estados más habituales son **Enviando**, **Mensaje guardado. Preparando respuesta**, **Recibiendo respuesta** y **Respuesta finalizada**. El contenido aparece de forma progresiva durante la generación.

## Qué se conserva

El historial se guarda asociado a la conversación y a la organización. Cerrar la pestaña o el navegador no elimina los mensajes: al volver, utiliza **Continuar conversación** para cargar el contenido guardado.

Si la pantalla indica que está conciliando el último turno, muestra mientras tanto el contenido durable disponible. Espera a que termine la recuperación antes de interpretar como definitiva una respuesta que estuviera en curso.

No compartas en una conversación claves, credenciales ni otros secretos. Los mensajes forman parte del historial funcional y pueden permanecer disponibles al retomar la conversación.

## Detener una respuesta

Mientras el asistente responde, pulsa **Detener respuesta** para solicitar la parada. El texto recibido hasta ese momento se conserva en el historial.

- **Parada enviada. Texto parcial conservado** confirma que la solicitud se transmitió.
- **Parada solicitada. Esperando confirmación** indica que la confirmación todavía está pendiente.
- Si no se pudo confirmar la parada, vuelve a pulsar **Detener** como indica la pantalla.

Después de una respuesta detenida o interrumpida puedes enviar otro mensaje y continuar la misma conversación.

## Recuperación de conexión

Si se pierde la conexión, el chat intenta recuperarse automáticamente al volver a estar disponible. Durante ese proceso puede mostrar **Sin conexión**, **Recuperando conexión** o **Intentando recuperarla**.

El contenido parcial recibido se conserva cuando una respuesta se interrumpe. Evita repetir inmediatamente el mismo mensaje: espera a que el estado se estabilice y comprueba primero el historial recuperado.

## Permisos y límites visibles

- Un rol con permiso de consulta puede ver el asistente, aunque no tenga permiso para abrir o continuar conversaciones.
- Si no hay asistentes habilitados, la pantalla lo indica y no permite iniciar una conversación.
- Cuando se alcanza el límite de una conversación, el envío queda deshabilitado y el historial existente permanece visible.
- El campo de mensaje aplica un límite de longitud; si no admite más texto, resume la consulta o divídela en varios mensajes.

Consulta [Roles y permisos](roles-permisos.md) para conocer la configuración inicial y [Incidencias y recuperación](incidencias.md) si la conversación no puede continuar.

## Alcance actual

Esta guía describe el chat autenticado dentro de Reagentia. No implica que el asistente esté disponible como chat público, widget empotrado o canal externo.
