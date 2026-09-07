# Conexión LLM

La conexión LLM permite que los agentes autorizados utilicen modelos de lenguaje dentro de los workflows de tu organización.

## Conectar

1. Abre **LLM Config**.
2. Selecciona **Conectar**.
3. Completa el flujo de autorización que se abre.
4. Regresa a Reagentia y espera a que el estado aparezca como conectado.
5. Ejecuta la prueba de conexión.
6. Comprueba que se muestran los modelos disponibles.

La conexión pertenece a la organización activa. No se comparte automáticamente con otras organizaciones.

## Comprobar el estado

Antes de lanzar un workflow que necesite modelos de lenguaje, revisa:

- que la conexión está activa;
- que la prueba termina correctamente;
- que el modelo requerido está disponible;
- que tu sesión pertenece a la organización correcta.

## Desconectar

La acción **Desconectar** revoca el uso desde Reagentia. Las ejecuciones en curso pueden terminar con error si aún necesitan una llamada al modelo, por lo que conviene detener o esperar esos trabajos antes de desconectar.

## Problemas frecuentes

| Síntoma | Qué hacer |
| --- | --- |
| No aparece **Conectar** | Solicita un rol con permiso de conexión. |
| La autorización no regresa a Reagentia | Cierra el flujo, vuelve a iniciar sesión y repite la conexión. |
| La prueba falla | Confirma el estado, vuelve a conectar y repite la prueba. |
| Falta un modelo | No lances el workflow; solicita revisar la configuración de modelos. |
| El estado pertenece a otra organización | Cambia a la organización correcta y vuelve a comprobarlo. |

No pegues claves, tokens ni capturas con datos de conexión en incidencias o documentación.
