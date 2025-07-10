# 🧾 API de Inventario y Facturación – Django REST

API REST construida con **Django** y **Django REST Framework** para gestionar productos, stock, ventas, clientes y facturación. Ideal para tiendas o empresas que necesitan control interno y emisión de facturas.

---

## 🚀 Tecnologías Usadas

- Python 3.11+
- Django 4.x
- Django REST Framework
- drf-writable-nested
- SQLite (puedes cambiar a PostgreSQL o MySQL)

---

## ⚙️ Instalación Rápida

```bash
# Clonar el proyecto
git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio

# Crear entorno virtual
python3 -m venv env
source env/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Migraciones y ejecución
python manage.py migrate
python manage.py runserver


## 🧩 Funcionalidades

- 📦 **Gestión de Productos**
  - Crear, listar, actualizar y eliminar productos.
  - Asignar categoría y moneda a cada producto.
  
- 🗃️ **Control de Inventario (Stock)**
  - Registro de cantidad en inventario por producto.
  - Actualización de stock al realizar ventas.

- 👥 **Clientes y Tipos de Cliente**
  - Registro de clientes finales.
  - Soporte para tipos: Persona Natural, Empresa, ONG, etc.

- 🧾 **Facturación y Ventas**
  - Crear facturas con múltiples productos.
  - Cálculo automático de subtotal, IVA y total.
  - Asociación con métodos de pago, moneda y fecha.

- 💵 **Soporte para Monedas y Pagos**
  - Registro de tipos de moneda (C$, USD, etc.).
  - Métodos de pago: Efectivo, Transferencia, etc.

- 🧩 **Estados de Factura**
  - Control de estado (Activa, Anulada).

🛠️ **Equipos Internos y Herramientas**
  - Registro de equipos usados en procesos técnicos.


## 🔌 Endpoints Principales

| Método | Endpoint              | Descripción                                                  |
|--------|-----------------------|--------------------------------------------------------------|
| GET    | `/products/`          | Listar todos los productos                                   |
| POST   | `/products/`          | Crear un nuevo producto                                      |
| GET    | `/productStock/`      | Ver stock actual por producto                                |
| POST   | `/productStock/`      | Registrar/actualizar cantidad en inventario                  |
| GET    | `/category/`          | Listar categorías de productos                               |
| POST   | `/category/`          | Crear nueva categoría                                        |
| GET    | `/equipment/`         | Listar equipos internos                                      |
| POST   | `/equipment/`         | Agregar equipo (ej. soldador, cautín, etc.)                 |
| GET    | `/equipmentCategory/` | Categorías de herramientas internas                          |
| GET    | `/customer/`          | Listar clientes                                              |
| POST   | `/customer/`          | Registrar cliente                                            |
| GET    | `/typeCustomer/`      | Listar tipos de cliente (Empresa, ONG, etc.)                 |
| GET    | `/bill/`              | Ver facturas registradas                                     |
| POST   | `/bill/`              | Crear nueva factura con múltiples productos                  |
| GET    | `/sale/`              | Detalle de productos vendidos                                |
| GET    | `/billState/`         | Estados disponibles para las facturas (Activa, Anulada)      |
| GET    | `/currencyType/`      | Listado de monedas (C$, USD, etc.)                           |
| GET    | `/paymentType/`       | Métodos de pago disponibles                                  |
| GET    | `/month/`             | Meses disponibles para organización temporal                 |
| GET    | `/year/`              | Años disponibles para agrupación                             |

