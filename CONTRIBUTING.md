# 🤝 Contribuir a 0xVKRAD Evolution Academy

Gracias por querer aportar al proyecto. 0xVKRAD es una academia open-source y cada contribución la hace mejor para toda la comunidad hispanohablante de ciberseguridad.

---

## ¿Qué puedes contribuir?

| Tipo | Descripción |
|---|---|
| 🐛 Bug report | Error en contenido, comando incorrecto, enlace roto |
| 📝 Mejora de contenido | Corrección técnica, mejor explicación, nueva referencia |
| 🎯 Nueva misión | Propuesta de operación con briefing, objetivos y flag |
| 🔧 Lab / entorno | Docker Compose para nuevo entorno vulnerable |
| 🌐 Traducción | Adaptación de recursos externos al español |
| 📚 Recurso | Herramienta, paper, writeup o guía relevante |

---

## Proceso para contribuir

### 1. Reportar un error o sugerir mejora

Abre un Issue con:
- Título descriptivo
- Misión o archivo afectado
- Descripción del problema o propuesta
- Evidencia (screenshot, output de terminal)

### 2. Contribuir contenido o código

```bash
# Forkea el repositorio
git clone https://github.com/<tu-usuario>/0xVKRAD-Evolution-Academy
cd 0xVKRAD-Evolution-Academy

# Crea una rama descriptiva
git checkout -b feat/nueva-mision-0xVK-004
# o
git checkout -b fix/correccion-payload-0xVK-001

# Haz tus cambios y commitea
git add .
git commit -m "feat(missions): add 0xVK-004 OSINT operation"

# Push y Pull Request
git push origin feat/nueva-mision-0xVK-004
```

### 3. Convención de commits

Usamos [Conventional Commits](https://www.conventionalcommits.org/):

```
feat(missions):   nueva misión o laboratorio
fix(content):     corrección técnica
docs(guides):     mejora de documentación
chore(infra):     cambios de infraestructura
refactor(labs):   reorganización sin cambio funcional
```

---

## Estándar para nuevas misiones

Si quieres proponer una operación nueva, debe incluir:

- [ ] Código único (`0xVK-XXX`)
- [ ] Briefing narrativo
- [ ] Mínimo 2 objetivos de aprendizaje verificables
- [ ] 3 fases estructuradas (Reconocimiento / Explotación / Escalada)
- [ ] Al menos 3 checkpoints técnicos
- [ ] Sistema de hints escalonados (mínimo 2)
- [ ] Flag en formato `0xVKRAD{...}`
- [ ] Tabla de XP y bonificaciones
- [ ] Lección técnica con código de ejemplo
- [ ] Referencia a remediación

---

## Código de conducta

- El conocimiento compartido aquí es para fines educativos y éticos
- No se aceptan contribuciones que promuevan actividad ilegal
- Respeto entre operadores, sin importar el nivel
- El español es el idioma principal del proyecto
- Los errores se señalan con respeto y se proponen soluciones

---

## Reconocimiento

Todos los contribuidores serán listados en el archivo `CONTRIBUTORS.md`.
Las contribuciones de misiones completas serán acreditadas directamente en la misión.

---

*0xVKRAD Evolution Academy — Open source, en español, para la comunidad.*
