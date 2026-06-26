# ⚡ Sistema de Progreso — 0xVKRAD Evolution Academy

> El progreso en 0xVKRAD no se mide en horas de video consumidas.
> Se mide en flags capturadas, sistemas comprometidos y conocimiento demostrado.

---

## Tabla de rangos

```
╔══════════════════════════════════════════════════════╗
║           TABLA DE RANGOS 0xVKRAD                    ║
╠═══════════╦══════════════════════════╦═══════════════╣
║    XP     ║         RANGO            ║   INSIGNIA    ║
╠═══════════╬══════════════════════════╬═══════════════╣
║     0     ║ Recluta                  ║      🪖       ║
║   300     ║ Operador                 ║      ⚙️       ║
║   700     ║ Especialista             ║      🔧       ║
║  1.200    ║ Intruso                  ║      🎯       ║
║  2.000    ║ Arquitecto de Ruptura    ║      🏗️       ║
║  3.500    ║ Ghost Lead               ║      👻       ║
║  6.000    ║ Root Commander           ║      💀       ║
╚═══════════╩══════════════════════════╩═══════════════╝
```

---

## XP por misión

| Dificultad | XP Base | XP Máximo posible |
|---|---|---|
| Fácil | 100 | 240 |
| Medio | 180 | 320 |
| Difícil | 300 | 460 |
| Experto | 500 | 750 |

---

## Bonificaciones

| Bonificación | XP | Condición |
|---|---|---|
| Primera resolución del día | +20 | Primero en resolver esa jornada |
| Sin hints (fácil/medio) | +30 | Completar sin usar ningún hint |
| Sin hints (difícil/experto) | +60 | Completar sin usar ningún hint |
| Writeup aprobado | +50 | Writeup revisado y aceptado |
| Evidencia en GitHub | +40 | Repo o gist público vinculado |
| Flag de privilegio máximo | +80 | Solo disponible en 0xVK-003 (krbtgt) |
| Remediación técnica completa | +40 | Propuesta de fix detallada en writeup |

---

## Estados de misión

```
🔒 LOCKED          → Prerrequisitos no cumplidos
🟡 READY           → Disponible para comenzar
🔵 IN PROGRESS     → Laboratorio activo
🟠 AWAITING        → Flag enviada, en validación
🟢 COMPLETED       → Flag validada y XP otorgado
⭐ MASTERED        → Completada + writeup aprobado + evidencia GitHub
```

---

## Costo de hints

Cada hint consumido descuenta XP del total de esa misión:

| Dificultad | Costo por hint |
|---|---|
| Fácil / Medio | -15 XP |
| Difícil / Experto | -20 XP |

> Usar 3 hints en una misión Difícil descuenta -60 XP del total.
> El XP base nunca baja de 0 por uso de hints.

---

## Badges disponibles

| Badge | Nombre | Condición |
|---|---|---|
| 🔥 | Primer Sangre | Primera flag capturada en la academia |
| 🧠 | Puro Cerebro | Completar una misión sin hints |
| 📝 | Cronista | Publicar 3 writeups aprobados |
| ⚡ | Velocista | Completar una misión en menos de 1 hora |
| 🌐 | Web Breaker | Completar todas las misiones de Web |
| 👻 | Fantasma | Completar 0xVK-002 sin disparar alertas |
| 👑 | Domain Lord | Completar 0xVK-003 extrayendo el hash krbtgt |
| 🗂️ | Archivista | Publicar evidencia en GitHub en 5 misiones |
| 💀 | Root Commander | Alcanzar el rango máximo |

---

## Streak (racha activa)

El sistema rastrea tu actividad continua:

- **Racha activa**: al menos 1 checkpoint completado por día
- **3 días seguidos**: +10 XP de bonus
- **7 días seguidos**: +25 XP de bonus + badge especial
- **30 días seguidos**: badge legendaria `⚡ Persistencia Absoluta`

Romper la racha reinicia el contador pero no quita el XP acumulado.

---

## Portafolio del operador

Cada misión completada puede generar artefactos exportables:

| Tipo | Descripción |
|---|---|
| Writeup técnico | Documento con el proceso completo |
| Informe de hallazgos | Formato profesional de pentest report |
| Repo de evidencia | GitHub con código, scripts y capturas |
| Badge compartible | Imagen con tu rango y misión completada |
| Certificado interno | PDF de ruta completada |

> El objetivo es que al terminar una ruta completa, tu GitHub tenga
> evidencia técnica real que ningún título universitario puede reemplazar.

---

*Sistema de progreso — 0xVKRAD Evolution Academy v1.0*
