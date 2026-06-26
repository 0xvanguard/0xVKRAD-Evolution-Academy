<div align="center">

```
 ██████╗ ██╗  ██╗██╗   ██╗██╗  ██╗██████╗  █████╗ ██████╗
██╔═████╗╚██╗██╔╝██║   ██║██║ ██╔╝██╔══██╗██╔══██╗██╔══██╗
██║██╔██║ ╚███╔╝ ██║   ██║█████╔╝ ██████╔╝███████║██║  ██║
████╔╝██║ ██╔██╗ ╚██╗ ██╔╝██╔═██╗ ██╔══██╗██╔══██║██║  ██║
╚██████╔╝██╔╝ ██╗ ╚████╔╝ ██║  ██╗██║  ██║██║  ██║██████╔╝
 ╚═════╝ ╚═╝  ╚═╝  ╚═══╝  ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝
          E V O L U T I O N   A C A D E M Y  ·  EST. 2026
```

**La academia de ciberseguridad ofensiva que opera en las sombras del sistema tradicional.**\
Gratuita. En español. Sin filtros académicos. Orientada a resultados reales.

---

[![Estado](https://img.shields.io/badge/ESTADO-OPERATIVO-00d4ff?style=flat-square&labelColor=0d1117)](https://github.com/0xvanguard/0xVKRAD-Evolution-Academy)
[![Misiones activas](https://img.shields.io/badge/MISIONES-3_ACTIVAS-39ff7a?style=flat-square&labelColor=0d1117)](./missions/)
[![Labs Docker](https://img.shields.io/badge/LABS-DOCKER_READY-ff9500?style=flat-square&labelColor=0d1117)](./labs/)
[![Licencia](https://img.shields.io/badge/LICENCIA-MIT-ff3b3b?style=flat-square&labelColor=0d1117)](./LICENSE)
[![Idioma](https://img.shields.io/badge/IDIOMA-ESPA%C3%91OL-c9d1d9?style=flat-square&labelColor=0d1117)](.)
[![Costo](https://img.shields.io/badge/COSTO-GRATUITO-39ff7a?style=flat-square&labelColor=0d1117)](.)

</div>

---

## ¿Qué es 0xVKRAD?

> *"¿Qué es 0xVKRAD? No es educación oscura por ocultismo; es educación KRAD porque opera en las sombras del sistema tradicional, enseñando lo que las universidades no se atreven a tocar."*

**0xVKRAD Evolution Academy** no es un curso en video. No tiene certificados de asistencia. No te da teoría bonita para un examen.

Es un sistema de operaciones de campo donde aprendes ciberseguridad ofensiva **ejecutando**, **fallando** y **documentando** ataques reales en entornos controlados. Cada misión completada genera evidencia técnica que va directo a tu portafolio en GitHub.

```
Universidad tradicional    →   Teoría → Examen → Olvido
0xVKRAD Evolution Academy  →   Briefing → Ejecución → Flag → Writeup → Portafolio
```

---

## El Manifiesto

Todo operador que entre a la academia acepta estas tres reglas sin negociación:

```
REGLA_01 — LA TEORÍA ES BASURA SIN PRÁCTICA
  Si no puedes demostrarlo rompiendo un entorno controlado,
  no sabes cómo funciona. El conocimiento que no genera
  output ejecutable es decoración.

REGLA_02 — NO BUSCAMOS TÍTULOS, BUSCAMOS HABILIDADES
  El código manda. Tu repositorio de GitHub dice más que
  cualquier diploma. Construye evidencia pública de lo que aprendes.

REGLA_03 — PENSAMIENTO HACKER OBLIGATORIO
  Si una puerta está cerrada, la vulnerabilidad no está
  en la puerta. Está en el diseño del sistema que la sostiene.
```

→ [Leer Manifiesto completo](./docs/manifesto.md)

---

## Misiones Activas

<div align="center">

| Código | Operación | Área Técnica | Dificultad | XP Máx | Estado |
|:---:|---|---|:---:|:---:|:---:|
| [`0xVK-001`](./missions/0xVK-001/) | Operación Rompe-Muros | SQL Injection · Auth Bypass | `MEDIO` | 320 | 🟢 ACTIVA |
| [`0xVK-002`](./missions/0xVK-002/) | Infiltración Fantasma | Evasión AV/EDR · C2 · LOL Binaries | `DIFÍCIL` | 460 | 🟢 ACTIVA |
| [`0xVK-003`](./missions/0xVK-003/) | Control de Red — AD | Active Directory · Kerberoasting · DCSync | `EXPERTO` | 750 | 🟢 ACTIVA |
| `0xVK-004` | *Próximamente* | OSINT · Reconocimiento pasivo | — | — | 🔒 BLOQUEADA |
| `0xVK-005` | *Próximamente* | Blue Team · Threat Hunting | — | — | 🔒 BLOQUEADA |

</div>

Cada misión incluye: briefing narrativo, 3 fases operativas con checkpoints, hints con costo en XP, flags capturables, lección técnica con código real y referencia a remediación.

→ [Ver mapa completo de misiones](./missions/README.md)

---

## Sistema de Progreso

El aprendizaje en 0xVKRAD no se mide en horas. Se mide en flags capturadas y conocimiento demostrado.

```
     XP       RANGO
  ─────────────────────────────────────────
       0    🪖  Recluta
     300    ⚙️  Operador
     700    🔧  Especialista
   1.200    🎯  Intruso
   2.000    🏗️  Arquitecto de Ruptura
   3.500    👻  Ghost Lead
   6.000    💀  Root Commander
```

| Fuente de XP | Puntos |
|---|:---:|
| Misión MEDIO completada | 180 |
| Misión DIFÍCIL completada | 300 |
| Misión EXPERTO completada | 500 |
| Primera resolución del día | +20 |
| Sin usar hints (medio) | +30 |
| Sin usar hints (difícil/experto) | +60 |
| Writeup técnico aprobado | +50 |
| Evidencia publicada en GitHub | +40 |
| Flag de privilegio máximo `0xVK-003` | +80 |

→ [Sistema completo: rangos, badges, streaks y portafolio](./docs/progress-system.md)

---

## Labs Docker

Cada misión tiene un entorno vulnerable listo para levantar. Sin configuración manual. Sin VMs pesadas.

```bash
# Lab 0xVK-001 — Aplicación web con SQL Injection
cd labs/0xVK-001
docker compose up -d --build

# Verificar que el lab está operativo
curl http://localhost:8080/health
# → {"lab": "0xVK-001", "status": "ok"}
```

| Lab | Stack | Vectores de ataque |
|---|---|---|
| [`0xVK-001`](./labs/0xVK-001/) | Flask · MySQL 8 · Nginx | Login bypass · UNION SELECT · LIKE injection |
| `0xVK-002` | *En desarrollo* | — |
| `0xVK-003` | *En desarrollo* | — |

> ⚠️ Los labs contienen código **intencionalmente inseguro** para fines educativos.
> No exponer en redes de producción ni en internet público.

---

## Cómo Empezar

```bash
# 1. Clona el repositorio
git clone https://github.com/0xvanguard/0xVKRAD-Evolution-Academy.git
cd 0xVKRAD-Evolution-Academy

# 2. Lee el manifiesto
cat docs/manifesto.md

# 3. Levanta el primer laboratorio
cd labs/0xVK-001 && docker compose up -d --build

# 4. Lee el briefing de la primera misión
cat missions/0xVK-001/README.md

# 5. Opera. Captura la flag. Documenta. Repite.
```

**Requisitos mínimos:**
- Docker ≥ 24.0 + Docker Compose ≥ 2.20
- Terminal básico (bash/zsh)
- Ganas de romper cosas en entornos controlados

---

## Facultades

<div align="center">

| Facultad | Área | Estado |
|:---:|---|:---:|
| `FAC-01` | Fundamentos de Ciberseguridad | 🟡 En construcción |
| `FAC-02` | Reconocimiento y OSINT | 🟡 En construcción |
| `FAC-03` | Pentesting y Red Team | 🟢 **Activa** |
| `FAC-04` | Blue Team y Detección | 🔒 Próximamente |
| `FAC-05` | DevSecOps y Automatización | 🔒 Próximamente |
| `FAC-06` | AI Security · LLM Hacking | 🔒 Próximamente |

</div>

---

## Contribuir

0xVKRAD es open-source. Puedes contribuir con:

- 🐛 **Bug reports** — errores en contenido o labs
- 🎯 **Nuevas misiones** — propuesta completa con briefing + lab Docker
- 🔧 **Mejoras técnicas** — correcciones, mejores referencias, herramientas
- 📝 **Writeups** — comparte tu proceso con la comunidad

→ [Guía de contribución completa](./CONTRIBUTING.md)

---

## Estructura del Repositorio

```
0xVKRAD-Evolution-Academy/
│
├── missions/                    ← Operaciones de campo
│   ├── README.md                   Mapa de misiones + sistema de progreso
│   ├── 0xVK-001/                   Operación Rompe-Muros (SQLi)
│   ├── 0xVK-002/                   Infiltración Fantasma (Evasión AV)
│   └── 0xVK-003/                   Control de Red — Active Directory
│
├── labs/                        ← Entornos Docker vulnerables
│   └── 0xVK-001/
│       ├── app/                    Flask app con 3 vectores SQLi
│       ├── db/                     Seed SQL con flags ocultas
│       ├── nginx/                  Proxy con vectores de reconocimiento
│       └── docker-compose.yml
│
├── docs/                        ← Documentación de la academia
│   ├── manifesto.md                Las 3 reglas del operador
│   └── progress-system.md          Rangos, XP, badges y streaks
│
├── templates/
│   └── writeup-template.md         10 secciones: recon → remediación
│
├── .github/ISSUE_TEMPLATE/      Templates para bugs y misiones nuevas
├── CONTRIBUTING.md
├── LICENSE
└── README.md
```

---

## Aviso Legal

Este repositorio es **exclusivamente educativo**. Todo el contenido opera en entornos controlados y autorizados. El uso de estas técnicas fuera de entornos con autorización explícita escrita es **ilegal**. Los autores y contribuidores de 0xVKRAD Evolution Academy no asumen responsabilidad por el uso indebido de este contenido.

Al usar este repositorio, declaras que aplicarás este conocimiento únicamente en entornos autorizados, competencias CTF, programas de bug bounty con alcance definido, o sistemas de tu propiedad.

→ [Leer LICENSE completo](./LICENSE)

---

<div align="center">

**Creado por [0xvanguard](https://github.com/0xvanguard)**\
Cybersecurity · Red Team · DevSecOps · Open Source

[![GitHub](https://img.shields.io/badge/GitHub-0xvanguard-00d4ff?style=flat-square&logo=github&labelColor=0d1117)](https://github.com/0xvanguard)

---

*«El reto no termina al entrar.*\
*Termina cuando tienes el control absoluto.»*

</div>
