# Incidencias frecuentes

## No puedo entrar

- Comprueba el correo y la contraseña.
- Confirma que activaste la cuenta.
- Solicita un nuevo enlace de recuperación si el anterior caducó.
- Evita varios intentos simultáneos desde pestañas diferentes.

## El código de acceso no funciona

- Usa siempre el último código de seis dígitos recibido.
- Si aparece **Código incorrecto**, revisa los dígitos antes de repetir.
- Si aparece **Código caducado**, pulsa **Reenviar código** y descarta el anterior.
- Si se han solicitado demasiados códigos, espera antes de volver a intentarlo.
- Si el usuario está bloqueado, contacta con **Soporte** y no continúes probando códigos.

## No veo una opción del menú

La navegación depende del rol y de las capacidades habilitadas. Consulta [Roles y permisos](roles-permisos.md) y solicita el cambio mediante **Soporte** en el menú si necesitas otro acceso.

## Un fichero no termina

1. Abre [Estado de los ficheros](estado_audios.md).
2. Comprueba que la carga aparece y revisa su estado.
3. Espera si todavía está procesando.
4. Si termina en error, conserva el nombre, la hora aproximada, el formulario y el mensaje mostrado.

## Faltan resultados

- Comprueba que el fichero terminó correctamente.
- Revisa formulario, fechas y filtros.
- Verifica que estás usando la cuenta y organización correctas.
- No compares pantallas con periodos distintos.

## No puedo unir o subir varios audios

- Comprueba que el grupo contiene entre 2 y 32 archivos MP3 o WAV PCM y que no
  supera 80 minutos ni 1 GiB.
- Revisa el orden y completa todos los metadatos obligatorios antes de iniciar
  la preparación.
- Escribe un nombre base en **Nombre del audio resultante**. Si está vacío o
  solo contiene espacios, la aplicación mantiene bloqueada la operación y
  muestra la corrección junto al campo. No añadas `.mp3` al nombre.
- Mantén abierta la página durante la unión y la subida. Cerrar o recargar la
  página elimina el resultado temporal.
- Si falla únicamente la subida, usa **Reintentar subida sin volver a unir**
  antes de modificar los archivos, el orden o el nombre. La aplicación
  reutilizará el resultado que ya estaba preparado mientras siga disponible.
- Si aparece un error de memoria o de compatibilidad, divide el grupo o utiliza
  la carga individual. Para grupos cercanos al límite, usa preferentemente un
  navegador Chromium de escritorio actualizado.
- Si la subida terminó correctamente y quieres continuar en el mismo
  formulario, usa **Realizar otra subida**. Después podrás iniciar otra unión o
  cambiar a **Subir archivos por separado** sin recargar la página.

Si el fichero combinado aparece en [Estado de los
ficheros](estado_audios.md) pero faltan algunas evaluaciones, conserva el nombre,
la hora, el formulario y el mensaje. Esto permite distinguir un problema de
procesamiento posterior de un fallo durante la unión.

## Una subida automática no encuentra ficheros

- Comprueba el estado de conexión de la fuente.
- Revisa la ruta, los filtros y el periodo de búsqueda.
- Comprueba si los ficheros aparecen como omitidos en [Subidas conector](subidas_conector.md).

## No puedo conectar SharePoint

- Una fuente en **Pendiente de conectar** todavía necesita autorización.
- Si indica **Token caducado** o **Revocado**, utiliza la acción de reconexión e inicia sesión de nuevo.
- Si indica **Error**, revisa que la URL corresponda al sitio, biblioteca, carpeta o enlace compartido correcto.
- Una regla solo puede utilizar una fuente con estado **Conectado**.

## La carga directa devuelve un error

- Comprueba que utilizas la URL SAS completa y que no ha caducado ni sido revocada.
- Asegúrate de haber añadido la ruta del fichero antes de los parámetros de la URL.
- Revisa el tipo de contenido y los nombres de los metadatos.
- Consulta la [guía de carga directa](../api/upload.md) antes de generar un acceso nuevo.

## No recibo el callback

- Comprueba que el formulario tiene una URL `https://` guardada.
- Verifica que el fichero terminó sin errores: no se envía callback para un procesamiento fallido.
- Confirma que el receptor responde en menos de 10 segundos.
- Revisa que la cabecera configurada sea la esperada y no compartas su valor en la incidencia.
- Consulta la [guía del callback](../api/callback.md).

## No puedo consultar Data Lake

- Revisa que el endpoint y el identificador de organización sean los entregados.
- Comprueba la caducidad del token SAS y que tu IP esté autorizada cuando exista una restricción.
- Si la conexión funciona pero faltan datos recientes, espera al siguiente ciclo diario.
- Consulta la [guía de Data Lake](../insights/datalake.md).

## Pedir soporte

Incluye siempre:

- apartado en el que ocurre;
- fecha y hora aproximada;
- formulario o regla afectada;
- estado y mensaje visible;
- pasos realizados antes del fallo.

No envíes contraseñas, credenciales, enlaces privados ni ficheros con datos personales salvo que exista un canal autorizado para ello.
