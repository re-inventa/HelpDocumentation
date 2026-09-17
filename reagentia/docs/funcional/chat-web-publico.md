# Chat web público en pruebas controladas

Una organización puede preparar un asistente para que personas visitantes conversen sin
crear una cuenta. Esta capacidad se encuentra en una fase de pruebas controladas: debe
habilitarse expresamente y no supone que el chat esté disponible para cualquier sitio o
para tráfico público general.

!!! warning "Disponibilidad limitada"
    Esta fase todavía no incluye un plugin para WordPress o Elementor, shortcode, burbuja
    flotante ni una pantalla de configuración para responsables del sitio. Tampoco incorpora
    aún la protección contra automatización necesaria para abrir el canal al público.

## Preparar el canal

Una persona con permiso para gestionar canales públicos define:

- el asistente y el canal que se utilizarán;
- los sitios previstos para la futura inserción;
- el perfil de límites y la política de conservación aplicables;
- una integración identificada para el sistema que entrega el acceso al visitante.

En esta fase, la lista de sitios queda registrada como parte de la configuración, pero el
acceso inicial depende de la integración autorizada. No debe interpretarse como una garantía
de que solo esos sitios puedan presentar o reenviar un enlace.

La credencial de la integración se guarda directamente en el gestor de secretos configurado
y no se muestra en el navegador al crearla o rotarla. El servidor del sitio debe leerla con
su propia identidad; no debe incluirla en páginas, scripts del navegador, capturas ni
documentación. Rotarla impide que la anterior inicie conversaciones nuevas. Revocar la
integración o deshabilitar el canal impide nuevos inicios y corta el acceso de sus sesiones
activas.

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

## Caducidad, revocación y límites

- **Código caducado o revocado**: solicita un enlace nuevo al sitio que ofrece el chat.
- **Sesión pública no válida o caducada**: la conversación ya no admite lectura, renovación
  ni mensajes desde esa sesión; solicita un nuevo inicio si el canal sigue disponible.
- **Acceso revocado**: el responsable puede haber retirado la integración o deshabilitado el
  canal. No intentes eludirlo con un enlace anterior.
- **Límite alcanzado**: el historial disponible no se amplía y no se admiten más mensajes en
  esa prueba. Los límites definitivos y la alternativa de contacto se incorporarán en una
  fase posterior.
- **Chat no disponible**: vuelve a intentarlo más tarde o utiliza el canal de contacto que
  el sitio responsable indique fuera del chat.

Los controles actuales reducen el alcance de la prueba, pero no garantizan por sí solos que
una web pública quede protegida frente a automatización o abuso.

## Uso responsable

El chat muestra una respuesta generada por un asistente automatizado. Comprueba la
información importante antes de actuar y no introduzcas contraseñas, claves, datos bancarios
ni otra información sensible. La política de conservación y eliminación del historial se
documentará cuando esa capacidad esté implementada y verificada.

Consulta [Incidencias y recuperación](incidencias.md#chat-web-publico) si no puedes abrir o
recuperar la sesión.
