# Data Lake para BI

El módulo Insights publica datos de ReAuditIA en formato Parquet para analizarlos con herramientas de BI. La incorporación es diaria: no es una consulta en tiempo real y una configuración nueva puede aparecer en el siguiente ciclo.

## Datos necesarios para conectarse

Solicita a **Soporte**:

- el identificador de tu organización;
- el endpoint de acceso y, si corresponde, el endpoint alternativo;
- un token SAS con caducidad;
- la confirmación de la herramienta desde la que se consumirá.

Pide los permisos mínimos de **lectura** y **listado**. Si necesitas restringir el acceso a una o varias IP, indícalas al solicitarlo. Los permisos de escritura no están incluidos salvo que se habiliten expresamente para un caso acordado.

## Custodiar el token

- Guárdalo en el almacén seguro de la herramienta de BI, nunca dentro de un informe compartido, un repositorio o un correo.
- Limita su caducidad al periodo necesario; no debe superar 12 meses.
- Solicita una renovación antes de que caduque y sustituye las credenciales de las consultas programadas.
- Solicita su revocación inmediata si se comparte por error o deja de ser necesario.

## Organización de los datos

Las rutas se dividen por fecha con `year`, `month` y `day`. El consumidor debe leer todos los ficheros Parquet de las particiones que necesite y no depender de un nombre de fichero concreto.

| Información | Ruta relativa |
| --- | --- |
| Fichas de evaluación | `scorecards/{ficha}/year=YYYY/month=MM/day=DD/` |
| Formularios de audio | `formularios/general/{formulario}/year=YYYY/month=MM/day=DD/` |
| Objeciones | `formularios/objeciones/{formulario}/{comprobacion}/year=YYYY/month=MM/day=DD/` |
| Hechos documentales | `formularios/{formulario}/facts/year=YYYY/month=MM/day=DD/` |
| Detalle documental | `formularios/{formulario}/details/category={categoria}/year=YYYY/month=MM/day=DD/` |
| Elementos de listas documentales | `formularios/{formulario}/items/category={categoria}/field={campo}/year=YYYY/month=MM/day=DD/` |

En las rutas documentales se usa el **nombre del formulario**, no su identificador numérico.

### Capas documentales

- `facts`: una vista resumida por documento y categoría.
- `details`: los campos extraídos para cada categoría.
- `items`: una fila por cada elemento de un campo que contiene una lista.

Si una categoría o un campo todavía no ha producido datos, su carpeta puede no existir hasta un ciclo posterior.

## Entender las columnas

- En un formulario de audio aparecen las comprobaciones configuradas y los metadatos informados en cada carga.
- En una ficha de evaluación aparecen sus categorías y subcategorías con las puntuaciones calculadas, además de los metadatos disponibles.
- Las objeciones se consultan por separado porque una misma conversación puede producir varias filas.
- En `facts`, las columnas comunes identifican el documento, el formulario, el fichero, la fecha, la categoría y el número de páginas.
- En `details`, `document_id` permite relacionar cada registro con `facts`; el resto de columnas son los campos escalares de su categoría.
- En `items`, `document_id` mantiene esa relación, `array_index` indica la posición del elemento y las demás columnas contienen sus subcampos.

El esquema depende de la configuración. Para anticipar las columnas, abre el formulario y revisa sus comprobaciones y metadatos; para una ficha, revisa sus categorías, subcategorías, pesos y rangos. Si cambia la configuración, vuelve a actualizar el esquema en la herramienta de BI.

## Conectar Power BI

1. Abre **Obtener datos > Azure > Azure Data Lake Storage Gen2**.
2. Introduce el endpoint hasta el contenedor de tu organización, sin añadir una ruta de fichero concreta.
3. Selecciona **Firma de acceso compartido (SAS)** y pega únicamente el token entregado.
4. En el navegador de datos, entra en `scorecards` o `formularios` y selecciona las rutas necesarias.
5. Combina los ficheros Parquet de las particiones y revisa los tipos de columna antes de publicar el informe.
6. Configura la actualización después de comprobar manualmente que la consulta devuelve datos.

Si el endpoint personalizado no funciona con el conector, utiliza el endpoint alternativo entregado por Soporte. No construyas una dirección diferente por tu cuenta.

## Conectar Databricks

1. Guarda el token SAS en el almacén seguro del espacio de trabajo; no lo escribas en el notebook.
2. Configura la conexión con el endpoint y el contenedor entregados.
3. Comprueba primero que puedes listar la raíz de tu organización.
4. Lee los Parquet de la ruta necesaria de forma recursiva para incluir sus particiones.
5. Filtra por `year`, `month` y `day` y valida el esquema antes de crear una tabla o vista estable.

Ejemplo de ruta sintética:

```text
formularios/FormularioEjemplo/items/category=Pedidos/field=Lineas/year=2026/month=09/day=28/
```

## Incidencias frecuentes

| Problema | Comprobación |
| --- | --- |
| Acceso denegado | Revisa la caducidad del token, los permisos de lectura/listado y la IP de salida |
| No se puede abrir el endpoint | Prueba el endpoint alternativo entregado y confirma que tu red permite la conexión |
| La carpeta está vacía | Comprueba el nombre del formulario, la fecha y si ya terminó el siguiente ciclo diario; el retraso puede llegar a 24 horas |
| Faltan columnas | Revisa si estás combinando categorías o periodos con esquemas diferentes |
| Faltan elementos de una lista | Consulta la capa `items` además de `facts` y `details` |
| La actualización programada falla | Sustituye el token caducado en las credenciales de la fuente y vuelve a probar |

Al pedir ayuda, indica la herramienta, la ruta relativa, la fecha consultada y el mensaje de error. No adjuntes el token SAS completo.
