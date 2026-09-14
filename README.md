# Documentación pública de Re-Inventa

Este repositorio mantiene dos zonas funcionales públicas e independientes:

- ReAuditIA: <https://re-inventa.github.io/HelpDocumentation/>
- Reagentia: <https://re-inventa.github.io/HelpDocumentation/reagentia/>

Ambas se escriben en Markdown y se construyen con Material for MkDocs. La documentación técnica permanece en los repositorios de código y no se publica aquí.

## Estructura

| Zona | Fuentes | Configuración | Salida local |
| --- | --- | --- | --- |
| ReAuditIA | `reauditia/docs/` | `reauditia/mkdocs.yml` | `build/reauditia/` |
| Reagentia | `reagentia/docs/` | `reagentia/mkdocs.yml` | `build/reagentia/` |

## Preparar el entorno

```powershell
python -m venv .venv-docs
.\.venv-docs\Scripts\Activate.ps1
python -m pip install -r reauditia/requirements-docs.txt
```

Las dependencias de ambas zonas deben mantenerse alineadas. Si trabajas solo en Reagentia, también puedes instalarlas desde `reagentia/requirements-docs.txt`.

## Validar y construir

ReAuditIA:

```powershell
python scripts/build_reauditia.py
```

Reagentia:

```powershell
python scripts/build_reagentia.py
```

Para comprobar además enlaces externos, añade `--external-links`.

Para ejecutar también la comprobación real en navegador de escritorio y móvil, instala `reauditia/requirements-responsive.txt` y añade `--responsive`.

## Previsualizar

ReAuditIA:

```powershell
python -m mkdocs serve --config-file reauditia/mkdocs.yml --dev-addr 127.0.0.1:8000
```

Reagentia:

```powershell
python -m mkdocs serve --config-file reagentia/mkdocs.yml --dev-addr 127.0.0.1:8001
```

La previsualización es local y no publica contenido.

## Publicación

- Una PR construye y valida únicamente las zonas afectadas. No despliega ni genera ZIP o artifacts.
- Una PR funcional asociada a una PR de producto debe declarar en su cuerpo `Source-PR: https://github.com/re-inventa/<repositorio>/pull/<numero>`. La línea se repite si documenta varias PR de producto.
- Una PR exclusiva del portal, sin PR de producto asociada, debe declarar `Source-PR: none`.
- Un `push` a `main` publica únicamente las zonas afectadas en `gh-pages`.
- Un `repository_dispatch` válido vuelve a publicar la zona funcional ya fusionada que corresponda.
- La publicación de ReAuditIA conserva `/reagentia/`; la de Reagentia conserva la raíz y cualquier `CNAME`.
- La issue del portal se referencia con `Refs` y solo se cierra después de que el smoke público confirme la publicación.

## Reglas de contenido público

- Explicar qué hace una capacidad, para qué sirve y cómo se utiliza.
- Usar ejemplos sintéticos.
- No publicar documentación técnica, secretos, endpoints privados, datos reales ni información específica de clientes o proyectos.
- Mantener las rutas públicas existentes cuando se reorganice el contenido.

## Compatibilidad con la publicación anterior

Las rutas, anclas y recursos públicos que deben seguir funcionando se controlan en `reauditia/scripts/validate_routes.py`. Se retiran de forma intencionada los recursos internos generados por Sphinx, como `_sources/`, `.doctrees/`, `.buildinfo`, `objects.inv`, `searchindex.js` y sus ficheros de tema; no forman parte del contrato público.

Si hay que bloquear un nuevo nombre interno o de cliente, genera su huella con:

```powershell
python reauditia/scripts/validate_content.py --hash-name "<nuevo-término>"
```

Añade únicamente la huella al mapa correspondiente. No guardes el término literal ni lo reconstruyas por fragmentos en el repositorio. La huella sirve para comparar nombres normalizados; no cifra ni protege un dato confidencial.
