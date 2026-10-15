# Acceso y cuenta

## Alcance actual

Pueden crear una cuenta las personas cuyo correo pertenece a un dominio habilitado por
una organización activa. El registro solo aparece en los entornos donde esta capacidad
está habilitada. Antes del primer acceso es obligatorio verificar el correo.

Cuando la protección por código está habilitada, la aplicación solicita un código por
correo al acceder desde un navegador o dispositivo no recordado. En esos entornos
también están disponibles la recuperación de contraseña y la sección **Seguridad** para
cambiarla. Si la recuperación indica que no está disponible o no aparece la sección
**Seguridad**, la capacidad todavía no está habilitada en ese entorno.

## Crear una cuenta

1. Abre la pantalla de inicio de sesión y pulsa **Crear cuenta**.
2. Introduce tu nombre y el correo electrónico de tu organización.
3. Escribe una contraseña de entre 12 y 128 caracteres y repítela.
4. Completa la comprobación de seguridad y pulsa **Crear cuenta**.
5. Introduce el código de seis dígitos recibido por correo y pulsa **Verificar email**.
6. Vuelve al inicio e inicia sesión con el correo y la contraseña elegidos.

El código caduca en 10 minutos y admite cinco intentos. **Reenviar código** se habilita
después de 60 segundos y permite como máximo tres reenvíos cada 15 minutos. Cada reenvío
invalida el código anterior; utiliza siempre el último recibido. El alta completa caduca
si el correo no se verifica en 24 horas. Después puedes empezar un registro nuevo con el
mismo correo.

La organización y el acceso inicial se determinan a partir del dominio del correo. No
puedes elegir otra organización ni solicitar un rol desde el formulario. Una cuenta
nueva entra como **Observador**, con acceso de consulta. Pide a una persona administradora
que cambie tu rol si necesitas realizar otras acciones.

La pantalla muestra la misma confirmación cuando el correo ya tiene una cuenta. En ese
caso no modifica la cuenta, la contraseña ni sus permisos, y el titular recibe un aviso
de seguridad. Esta respuesta uniforme evita revelar a otras personas qué correos están
registrados.

## Iniciar sesión

1. Abre la pantalla de inicio de sesión.
2. Introduce tu correo electrónico y tu contraseña.
3. Si aparece una comprobación de seguridad, complétala antes de continuar.
4. Pulsa **Iniciar sesión**.
5. Si aparece **Confirma el acceso**, introduce el código recibido por correo.
6. Marca **Recordar este dispositivo durante 30 días** solo si es un dispositivo
   personal y protegido.
7. Pulsa **Verificar código**.

Una sesión iniciada correctamente dura como máximo cuatro horas y no amplía ese plazo
por seguir navegando. Al finalizar, vuelve a identificarte desde la pantalla de acceso.

Usa **Cerrar sesión** cuando termines, especialmente en un equipo compartido. El cierre
retira el acceso de esa sesión y devuelve a la pantalla de inicio.

## Código de acceso y dispositivo recordado

El código de acceso tiene seis dígitos, caduca en 10 minutos y solo puede utilizarse una
vez. Después de cinco intentos incorrectos deja de ser válido. Usa **Reenviar código** si
no lo recibes: el botón vuelve a estar disponible después de 60 segundos y admite como
máximo tres reenvíos cada 15 minutos. Cuando solicites otro, utiliza siempre el código
más reciente.

La opción **Recordar este dispositivo durante 30 días** evita pedir otro código en ese
navegador durante ese plazo. No la marques en equipos compartidos. La aplicación volverá
a solicitar el código si termina el plazo, si se eliminan los datos del navegador o si
se revoca la confianza del dispositivo. Cambiar o recuperar la contraseña revoca todos
los dispositivos recordados; la desactivación del acceso también puede revocarlos.

El mensaje **El código no es válido, ha caducado o ha agotado sus intentos.** no distingue
la causa. Solicita un código nuevo, espera a recibirlo e introduce solo el último.

## Comprobación de seguridad

Según la configuración del entorno, la pantalla puede pedir una comprobación antes de
enviar las credenciales o solicitar la recuperación. Complétala en la propia página. Si
el acceso falla, la comprobación anterior deja de servir y la pantalla puede pedir una
nueva.

Si aparece **Completa la verificación de seguridad.**, espera a que el control termine
y vuelve a pulsar **Iniciar sesión**. Si no carga o se reinicia repetidamente, recarga
la página una vez y consulta [Incidencias y recuperación](incidencias.md#acceso-a-la-cuenta).

## Rechazos y esperas temporales

**Credenciales incorrectas.** es un mensaje deliberadamente genérico. Puede indicar
que el correo o la contraseña no son válidos, pero también que la cuenta, la
verificación del correo o el acceso a la organización no están activos. La pantalla no
distingue esas causas para no revelar información sobre otras cuentas.

Después de varios intentos fallidos puede aplicarse una espera temporal. La espera se
hace mayor si continúan los fallos y nunca desactiva permanentemente la cuenta. No
repitas el envío de forma continua: espera unos minutos y vuelve a intentarlo una sola
vez. Si sigue fallando, pide a la persona administradora que confirme tu acceso sin
compartir la contraseña.

!!! warning "Protege tus credenciales y códigos"
    No compartas contraseñas, códigos ni comprobaciones de seguridad. Si recibes un
    código que no has solicitado, no lo utilices ni lo comuniques: cambia la contraseña
    desde un dispositivo de confianza o avisa a la persona responsable de tu
    organización.

## Requisitos de la contraseña

Una contraseña nueva debe tener entre 12 y 128 caracteres. No es obligatorio combinar
mayúsculas, minúsculas, números y símbolos, por lo que puedes usar una frase larga que
te resulte fácil de recordar y difícil de adivinar.

La contraseña no puede contener tu dirección de correo, la parte anterior a `@` ni el
nombre de la organización. La aplicación también rechaza contraseñas que aparecen en
filtraciones conocidas. No reutilices una contraseña de otro servicio.

## Recuperar una contraseña olvidada

1. En la pantalla de inicio, pulsa **¿Has olvidado tu contraseña?**.
2. Introduce tu correo y completa la comprobación de seguridad si aparece.
3. Pulsa **Enviar código**. La respuesta es la misma exista o no una cuenta con ese
   correo.
4. Introduce el código de seis dígitos recibido, la nueva contraseña y su confirmación.
5. Pulsa **Cambiar contraseña** y vuelve al inicio de sesión.

El código de recuperación comparte el plazo de 10 minutos y el máximo de cinco intentos.
Al completar la recuperación se cierran todas las sesiones y se revocan todos los
dispositivos recordados. La aplicación envía una confirmación al correo de la cuenta.

## Cambiar la contraseña con la sesión iniciada

1. Abre **Seguridad** en la navegación de la aplicación.
2. Introduce la contraseña actual.
3. Escribe la nueva contraseña y repítela.
4. Pulsa **Cambiar contraseña**.

La aplicación conserva la sesión actual cuando puede hacerlo, pero cierra las demás
sesiones y revoca los dispositivos recordados. Si no puede conservarla, vuelve a la
pantalla de inicio para identificarte con la contraseña nueva. También recibirás una
confirmación por correo.
