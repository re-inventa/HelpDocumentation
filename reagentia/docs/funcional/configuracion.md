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

Las tools amplían lo que puede hacer un agente. Su gestión está reservada a administradores. Cada versión de tool indica si funciona en workflows, conversaciones o ambos. Asignarla a un agente no garantiza que esté disponible en todas las superficies: también deben estar activos el binding y los recursos que exige.

En **Asistentes**, quien puede editar agentes elige la base reguladora publicada autorizada para conversaciones nuevas. La búsqueda solo estará disponible cuando esa versión tenga un índice listo. El cambio no modifica conversaciones ya iniciadas.

## Recursos

Los recursos son documentos de referencia versionados. La interfaz distingue la carga, el procesamiento y la versión publicada.

No lances una ejecución que dependa de un recurso hasta que la interfaz confirme que está preparado. Una carga correcta solo acredita que el archivo llegó; no que su procesamiento haya terminado.
