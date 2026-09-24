# Chat web público en pruebas controladas

Una organización puede preparar un asistente para que personas visitantes conversen sin
crear una cuenta. Esta capacidad se encuentra en una fase de pruebas controladas: debe
habilitarse expresamente y no supone que el chat esté disponible para cualquier sitio o
para tráfico público general.

!!! warning "Disponibilidad limitada"
    Esta fase todavía no incluye un plugin para WordPress o Elementor, shortcode, burbuja
    flotante ni una pantalla de configuración para responsables del sitio. Tampoco incorpora
    aún todas las protecciones necesarias para abrir el canal al público. El inicio preparado
    incluye protección contra automatización mediante una comprobación, pero no habilita por
    sí solo el servicio.

    El canal y su acceso público deben permanecer deshabilitados hasta que el ciclo completo
    de respuestas y control de límites esté desplegado y validado. Mientras tanto no se
    deben emitir enlaces ni iniciar conversaciones de prueba.

## Preparar el canal

Una persona con permiso para gestionar canales públicos puede dejar preparada la
configuración, pero todavía no debe habilitarla. Define:

- el asistente y el canal que se utilizarán;
- el estado del canal y del acceso público, que deben permanecer deshabilitados;
- los sitios previstos para la futura inserción;
- el perfil de límites de uso y la referencia de conservación;
- la integración que se creará cuando la prueba pueda habilitarse.

En esta fase, la lista de sitios queda registrada como parte de la configuración, pero el
acceso inicial depende de la integración autorizada. No debe interpretarse como una garantía
de que solo esos sitios puedan presentar o reenviar un enlace.

La credencial de la integración se genera y custodia fuera del navegador. No se muestra al
crearla o rotarla ni debe incluirse en páginas, scripts del navegador, capturas o
documentación. Una integración que la utilice debe conservarla exclusivamente en su
servidor. Rotarla impide que la credencial anterior solicite nuevos inicios; los códigos ya
emitidos pueden utilizarse hasta que venza su plazo original de 2 minutos.

El estado del canal y el acceso público son controles distintos. Deshabilitar solo el acceso
público mantiene activo el canal para otros usos presentes o futuros, pero impide preparar o
abrir nuevos accesos públicos y bloquea los mensajes y renovaciones de sus sesiones. Al
deshabilitar el canal se detiene además su ciclo de vida completo. Volver a habilitar el
acceso público no reactiva un canal que siga deshabilitado.

Revocar la integración produce el mismo cierre para los accesos asociados. Al deshabilitar
el acceso público, deshabilitar el canal o revocar la integración, una respuesta que ya se
está mostrando puede terminar de aparecer, pero esto no restablece la sesión ni permite
continuar la conversación.

## Comprobación del inicio

Cuando la prueba esté habilitada, la persona visitante completa una comprobación Turnstile
antes de recibir el código de inicio. El resultado solo se acepta para el sitio configurado
por la organización. Esta protección reduce los inicios automatizados, pero no garantiza
que una web pública quede libre de abuso.

Si una interrupción impide recibir la respuesta, el sitio puede repetir enseguida
exactamente el mismo inicio mientras el código siga vigente. Esa repetición recupera el
mismo código y no crea otra apertura. El sitio no debe combinar datos de intentos distintos
ni reutilizar una comprobación Turnstile para iniciar otra conversación.

Desde una misma conexión se pueden obtener como máximo 10 códigos para un mismo canal en
cualquier periodo de 60 minutos. Varias personas que comparten esa conexión pueden consumir
el mismo cupo. Al alcanzar el límite aparece **Se ha alcanzado el límite temporal de
aperturas.** Espera a que avance la ventana antes de volver a solicitar acceso.

Los errores temporales muestran **No se pudo verificar el inicio; reintenta la misma
petición.** o **La verificación del inicio está en curso; reintenta la misma petición.**
También puede aparecer la variante **La verificación del inicio está en curso.** Mantén la
misma página y repite la acción. Si aparece **No se pudo verificar el inicio.**, completa de
nuevo la comprobación y solicita otro inicio al sitio responsable. Si el rechazo se repite,
el responsable debe revisar la configuración de los sitios autorizados.

## Abrir una conversación como visitante

1. Accede al enlace temporal proporcionado por el sitio autorizado. También puedes
   introducir el código en la pantalla **Chat público**.
2. El código debe utilizarse en los 2 minutos siguientes a su emisión.
3. La pantalla abre una única conversación y muestra hasta cuándo estará activa la sesión.
4. Escribe el mensaje y pulsa **Enviar mensaje**. La respuesta aparece progresivamente.
5. Mientras responde, puedes pulsar **Detener respuesta**. El texto ya recibido permanece
   visible.

La sesión dura 30 minutos desde la primera apertura. Enviar mensajes, recargar o recuperar
la conexión no amplía ese plazo.

## Límites de uso de la prueba

Cuando la prueba esté habilitada después de completar su validación, el perfil admitirá como
máximo 20 mensajes por sesión y 6 mensajes en 60 segundos.
Puede haber hasta 5 respuestas en curso a la vez en un mismo canal, pero solo una por
conversación. Los mensajes ya intentados siguen contando para el límite de la sesión aunque
una ejecución se interrumpa o termine sin generar consumo.

El uso del chat también está sujeto a un presupuesto por conversación y a un presupuesto
diario controlado. El consumo ya registrado se comprueba al enviar cada mensaje: una
respuesta en curso puede alcanzar el presupuesto, y los mensajes siguientes quedarán
bloqueados. Su valoración interna no es un precio mostrado a la persona visitante. Cuando
se agota un límite de mensajes, ritmo o presupuesto aparece
**Se ha alcanzado un límite de uso del canal.** Espera a que termine la ventana temporal o
utiliza la alternativa de contacto publicada por el sitio. Alcanzar el límite total de la
sesión requiere iniciar otra cuando el sitio vuelva a ofrecer acceso.

Si ya hay una respuesta activa en la conversación o el canal alcanzó su concurrencia,
aparece **Hay otra respuesta en curso o se alcanzó la concurrencia del canal.** Espera a
que finalice la respuesta y vuelve a intentarlo. Repetir inmediatamente el envío no amplía
los límites ni abre una segunda respuesta para la misma conversación.

## Recarga y recuperación

El navegador guarda en la pestaña los datos temporales necesarios para recuperar la misma
conversación. Si la apertura o una respuesta se interrumpe, recarga la página o repite la
misma apertura desde esa pestaña. La recuperación mantiene la conversación original; no
crea otra ni reinicia su caducidad.

Si otra petición está terminando la apertura, puede aparecer **La apertura está en curso.
Vuelve a intentarlo.** Espera unos instantes y repite la acción. Si aparece **No se pudo
confirmar la apertura. Reintenta el mismo inicio.**, no solicites inmediatamente otro código:
prueba primero de nuevo desde la misma pestaña.

Cerrar la pestaña, borrar los datos del sitio o abrir el enlace en otro navegador puede
impedir la recuperación. Esta fase no ofrece una cuenta de visitante ni otro mecanismo para
trasladar la conversación entre dispositivos.

## Caducidad, revocación e indisponibilidad

- **Código de inicio no válido, caducado o revocado.** Solicita un enlace nuevo al sitio que
  ofrece el chat.
- **Sesión pública no válida o caducada.** La conversación ya no admite lectura, renovación
  ni mensajes desde esa sesión; solicita un nuevo inicio si el canal sigue disponible.
- **Acceso revocado**: el responsable puede haber retirado la integración, deshabilitado el
  acceso público o deshabilitado el canal. No intentes eludirlo con un enlace anterior.
- **Chat no disponible.** Vuelve a intentarlo más tarde o utiliza el canal de contacto que
  el sitio responsable indique fuera del chat.
- **Se ha alcanzado un límite de uso del canal.** Espera antes de reintentar o utiliza la
  alternativa de contacto del sitio si necesitas continuar.
- **Hay otra respuesta en curso o se alcanzó la concurrencia del canal.** Espera a que la
  respuesta activa termine antes de enviar otra consulta.

Los controles actuales reducen el alcance de la prueba, pero no garantizan por sí solos que
una web pública quede protegida frente a automatización o abuso.

## Uso responsable

El chat muestra una respuesta generada por un asistente automatizado. Comprueba la
información importante antes de actuar y no introduzcas contraseñas, claves, datos bancarios
ni otra información sensible. La política de conservación y eliminación del historial se
documentará cuando esa capacidad esté implementada y verificada.

Consulta [Incidencias y recuperación](incidencias.md#chat-web-publico) si no puedes abrir o
recuperar la sesión.
