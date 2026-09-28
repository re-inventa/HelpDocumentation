# Carga directa de ficheros

<span id="upload"></span>
<span id="post--api-upload (Ejemplo)"></span>

La carga directa permite que una aplicación entregue ficheros a un formulario sin utilizar la pantalla de subida ni una regla automática. Cada acceso está asociado a un formulario y utiliza una URL SAS con fecha de caducidad.

## Obtener o revocar el acceso

Si tu perfil permite configurar el formulario:

1. Abre el formulario y localiza el apartado **Token SAS**.
2. Crea un acceso con un nombre que identifique la integración y selecciona su caducidad.
3. Copia la URL completa cuando se muestre y guárdala en el almacén seguro de la aplicación que realizará las cargas.
4. Para renovar el acceso, crea uno nuevo, cambia la integración y comprueba una carga antes de revocar el anterior.
5. Para cancelar un acceso, elimínalo desde la misma tabla.

Si el apartado no aparece, solicita a **Soporte** un acceso para el formulario e indica la finalidad, la caducidad necesaria y el entorno. No envíes la URL SAS por correo ni la incluyas en capturas o incidencias.

## Construir la dirección del fichero

La URL entregada contiene una dirección base y parámetros de autorización después de `?`. Para subir un fichero:

1. Conserva todos los parámetros recibidos.
2. Añade la carpeta y el nombre del fichero **antes** de `?`.
3. Codifica los espacios y caracteres especiales del nombre.

Ejemplo sintético:

```text
URL entregada:
https://storage.example.invalid/formulario?{PARAMETROS_SAS}

Fichero de destino:
https://storage.example.invalid/formulario/20260928/llamada-001.wav?{PARAMETROS_SAS}
```

La URL SAS ya contiene la autorización. No envíes una cabecera `Authorization: SharedKey` ni trates la firma como una contraseña separada.

## Enviar el fichero

Realiza una petición `PUT` con el contenido binario:

```bash
curl --request PUT \
  'https://storage.example.invalid/formulario/20260928/llamada-001.wav?{PARAMETROS_SAS}' \
  --header 'x-ms-blob-type: BlockBlob' \
  --header 'Content-Type: audio/wav' \
  --header 'x-ms-meta-canal: telefono' \
  --data-binary '@llamada-001.wav'
```

- `x-ms-blob-type: BlockBlob` identifica el tipo de carga esperado.
- `Content-Type` debe corresponder al fichero, por ejemplo `audio/wav`, `audio/mpeg` o `application/pdf`.
- Cada metadato se envía como `x-ms-meta-<nombre>`. El nombre debe coincidir con el configurado en el formulario.
- El cuerpo debe contener el fichero, no una representación en texto.

El ejemplo no incluye una firma válida y no puede utilizarse para acceder a ningún dato.

## Interpretar la respuesta

| Resultado | Significado | Acción recomendada |
| --- | --- | --- |
| `201 Created` | El fichero fue aceptado | Comprueba su aparición en **Estado de los Ficheros** |
| `400 Bad Request` | La ruta, una cabecera o un metadato no es válido | Revisa la dirección, el tipo de fichero y los metadatos |
| `403 Forbidden` | La URL ha caducado, fue revocada o no permite la operación | Sustituye el acceso por uno vigente |
| `404 Not Found` | El destino no corresponde al formulario o la dirección está incompleta | Vuelve a copiar la URL base y reconstruye la ruta |
| `409 Conflict` | El destino mantiene un estado incompatible con la carga | Evita cargas simultáneas sobre la misma ruta; si persiste, utiliza otro nombre y contacta con Soporte |

Que la petición sea aceptada no significa que el análisis haya terminado.

## Comprobar el procesamiento

1. Abre [Estado de los ficheros](../panel/estado_audios.md).
2. Busca el nombre enviado y comprueba el formulario y la hora.
3. Espera a **Completado** o revisa el mensaje si termina en **Error**.
4. Si has configurado un [callback](callback.md), confirma también la recepción del resultado.

No repitas la carga mientras el fichero siga **En proceso**.
