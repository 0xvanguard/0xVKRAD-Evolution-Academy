# 🧪 Lab 0xVK-001 — Entorno Vulnerable

> Entorno Docker simulado para la Operación Rompe-Muros.
> **Uso exclusivo educativo. No exponer en internet ni en redes de producción.**

---

## Arquitectura del lab

```
┌─────────────────────────────────────────────────────┐
│  Operador (tú)                                      │
└──────────────────┬──────────────────────────────────┘
                   │
           http://localhost:8080
                   │
           ┌───────┴───────┐
           │  Nginx Proxy  │  :80 interno / :8080 host
           └───────┬───────┘
                   │
           ┌───────┴───────┐
           │   Flask App   │  :5000
           └───────┬───────┘
                   │
           ┌───────┴───────┐
           │  MySQL 8.0    │  :3306
           └───────────────┘
```

| Servicio | Puerto host | URL |
|---|---|---|
| Proxy Nginx | 8080 | http://localhost:8080 |
| Flask App (directo) | 5000 | http://localhost:5000 |
| MySQL | 3306 | localhost:3306 |

---

## Requisitos

- Docker >= 24.0
- Docker Compose >= 2.20
- Puertos 5000, 8080 y 3306 disponibles
- 512 MB RAM libres mínimo

---

## Levantar el laboratorio

```bash
# 1. Clonar el repositorio
git clone https://github.com/0xvanguard/0xVKRAD-Evolution-Academy.git
cd 0xVKRAD-Evolution-Academy/labs/0xVK-001

# 2. Construir e iniciar todos los servicios
docker compose up -d --build

# 3. Esperar ~20s para que MySQL inicialice, luego verificar
docker compose ps
curl http://localhost:8080/health
# Respuesta esperada: {"lab": "0xVK-001", "status": "ok"}

# 4. Ver logs en tiempo real
docker compose logs -f app
```

---

## Credenciales del entorno

| Servicio | Usuario | Contraseña |
|---|---|---|
| MySQL root | root | r00tpassword |
| MySQL app  | webapp | webapp2024 |
| App login  | (descúbrelo vía SQLi) | *** |

---

## Vectores de ataque disponibles

El lab tiene **3 puntos de inyección** intencionalmente vulnerables:

| Endpoint | Método | Parámetro | Tipo |
|---|---|---|---|
| `/login` | POST | `username`, `password` | String-based, auth bypass |
| `/products` | GET | `id` | Integer-based, UNION SELECT |
| `/search` | GET | `q` | String LIKE, UNION SELECT |

Además, el servidor expone información en headers HTTP útil para la fase de reconocimiento.

---

## Tablas en la base de datos

```
corp_db
├── users      ← Objetivo principal
├── products   ← Vector de ataque secundario
├── flags      ← Objetivo oculto (encuéntralo vía SQLi)
└── audit_log  ← Contexto adicional
```

---

## Detener y limpiar

```bash
# Detener (mantiene datos)
docker compose down

# Reset completo (elimina volúmenes)
docker compose down -v

# Limpiar imagen
docker rmi 0xvk001-app
```

---

> ⚠️ Este laboratorio contiene código **intencionalmente inseguro**.
> Las vulnerabilidades están marcadas con `⚠️` en el código fuente.
> Nunca uses estos patrones en aplicaciones reales.

*Lab v1.0 — 0xVKRAD Evolution Academy*
