# Gestión documental

ReAuditIA puede analizar documentos además de conversaciones cuando la capacidad está habilitada.

## Formularios documentales

Un formulario documental define los campos y comprobaciones que se obtendrán de cada fichero. Los administradores pueden crearlo desde **Diseño** y asociar uno de los analizadores disponibles para su organización.

## Analizadores

Desde **Diseño**, un Administrador puede asociar a sus formularios los analizadores disponibles para su organización.

Si no aparece el analizador necesario, solicítalo mediante **Soporte** en el menú. No intentes abrir una dirección directa que no aparezca en el menú.

## Elegir cómo dividir un documento

En el editor de un analizador de tipo **Clasificador-router**, la opción
**Segmentar automáticamente el documento** permite elegir cómo tratar el archivo:

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
sus selecciones. Al volver a activarla, revisa qué categorías las necesitan.
El modo elegido se conserva al guardar y volver a editar el clasificador.

El ajuste corresponde al clasificador editado. Si una categoría envía el archivo
a otro clasificador, este conserva su propia configuración.

## Asistencia para instrucciones

Algunos formularios ofrecen ayuda para proponer o evaluar instrucciones. La propuesta no se aplica automáticamente: revisa el resultado, compara el comportamiento y confirma el cambio solo si mejora el objetivo del formulario.
