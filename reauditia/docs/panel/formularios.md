# Formularios

Un formulario define qué comprobaciones se aplican a los ficheros y cómo se presentan sus resultados.

## Abrir un formulario

1. Despliega **Formularios** en el menú lateral.
2. Utiliza el buscador si la lista es larga.
3. Selecciona el formulario adecuado.

## Cargar ficheros manualmente

1. Comprueba que estás en el formulario correcto.
2. Completa los metadatos que haya configurado el administrador. Un campo bloqueado solo admite sus valores disponibles; uno abierto permite escribir otro valor.
3. Selecciona o arrastra los ficheros admitidos. Puedes preparar cargas separadas con distintos metadatos para comparar después sus resultados.
4. Comprueba la lista y el número de ficheros que se van a procesar.
5. Pulsa **Subir ficheros**.
6. Abre **Tareas Background > Estado de los Ficheros** para seguir el procesamiento.

No cierres la ventana mientras la propia pantalla indique que la carga local sigue en curso. Una carga aceptada todavía puede necesitar procesamiento posterior.

## Unir varios audios en una sola carga

En los formularios de audio puedes activar **Unir en un único audio** para
evaluar varios segmentos consecutivos como una sola conversación.

1. Completa todos los metadatos obligatorios del formulario.
2. Activa **Unir en un único audio** y selecciona al menos dos segmentos MP3 o
   WAV PCM.
3. Ordena los segmentos tal como deben escucharse. El resultado respeta el
   orden mostrado, no el orden en que el selector devolvió los archivos.
4. Revisa la duración y el tamaño agregado. Escribe un nombre base
   significativo en **Nombre del audio resultante**. El campo comienza vacío,
   es obligatorio y no debes añadir `.mp3`: la aplicación incorpora la
   extensión automáticamente.
5. Inicia la carga y mantén abierta la página hasta que termine la preparación
   local y la subida.

La aplicación prepara el audio en tu equipo y sube únicamente el archivo
combinado. Los originales no se suben como parte de esa operación. Si quieres
procesarlos por separado, conserva el modo de carga individual.

Mientras se prepara el resultado puedes usar **Cancelar preparación**. La
aplicación detiene la unión y no inicia la subida; después puedes revisar el
grupo y comenzar de nuevo.

Los límites comprobados para una operación son:

- hasta 80 minutos en total;
- entre 2 y 32 segmentos y hasta 1 GiB de entrada agregada;
- MP3 o WAV PCM, con uno o dos canales y frecuencias entre 8 y 96 kHz.

La preparación de 80 minutos se ha validado en Chromium de escritorio. Otros
navegadores y dispositivos pueden disponer de menos memoria; si la aplicación
rechaza la operación, reduce el grupo o utiliza la carga individual.

El resultado preparado solo se conserva temporalmente en la sesión abierta.
Un fallo de subida permite reintentarlo sin repetir la unión mientras el
resultado siga disponible. Si cierras o recargas la página, tendrás que volver
a seleccionar y preparar los segmentos.

Después de un envío correcto, pulsa **Realizar otra subida** para retirar los
segmentos, el progreso y el resultado temporal de la operación anterior. El
nombre vuelve a quedar vacío y puedes preparar otra unión o seleccionar
**Subir archivos por separado**, sin recargar ni abandonar el formulario. Este
reinicio no se realiza automáticamente cuando falla la subida, para que siga
disponible **Reintentar subida sin volver a unir**.

Esta unión es una operación manual realizada desde el formulario. No sustituye
la agrupación automática que pueda realizar una regla de origen; consulta
[Subidas conector](subidas_conector.md) para seguir esas cargas.

## Doblar audios al español y publicarlos en SharePoint

Un formulario configurado para doblaje recibe MP3 o WAV y entrega un WAV en
español en SharePoint. Este flujo realiza el doblaje y la publicación; no genera
una transcripción ni una evaluación de calidad en ReAuditIA.

### Revisar el workflow

Los perfiles con permisos de administración pueden abrir **Workflow de audio >
Ver configuración JSON** y usar **Editar configuración** para guardar cambios.
La configuración contiene dos pasos, en este orden: `doblaje` y
`subida_sharepoint`. Cada paso se identifica en el JSON con `type`.

Antes de guardar, revisa:

| Campo | Qué configura |
| --- | --- |
| `doblajeId` | El servicio de doblaje facilitado por la administración. Su tarifa se gestiona fuera del formulario. |
| `sourceLanguage` | El idioma original; `auto` permite detectarlo automáticamente. |
| `targetLanguage` | `es`, para obtener el audio en español. |
| `sharepointSourceId` | El ID de una fuente SharePoint ya creada en la organización. Puedes consultarlo en **Subida automática > Fuentes SharePoint**. |
| `destinationUrl` | La dirección de la carpeta base donde quieres recibir los resultados. Se configura independientemente de la carpeta de entrada de la fuente. |
| `folderTemplate` | La estructura de subcarpetas; por ejemplo, `Doblajes/{yyyy}/{MM}/{dd}`. |
| `timeZone` | La zona horaria que determina la fecha de las carpetas; por ejemplo, `Europe/Madrid`. |

El proceso crea las carpetas de salida al publicar el audio. La fecha corresponde
a la recepción del fichero, aunque la publicación termine más tarde. El nombre
del resultado incluye un identificador del trabajo y el idioma de destino.

La fuente aporta la autorización de Microsoft; no necesitas crear una regla de
subida automática para hacer una carga manual. No incluyas contraseñas, claves
ni tokens en el JSON.

### Comprobar la conexión antes de subir

1. Revisa **Conexión con SharePoint** en el formulario y comprueba que aparece
   la fuente asignada.
2. Si indica **Pendiente de conectar** o **Requiere reconexión**, un usuario con
   permisos de administración debe pulsar **Conectar con Microsoft** o **Reconectar con
   Microsoft** y aceptar el acceso de escritura solicitado.
3. Al volver de Microsoft, el formulario actualiza el estado automáticamente.
   También puedes usar **Comprobar conexión**.
4. Espera a que aparezca **Conectado** antes de subir. La aplicación comprueba de
   nuevo la conexión inmediatamente antes de transferir los ficheros.

La subida permanece deshabilitada mientras la conexión no esté disponible.
Si la autorización falla antes de transferir, la selección de ficheros se conserva
para que puedas intentarlo después de recuperar la conexión.

Los perfiles con permisos de administración disponen de **Editar**, que abre
[Subida automática](subida_automatica.md) para gestionar las fuentes. Desde el
formulario se gestiona la autorización de la fuente asignada; la creación de
fuentes se realiza en Subida automática.

### Revisar el resultado y recuperar un fallo

Sigue el trabajo en [Estado de los ficheros](estado_audios.md) y abre la carpeta
de SharePoint configurada para escuchar el resultado. Una subida aceptada por el
formulario todavía puede estar esperando o procesando el doblaje.

Si el doblaje termina y falla la publicación, el resultado se conserva
temporalmente para recuperarlo en los reintentos del mismo trabajo. Una entrega
confirmada seguida de un fallo de limpieza solo repite la limpieza. Al terminar
correctamente la publicación y la limpieza, la copia temporal se elimina.

El cargo corresponde al doblaje completado, incluso si después falla SharePoint.
Los reintentos del mismo trabajo no repiten ese cargo. Volver a subir el fichero
crea otra operación; no es un reintento de la anterior. Consulta el detalle en
[Cartera y consumo](cartera.md#consumo-de-doblaje).

## Configuración disponible

Los usuarios autorizados pueden ver opciones adicionales, como el método de procesamiento, las instrucciones del formulario, los metadatos, el destino de resultados o las bases de conocimiento asociadas. Modifica únicamente los campos cuyo efecto conozcas y guarda antes de salir.

## Eliminar un formulario

La eliminación puede continuar en segundo plano. Si tu rol permite iniciarla, confirma el formulario seleccionado y consulta **Estado del borrado Formularios** hasta que termine. No crees otro formulario con el mismo propósito hasta conocer el resultado.

## Publicar resultados documentales en Insights

En los formularios documentales con esta función habilitada, **Sincronizar**
abre un popup con el aviso de documentos completados; **Aceptar** inicia su
publicación y permite seguir la exportación. Consulta
[Sincronizar los resultados con Insights](documentos.md#sincronizar-los-resultados-con-insights)
para conocer los permisos, estados y tratamiento de documentos en procesamiento.
