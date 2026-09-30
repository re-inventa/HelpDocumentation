# Callback de resultados

El callback permite que un sistema externo reciba el resultado de un formulario de audio mediante una petición `POST`.

ReAuditIA lo envía cuando el procesamiento clásico termina correctamente y no hay errores en las comprobaciones. Si el formulario no tiene una URL configurada, o el procesamiento termina con error, no se envía.

## Configurarlo

1. Abre el formulario con un perfil que pueda editar su configuración.
2. En **Callback**, introduce una URL que comience por `https://`.
3. Si el receptor exige autenticación, indica la cabecera en formato `Nombre:valor`.
4. Guarda los cambios y prueba el recorrido completo con un fichero sin datos reales.

Si eliminas la URL, también deja de utilizarse la cabecera asociada. Guarda el valor de la cabecera en un almacén seguro y no lo incluyas en documentación, capturas ni incidencias.

## Campos comunes

| Campo | Contenido |
| --- | --- |
| `form` | Identificador del formulario que procesó el fichero |
| `audio_file` | Nombre del fichero procesado |
| `metadata` | Lista de metadatos presentes, cada uno con su nombre y valor |
| `audit` | Lista de comprobaciones con `item` y `value` |

El valor de una comprobación puede ser texto o una estructura, según su tipo.

## Contrato sin diarización

El contrato heredado utiliza `transcription`. Su valor es una lista en la que cada elemento relaciona el nombre del transcriptor con el texto obtenido.

```json
{
  "transcription": [
    {"principal": "Buenos días, ¿en qué puedo ayudarle?"}
  ],
  "form": 42,
  "audio_file": "llamada-001.wav",
  "metadata": [
    {"Canal": "Telefono"}
  ],
  "audit": [
    {"item": "Saludo inicial", "value": "Correcto"}
  ]
}
```

## Contrato con diarización

Cuando el formulario utiliza diarización, el cuerpo contiene `transcriptions` en lugar de `transcription`. Puede incluir una transcripción `primary` y otra `secondary`.

```json
{
  "transcriptions": [
    {
      "role": "primary",
      "transcriptor": "principal",
      "text": "Buenos días, ¿en qué puedo ayudarle?",
      "duration": 3.8,
      "words": [
        {"start": 0, "end": 400, "text": "Buenos", "speaker": 0}
      ]
    },
    {
      "role": "secondary",
      "transcriptor": "secundario",
      "text": "Buenos días.",
      "duration": 1.2,
      "words": []
    }
  ],
  "form": 42,
  "audio_file": "llamada-001.wav",
  "metadata": [
    {"Canal": "Telefono"}
  ],
  "audit": [
    {"item": "Saludo inicial", "value": "Correcto"}
  ]
}
```

| Campo de cada transcripción | Contenido |
| --- | --- |
| `role` | `primary` o `secondary` |
| `transcriptor` | Nombre del transcriptor utilizado |
| `text` | Texto completo |
| `duration` | Duración informada |
| `words` | Detalle por palabras devuelto por el transcriptor; la forma de cada elemento puede variar |

Para relacionar la notificación con el envío original, utiliza `audio_file` y añade un metadato estable si el nombre del fichero no es suficiente.

## Tiempo de respuesta y reintentos

- Cada intento espera como máximo 10 segundos.
- Si falla el primero, pueden realizarse hasta tres reintentos.
- Los reintentos solo se realizan mientras quede tiempo dentro del procesamiento; no se garantiza que siempre se ejecuten los tres.

El receptor debe validar la petición, responder rápidamente con un estado correcto y continuar su trabajo de forma asíncrona. No mantengas la conexión abierta mientras realizas procesos largos.

## Comprobación

1. Procesa un fichero de prueba y espera a que termine correctamente.
2. Comprueba que el receptor obtiene una sola entrega correcta o identifica posibles reintentos.
3. Valida ambos contratos si tu organización utiliza formularios con y sin diarización.
4. Si no llega, sigue las comprobaciones de [Incidencias frecuentes](../panel/incidencias.md#no-recibo-el-callback).
