# Borrado de organizaciones

El borrado definitivo retira una organización que lleva tiempo inactiva, sin
interacción ni trabajo en curso. Solo puede solicitarlo una cuenta
**Superadmin** desde **Administración > Organizaciones**.

!!! danger "Acción irreversible"
    La confirmación inicia una baja definitiva. No hay una opción para cancelar
    la solicitud ni recuperar los datos ya eliminados.

## Qué se elimina y qué se conserva

El alcance incluye usuarios, movimientos económicos, formularios, resultados,
configuraciones de ingesta, ficheros, analítica y archivo histórico de la
organización. También incluye sus copias de seguridad y los recursos de Azure
asociados exclusivamente a ella, si existen. Se comprueba tanto el origen como
la **continuidad**, la copia operativa mantenida en un segundo destino.

Se conservan los datos y recursos de otras organizaciones, los recursos
compartidos y los ficheros originales de los sistemas externos, como FTP o
SharePoint. Eliminar una copia gestionada por ReAuditIA no borra ese original.

!!! warning "Las copias pueden seguir pendientes"
    Las copias gestionadas sujetas a retención no desaparecen de inmediato.
    La solicitud sigue pendiente hasta comprobar su caducidad y la eliminación
    en ambos destinos. Que la organización ya no aparezca en el listado no
    significa que todo el borrado haya terminado.

## Solicitar el borrado

1. Entra con una cuenta Superadmin y abre **Administración > Organizaciones**.
2. Localiza la organización y pulsa **Eliminar**. No puedes borrar la
   organización de tu propia cuenta.
3. Revisa el nombre, los recuentos y la fecha del último trabajo registrado.
   Si no se puede cargar el inventario o existe trabajo en curso, el borrado
   queda bloqueado.
4. Confirma que la organización lleva tiempo inactiva, sin interacción ni
   trabajo en curso. La fecha mostrada ayuda a revisarlo; no sustituye esa
   comprobación ni establece un plazo automático de días.
5. Escribe el nombre exacto que aparece, respetando espacios y mayúsculas.
6. Pulsa **Solicitar borrado irreversible**.
7. En la parte inferior de **Administración > Organizaciones**, consulta la sección
   **Borrado de organizaciones** para seguir la solicitud.

Puedes usar **Cancelar** antes de confirmar. Tras registrar la solicitud se
bloquean nuevos accesos de carga y su renovación; una URL de carga emitida
antes no se considera revocada por el mero registro de la solicitud.

El proceso coordina el cierre de las subidas automáticas, el archivo histórico,
las notificaciones y la copia de continuidad. Una operación automática pendiente
puede impedir que avance hasta que se compruebe su finalización.

## Seguimiento y reintentos

Puedes recargar la página y volver a **Borrado de organizaciones**, aunque la
organización ya no aparezca arriba. Pulsa **Ver estado de #…** o guarda el enlace
de la página después de seleccionar la solicitud para volver a ella.

| Fase | Qué significa |
| --- | --- |
| Solicitud registrada | El cierre está registrado; el proceso puede seguir pendiente de arrancar |
| Inventario preparado | Se han identificado los datos y recursos que debe comprobar el borrado |
| Borrando datos | La eliminación avanza conservando el progreso confirmado |
| Verificando continuidad y copias | Los datos de origen ya se han retirado; faltan comprobaciones de destino o copias retenidas |
| Borrado verificado | Se ha comprobado la finalización del alcance completo |

El detalle muestra filas eliminadas, recursos pendientes y, cuando corresponde,
la próxima comprobación. No son un porcentaje ni una estimación del tiempo
restante. Una solicitud registrada o un reintento aceptado no equivale a un
borrado verificado.

Si no se pudo iniciar el proceso o una comprobación falla, pulsa
**Reintentar borrado** en la misma solicitud. El reintento conserva el progreso;
no crea otra baja ni vuelve a eliminar lo ya confirmado. La acción deja de
aparecer cuando el estado es **Borrado verificado**.

Si el estado pide revisar permisos, configuración o inventario, o no puedes
consultarlo, contacta con [Soporte](incidencias.md#pedir-soporte). Conserva el
identificador de la solicitud, la hora y el mensaje visible. No recrees la
organización para resolver un error ni envíes credenciales o enlaces privados.
