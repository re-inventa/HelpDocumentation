# Subida automática

La subida automática permite recoger ficheros desde una fuente SFTP o SharePoint autorizada y enviarlos al formulario correspondiente mediante reglas programadas.

Solo los perfiles administradores pueden configurar este apartado.

## 1. Crear una fuente SFTP

1. Abre **Subida automática > Fuentes SFTP**.
2. Escribe un nombre identificativo y pulsa **Añadir**.
3. Indica la dirección mediante un dominio o una IP pública, el puerto entre 1 y 65535, el usuario y la contraseña.
4. Guarda la fuente. Después podrás editarla o eliminarla desde la tabla.

Utiliza una cuenta técnica con el acceso mínimo a las carpetas necesarias. Al editar una fuente, deja la contraseña en blanco para conservar la actual.

## 2. Crear una fuente SharePoint

1. Abre **Subida automática > Fuentes SharePoint**.
2. Escribe un nombre y una dirección `https://` del sitio o carpeta.
3. Pulsa **Conectar con Microsoft**, inicia sesión y acepta el acceso solicitado.
4. Comprueba el estado de la fuente. Puede aparecer como pendiente, conectada, caducada, revocada o con error.

Si la autorización caduca o se revoca, utiliza la acción de reconexión de la tabla. No compartas credenciales en nombres, descripciones o capturas.

## 3. Crear una regla

1. Selecciona la fuente.
2. Elige el formulario de destino.
3. Indica la ruta que deba revisarse; debe comenzar por `/`.
4. Decide si la regla queda activa y si debe buscar en subcarpetas.
5. Fija el inicio y programa la revisión mediante **Intervalo** o **Cron (UTC)**. Debes usar solo uno de los dos.
6. Selecciona la estrategia de audio y configura únicamente los límites, filtros y metadatos que necesites.
7. Guarda la regla. Desde la tabla podrás activarla, desactivarla o editarla.

### Opciones de la regla

- **Borrar tras subir** elimina el fichero de la fuente después de una entrega correcta. Actívalo únicamente si la organización ha autorizado expresamente el borrado en origen.
- **Control de duración** descarta audios que queden fuera del mínimo o máximo configurado. El valor 0 deja ese límite sin aplicar.
- **Muestreo aleatorio** limita las grabaciones elegidas por directorio. Puede seguir probando candidatos hasta completar la cuota y limitar la muestra a los últimos 1-365 días.
- **Antigüedad máxima de descarga** omite directorios SFTP más antiguos que el número indicado, entre 1 y 365 días. Vacío significa sin límite.
- **Máximo de audios por conversación** descarta un grupo completo si supera el tope. Solo aparece en estrategias que agrupan.
- **Filtros de origen** permiten filtrar elementos de SharePoint por una propiedad, usando igualdad o una lista de valores.

## 4. Elegir la estrategia de audio

- **Sin agrupación**: cada fichero se procesa por separado.
- **Teléfono**: agrupa los fragmentos que comparten el teléfono según el convenio del nombre. Es una opción heredada y no se recomienda para configuraciones nuevas.
- **TeléfonoIdLlamada**: combina el teléfono y el identificador de llamada para formar el grupo. También es una opción heredada y no se recomienda para configuraciones nuevas.
- **Expresión regular (RegEx)**: extrae del nombre los grupos definidos por una regla. Es la opción recomendada cuando los ficheros siguen una nomenclatura acordada. Comprueba siempre el patrón con un nombre de fichero representativo antes de guardar.

## 5. Completar los metadatos

Cada metadato configurado en el formulario puede recibir:

- un valor fijo para todos los ficheros de la regla;
- un valor extraído mediante una expresión regular;
- una extracción aplicada solo al nombre del fichero o a la ruta completa.

Si el formulario limita el metadato a una lista cerrada, utiliza uno de sus valores. Un fallo de extracción impide subir el fichero y aparecerá en el seguimiento.

## 6. Editar metadatos en lote

La edición en lote permite aplicar el mismo cambio de metadatos a varias reglas sin abrirlas una por una. Solo admite reglas que cumplan las tres condiciones siguientes:

- son reglas SFTP, no reglas SharePoint;
- extraen el mismo conjunto de metadatos;
- aplican las expresiones al mismo ámbito: **Solo nombre** o **Ruta completa**.

Para actualizar las reglas:

1. En **Subida automática**, marca las reglas SFTP que quieras cambiar. La casilla de la cabecera selecciona todas las reglas SFTP de la tabla; las reglas SharePoint no se pueden incluir.
2. Comprueba el número de reglas seleccionadas y pulsa **Editar RegEx de metadatos en lote**.
3. Revisa la lista de reglas afectadas, identificadas por fuente, ruta y formulario.
4. Elige si las expresiones se aplican a **Solo nombre** o a **Ruta completa**.
5. Marca únicamente los metadatos que quieras actualizar. Los que no marques conservan el valor de cada regla.
6. Para cada metadato marcado, escribe el valor y utiliza **Regex** para alternar entre **Valor estático** y **Expresión regular**.
7. Si también quieres sustituir la expresión y los grupos de la estrategia de audio, marca **Incluir estrategia de agrupación (RegEx)**.
8. Pulsa **Aplicar a N reglas**. La pantalla limpia la selección, actualiza la tabla e indica cuántas reglas se modificaron. Si una falla, el aviso identifica su ruta.

La ventana no permite aplicar el cambio si detecta alguno de estos casos:

- no hay reglas seleccionadas;
- la selección incluye una regla SharePoint;
- las reglas no extraen el mismo conjunto de metadatos;
- las reglas no tienen metadatos configurados;
- las reglas no comparten el mismo ámbito de aplicación.

Después de aplicar el cambio, abre una de las reglas editadas y comprueba con un nombre de fichero real que la expresión extrae el valor esperado.

## 7. Evitar duplicados y cargas excesivas

- Antes de activar una regla para todo el origen, pruébala con una carpeta acotada y pocos ficheros.
- Utiliza una ruta lo más concreta posible.
- Ajusta el rango temporal al volumen habitual.
- Define límites de cantidad o duración cuando estén disponibles.
- No crees dos reglas activas que cubran exactamente los mismos ficheros.
- Comprueba el seguimiento después de modificar una regla.

## Ejemplo

Una organización recibe cada día grabaciones en una carpeta separada. El administrador crea una fuente, limita la regla a esa carpeta, selecciona el formulario de calidad, utiliza `Canal` como metadato fijo y programa una revisión diaria. Después valida la primera ejecución en **Subidas conector**.
