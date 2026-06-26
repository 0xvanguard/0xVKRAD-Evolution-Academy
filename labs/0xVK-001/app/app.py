# ============================================================
#  0xVKRAD Lab — 0xVK-001: Operación Rompe-Muros
#  Aplicación Flask INTENCIONALMENTE VULNERABLE
#  Diseñada para práctica de SQL Injection educativa
#  NO USAR EN PRODUCCIÓN
# ============================================================

import os
import mysql.connector
from flask import (
    Flask, request, render_template_string,
    jsonify, redirect, url_for, session
)

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'insecure_key')


def get_db():
    return mysql.connector.connect(
        host=os.environ.get('DB_HOST', 'db'),
        port=int(os.environ.get('DB_PORT', 3306)),
        database=os.environ.get('DB_NAME', 'corp_db'),
        user=os.environ.get('DB_USER', 'webapp'),
        password=os.environ.get('DB_PASS', 'webapp2024')
    )


# ── Estilos base (terminal 0xVKRAD) ─────────────────────────
BASE_STYLE = """
<style>
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  font-family: 'Courier New', monospace;
  background: #0a0e14; color: #c9d1d9;
  min-height: 100vh; display: flex;
  flex-direction: column; align-items: center;
  justify-content: center; padding: 2rem;
}
.card {
  background: #0d1117; border: 1px solid #1e2d3d;
  border-radius: 8px; padding: 2rem;
  width: 100%; max-width: 520px;
  box-shadow: 0 8px 32px rgba(0,0,0,.6);
}
.logo {
  font-size: .72rem; color: #00d4ff;
  letter-spacing: .15em; text-align: center;
  margin-bottom: 1.5rem;
}
h1 {
  font-size: 1.1rem; color: #e2e8f0;
  text-align: center; margin-bottom: 1.5rem;
  letter-spacing: .05em;
}
label {
  font-size: .78rem; color: #7f9aaf;
  letter-spacing: .08em; display: block;
  margin-bottom: .35rem;
}
input {
  width: 100%; padding: .6rem .8rem;
  background: #131b24; border: 1px solid #1e2d3d;
  border-radius: 4px; color: #e2e8f0;
  font-family: inherit; font-size: .9rem;
  margin-bottom: 1rem;
}
input:focus { outline: none; border-color: #00d4ff; }
button {
  width: 100%; padding: .75rem;
  background: #00d4ff; color: #0a0e14;
  border: none; border-radius: 4px;
  font-family: inherit; font-weight: 700;
  letter-spacing: .08em; cursor: pointer;
  font-size: .9rem;
}
button:hover { background: #00b8e0; }
.error {
  color: #ff3b3b; font-size: .8rem;
  margin-top: .5rem; padding: .5rem;
  background: rgba(255,59,59,.08);
  border: 1px solid rgba(255,59,59,.2);
  border-radius: 4px;
}
.success {
  color: #39ff7a; font-size: .85rem;
  margin-top: .5rem; padding: .5rem;
  background: rgba(57,255,122,.08);
  border: 1px solid rgba(57,255,122,.2);
  border-radius: 4px;
}
.hint {
  color: #7f9aaf; font-size: .72rem;
  text-align: center; margin-top: 1rem;
}
table { width: 100%; border-collapse: collapse; margin-top: 1rem; }
th {
  color: #00d4ff; font-size: .72rem;
  letter-spacing: .1em; text-align: left;
  padding: .5rem; border-bottom: 1px solid #1e2d3d;
}
td {
  font-size: .78rem; padding: .5rem;
  border-bottom: 1px solid #131b24; color: #c9d1d9;
}
.badge {
  display: inline-block; padding: .18rem .5rem;
  background: rgba(0,212,255,.1);
  border: 1px solid rgba(0,212,255,.2);
  border-radius: 4px; font-size: .68rem; color: #00d4ff;
}
nav { margin-bottom: 1.5rem; }
nav a {
  color: #7f9aaf; font-size: .75rem;
  text-decoration: none; margin-right: 1rem;
  letter-spacing: .05em;
}
nav a:hover { color: #00d4ff; }
pre {
  background: #131b24; padding: 1rem;
  border-radius: 4px; font-size: .72rem;
  color: #39ff7a; overflow-x: auto;
  border: 1px solid #1e2d3d; margin-top: .5rem;
}
</style>
"""

LOGIN_TPL = BASE_STYLE + """
<div class="card">
  <div class="logo">0xVKRAD EVOLUTION ACADEMY // LAB 0xVK-001</div>
  <h1>CORP LOGISTICS — PANEL DE ACCESO</h1>
  <nav>
    <a href="/">Login</a>
    <a href="/products">Productos</a>
    <a href="/search">Búsqueda</a>
  </nav>
  <form method="POST" action="/login">
    <label>USUARIO</label>
    <input type="text" name="username" placeholder="admin" autocomplete="off">
    <label>CONTRASEÑA</label>
    <input type="password" name="password" placeholder="••••••••">
    <button type="submit">ACCEDER</button>
  </form>
  {% if error %}
    <div class="error">{{ error }}</div>
  {% endif %}
  <p class="hint">// Sistema interno Corp Logistics SA — Acceso restringido</p>
</div>
"""

DASHBOARD_TPL = BASE_STYLE + """
<div class="card">
  <div class="logo">0xVKRAD EVOLUTION ACADEMY // LAB 0xVK-001</div>
  <h1>PANEL ADMINISTRATIVO</h1>
  <nav>
    <a href="/dashboard">Dashboard</a>
    <a href="/products">Productos</a>
    <a href="/search">Búsqueda</a>
    <a href="/logout">Salir</a>
  </nav>
  <div class="success">✓ Sesión iniciada como: <strong>{{ username }}</strong></div>
  <p style="margin-top:1rem;color:#7f9aaf;font-size:.8rem;">
    Bienvenido al panel interno. Gestión de inventario y usuarios.
  </p>
</div>
"""

PRODUCTS_TPL = BASE_STYLE + """
<div class="card" style="max-width:680px">
  <div class="logo">0xVKRAD EVOLUTION ACADEMY // LAB 0xVK-001</div>
  <h1>INVENTARIO DE PRODUCTOS</h1>
  <nav>
    <a href="/dashboard">Dashboard</a>
    <a href="/products">Productos</a>
    <a href="/search">Búsqueda</a>
    <a href="/logout">Salir</a>
  </nav>
  <p style="font-size:.72rem;color:#7f9aaf;margin-bottom:.5rem;">
    Producto ID: <code style="color:#00d4ff">{{ product_id }}</code>
  </p>
  {% if rows %}
  <table>
    <tr><th>ID</th><th>NOMBRE</th><th>CATEGORÍA</th><th>PRECIO</th></tr>
    {% for row in rows %}
    <tr>
      <td>{{ row[0] }}</td><td>{{ row[1] }}</td>
      <td>{{ row[2] }}</td><td>{{ row[3] }}</td>
    </tr>
    {% endfor %}
  </table>
  {% else %}
  <div class="error">Sin resultados.</div>
  {% endif %}
  <p class="hint">// Endpoint: /products?id=1</p>
</div>
"""

SEARCH_TPL = BASE_STYLE + """
<div class="card" style="max-width:680px">
  <div class="logo">0xVKRAD EVOLUTION ACADEMY // LAB 0xVK-001</div>
  <h1>BÚSQUEDA DE USUARIOS</h1>
  <nav>
    <a href="/dashboard">Dashboard</a>
    <a href="/products">Productos</a>
    <a href="/search">Búsqueda</a>
    <a href="/logout">Salir</a>
  </nav>
  <form method="GET">
    <label>BUSCAR USUARIO</label>
    <input type="text" name="q" value="{{ query }}" placeholder="nombre...">
    <button type="submit">BUSCAR</button>
  </form>
  {% if rows %}
  <table>
    <tr><th>ID</th><th>USERNAME</th><th>EMAIL</th><th>DEPTO</th></tr>
    {% for row in rows %}
    <tr>
      <td>{{ row[0] }}</td><td>{{ row[1] }}</td>
      <td>{{ row[2] }}</td>
      <td><span class="badge">{{ row[3] }}</span></td>
    </tr>
    {% endfor %}
  </table>
  {% elif query %}
  <div class="error">Sin resultados para: {{ query }}</div>
  {% endif %}
  <p class="hint">// Endpoint: /search?q=admin</p>
</div>
"""


# ── Rutas ───────────────────────────────────────────────────

@app.route('/')
def index():
    return render_template_string(LOGIN_TPL, error=None)


@app.route('/health')
def health():
    return jsonify({'status': 'ok', 'lab': '0xVK-001'})


# VULNERABILIDAD 1 — Login bypass (string concatenation)
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    try:
        conn = get_db()
        cursor = conn.cursor()
        # ⚠️  INTENCIONALMENTE VULNERABLE — concatenación directa sin sanitizar
        query = (
            f"SELECT id, username, role FROM users "
            f"WHERE username = '{username}' AND password = '{password}'"
        )
        cursor.execute(query)
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        if row:
            session['user_id']  = row[0]
            session['username'] = row[1]
            session['role']     = row[2]
            return redirect(url_for('dashboard'))
        return render_template_string(LOGIN_TPL, error='Credenciales incorrectas.')
    except Exception as e:
        # Error visible intencionalmente — ayuda al operador a entender la DB
        return render_template_string(LOGIN_TPL, error=f'DB Error: {e}')


@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('index'))
    return render_template_string(DASHBOARD_TPL, username=session['username'])


# VULNERABILIDAD 2 — GET param SQLi integer-based (UNION SELECT posible)
@app.route('/products')
def products():
    product_id = request.args.get('id', '1')
    try:
        conn = get_db()
        cursor = conn.cursor()
        # ⚠️  INTENCIONALMENTE VULNERABLE
        query = f"SELECT id, name, category, price FROM products WHERE id = {product_id}"
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template_string(PRODUCTS_TPL, rows=rows, product_id=product_id)
    except Exception as e:
        return render_template_string(PRODUCTS_TPL, rows=[], product_id=product_id)


# VULNERABILIDAD 3 — Search SQLi string-based LIKE
@app.route('/search')
def search():
    q = request.args.get('q', '')
    rows = []
    if q:
        try:
            conn = get_db()
            cursor = conn.cursor()
            # ⚠️  INTENCIONALMENTE VULNERABLE
            query = (
                f"SELECT id, username, email, department FROM users "
                f"WHERE username LIKE '%{q}%'"
            )
            cursor.execute(query)
            rows = cursor.fetchall()
            cursor.close()
            conn.close()
        except Exception as e:
            return render_template_string(SEARCH_TPL, rows=[], query=q)
    return render_template_string(SEARCH_TPL, rows=rows, query=q)


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
