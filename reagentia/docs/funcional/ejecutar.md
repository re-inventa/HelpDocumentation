# Lanzar una ejecución

## Antes de empezar

Comprueba que:

- estás en la organización correcta;
- el workflow está publicado y disponible;
- la conexión LLM está operativa cuando sea necesaria;
- los recursos requeridos están preparados;
- los documentos cumplen el tipo y tamaño indicados en pantalla.

## Preparar y lanzar

1. Abre **Runs** y selecciona la solución y el workflow.
2. Crea una sesión de carga.
3. Añade los documentos solicitados.
4. Espera a que cada archivo figure como completado.
5. Revisa el resumen y retira cualquier archivo incorrecto.
6. Pulsa **Lanzar** una sola vez.
7. Guarda el identificador visible de la ejecución para seguimiento.

La sesión de carga mantiene los archivos en una zona temporal hasta que el lanzamiento los asocia a una ejecución válida.

!!! warning "No dupliques el trabajo"
    Si la pantalla tarda en responder, abre el historial antes de volver a lanzar. Una ejecución creada puede estar pendiente de despacho y disponer de una acción específica de reintento.

## Qué queda fijado

El lanzamiento conserva las versiones publicadas y la configuración efectiva. Si un administrador publica cambios después, se aplicarán a nuevos lanzamientos, no al que ya está en curso.
