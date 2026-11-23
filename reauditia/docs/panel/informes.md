# Informes

Los informes permiten consultar y descargar los resultados de los formularios.

## Auditorías automáticas y manuales

Los resultados de audio indican si la auditoría es **Automática** o **Manual**.
Utiliza el filtro de modalidad en las vistas y descargas que lo ofrecen para
consultarlas juntas o por separado. El acceso de un Supervisor incluye los
formularios propios y los que tenga asignados.

Solo se publican las auditorías manuales finalizadas. Las pendientes, los
borradores y las caducadas no se incluyen en tablas, CSV, gráficas ni fichas.
La fecha de auditoría de una manual es su finalización; la fecha de carga se
conserva por separado. Tenlo en cuenta al elegir el periodo.

El resultado conserva las respuestas y la autoría de carga, guardado y
finalización. La puntuación usa el informe vigente: editar su diseño puede
recalcular la nota sin modificar las respuestas cerradas.

En Insights/Metabase, la modalidad acompaña a los resultados cuando la
publicación analítica del formulario está habilitada. La disponibilidad depende
de esa publicación; no basta con haber guardado un borrador.

Consulta [Auditoría manual de grabaciones](formularios.md#auditoria-manual-de-grabaciones)
para conocer la carga, el guardado y la fecha límite.

## Resultado de Formulario

Esta descarga está disponible para el perfil Supervisor.

1. Abre **Informes > Resultado de Formulario**.
2. Selecciona un formulario y el rango de fechas.
3. En un formulario documental con varias categorías, elige también la categoría. Si solo existe una, ReAuditIA la selecciona automáticamente.
4. Pulsa **Generar CSV**.

En formularios documentales con campos de lista, la descarga puede ser un ZIP con un CSV principal y un CSV separado por cada lista.

En formularios de auditoría también pueden aparecer descargas separadas para comprobaciones de rebatimiento.

## Fichas de Evaluación

Esta vista muestra los informes asignados al Supervisor.

1. Abre **Informes > Fichas de Evaluación** y selecciona un informe.
2. Elige un rango de hasta 90 días.
3. Abre **Vista previa del informe** para comprobar categorías, subcategorías, comprobaciones, pesos y rangos.
4. Filtra por los metadatos disponibles cuando necesites analizar un segmento concreto.
5. Utiliza los controles de presentación:
   - **Normalizar resultados** lleva las puntuaciones a una base de 0 a 100.
   - **Cambiar el tipo de visualización de tabla** muestra la media de las categorías en tabla.
   - **Mostrar nota final en gráfico** añade la nota final a la gráfica.
6. Revisa las tarjetas, las gráficas y el resumen de la nota final. Este resumen incluye media, rango, mediana, moda, varianza, desviación típica y tamaño de la muestra.
7. Pulsa **Descargar informe** para obtener el CSV del informe y del rango de fechas. Los filtros de metadatos y los controles de presentación cambian la vista, no el contenido ni la escala del CSV.

## Visualización de Datos de Formularios

Esta vista ofrece una lectura general de la actividad del formulario:

1. Selecciona un rango de hasta 90 días, el formulario y, si existen, los metadatos.
2. Consulta las auditorías realizadas por día.
3. Selecciona una barra para centrar el análisis en ese formulario.
4. Revisa el resultado por cada comprobación de la auditoría.

## Panel analítico adicional

Algunas organizaciones disponen de un enlace adicional en el menú. Se abre en otra pestaña y respeta la información habilitada para la cuenta.

Si los totales no coinciden con una descarga, comprueba que ambas consultas usan el mismo formulario, periodo y filtros y que todos los ficheros están en estado final.
