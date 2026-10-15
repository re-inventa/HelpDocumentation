# Administración de organizaciones, usuarios y accesos

La sección **Administración** reúne tres superficies distintas. Cada persona ve solo las
que corresponden a sus permisos:

| Sección | Alcance | Quién puede utilizarla |
| --- | --- | --- |
| **Organizaciones** | Todas las organizaciones | Administrador de plataforma |
| **Usuarios** | Todas las cuentas y sus accesos | Administrador de plataforma |
| **Miembros** | Solo la organización activa | Administrador de plataforma y administrador de organización |

Una membresía es el acceso de una cuenta a una organización concreta. Una misma persona
puede tener varias membresías, con un rol y un estado diferentes en cada organización.
Desactivar una membresía no desactiva necesariamente la cuenta completa.

Cada cambio queda registrado para facilitar su revisión posterior. Si ese registro no puede
completarse, la aplicación no aplica la operación.

## Gestionar organizaciones

### Consultar organizaciones

Abre **Administración → Organizaciones** para ver el nombre, el identificador corto, el
estado, el número de miembros y los dominios de cada organización.

Puedes buscar por nombre, identificador corto o dominio. La lista se divide en páginas cuando
hay más resultados de los que caben en una sola vista.

### Crear una organización

1. Escribe el nombre visible de la organización.
2. Define un identificador corto, por ejemplo `empresa-demostracion`.
3. Selecciona **Crear organización**.

El identificador corto admite minúsculas, números y guiones. Debe ser único y queda fijo tras
la creación para no romper direcciones o integraciones. Después puedes cambiar el nombre
visible, pero no ese identificador.

La organización se crea activa y sin dominios. Crear una organización no crea usuarios ni
les concede acceso automáticamente.

### Cambiar el nombre

1. Selecciona la organización en la lista.
2. Modifica el nombre visible.
3. Selecciona **Guardar nombre**.

Este cambio no modifica el identificador corto, los dominios, los miembros ni el estado.

### Suspender una organización

1. Selecciona una organización activa.
2. Selecciona **Suspender organización**.
3. Escribe un motivo y confirma la suspensión.

Una organización suspendida conserva su configuración y sus datos, pero deja de permitir el
acceso. Las personas que solo pertenecen a esa organización pierden sus sesiones abiertas y
sus dispositivos dejan de estar recordados. Si una persona también pertenece a otra
organización activa, conserva el acceso a esa otra organización.

La aplicación impide una suspensión que dejaría la plataforma sin ninguna persona con
administración global activa.

### Reactivar una organización

1. Selecciona una organización suspendida.
2. Selecciona **Reactivar organización**.
3. Escribe un motivo y confirma la reactivación.

La reactivación vuelve a permitir que la organización participe en el acceso. No recupera las
sesiones que se cerraron al suspenderla: las personas afectadas deben iniciar sesión de nuevo.

### Gestionar dominios de registro

Los dominios permiten asociar nuevas cuentas a la organización correcta durante el registro.
Por ejemplo, una organización ficticia podría utilizar `empresa-demostracion.example`.

Para añadir uno:

1. Selecciona la organización.
2. Escribe el dominio sin `@`, espacios, protocolo ni ruta.
3. Selecciona **Añadir dominio**.

El dominio se guarda en minúsculas. Un dominio solo puede estar reservado para una
organización y no se admiten proveedores de correo público. Si ya pertenece a otra
organización, solicita que una persona administradora revise la asignación; no intentes crear
una variante con mayúsculas.

Para dejar de admitir nuevos registros con un dominio, selecciónalo y pulsa **Retirar**. La
aplicación pide confirmación. Retirar un dominio no elimina usuarios ni membresías existentes,
ni traslada el dominio automáticamente a otra organización.

!!! warning "Comprueba la organización antes de confirmar"
    La suspensión afecta al acceso de sus miembros y la retirada de un dominio afecta a
    futuros registros. Revisa el nombre, el identificador y el motivo antes de continuar.

## Gestionar miembros de la organización activa

Abre **Administración → Miembros** para consultar únicamente las personas de la organización
activa. La lista nunca muestra sus accesos a otras organizaciones. Puedes buscar por nombre o
correo y filtrar por estado de la membresía o por rol.

### Cambiar el rol de un miembro

1. Localiza a la persona en **Miembros**.
2. Elige **Administrador de organización**, **Operador** o **Lector**.
3. Selecciona **Guardar rol**.
4. Revisa el cambio y pulsa **Confirmar rol**.

El nuevo rol se aplica en la siguiente petición de la persona afectada. Una administración de
organización no puede modificar una membresía con el rol protegido de administrador de
plataforma.

### Desactivar o reactivar una membresía

Selecciona **Desactivar membresía** para retirar el acceso a la organización activa y confirma
la operación. Si esa era la única membresía activa de la persona, sus sesiones y dispositivos
recordados se revocan. Si conserva otra membresía válida, la aplicación puede pasar a esa otra
organización.

Selecciona **Reactivar membresía** para devolver el acceso. La reactivación no recupera las
sesiones cerradas: la persona debe iniciar sesión de nuevo cuando corresponda.

### Forzar el cierre de sesión

Selecciona **Forzar cierre** para revocar las sesiones y dispositivos recordados de ese
miembro. Esta acción no desactiva su cuenta ni su membresía; podrá identificarse de nuevo
mientras ambas continúen activas.

## Gestionar usuarios de toda la plataforma

La sección **Administración → Usuarios** está reservada a la administración de plataforma.
Permite buscar cuentas por persona u organización, filtrar por estado y consultar todas las
membresías de cada cuenta.

### Añadir un usuario existente a otra organización

1. Busca a la persona y selecciona **Administrar**.
2. En **Añadir a otra organización**, busca la organización por nombre o identificador corto.
3. Selecciona la organización y elige **Administrador de organización**, **Operador** o
   **Lector**.
4. Pulsa **Preparar alta**, revisa el resumen y selecciona **Confirmar alta**.

Esta operación solo sirve para cuentas que ya existen. No envía una invitación ni crea una
cuenta nueva. Una persona solo puede tener una membresía en cada organización.

Desde el mismo detalle puedes cambiar el rol y activar o desactivar cualquiera de sus
membresías. El rol de administrador de plataforma aparece como **Rol protegido** y no puede
concederse, modificarse ni retirarse desde estas pantallas.

### Desactivar o reactivar una cuenta

Selecciona **Desactivar cuenta** para retirar el acceso de la persona a todas sus
organizaciones. La operación revoca sus sesiones y dispositivos recordados. La aplicación la
rechaza si dejaría alguna organización activa sin administración.

Selecciona **Reactivar cuenta** para permitir de nuevo el acceso mediante sus membresías
activas. Las sesiones cerradas no se recuperan automáticamente.

### Forzar el cierre global

Selecciona **Forzar cierre global** para revocar todas las sesiones y dispositivos recordados
de la cuenta sin cambiar su estado ni el de sus membresías.

## Reglas que protegen el acceso

- Una organización activa siempre debe conservar al menos una persona con rol
  **Administrador de organización**, cuenta activa y membresía activa.
- La aplicación rechaza el cambio de rol, la desactivación de una membresía o la desactivación
  de una cuenta que incumpla esa regla, incluso si dos cambios se intentan a la vez.
- El rol de administrador de plataforma no se concede ni se retira desde la interfaz.
- Las acciones sensibles muestran una confirmación con la persona, la organización y el efecto
  esperado. Revisa esos datos antes de confirmar.
- Los cambios de rol, estado y organización activa tienen efecto inmediato en las siguientes
  operaciones de la persona afectada.

Si una acción se rechaza, consulta [Incidencias y recuperación](incidencias.md#organizacion-activa-y-administracion).
