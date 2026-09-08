# Casos de uso y ejemplos

Los siguientes casos son sintéticos. Sirven para entender cómo se adapta Reagentia a
procesos distintos sin depender de una organización o implantación concreta.

## Revisar un paquete documental

La organización ficticia **Organización Ejemplo** publica la solución **Control
documental** y el workflow **Revisión de paquete**.

1. Un administrador publica la configuración, los agentes y los recursos necesarios.
2. Un operador abre **Runs**, selecciona la solución y el workflow y carga dos documentos
   inventados.
3. Reagentia valida las entradas y crea una ejecución.
4. El operador sigue el progreso y descarga el resultado cuando termina.
5. Un observador autorizado consulta el historial, pero no modifica la configuración.

Este caso resulta útil cuando un proceso debe aplicar siempre los mismos pasos y conservar
qué versiones se utilizaron.

## Comparar una nueva configuración

Un responsable funcional quiere mejorar las instrucciones de un workflow sin alterar
ejecuciones anteriores.

1. Crea un borrador desde la versión publicada.
2. Modifica únicamente los campos disponibles en pantalla.
3. Revisa y publica la nueva versión.
4. Lanza una ejecución con datos sintéticos.
5. Compara el resultado con una ejecución anterior.

La ejecución anterior mantiene su configuración original. La nueva versión solo afecta a
lanzamientos posteriores.

## Recuperar una ejecución

Una ejecución queda pendiente de entrega o termina con un error operable.

1. El usuario abre el detalle desde **Runs**.
2. Lee el estado y la acción recomendada.
3. Usa **Reintentar despacho** si aparece disponible.
4. Si el proceso ya terminó y necesita repetirlo con las versiones actuales, utiliza
   **Relanzar**.
5. Comprueba que el nuevo intento o la nueva ejecución aparecen en el historial.

Las acciones visibles dependen del estado y de los permisos del usuario. No debe repetirse
el lanzamiento si la interfaz ya muestra una ejecución creada.

