# Asistentes y conversaciones

La sección **Asistentes** permite mantener varias conversaciones independientes con un mismo asistente habilitado para la organización activa. Cada conversación conserva su propio historial y puede retomarse después de cerrar el navegador.

El asistente utiliza una versión publicada de un agente, con sus instrucciones y herramientas asignadas. Cada herramienta tiene sus propios requisitos: para utilizarla en una conversación debe admitir ese uso, estar habilitada para la organización y disponer del contexto o los recursos que necesite.

!!! note "Disponibilidad"
    La sección muestra únicamente los asistentes habilitados para la organización activa. La pantalla y los permisos efectivos determinan si puedes consultar un asistente, abrir una conversación o continuarla.

## Iniciar y elegir conversaciones

1. Accede a **Asistentes** con la organización correcta seleccionada.
2. Revisa el nombre y la descripción del asistente mostrado.
3. Consulta **Tools asignadas y disponibilidad para conversaciones nuevas**. Revisa cuáles pueden utilizarse y la causa indicada para las que no están disponibles.
4. Pulsa **Nueva conversación** para empezar otra, aunque ya tengas una activa. La nueva aparece en el listado sin modificar las anteriores.
5. Para continuar una existente, selecciónala en el listado por su fecha y estado. Usa **Ver conversaciones anteriores** para recorrer las más antiguas.
6. Escribe el mensaje y pulsa **Enviar mensaje**. También puedes pulsar `Intro`; utiliza `Mayús+Intro` para añadir una línea nueva.
7. Consulta el estado situado bajo el historial mientras se prepara y recibe la respuesta.

Los estados más habituales son **Enviando**, **Mensaje guardado. Preparando respuesta**, **Recibiendo respuesta** y **Respuesta finalizada**. El contenido aparece de forma progresiva durante la generación.

## Qué se conserva

El historial se guarda asociado a cada conversación y a la organización. Cerrar la pestaña o el navegador no elimina los mensajes: al volver, selecciona la conversación que quieras recuperar. Al cambiar entre conversaciones, se muestra el historial y el estado de la elegida, sin mezclar las respuestas de otras.

Cuando una conversación crece, el asistente puede utilizar una representación resumida o acotada de la información anterior para preparar nuevas respuestas. Este ajuste no borra ni modifica el historial visible: puedes seguir consultando los mensajes, respuestas y detalles de herramientas guardados.

Los turnos recientes y las referencias necesarias se mantienen disponibles para continuar el tema. Si necesitas separar asuntos o empezar sin el contexto de la conversación actual, abre una conversación nueva. La conversación nueva no hereda mensajes, resúmenes ni resultados de herramientas de las anteriores.

Una conversación nueva conserva la versión publicada del agente y la configuración de herramientas con la que se inició. Publicar otra versión del agente no actualiza las conversaciones existentes. Cuando una herramienta utiliza un recurso cuya versión queda fijada en la conversación, las publicaciones posteriores de ese recurso tampoco sustituyen la versión elegida.

Conservar esa configuración no garantiza que una herramienta siga disponible: su activación y los requisitos necesarios para ejecutarla se comprueban también al utilizarla.

## Herramientas y requisitos de uso

Una herramienta amplía las acciones que el asistente puede realizar. La lista de **Tools asignadas y disponibilidad para conversaciones nuevas** permite distinguir su asignación de su disponibilidad:

- **Asignada**: forma parte de la versión del agente.
- **Compatible con conversaciones**: admite su uso en el chat; algunas herramientas solo admiten workflows.
- **Disponible**: además de estar asignada y ser compatible, está habilitada para la organización y cumple sus requisitos de contexto y recursos.

No todas las herramientas necesitan los mismos recursos. Por ejemplo, consultar la hora no requiere un documento; una herramienta de búsqueda documental sí necesita una fuente autorizada y preparada para consultar. La pantalla indica la causa cuando un requisito impide utilizar una herramienta.

Si falta una configuración o un recurso, una persona con los permisos correspondientes debe completarlo. Revisa a qué conversaciones se aplica el cambio: la disponibilidad indicada para conversaciones nuevas no amplía por sí sola las capacidades de una conversación ya creada.

## Consultar la actividad de herramientas

El asistente puede ejecutar ninguna, una o varias herramientas antes de completar una respuesta. No existe un número fijo de ejecuciones: depende de la pregunta y de las herramientas disponibles.

Cuando se utiliza alguna, la respuesta reúne su actividad en un único bloque compacto. El encabezado muestra, cuando están disponibles, el número de ejecuciones, el número de resultados y el estado conjunto. Por ejemplo:

> **Herramientas · 3 ejecuciones · 11 resultados · Completada**

La respuesta del asistente sigue siendo el contenido principal. El bloque permanece contraído de forma predeterminada para que los resultados extensos no desplacen la respuesta. Mientras continúa el trabajo, el encabezado actualiza su estado sin exigir que abras cada ejecución.

Los estados posibles son:

- **En curso**: todavía hay una herramienta trabajando.
- **Completada**: todas las ejecuciones finalizaron correctamente.
- **Resultado parcial**: las ejecuciones terminaron con estados diferentes; algunas pueden haber aportado información y otras no.
- **Fallida**: ninguna ejecución pudo completarse correctamente.
- **Cancelada**: todas las ejecuciones se detuvieron antes de terminar, por ejemplo al usar **Detener respuesta**.

Selecciona el encabezado para desplegar la sección y consulta cada ejecución por separado. Puedes hacerlo con el ratón o mediante teclado, situando el foco en el encabezado y pulsando `Intro` o `Espacio`. Los detalles pueden incluir una descripción breve, datos principales, referencias y fuentes. Si no se puede determinar un recuento exacto, la interfaz no muestra el total de resultados.

Si aparece **Los detalles no están disponibles para esta versión del contrato.**, la respuesta puede conservar el estado de la ejecución sin mostrar su contenido detallado. No presupongas que el bloque está vacío ni que la herramienta no se ejecutó; utiliza la respuesta del asistente y el estado mostrado como información disponible.

El bloque presenta únicamente información preparada para su consulta. No sustituye el historial guardado ni muestra automáticamente todos los datos internos producidos por una herramienta.

### Ejemplo: una herramienta de búsqueda documental

La herramienta **Buscar en la base reguladora** ilustra este comportamiento. Requiere una base publicada de la organización y un índice preparado para consultar su contenido. Este requisito pertenece a esa herramienta.

Si tu rol permite editar agentes, usa **Base reguladora autorizada para este asistente** y pulsa **Guardar base** antes de abrir una conversación nueva. La lista muestra bases publicadas de tu organización e indica si falta el índice. Elegir una base sin índice no habilita aún la búsqueda. **Sin base reguladora** desactiva la consulta documental para las conversaciones nuevas.

Cuando se crea la conversación con el recurso autorizado y preparado, se fija su versión. La pantalla muestra el nombre y la versión del documento fijado, o **Sin base reguladora fijada** si no dispone de él. Una conversación creada sin ese recurso no obtiene acceso al documento al configurarlo después.

Si la herramienta de búsqueda está disponible, puedes preguntar por el contenido del documento. Las evidencias muestran su versión, la sección cuando se reconoce y las páginas del fragmento. Puedes contrastarlas con el documento original.

Si la búsqueda figura como no disponible, revisa la causa en la lista de herramientas. El asistente puede seguir respondiendo sin búsqueda documental, pero una respuesta sin evidencias no acredita que haya consultado el documento.

## Interpretar el estado de una respuesta

Si la pantalla indica que está conciliando el último turno, muestra mientras tanto el contenido durable disponible. Espera a que termine la recuperación antes de interpretar como definitiva una respuesta que estuviera en curso.

No compartas en una conversación claves, credenciales ni otros secretos. Los mensajes forman parte del historial funcional y pueden permanecer disponibles al retomar la conversación.

## Detener una respuesta

Mientras el asistente responde, pulsa **Detener respuesta** para solicitar la parada. El texto recibido hasta ese momento se conserva en el historial.

- **Parada enviada. Texto parcial conservado** confirma que la solicitud se transmitió.
- **Parada solicitada. Esperando confirmación** indica que la confirmación todavía está pendiente.
- Si no se pudo confirmar la parada, vuelve a pulsar **Detener** como indica la pantalla.

Después de una respuesta detenida o interrumpida puedes enviar otro mensaje y continuar la misma conversación.

## Cerrar una conversación

Selecciona una conversación activa y pulsa **Cerrar conversación** cuando hayas terminado. Esa conversación pasa a **Cerrada** en el listado. Puedes abrirla después para leer el historial, pero no admite mensajes nuevos. Las demás conversaciones siguen disponibles.

Si hay una respuesta en curso, espera a que termine o detenla antes de volver a intentar el cierre. Cerrar una conversación no borra sus mensajes.

## Recuperación de conexión

Si se pierde la conexión, el chat intenta recuperarse automáticamente al volver a estar disponible. Durante ese proceso puede mostrar **Sin conexión**, **Recuperando conexión** o **Intentando recuperarla**.

El contenido parcial recibido se conserva cuando una respuesta se interrumpe. Evita repetir inmediatamente el mismo mensaje: espera a que el estado se estabilice y comprueba primero el historial recuperado.

## Permisos y límites visibles

- Un rol con permiso de consulta puede ver el asistente, aunque no tenga permiso para listar, iniciar, continuar o cerrar conversaciones.
- Si no hay asistentes habilitados, la pantalla lo indica y no permite iniciar una conversación.
- Cuando se alcanza el límite de una conversación, el envío queda deshabilitado y el historial existente permanece visible.
- El campo de mensaje aplica un límite de longitud; si no admite más texto, resume la consulta o divídela en varios mensajes.
- Si aparece **Esta conversación ha alcanzado su límite de contexto. Inicia otra conversación para continuar.**, abre una conversación nueva; la conversación actual ya no puede continuar incluso usando una representación resumida o acotada del historial.
- Si aparece **El modelo del asistente no tiene un perfil de contexto válido. Contacta con un administrador.**, solicita a una persona administradora que revise la configuración del agente.

Consulta [Roles y permisos](roles-permisos.md) para conocer la configuración inicial y [Incidencias y recuperación](incidencias.md) si la conversación no puede continuar.

## Alcance actual

Esta guía describe el chat autenticado dentro de Reagentia. Un asistente solo queda
disponible fuera de la plataforma cuando una persona con el permiso específico configura
y habilita un canal independiente. La primera fase de ese recorrido se describe en
[Chat web público en pruebas controladas](chat-web-publico.md); todavía no incluye widget
empotrado ni plugin para gestores de contenido. Ese canal aplica sus propios límites de
mensajes, ritmo, presupuesto y respuestas simultáneas, independientes de los permisos del
chat autenticado.
