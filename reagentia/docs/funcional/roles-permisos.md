# Roles y permisos

Los permisos se aplican dentro de la organización activa. El administrador de plataforma es el único rol que puede actuar de forma transversal.

| Acción | Administrador de plataforma | Administrador de organización | Operador | Observador |
| --- | :---: | :---: | :---: | :---: |
| Ver workflows, agentes y ejecuciones | Sí | Sí | Sí | Sí |
| Ver asistentes | Sí | Sí | Sí | Sí |
| Listar, iniciar, continuar, detener y cerrar conversaciones | Sí | Sí | Sí | No |
| Lanzar, cancelar y relanzar | Sí | Sí | Sí | No |
| Conectar o desconectar el acceso LLM | Sí | Sí | Sí | No |
| Editar y publicar agentes | Sí | Sí | No | No |
| Configurar y revocar canales públicos de asistentes | Sí | Sí | No | No |
| Configurar y publicar workflows | Sí | Sí | No | No |
| Gestionar tools, miembros y auditoría | Sí | Sí | No | No |
| Eliminar artifacts antes de su vencimiento | Sí | Sí | No | No |
| Gestionar organizaciones | Sí | No | No | No |

!!! warning "El permiso es la regla"
    La tabla refleja la configuración inicial. La autorización efectiva se valida por permiso en cada operación; el nombre del rol por sí solo no concede acceso.

## Acciones condicionadas por estado

Tener permiso no implica que una acción siempre esté disponible:

- cancelar solo se ofrece mientras la ejecución puede detenerse;
- detener una respuesta solo se ofrece mientras el asistente está respondiendo;
- cerrar una conversación requiere que no haya una respuesta en curso; las cerradas solo se consultan;
- abrir o continuar una conversación exige que el asistente esté habilitado;
- relanzar solo se ofrece para estados finales;
- reintentar el despacho solo aparece cuando la ejecución sigue creada y no tiene trabajo activo;
- descargar exige que exista un resultado disponible y dentro de retención;
- publicar exige un borrador válido.
