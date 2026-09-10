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

Si la autorización caduca o se revoca, utiliza la acción de reconexión de la tabla.

No compartas credenciales en nombres, descripciones o capturas. Si una autorización caduca o se revoca, vuelve a conectar la fuente desde la propia pantalla.

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
- **Lookback de descarga** omite directorios SFTP más antiguos que el número indicado, entre 1 y 365 días. Vacío significa sin límite.
- **Máximo de audios por conversación** descarta un grupo completo si supera el tope. Solo aparece en estrategias que agrupan.
- **Filtros de origen** permiten filtrar elementos de SharePoint por una propiedad, usando igualdad o una lista de valores.

## 4. Elegir la estrategia de audio

- **Sin agrupación**: cada fichero se procesa por separado.
- **Teléfono**: agrupa los fragmentos que comparten el teléfono según el convenio del nombre.
- **Teléfono e identificador de llamada**: combina ambos datos para formar el grupo.
- **Expresión regular**: extrae del nombre los grupos definidos por una regla. Comprueba siempre el patrón con un nombre real antes de guardar.

## 5. Completar los metadatos

Cada metadato configurado en el formulario puede recibir:

- un valor fijo para todos los ficheros de la regla;
- un valor extraído mediante una expresión regular;
- una extracción aplicada solo al nombre del fichero o a la ruta completa.

Si el formulario limita el metadato a una lista cerrada, utiliza uno de sus valores. Un fallo de extracción impide subir el fichero y aparecerá en el seguimiento.

## 6. Evitar duplicados y cargas excesivas

- Antes de activar una regla para todo el origen, pruébala con una carpeta acotada y pocos ficheros.
- Utiliza una ruta lo más concreta posible.
- Ajusta el rango temporal al volumen habitual.
- Define límites de cantidad o duración cuando estén disponibles.
- No crees dos reglas activas que cubran exactamente los mismos ficheros.
- Comprueba el seguimiento después de modificar una regla.

## Ejemplo

Una organización recibe cada día grabaciones en una carpeta separada. El administrador crea una fuente, limita la regla a esa carpeta, selecciona el formulario de calidad, utiliza `Canal` como metadato fijo y programa una revisión diaria. Después valida la primera ejecución en **Subidas conector**.
