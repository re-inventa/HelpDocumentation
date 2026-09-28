# Estado de los ficheros

<span id="estado-de-audios"></span>

Esta pantalla permite seguir los ficheros cargados manualmente o mediante una regla automática.

Utiliza el formulario y el rango de fechas para acotar la consulta antes de interpretar los estados.

La carga y el procesamiento son pasos distintos. Una carga manual, una regla automática o una [integración](../api/upload.md) entrega el fichero. Después, ReAuditIA lo prepara, lo transcribe cuando corresponde, realiza el análisis y publica el resultado.

La interfaz resume esas fases internas con estos estados:

| Estado | Significado | Qué hacer |
| --- | --- | --- |
| En proceso | El fichero fue aceptado y la transcripción o el análisis todavía no han terminado | Espera y actualiza la vista más tarde |
| Completado | El resultado está disponible | Abre el formulario o informe correspondiente |
| Error | El trabajo no pudo finalizar | Revisa el mensaje y aplica la acción indicada |

No se muestran estados independientes para cada fase. Que un fichero continúe **En proceso** no permite saber solo desde esta pantalla si está preparándose, transcribiéndose o analizándose.

## Comprobaciones útiles

- Confirma que el fichero aparece una sola vez.
- Comprueba el formulario y la fecha de carga.
- Espera a un estado final antes de usar el resultado.
- Si hay error, conserva el nombre del fichero, la hora aproximada y el mensaje mostrado para facilitar la asistencia.

Si un fichero permanece **En proceso** mucho más tiempo de lo habitual, actualiza la vista y comprueba que no exista otra entrada completada para el mismo fichero. Si continúa igual, contacta con **Soporte** indicando el formulario, el nombre y la hora aproximada. No lo cargues otra vez mientras siga activo.

No vuelvas a cargar inmediatamente un fichero que sigue procesándose: podrías crear un duplicado.

## Audios unidos durante la carga

Una unión manual aparece en el seguimiento como un único fichero con el nombre
elegido antes de la subida. La preparación y la unión ocurren primero en el
navegador; esta pantalla solo muestra el procesamiento posterior una vez que el
archivo combinado ha sido aceptado.

Comprueba que aparece una única entrada y que su formulario y metadatos son los
esperados. Un estado de error puede corresponder a la transcripción, a una
evaluación concreta o a metadatos obligatorios ausentes, aunque la unión y la
subida hayan terminado correctamente.
