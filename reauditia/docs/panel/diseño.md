# Diseño

El apartado **Diseño** permite a los perfiles autorizados crear formularios e informes.

## Crear un formulario de auditoría

1. Abre **Diseño > Crear un Formulario de Auditoría**.
2. Selecciona el supervisor que utilizará el formulario.
3. Escribe un nombre de 4 a 30 caracteres, con letras minúsculas, números y guiones. Debe empezar y terminar por letra o número y no debe contener guiones consecutivos.
4. Pasa a la columna de seleccionados las comprobaciones que necesites. Puedes buscarlas, consultar su descripción y moverlas de una en una o en bloque.
5. Configura los metadatos y el resto de opciones aplicables.
6. Revisa el resumen y crea el formulario.

Incluye solo las comprobaciones necesarias: cada una añade información al resultado y puede aumentar el tiempo y el consumo del procesamiento.

### Clasificar las cargas con metadatos

Puedes crear hasta **12 metadatos** por formulario, por ejemplo `Agente`, `Servicio` o `Canal`.

- Para que el nombre sea compatible con la carga directa, debe comenzar por una letra o guion bajo y continuar solo con letras sin tilde, números o guion bajo; no admite espacios. La pantalla avisa si no cumple este formato.
- Puedes introducir varios valores separados por comas. No se duplican valores que solo cambian en mayúsculas o minúsculas.
- Con el candado cerrado, quien carga ficheros debe elegir uno de los valores definidos. Por eso un metadato bloqueado necesita al menos un valor.
- Con el candado abierto, quien carga puede introducir un valor distinto.

Ejemplo: crea el metadato `Canal`, añade `Entrada` y `Salida` y ciérralo para que todas las cargas utilicen una de esas dos clasificaciones.

## Editar un formulario de auditoría

Un Administrador puede abrir un formulario existente y, cuando la edición esté habilitada:

- añadir nuevas comprobaciones;
- activar o desactivar comprobaciones existentes;
- cambiar los transcriptores y sus opciones disponibles;
- modificar la configuración que muestre el formulario.

No hace falta crear otro formulario solo para añadir una comprobación. Antes de editar, revisa el impacto sobre cargas futuras y sobre el informe asociado.

## Crear un formulario de gestión documental

1. Abre **Diseño > Crear un Formulario de Gestión Documental**.
2. Asigna el supervisor.
3. Indica un nombre y configura los campos solicitados.
4. Revisa el resumen antes de confirmar.

Las opciones documentales dependen de las capacidades habilitadas. Si necesitas definir categorías o extractores, consulta [Gestión documental](documentos.md).

## Crear un informe

1. Abre **Diseño > Crear un Informe**.
2. Crea un informe o selecciona uno existente para modificarlo.
3. Selecciona el supervisor y uno de sus formularios.
4. Añade categorías y, si necesitas un nivel intermedio, subcategorías.
5. Añade las comprobaciones del formulario a la categoría o subcategoría correspondiente.
6. Define los parámetros y guarda el informe.
7. Comprueba el resultado desde **Informes > Fichas de Evaluación**.

### Estructura y parámetros

- **Categoría**: bloque principal de la evaluación.
- **Subcategoría**: división opcional dentro de una categoría.
- **Comprobación**: elemento evaluado por el formulario.
- **Peso**: influencia del elemento dentro de su nivel. Al guardar, ReAuditIA ajusta los pesos para calcular el resultado de forma coherente.
- **Rango**: puntuación mínima y máxima, con formato `mínimo-máximo`. En una comprobación de verdadero o falso el rango queda fijado.
- **Crítico**: si una comprobación crítica obtiene un resultado negativo, el bloque correspondiente recibe su valor mínimo.

Puedes cambiar nombres, parámetros y elementos, eliminar componentes y reordenarlos o moverlos entre bloques. La interfaz permite hacerlo arrastrando o con las acciones **Subir**, **Bajar** y **Mover a**.

!!! warning "Informe con análisis activo"
    Un informe con el análisis activo queda bloqueado para edición y no puede guardarse hasta que deje de estar activo.
