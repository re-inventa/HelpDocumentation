# Roles y permisos

ReAuditIA adapta el menú y las acciones al rol de cada cuenta.

| Rol | Uso principal | Acciones habituales |
| --- | --- | --- |
| Supervisor | Revisar el trabajo asignado | Abrir formularios, cargar ficheros para auditoría automática o manual, auditar manualmente y consultar resultados e informes |
| Administrador | Configurar el trabajo de su organización | Crear y editar formularios, informes y reglas de subida automática; asociar a formularios los analizadores disponibles para su organización |
| Superadmin | Administración global de organizaciones | Solicitar el borrado definitivo de organizaciones inactivas y consultar su seguimiento |

Una opción puede estar limitada además por la organización o por la configuración del formulario.

La carga para auditoría automática y el trabajo de auditoría manual corresponden
al Supervisor. Administrador y Superadmin configuran el trabajo y consultan los
resultados según sus permisos; esos roles no ejecutan auditorías directamente.

El registro crea la cuenta con rol **Supervisor**. El cambio a Administrador debe solicitarse mediante **Soporte** en el menú.

Esta indicación se refiere al Administrador de la propia organización. Superadmin
corresponde a la administración global del servicio y no se obtiene con el registro.

El borrado definitivo está reservado a Superadmin; ser Administrador de una
organización no concede ese permiso. Consulta [Borrado de organizaciones](borrado_organizaciones.md)
para revisar su alcance irreversible y las condiciones de confirmación.

## Acceso compartido a formularios

Un Supervisor puede acceder a sus formularios y a los que le asigne la
administración dentro de su organización. Ese acceso incluye cargas, auditorías
manuales, resultados, fichas y exportaciones del formulario.

El propietario conserva su acceso. Las asignaciones adicionales no conceden
administración ni borrado, ni cambian la autoría de los datos anteriores. Un
Administrador de la organización o un Superadmin gestiona la lista de
**Supervisores autorizados**; consulta
[Formularios compartidos](formularios.md#formularios-compartidos).

!!! warning "Permiso insuficiente"
    No intentes acceder mediante una dirección guardada si la opción no aparece en el menú. Solicita mediante **Soporte** que comprueben tu rol.
