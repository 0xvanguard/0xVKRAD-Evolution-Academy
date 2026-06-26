# 📝 Plantilla de Writeup — 0xVKRAD Evolution Academy

> Completa cada sección con tus propias palabras. Un writeup copiado = 0 XP.
> El objetivo no es reproducir la solución — es demostrar que entiendes por qué funciona.

---

## Encabezado

```
OPERACIÓN   : [Nombre de la misión — ej. Operación Rompe-Muros]
CÓDIGO      : [ej. 0xVK-001]
OPERADOR    : [tu username en la academia]
FECHA       : [YYYY-MM-DD]
DIFICULTAD  : [MEDIO / DIFÍCIL / EXPERTO]
TIEMPO TOTAL: [ej. 2h 30min]
HINTS USADOS: [0 / 1 / 2 / 3]
FLAG        : 0xVKRAD{REDACTED}
```

---

## 1. Resumen ejecutivo

> En 3-5 líneas: ¿qué encontraste, cómo lo explotaste y cuál fue el impacto?

*Ejemplo: El servidor exponía un formulario de login con inyección SQL en el parámetro `username`. Mediante UNION SELECT logré extraer la base de datos `corp_db`, obteniendo 247 registros de usuarios incluyendo hashes MD5. La flag estaba embebida en la tabla `flags` como valor de la columna `secret`.*

---

## 2. Reconocimiento

### 2.1 Escaneo de puertos

```bash
# Comando usado
$ nmap ...

# Output relevante
PORT     STATE SERVICE VERSION
...
```

### 2.2 Tecnologías identificadas

| Componente | Tecnología | Versión |
|---|---|---|
| Servidor web | | |
| Lenguaje backend | | |
| Base de datos | | |
| Sistema operativo | | |

### 2.3 Superficie de ataque identificada

- ¿Qué rutas/endpoints encontraste?
- ¿Qué formularios o parámetros analizaste?
- ¿Qué llamó tu atención como posible vector?

---

## 3. Explotación

### 3.1 Vulnerabilidad encontrada

**Tipo:** [ej. SQL Injection / XSS / RCE / LFI]
**CVE relacionado (si aplica):** [ej. CVE-2021-XXXX o N/A]
**OWASP Category:** [ej. A03:2021 – Injection]

### 3.2 Prueba de concepto (PoC)

```bash
# Payload / comando exacto que funcionó
# Explica cada parte del payload
```

**¿Por qué funciona?**

> Explica la lógica técnica detrás del exploit. ¿Qué fallo del sistema estás abusando?

### 3.3 Proceso paso a paso

1. [Primer intento / prueba]
2. [Resultado y ajuste]
3. [Payload final]
4. ...

### 3.4 Evidencia

> Screenshots, output de terminal o logs relevantes.

```
[Pega aquí el output del terminal o describe la evidencia]
```

---

## 4. Escalada / Post-explotación

> (Si aplica según la misión)

### 4.1 ¿Qué acceso obtuviste inicialmente?

### 4.2 ¿Cómo escalaste privilegios o ampliaste el acceso?

```bash
# Comandos usados
```

### 4.3 Datos / acceso final obtenido

---

## 5. Flag capturada

```
0xVKRAD{REDACTED}
```

> No incluyas la flag completa en writeups públicos.
> Para la entrega privada en el panel, sí debes incluirla completa.

---

## 6. Remediación

> Esta sección vale tanto como la explotación. Demuestra que entiendes el problema de raíz.

### 6.1 Causa raíz de la vulnerabilidad

> ¿Por qué existía este fallo? ¿Qué decisión de diseño o implementación lo causó?

### 6.2 Cómo lo corregiría un desarrollador

```python
# Código vulnerable
...

# Código corregido
...
```

### 6.3 Controles adicionales recomendados

- [ ] Control 1
- [ ] Control 2
- [ ] Control 3

### 6.4 Referencias técnicas

- [OWASP - Nombre del tipo de ataque](https://owasp.org/)
- [PortSwigger - Guía relacionada](https://portswigger.net/)
- [Recurso adicional]()

---

## 7. Herramientas utilizadas

| Herramienta | Versión | Propósito en esta operación |
|---|---|---|
| nmap | | |
| | | |
| | | |

---

## 8. Lecciones aprendidas

> ¿Qué aprendiste que no sabías antes de esta misión?
> ¿Qué harías diferente en la próxima operación?

1.
2.
3.

---

## 9. Tiempo por fase

| Fase | Tiempo invertido | Dificultad personal |
|---|---|---|
| Reconocimiento | | |
| Explotación | | |
| Post-explotación | | |
| Writeup | | |

---

## 10. Evidencia en GitHub

> Enlace a tu repositorio o gist con el código, scripts o evidencia técnica de esta operación.

```
https://github.com/<tu-usuario>/<tu-repo>
```

---

*Writeup generado bajo el marco educativo de 0xVKRAD Evolution Academy.
Entorno controlado y simulado. Uso exclusivo ético.*
