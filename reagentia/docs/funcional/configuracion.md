# Workflows, agentes y recursos

## Workflows

La pantalla **Workflows** muestra los procesos asignados a tu organización y la versión de configuración disponible.

Una configuración publicada determina:

- qué entradas se admiten;
- qué pasos se ejecutan;
- qué versiones de agente intervienen;
- qué recursos de referencia se necesitan;
- qué resultados se esperan.

Los administradores pueden crear un borrador, validarlo, descartarlo o publicarlo. Publicar archiva la versión publicada anterior para nuevos lanzamientos, pero no modifica ejecuciones ya creadas.

## Agentes

La pantalla **Agentes** permite consultar el agente y sus versiones. Los administradores pueden editar un borrador y publicar una versión válida.

Antes de publicar comprueba que:

- las instrucciones describen una responsabilidad concreta;
- el modelo configurado está disponible;
- las tools vinculadas son las necesarias;
- el formato de salida coincide con el contrato del workflow;
- no hay secretos ni datos reales en las instrucciones.

## Tools

Las herramientas, llamadas **tools** en la interfaz, amplían lo que puede hacer un agente. Su gestión está reservada a administradores. Cada versión indica si funciona en workflows, conversaciones o ambos, y qué contexto o recursos necesita.

Para utilizar una herramienta deben cumplirse todas estas condiciones:

- Está asignada a la versión del agente utilizada.
- Es compatible con el workflow o la conversación donde se quiere usar.
- Está habilitada para la organización.
- Dispone del contexto y de los recursos que exige, con la autorización y el estado necesarios.

En **Asistentes** puedes consultar la disponibilidad para conversaciones nuevas y la causa de cualquier requisito pendiente. La configuración necesaria depende de cada herramienta. Como ejemplo, la búsqueda documental requiere una fuente autorizada y preparada para consultar; otras herramientas pueden funcionar sin documentos. Consulta [Herramientas y requisitos de uso](asistentes.md#herramientas-y-requisitos-de-uso) para ver el comportamiento y un ejemplo de configuración.

## Recursos

Los recursos son documentos de referencia versionados. La interfaz distingue la carga, el procesamiento y la versión publicada.

No lances una ejecución que dependa de un recurso hasta que la interfaz confirme que está preparado. Una carga correcta solo acredita que el archivo llegó; no que su procesamiento haya terminado.
