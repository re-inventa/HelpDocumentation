# Guía de uso de ReAuditIA

<span id="bienvenido-a-la-plataforma-de-auditorias-automaticas-re-auditia"></span>
<span id="panel"></span>
<span id="api"></span>

ReAuditIA ayuda a revisar de forma homogénea grandes volúmenes de conversaciones y documentos. Permite definir qué se quiere comprobar, cargar los ficheros, seguir su procesamiento y consultar los resultados.

Esta guía explica **qué hace cada apartado, para qué sirve y cómo utilizarlo**. Las opciones disponibles dependen de tu rol y de las capacidades habilitadas para tu organización.

<div class="grid cards" markdown>

-   **Entrar en la plataforma**

    ---

    Accede, recupera tu contraseña y reconoce las opciones disponibles para tu perfil.

    [Primeros pasos](panel/inicio.md)

-   **Procesar ficheros**

    ---

    Elige un formulario, carga los ficheros y comprueba el resultado del procesamiento.

    [Formularios y cargas](panel/formularios.md)

-   **Configurar una ficha de evaluación**

    ---

    Define formularios, comprobaciones, metadatos e informes para adaptar la evaluación.

    [Diseño de fichas](panel/diseño.md)

-   **Consultar resultados**

    ---

    Filtra resultados, descarga información y revisa el consumo asociado.

    [Informes](panel/informes.md)

-   **Resolver una incidencia**

    ---

    Identifica estados pendientes o erróneos y aplica las comprobaciones recomendadas.

    [Incidencias frecuentes](panel/incidencias.md)

-   **Conectar otros sistemas**

    ---

    Automatiza cargas, recibe resultados por callback o consulta datos preparados para BI.

    [Integraciones](api/upload.md) · [Data Lake](insights/datalake.md)

</div>

## Flujo habitual

1. Entra con tu cuenta.
2. Abre el formulario que corresponda al tipo de fichero.
3. Carga los ficheros manualmente o utiliza una regla de subida automática si tu perfil dispone de ella.
4. Revisa **Tareas Background > Estado de los Ficheros** hasta que finalice el procesamiento.
5. Consulta el formulario o los apartados de informes para revisar los resultados.

## Accesos directos

- [Crear una cuenta e iniciar sesión](panel/inicio.md)
- [Diseñar formularios y fichas de evaluación](panel/diseño.md)
- [Configurar fuentes y reglas automáticas](panel/subida_automatica.md)
- [Revisar las ejecuciones de los conectores](panel/subidas_conector.md)
- [Cargar ficheros mediante una integración](api/upload.md)
- [Recibir resultados mediante callback](api/callback.md)
- [Consumir datos desde Data Lake](insights/datalake.md)
