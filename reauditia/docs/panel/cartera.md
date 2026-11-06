# Cartera y consumo

<span id="cartera"></span>

**Cartera** muestra el saldo y el historial de consumo accesible para tu cuenta.

Puede incluir:

- saldo disponible;
- consumo acumulado;
- evolución por fecha;
- detalle de operaciones o descarga del historial.

El consumo puede agrupar distintas fases de un procesamiento. Para comparar dos periodos, utiliza las mismas fechas y espera a que los trabajos asociados hayan finalizado.

## Consumo de doblaje

El detalle de doblaje muestra el formulario, el servicio utilizado, los minutos
facturados, la tarifa aplicada y el importe. Los minutos se calculan a partir de
la duración del audio original y el precio es la tarifa configurada del servicio.

El cálculo es proporcional: duración en segundos / 60 × tarifa por minuto. No se
redondea la duración a minutos completos ni se añade un fijo por los pasos de
doblaje y publicación. Por ejemplo, 150 segundos a una tarifa ilustrativa de
0,40 por minuto generan un cargo de 1,00 en las unidades monetarias del saldo.

El cargo se registra cuando termina el doblaje, aunque la publicación posterior
en SharePoint falle. Un doblaje fallido no genera ese cargo y los reintentos de
publicación o limpieza del mismo trabajo no lo duplican.

La tarifa aplicada queda guardada en la operación: cambiar la tarifa del servicio
no recalcula consumos anteriores. Si no hay una tarifa válida o está a cero, no
se solicita el doblaje. La tarifa no se edita desde el formulario.

Si detectas una operación que no reconoces, anota la fecha, el formulario y el fichero relacionado sin copiar datos personales en la solicitud de soporte.
