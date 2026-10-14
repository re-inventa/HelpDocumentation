# Administración de organizaciones

La administración de organizaciones es una función global reservada a quienes tienen el
rol **Administrador de plataforma**. Los demás roles no pueden abrir esta sección ni realizar
estas operaciones mediante la aplicación.

Cada cambio queda registrado para facilitar su revisión posterior. Si ese registro no puede
completarse, la aplicación no aplica la operación.

## Consultar organizaciones

Abre **Administración → Organizaciones** para ver el nombre, el identificador corto, el
estado, el número de miembros y los dominios de cada organización.

Puedes buscar por nombre, identificador corto o dominio. La lista se divide en páginas cuando
hay más resultados de los que caben en una sola vista.

## Crear una organización

1. Escribe el nombre visible de la organización.
2. Define un identificador corto, por ejemplo `empresa-demostracion`.
3. Selecciona **Crear organización**.

El identificador corto admite minúsculas, números y guiones. Debe ser único y queda fijo tras
la creación para no romper direcciones o integraciones. Después puedes cambiar el nombre
visible, pero no ese identificador.

La organización se crea activa y sin dominios. Crear una organización no crea usuarios ni
les concede acceso automáticamente.

## Cambiar el nombre

1. Selecciona la organización en la lista.
2. Modifica el nombre visible.
3. Selecciona **Guardar nombre**.

Este cambio no modifica el identificador corto, los dominios, los miembros ni el estado.

## Suspender una organización

1. Selecciona una organización activa.
2. Selecciona **Suspender organización**.
3. Escribe un motivo y confirma la suspensión.

Una organización suspendida conserva su configuración y sus datos, pero deja de permitir el
acceso. Las personas que solo pertenecen a esa organización pierden sus sesiones abiertas y
sus dispositivos dejan de estar recordados. Si una persona también pertenece a otra
organización activa, conserva el acceso a esa otra organización.

La aplicación impide una suspensión que dejaría la plataforma sin ninguna persona con
administración global activa.

## Reactivar una organización

1. Selecciona una organización suspendida.
2. Selecciona **Reactivar organización**.
3. Escribe un motivo y confirma la reactivación.

La reactivación vuelve a permitir que la organización participe en el acceso. No recupera las
sesiones que se cerraron al suspenderla: las personas afectadas deben iniciar sesión de nuevo.

## Gestionar dominios de registro

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
