# Incidencias y recuperación

## La ejecución sigue creada

Espera el umbral que indique la interfaz. Si aparece **Reintentar despacho**, úsalo una vez y vuelve al detalle. No crees otro lanzamiento salvo que el sistema confirme que el anterior no existe.

## La cancelación no termina

Una cancelación puede permanecer en **Cancelando** mientras se confirma el estado. Si aparece **Reintentar cancelación**, úsalo y conserva el identificador de la ejecución para soporte.

## La ejecución falla o caduca

1. Revisa el evento y el paso que falló.
2. Comprueba conexión LLM, recursos y archivos de entrada.
3. Corrige la causa fuera de la ejecución terminada.
4. Usa **Relanzar** para crear una ejecución trazable con la configuración permitida.

## No hay resultados descargables

Comprueba que el paso productor terminó correctamente y que el artifact no está eliminado o fuera de retención. Una ejecución puede tener resultados parciales; revisa cada item y paso.

## Acceso denegado

Verifica organización activa y rol. No compartas una sesión ni pidas que se amplíen permisos por tanteo: indica la acción concreta que necesitas realizar.

## Qué incluir al pedir soporte

- identificador visible de la ejecución;
- fecha y hora aproximadas;
- organización, sin datos personales;
- estado mostrado y acción intentada;
- texto del error saneado;
- si el problema se repite en un lanzamiento nuevo.

No incluyas documentos, claves, tokens, enlaces temporales de descarga ni capturas con información sensible.
