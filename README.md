# 🚀 Integración Nómina API

API desarrollada en **FastAPI** con autenticación **OAuth2 Client Credentials**, seguridad con **JWT (RS256)**, control de **scopes**, y base de datos **Oracle**.

---

## 📌 Características

* 🔐 OAuth2 Client Credentials Flow
* 🧾 JWT firmado con RSA (RS256)
* 🔑 Control de scopes por proveedor
* 🗄️ Oracle Database (SQLAlchemy)
* 🧱 Arquitectura limpia (Domain / Application / Infrastructure / Interfaces)
* ⚙️ Middleware de autenticación JWT
* 🚫 Validación de permisos por endpoint

---

## 🧰 Requisitos

* Python 3.10+
* Oracle Client / acceso a BD Oracle
* Git
* Virtualenv o venv

---

## 📁 Estructura del proyecto

```text
src/
│
├── domain/
├── application/
├── infrastructure/
│   ├── database/
│   ├── models/
│   ├── persistence/
│   └── security/
├── interfaces/
│   ├── api/
│   └── middlewares/
├── shared/
└── main.py
```

---

## ⚙️ Instalación

### 1. Clonar proyecto

```bash
git clone <repo-url>
cd IntegracionNomina
```

---

### 2. Crear entorno virtual

```bash
python -m venv .venv
```

Activar:

**Windows:**

```bash
.venv\Scripts\activate
```

**Linux/Mac:**

```bash
source .venv/bin/activate
```

---

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 🔐 Variables de entorno

Crear archivo `.env`:

```env
APP_NAME=NominaIntegration
APP_VERSION=1.0.0

DB_USER=DATA_USR
DB_PASSWORD=*****
DB_HOST=*****
DB_PORT=1521
DB_SERVICE=ORCLPDB1

JWT_ALGORITHM=RS256
JWT_EXPIRE_MINUTES=60

PRIVATE_KEY_PATH=keys/private.pem
PUBLIC_KEY_PATH=keys/public.pem
```

---

## 🔑 Llaves RSA

Colocar las llaves en:

```text
keys/
├── private.pem
└── public.pem
```

⚠️ No subir estas llaves al repositorio.

---

## ▶️ Ejecutar proyecto

```bash
uvicorn src.main:app --reload
```

Por defecto:

```text
http://127.0.0.1:8000
```
python run.py

---

## 🔐 Autenticación OAuth2

### 📌 Obtener Token

```http
POST /oauth/token
```

Body:

```json
{
  "client_id": "NOMINA_APP",
  "client_secret": "123456"
}
```

Respuesta:

```json
{
  "access_token": "eyJhbGciOiJSUzI1NiIs...",
  "token_type": "Bearer",
  "expires_in": 3600
}
```

---

## 🔐 Uso del Token

Enviar en headers:

```http
Authorization: Bearer <token>
```

---

## 🔒 Scopes

Los permisos se manejan por proveedor:

Ejemplo:

```text
employees:read
employees:create
employees:update
```

---

## 📌 Protección de endpoints

### Solo autenticación

```python
Depends(JWTBearer())
```

---

### Con scopes

```python
Depends(JWTBearer(["employees:read"]))
```

---

## 👥 Ejemplo de endpoints

### Obtener empleados

```http
GET /employees
Authorization: Bearer <token>
```

Requiere:

```text
employees:read
```

---

### Crear empleado

```http
POST /employees
```

Requiere:

```text
employees:create
```

---

## 🧪 Endpoint de prueba

```http
GET /oauth/me
```

Devuelve el contenido del token.

---

## 🗄️ Base de datos

Tabla de proveedores:

```sql
CREATE TABLE EXTERNAL_PROVIDER (
    PROVIDER_ID VARCHAR2(100) PRIMARY KEY,
    PROVIDER_SECRET_HASH VARCHAR2(500) NOT NULL,
    PROVIDER_NAME VARCHAR2(200),
    PROVIDER_SCOPES VARCHAR2(500),
    STATUS NUMBER(1) DEFAULT 1,
    CREATED_AT DATE DEFAULT SYSDATE
);
```

---

## 🔥 Notas importantes

* Los scopes NO se envían desde el cliente
* Se controlan desde la base de datos
* El JWT solo es verificación, no autorización por sí solo
* Siempre validar scopes en backend

---

## 🧑‍💻 Autor

Proyecto interno de integración de nómina.

---

## 📌 Estado

✔ OAuth2 Client Credentials funcionando
✔ JWT RS256 implementado
✔ Control de scopes activo
✔ Oracle integrado


## GENERA LLAVE PUBLIC Y PROVADA 

openssl genrsa -out keys/private.pem 2048 

openssl rsa -in keys/private.pem -pubout -out keys/public.pem 