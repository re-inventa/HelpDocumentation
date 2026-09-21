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
2. Activa **Unir en un único audio** y selecciona los segmentos MP3 o WAV.
3. Ordena los segmentos tal como deben escucharse. El resultado respeta el
   orden mostrado, no el orden en que el selector devolvió los archivos.
4. Revisa la duración, el tamaño agregado y el nombre del resultado.
5. Inicia la carga y mantén abierta la página hasta que termine la preparación
   local y la subida.

La aplicación prepara el audio en tu equipo y sube únicamente el archivo
combinado. Los originales no se suben como parte de esa operación. Si quieres
procesarlos por separado, conserva el modo de carga individual.

Los límites comprobados para una operación son:

- hasta 80 minutos en total;
- hasta 32 segmentos y 1 GiB de entrada agregada;
- MP3 o WAV PCM, con uno o dos canales y frecuencias entre 8 y 96 kHz.

La preparación de 80 minutos se ha validado en Chromium de escritorio. Otros
navegadores y dispositivos pueden disponer de menos memoria; si la aplicación
rechaza la operación, reduce el grupo o utiliza la carga individual.

El resultado preparado solo se conserva temporalmente en la sesión abierta.
Un fallo de subida permite reintentarlo sin repetir la unión mientras el
resultado siga disponible. Si cierras o recargas la página, tendrás que volver
a seleccionar y preparar los segmentos.

## Configuración disponible

Los usuarios autorizados pueden ver opciones adicionales, como el método de procesamiento, las instrucciones del formulario, los metadatos, el destino de resultados o las bases de conocimiento asociadas. Modifica únicamente los campos cuyo efecto conozcas y guarda antes de salir.

## Eliminar un formulario

La eliminación puede continuar en segundo plano. Si tu rol permite iniciarla, confirma el formulario seleccionado y consulta **Estado del borrado Formularios** hasta que termine. No crees otro formulario con el mismo propósito hasta conocer el resultado.
