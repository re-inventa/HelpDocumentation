# Conceptos y alcance

## Qué es Reagentia

Reagentia es una plataforma para ejecutar procesos documentales asistidos por agentes. Separa la definición reutilizable del proceso, la configuración de cada organización y el historial de cada ejecución.

No está limitada a un procedimiento ni a una taxonomía concreta: las soluciones, workflows, agentes, herramientas y recursos se incorporan mediante configuración y versiones publicadas.

## Conceptos principales

| Concepto | Significado |
| --- | --- |
| Solución | Agrupación funcional de workflows relacionados. |
| Workflow | Contrato que define entradas, pasos y resultados esperados. |
| Agente | Comportamiento especializado que participa en uno o varios pasos. |
| Asistente | Punto de acceso conversacional que utiliza una versión publicada de un agente. |
| Conversación | Historial de mensajes intercambiados con un asistente que puede continuarse posteriormente. |
| Versión | Fotografía inmutable de una configuración publicada. |
| Tool | Capacidad que un agente puede utilizar durante su trabajo. |
| Recurso | Documento de referencia versionado que utiliza un workflow. |
| Ejecución | Instancia concreta de un workflow lanzada por una persona. |
| Item | Unidad de trabajo dentro de una ejecución. |
| Paso | Parte ordenada del procesamiento de un item. |
| Artifact | Documento de entrada o resultado asociado a la ejecución. |

## Qué conserva una ejecución

Al lanzar, Reagentia fija las versiones publicadas y una copia de la configuración relevante. Los cambios posteriores no alteran una ejecución ya creada.

El historial muestra quién lanzó el trabajo, cuándo ocurrió cada transición, el progreso por items y pasos, y los resultados que siguen disponibles.

## Qué conserva una conversación

Una conversación mantiene los mensajes enviados, las respuestas recibidas y el contenido parcial que ya se hubiera mostrado antes de una parada o interrupción. Está vinculada al asistente y a la organización con los que se abrió.

Al continuarla, Reagentia recupera el historial guardado. Una actualización posterior del agente no sustituye silenciosamente la versión utilizada por una conversación ya existente.

## Límites visibles

- Una configuración en borrador no se usa para ejecutar hasta que se publica.
- Una conversación solo puede abrirse o continuarse con un asistente habilitado y los permisos necesarios.
- Un recurso que aún no está listo no debe considerarse disponible.
- La finalización del despacho no equivale a un resultado correcto: revisa el estado final y los outputs.
- La disponibilidad funcional de un documento y su borrado físico no son instantáneos ni equivalentes.
