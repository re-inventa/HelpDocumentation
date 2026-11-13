# Gestión documental

ReAuditIA puede analizar documentos además de conversaciones cuando la capacidad está habilitada.

## Formularios documentales

Un formulario documental define los campos y comprobaciones que se obtendrán de cada fichero. Los administradores pueden crearlo desde **Diseño** y asociar uno de los analizadores disponibles para su organización.

## Analizadores

Desde **Diseño**, un Administrador puede asociar a sus formularios los analizadores disponibles para su organización.

Si tu menú incluye el listado de analizadores, ábrelo para crear uno o editar
uno existente. Si no tienes esa opción o no aparece el analizador necesario,
solicítalo mediante **Soporte** en el menú.

## Elegir cómo dividir un documento

En el editor de un analizador de tipo **Clasificador-router**, la opción
**Segmentar automáticamente el documento** permite elegir cómo tratar el archivo.
Al crear un clasificador, viene activada:

- **Activada:** el clasificador puede reconocer varios documentos dentro del
  archivo y dividirlo en segmentos según su contenido.
- **Desactivada:** el clasificador trata todo el archivo como un único documento
  y lo envía completo al analizador destino. Es adecuado, por ejemplo, para las
  distintas páginas de un mismo contrato.

Con la segmentación activada, las categorías que terminan en un extractor pueden
ofrecer **Procesar cada página por separado**. Esta opción ejecuta la extracción
una vez por página. Desmarcarla mantiene la segmentación automática; para tratar
el archivo completo hay que desactivar la opción general.

Al desactivar la opción general desaparecen las opciones por página y se borran
sus selecciones. Al volver a activarla, las selecciones por página anteriores no
se recuperan: marca de nuevo las categorías que las necesiten.
El modo elegido se conserva al guardar y volver a editar el clasificador.

El ajuste corresponde al clasificador editado. Todos los analizadores destino
conservan su propia configuración, tanto extractores como otros clasificadores.

## Asistencia para instrucciones

Algunos formularios ofrecen ayuda para proponer o evaluar instrucciones. La propuesta no se aplica automáticamente: revisa el resultado, compara el comportamiento y confirma el cambio solo si mejora el objetivo del formulario.

## Sincronizar los resultados con Insights

Cuando la función esté habilitada para tu organización, abre el formulario
documental y pulsa **Sincronizar** en el apartado **Insights**. Se abrirá un popup
con el aviso de qué documentos se incluyen y cuándo pueden verse en Insights.
Revisa el aviso y pulsa **Aceptar** para lanzar la sincronización. **Cancelar**,
Escape o cerrar el popup no envían ninguna solicitud. Un usuario normal
puede sincronizar sus formularios; un administrador, los de su organización.
El botón aparece cuando la organización tiene Insights y la exportación preparada.

> Solo se sincronizarán con Insights los documentos que aparezcan como completados en Tareas en segundo plano.

Los que sigan en procesamiento no se incluirán.

La acción publica los resultados disponibles; no inicia ni repite el análisis.
Por ejemplo, si tres documentos están completados y dos siguen en procesamiento,
se publican los tres completados. Los otros podrán entrar en una sincronización
posterior, cuando sus tareas estén completadas.

| Estado | Qué verás |
| --- | --- |
| Pendiente | Actualización solicitada. Pendiente de ejecución |
| En curso | Actualizando Insights |
| Completada | Exportación completada a las HH:mm |
| Fallida durante la sincronización | No se ha podido completar la sincronización con Insights. Por favor, contacta con el servicio técnico e indica que ha fallado la sincronización del formulario. |

Puedes cerrar la pestaña y volver después: el seguimiento se conserva. La fecha
de la última exportación correcta permanece visible aunque otra solicitud falle.
Si terminan más documentos mientras se actualiza Insights, puedes volver a pulsar
**Sincronizar** y confirmar con **Aceptar** para incluir los resultados posteriores. Los clics repetidos que
cubren los mismos resultados se agrupan. Tras un fallo puedes reintentar; si se
te pide esperar, deja pasar unos segundos antes de volver a solicitarlo.

Si todos los documentos completados ya están publicados, el botón confirma:
**Insights ya está actualizado. No hay nuevos documentos completados que
sincronizar.** La fecha de exportación se conserva. Si la solicitud sigue
pendiente o en curso, otro clic también lo confirma en pantalla.

Si no se puede iniciar la sincronización, se te pedirá contactar con el servicio
técnico y la solicitud quedará conservada. Si el arranque no puede confirmarse,
seguirá pendiente hasta que una ejecución la atienda; esto no significa que esté
procesando ni que haya fallado. Una petición recibida al terminar otra ejecución
puede esperar hasta la siguiente actualización automática u otra ejecución que se inicie antes.

Usa **Abrir Insights** cuando aparezca el enlace. Una exportación completada puede
tardar en reflejarse en la pantalla o caché de Insights. La actualización automática
será horaria en los entornos donde se ponga en servicio esta función; consulta
[Data Lake para BI](../insights/datalake.md) para el acceso a los datos publicados.
