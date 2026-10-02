# Chat web público en pruebas controladas

Una organización puede preparar un asistente para que personas visitantes conversen sin
crear una cuenta. Esta capacidad se encuentra en una fase de pruebas controladas: debe
habilitarse expresamente y no supone que el chat esté disponible para cualquier sitio o
para tráfico público general.

!!! warning "Disponibilidad limitada"
    El asistente insertado en una página se está validando en un sitio de prueba.
    Todavía no hay plugin para WordPress o Elementor, shortcode ni burbuja flotante.
    La existencia del asistente insertable y de la pantalla de administración no abre
    el servicio al tráfico público general. La comprobación inicial reduce abusos,
    pero no garantiza que una web pública quede libre de ellos.

    El canal y su acceso público permanecen deshabilitados fuera de ventanas de prueba
    controladas y autorizadas. La disponibilidad general requiere la aceptación final.
    La matriz de navegadores y las comprobaciones de teclado, foco, lector de pantalla
    y diseño móvil siguen pendientes antes de esa apertura.

## Preparar el canal

Una persona con permiso para gestionar canales públicos puede abrir **Asistentes →
Configurar canal público** y seleccionar un asistente de su organización. Puede dejar
preparada la configuración; el acceso general debe seguir cerrado. Define:

- el asistente y el canal que se utilizarán;
- el estado del canal y del acceso público, que deben permanecer deshabilitados fuera de
  una ventana de prueba autorizada;
- los sitios previstos para la futura inserción;
- el perfil de límites y la política de conservación previstos para la prueba;
- la integración que se creará cuando la prueba pueda habilitarse.

En la pantalla se muestran el estado del canal, el modo de acceso, los orígenes
permitidos, el perfil de límites disponible, el estado de la conservación y el
inventario de integraciones. Cada integración muestra su nombre, clave identificadora, estado,
versión y una pista de credencial. La pista ayuda a identificar qué credencial está
provisionada; no permite recuperar su valor.

Para modificar el canal, elige **Activo** o **Deshabilitado** y el modo de acceso.
Introduce cada origen en una línea, como `https://chat.example.invalid`, sin ruta.
Solo se admite HTTP para pruebas locales en localhost, `127.0.0.1` o `[::1]`. La
pantalla ofrece un único
perfil de límites para esta prueba: 20 mensajes por sesión, 6 por minuto, hasta 5
respuestas simultáneas por canal y un presupuesto diario. Si aparece **Perfil actual no
disponible para selección**, el canal conserva una referencia anterior: selecciona el
perfil disponible para preparar una prueba nueva o consulta a la persona responsable si
no esperabas esa configuración. La pantalla muestra la política prevista de 30 días
desde la caducidad de la sesión. Su ejecución en un entorno depende de que se hayan
aplicado la actualización y las comprobaciones operativas correspondientes; la
pantalla no permite elegir otra política. Pulsa **Guardar canal**. El estado **Activo** junto con
**Prueba controlada**
solo debe usarse durante una ventana de prueba autorizada y exige marcar su
confirmación en la pantalla. **Deshabilitar canal** permite cerrar esa ventana.

Cuando el canal guardado esté activo en modo de prueba controlada, vuelve a marcar la
confirmación de la ventana autorizada antes de crear una integración con una clave y un
nombre: la confirmación se desmarca al guardar el canal, cambiar de asistente o canal,
o crear una integración correctamente.
Al crearla, la pantalla muestra la credencial
nueva **una sola vez** y permite copiarla. Guárdala en el servidor que hará las peticiones;
el alta no instala ni configura ese componente. **Rotar** solicita confirmación,
sustituye la credencial para nuevos inicios y muestra la nueva versión una sola vez para
su provisión segura.
**Revocar** solicita confirmación y retira el acceso de la integración. Su registro
permanece visible para auditoría y no puede reactivarse. No existe una acción de
borrado físico. Si hace falta otro acceso, crea una integración nueva.

En esta fase, la lista de sitios queda registrada como parte de la configuración, pero el
acceso inicial depende de la integración autorizada. No debe interpretarse como una garantía
de que solo esos sitios puedan solicitar o entregar un inicio.

La credencial recién creada o rotada solo aparece durante esa operación administrativa.
Al cerrar el aviso o abandonar la página desaparece y no puede consultarse de nuevo en el
inventario. No debe incluirse en páginas, scripts del navegador, capturas o documentación.
Si la copias, puede permanecer en el portapapeles después de cerrar el aviso: pégala en
su destino seguro y limpia el portapapeles al terminar.
Si se pierde, actualiza el estado: si la integración existe, rótala para obtener una nueva;
si el alta no llegó a completarse, vuelve a crearla. Las integraciones anteriores también
requieren rotación para obtener un valor que se pueda provisionar. Una integración que la
utilice debe conservarla exclusivamente en su servidor. Rotarla impide que la
credencial anterior solicite nuevos inicios; los códigos ya
emitidos pueden utilizarse hasta que venza su plazo original de 2 minutos.

El estado del canal y el acceso público son controles distintos. Deshabilitar solo el acceso
público mantiene activo el canal para otros usos presentes o futuros, pero impide preparar o
abrir nuevos accesos públicos y bloquea los mensajes y renovaciones de sus sesiones. Al
deshabilitar el canal se detiene además su ciclo de vida completo. Volver a habilitar el
acceso público no reactiva un canal que siga deshabilitado.

Revocar la integración produce el mismo cierre para los accesos asociados. Al deshabilitar
el acceso público, deshabilitar el canal o revocar la integración, una respuesta que ya se
había iniciado puede terminar de generarse y aparecer después de la confirmación. Esa
respuesta puede consumir recursos dentro de los límites configurados. No se admiten nuevos
mensajes ni renovaciones de lectura en las sesiones afectadas. La confirmación de
desactivación indica que el acceso quedó bloqueado; no indica que todas las respuestas
en curso hayan terminado. Esto no restablece la sesión ni permite continuarla.

## Comprobación del inicio

Cuando la prueba esté habilitada, la persona visitante completa una comprobación Turnstile
en el sitio autorizado. El asistente insertado muestra **Completa la comprobación de inicio
en el sitio.** mientras espera. Si se rechaza, muestra **No se pudo verificar el inicio.
Completa de nuevo la comprobación en el sitio.** Esta protección reduce los inicios
automatizados, pero no garantiza que una web pública quede libre de abuso.

El sitio gestiona el código de inicio sin mostrarlo a la persona visitante. Dura 2 minutos.
Si una interrupción impide recibir la respuesta, la integración del sitio puede repetir
exactamente la misma petición mientras el código siga vigente. Esa repetición recupera el
mismo código y no crea otra apertura. El sitio no debe combinar datos de intentos distintos
ni reutilizar una comprobación Turnstile para iniciar otra conversación.

Desde una misma conexión se pueden obtener como máximo 10 códigos para un mismo canal en
cualquier periodo de 60 minutos. Varias personas que comparten esa conexión pueden consumir
el mismo cupo. Al alcanzarlo, el sitio debe pedir que se espere antes de solicitar otro
inicio o indicar su contacto alternativo. Las respuestas técnicas de reintento del inicio
pertenecen a la integración; la persona visitante no necesita copiar ni reutilizar códigos.

La petición de inicio del sitio puede responder **Inicio no disponible.** o
**El token Turnstile ya fue utilizado por otro inicio.** También puede señalar que la
verificación está en curso o que no pudo confirmarse. Esos mensajes llegan a la
integración, no son el catálogo de avisos visibles del asistente insertado. La
especificación técnica de integración del canal documenta la petición, su idempotencia
y las condiciones de reintento; el sitio debe conservar el mismo intento cuando el
resultado sea incierto.

## Abrir una conversación como visitante

1. En el sitio autorizado durante una prueba, completa la comprobación y utiliza la
   acción de inicio que ofrezca el sitio. Su etiqueta depende del sitio. Este entrega
   el acceso temporal al asistente insertado sin pedirte copiar un enlace ni un código.
2. El asistente abre una única conversación y muestra cuándo caduca la sesión.
3. Escribe el mensaje y pulsa **Enviar mensaje**. La respuesta aparece progresivamente.
4. Mientras responde, puedes pulsar **Detener respuesta**. El texto ya recibido permanece
   visible.

La sesión dura 30 minutos desde la primera apertura. Enviar mensajes, recargar o recuperar
la conexión no amplía ese plazo.

### Pantalla autónoma de pruebas

En un entorno de prueba controlada puede estar disponible una pantalla separada
**Chat público**, con el campo **Código de inicio** y la acción **Abrir sesión**.
Solo se utiliza cuando la integración autorizada entrega expresamente un código
temporal para esta prueba; el código caduca a los 2 minutos. Esta pantalla no forma
parte del recorrido del asistente insertado ni abre el servicio al público general.
Si no recibiste un código para una prueba concreta, inicia desde el sitio autorizado.

## Límites de uso de la prueba

Cuando la prueba esté habilitada después de completar su validación, el perfil admitirá como
máximo 20 mensajes por sesión y 6 mensajes en 60 segundos.
Puede haber hasta 5 respuestas en curso a la vez en un mismo canal, pero solo una por
conversación. Los mensajes ya intentados siguen contando para el límite de la sesión aunque
una ejecución se interrumpa o termine sin generar consumo.

El uso del chat también está sujeto a un presupuesto por conversación y a un presupuesto
diario controlado, compartido por las conversaciones del chat ofrecido por la organización.
El consumo ya registrado se comprueba al enviar cada mensaje: una
respuesta en curso puede alcanzar el presupuesto, y los mensajes siguientes quedarán
bloqueados. Su valoración interna no es un precio mostrado a la persona visitante.
El asistente distingue **Se ha alcanzado el límite temporal de uso.** para el ritmo,
**Se ha alcanzado el límite de mensajes.** para la sesión y
**Se ha alcanzado el presupuesto de uso del chat.** para el presupuesto. Espera a que
termine la ventana temporal o utiliza la alternativa de contacto publicada por el sitio.
Alcanzar el límite total de la sesión requiere iniciar otra cuando el sitio vuelva a
ofrecer acceso. Durante la apertura, el aviso de mensajes puede usar la variante
**Se ha alcanzado el límite de mensajes de la sesión.**

Si ya hay una respuesta activa en la conversación o el canal alcanzó su concurrencia,
aparece **Hay otra respuesta en curso o se alcanzó la concurrencia del canal.** Espera a
que finalice la respuesta y vuelve a intentarlo. Repetir inmediatamente el envío no amplía
los límites ni abre una segunda respuesta para la misma conversación. Durante la apertura,
el aviso usa **Hay otra respuesta en curso o se alcanzó el límite de respuestas
simultáneas.**

## Recarga y recuperación

El navegador guarda en la pestaña los datos temporales necesarios para recuperar la misma
conversación. Si la apertura o una respuesta se interrumpe, recarga la página o repite la
misma apertura desde esa pestaña. La recuperación mantiene la conversación original; no
crea otra ni reinicia su caducidad.

El asistente insertado separa los datos de cada chat y sitio. Si el navegador bloquea el
almacenamiento de la pestaña, puedes conversar mientras mantengas la página abierta,
pero verás un aviso de que no podrás recuperar esa sesión tras recargar. Otra pestaña o
dispositivo no hereda la conversación. El asistente no inicia por su cuenta una nueva
conversación cuando la anterior caduca o falla: solicita un inicio nuevo al sitio.

Si la apertura no se confirma, el asistente puede mostrar **No se pudo confirmar la
conversación. Reintenta desde esta pestaña o utiliza el contacto alternativo.** Usa
**Reintentar apertura** para repetir el mismo intento. Si ya no puede completarse,
**Solicitar nuevo inicio** pide otra comprobación al sitio. Ante un resultado incierto,
prueba primero la apertura pendiente para evitar crear otra conversación.

Cerrar la pestaña, borrar los datos del sitio o abrir el asistente en otro navegador puede
impedir la recuperación. Esta fase no ofrece una cuenta de visitante ni otro mecanismo para
trasladar la conversación entre dispositivos.

## Caducidad, revocación e indisponibilidad

- **La sesión ha caducado. Solicita un nuevo inicio al sitio.** La conversación ya no
  admite nuevas operaciones desde esa sesión.
- **El acceso a esta conversación ha sido revocado.** El responsable retiró el acceso a
  esa sesión o a la integración que la habilitó. Solicita ayuda al sitio.
- **El canal no está disponible.** El responsable deshabilitó el canal o su acceso
  público. Usa el contacto alternativo que ofrezca el sitio.
- **La sesión no es válida. Solicita un nuevo inicio al sitio.** Comprueba que estás
  en la pestaña original antes de solicitarlo. Dentro de una conversación ya abierta,
  el aviso puede abreviarse a **La sesión no es válida.**
- **El chat no está disponible temporalmente.** Vuelve a intentarlo más tarde o utiliza
  el contacto alternativo del sitio. Al enviar un mensaje puede aparecer
  **El servicio de chat no está disponible temporalmente.**
- **El canal no está disponible en este sitio.** Comprueba que abriste el asistente desde
  el sitio autorizado y dentro de una prueba habilitada; si persiste, utiliza su
  contacto alternativo.
- **Hay otra respuesta en curso o se alcanzó la concurrencia del canal.** Espera a que la
  respuesta activa termine antes de enviar otra consulta.

Los controles actuales reducen el alcance de la prueba, pero no garantizan por sí solos que
una web pública quede protegida frente a automatización o abuso.

## Uso responsable

El chat muestra una respuesta generada por un asistente automatizado. Comprueba la
información importante antes de actuar y no introduzcas contraseñas, claves, datos bancarios
ni otra información sensible.
Deshabilitar el canal o perder el acceso no elimina automáticamente el historial ya
conservado ni retira información que el navegador haya mostrado antes.

## Conservación de conversaciones

La sesión permite acceder al chat durante 30 minutos desde su apertura. Recargar,
renovar la lectura, revocar el acceso o reintentar una petición no cambia esa fecha.
Una vez caducada, conservar datos durante más tiempo no permite volver a entrar en la
conversación con la misma sesión.

La política prevista para el almacenamiento principal elimina juntos los mensajes,
resúmenes, resultados y datos individuales de la conversación a partir de 30 días
después de esa caducidad. El proceso se programa diariamente; puede tardar más si hay
una respuesta o una comprobación de consumo pendiente, si falla la ejecución o si
hay una incidencia operativa. La eliminación no ocurre necesariamente a una hora
exacta. Esta política debe comprobarse en el entorno antes de presentarse como
activa para sus visitantes.

El proveedor que ejecuta el chat conserva algunas copias temporales durante un plazo
aproximado de 28 a 30 días desde que se escriben. Otros registros técnicos y copias
de respaldo no tienen un plazo máximo de eliminación garantizado. Los respaldos
propios siguen su política separada; al restaurarlos se debe volver a aplicar la
limpieza vencida antes de permitir el acceso. Eliminar el historial del
almacenamiento principal no elimina simultáneamente todas esas copias.

Consulta [Incidencias y recuperación](incidencias.md#chat-web-publico) si no puedes abrir o
recuperar la sesión.
