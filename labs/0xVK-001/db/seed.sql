-- ============================================================
--  0xVKRAD Lab — 0xVK-001: Corp Logistics SA
--  Base de datos interna simulada
--  USO EXCLUSIVO EDUCATIVO
-- ============================================================

CREATE DATABASE IF NOT EXISTS corp_db;
USE corp_db;

-- ── Tabla de usuarios (objetivo principal) ──────────────────
CREATE TABLE IF NOT EXISTS users (
  id         INT AUTO_INCREMENT PRIMARY KEY,
  username   VARCHAR(50)  NOT NULL UNIQUE,
  password   VARCHAR(100) NOT NULL,
  email      VARCHAR(100),
  department VARCHAR(50),
  role       VARCHAR(20)  DEFAULT 'user',
  created_at TIMESTAMP    DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO users (username, password, email, department, role) VALUES
  ('admin',    '5f4dcc3b5aa765d61d8327deb882cf99', 'admin@corp-logistics.co',    'IT',         'admin'),
  ('jperez',   '827ccb0eea8a706c4c34a16891f84e7b', 'jperez@corp-logistics.co',   'Operaciones', 'user'),
  ('mgomez',   'e10adc3949ba59abbe56e057f20f883e', 'mgomez@corp-logistics.co',   'RRHH',        'user'),
  ('ltorres',  '25d55ad283aa400af464c76d713c07ad', 'ltorres@corp-logistics.co',  'Finanzas',    'user'),
  ('sysadmin', '098f6bcd4621d373cade4e832627b4f6', 'sysadmin@corp-logistics.co', 'IT',          'admin');

-- ── Tabla de productos (vector secundario) ──────────────────
CREATE TABLE IF NOT EXISTS products (
  id       INT AUTO_INCREMENT PRIMARY KEY,
  name     VARCHAR(100),
  category VARCHAR(50),
  price    DECIMAL(10,2),
  stock    INT
);

INSERT INTO products (name, category, price, stock) VALUES
  ('Paleta industrial 1200kg',   'Equipos',       850000.00, 12),
  ('Cinta transportadora 5m',    'Equipos',      1250000.00,  5),
  ('Casco seguridad clase A',    'EPP',             45000.00, 200),
  ('Guantes anticorte nivel 5',  'EPP',             32000.00, 350),
  ('Montacargas eléctrico',      'Vehículos',   18500000.00,  2),
  ('Estante metálico 4 niveles', 'Almacenamiento', 320000.00, 40);

-- ── Tabla de flags (objetivo oculto — no visible en UI) ─────
CREATE TABLE IF NOT EXISTS flags (
  id          INT AUTO_INCREMENT PRIMARY KEY,
  mission     VARCHAR(20),
  secret      VARCHAR(200),
  description VARCHAR(100)
);

INSERT INTO flags (mission, secret, description) VALUES
  ('0xVK-001', '0xVKRAD{sql_1nj3ct10n_c0rp_db_pwn3d_2024}', 'Flag principal — extraída via UNION SELECT'),
  ('0xVK-001', '0xVKRAD{b0nus_auth_byp4ss_adm1n_1s_y0urs}',  'Flag bonus — autenticación bypasseada como admin');

-- ── Audit log (contexto adicional) ──────────────────────────
CREATE TABLE IF NOT EXISTS audit_log (
  id         INT AUTO_INCREMENT PRIMARY KEY,
  user_id    INT,
  action     VARCHAR(100),
  ip_address VARCHAR(45),
  timestamp  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO audit_log (user_id, action, ip_address) VALUES
  (1, 'LOGIN_SUCCESS',      '192.168.1.10'),
  (1, 'EXPORT_USERS',       '192.168.1.10'),
  (2, 'LOGIN_SUCCESS',      '192.168.1.25'),
  (5, 'CONFIG_CHANGE',      '192.168.1.1'),
  (5, 'PRIVILEGE_ESCALATE', '192.168.1.1');
