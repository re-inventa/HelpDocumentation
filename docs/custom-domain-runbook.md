# Activación y reversión de `docs.re-inventa.es`

Este procedimiento se ejecuta únicamente después de aprobar y fusionar el cambio de estructura del portal. No se guardan en el repositorio los valores de verificación entregados por GitHub.

## Estado previo obligatorio

- La publicación desde `main` ha terminado correctamente en el dominio anterior.
- `gh-pages` contiene la entrada neutral, `/reauditia/`, `/reagentia/` y las redirecciones antiguas.
- Se dispone de acceso a la zona DNS de `re-inventa.es`, a la configuración de la organización `re-inventa` y a **Settings > Pages** del repositorio.
- Se ha anotado el estado anterior del DNS y de GitHub Pages para poder revertirlo.

## Activación coordinada

1. En la configuración de Pages de la organización `re-inventa`, inicia la verificación de `re-inventa.es`.
2. GitHub mostrará un valor TXT. Créalo en Raiola con el nombre `_github-pages-challenge-re-inventa.re-inventa.es` y conserva el registro después de la verificación.
3. Confirma mediante una consulta DNS pública que el TXT ya responde con el valor indicado por GitHub.
4. Comprueba que `docs.re-inventa.es` no tiene registros A, AAAA o CNAME incompatibles.
5. En **Settings > Pages** del repositorio `HelpDocumentation`, configura `docs.re-inventa.es` como dominio personalizado y guarda el cambio. Como la publicación usa la rama `gh-pages`, GitHub crea en su raíz un fichero `CNAME` con ese valor. No publiques todavía el CNAME en Raiola.
6. Confirma en `gh-pages` que el fichero `CNAME` contiene únicamente `docs.re-inventa.es`.
7. Crea en Raiola un único registro CNAME para `docs.re-inventa.es` con destino `re-inventa.github.io`. El destino no incluye `/HelpDocumentation` ni otra ruta.
8. Espera hasta que una consulta DNS pública devuelva exactamente ese CNAME.
9. Espera a que GitHub valide el DNS y emita el certificado. Activa **Enforce HTTPS** cuando la opción esté disponible.
10. Ejecuta manualmente el workflow **Validate and publish documentation**. El workflow detectará el `CNAME`, validará su valor y realizará el smoke contra `https://docs.re-inventa.es/`.
11. Verifica la raíz neutral, `/reauditia/`, `/reagentia/`, una página profunda de cada guía y una URL antigua de ReAuditIA.

## Comprobaciones de aceptación

- `https://docs.re-inventa.es/` muestra solo la entrada neutral.
- `https://docs.re-inventa.es/reauditia/` y `https://docs.re-inventa.es/reagentia/` cargan sus guías independientes.
- Una URL antigua como `https://re-inventa.github.io/HelpDocumentation/panel/inicio.html` termina en `/reauditia/panel/inicio.html` bajo el dominio personalizado.
- El certificado es válido, HTTPS está forzado y no existe contenido mixto.
- `gh-pages/CNAME` contiene únicamente `docs.re-inventa.es`.
- Los marcadores `/reauditia/publication-sha.txt` y `/reagentia/publication-sha.txt` coinciden con la revisión publicada de `main`.

## Reversión

1. Retira el dominio personalizado desde **Settings > Pages** del repositorio.
2. Comprueba que `CNAME` ha desaparecido de `gh-pages`; si GitHub no lo retira automáticamente, elimínalo de esa rama.
3. Elimina en Raiola el CNAME de `docs.re-inventa.es`. El TXT de verificación del dominio puede conservarse: no dirige tráfico y evita tener que repetir la verificación.
4. Ejecuta manualmente el workflow. Al no existir `gh-pages/CNAME`, el smoke utilizará `https://re-inventa.github.io/HelpDocumentation/`.
5. Verifica que la entrada neutral, `/reauditia/`, `/reagentia/` y las redirecciones antiguas vuelven a responder en el dominio de GitHub Pages.

La reversión no modifica el contenido funcional ni mezcla ambas guías; únicamente devuelve el acceso al dominio anterior.
