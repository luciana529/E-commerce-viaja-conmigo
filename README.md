# Viaja Conmigo 🌍✈️

<p align="center">
  <img src="static/images/logo02.jpg" alt="Logo Viaja Conmigo" style="width: 30%; max-width: 200px;"> 

<h5 align="center">Tu destino para experiencias de viaje inolvidables</h5>

**Viaja Conmigo** es un e-commerce moderno desarrollado en Django que ofrece una experiencia completa de compra y reserva de paquetes turísticos. Descubre destinos exóticos, organiza tus vacaciones soñadas y disfruta de una plataforma intuitiva diseñada para viajeros como tú.

## 🎯 ¿En qué consiste?

Este proyecto es un e-commerce especializado en turismo y viajes, desarrollado con **Django Framework** en Python. Utiliza un entorno virtual configurado para desarrollo seguro y escalable. Las tecnologías incluyen Python, JavaScript, HTML, Bootstrap/CSS, jQuery y SQLite. Todas las páginas del sitio web son dinámicas e interactivas.

### Stack Tecnológico
- **Backend:** Django (Python)
- **Frontend:** HTML5, Bootstrap, CSS3, jQuery
- **Base de Datos:** SQLite
- **Autenticación:** JWT con Base64
- **Pagos:** PayPal Sandbox (para testing)
- **Email:** Gmail SMTP (para notificaciones)

---

## ✨ Características Destacadas

### 🏢 Panel de Administrador
- Gestionar paquetes turísticos con información detallada (destino, precio, duración, disponibilidad)
- Ver y responder reseñas de clientes verificados
- Administrar órdenes de reservas con detalles completos
- Controlar transacciones de pago
- Visualizar productos solicitados con variaciones

### 🗺️ Categorías de Viajes
- Playas y resorts
- Montaña y trekking
- Ciudades y cultura
- Aventura y extremo
- Viajes familiares
- Lujo y escapadas románticas

### 🛒 Carrito de Compras Inteligente
- Carrito persistente identificado por cartID único
- Visualización de paquetes seleccionados
- Control de cantidad y disponibilidad
- Resumen dinámico de costos

### 👤 Gestión de Cuentas
- Sistema de grupos y roles con Django
- Perfiles de usuario con información personal
- Historial de reservas y compras

### 📧 Usuarios y Perfiles
- Registro seguro con verificación por email
- Perfiles personalizados con foto, ubicación, datos de contacto
- Sistema de recuperación de contraseña
- Información completa de cuenta

### 💳 Carrito y Checkout
- Agregar/eliminar paquetes
- Ajustar cantidades antes de comprar
- Resumen de compra detallado
- Selección de dirección de envío

### 💰 Pago Seguro
- Integración con PayPal
- Métodos de pago múltiples
- Confirmación instantánea de transacción

### ✅ Confirmación de Compra
- Email de confirmación automático
- Detalles de la reserva
- Información de entrega/viaje
- Número de pedido único

---

## 🚀 Instalación y Ejecución

### Requisitos Previos
- Python 3.11+
- Git
- pip (gestor de paquetes Python)

### Pasos de Instalación

1. **Clonar el repositorio:**
```bash
git clone https://github.com/tu-usuario/viaja-conmigo.git
cd viaja-conmigo
```

2. **Crear entorno virtual:**
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

4. **Configurar variables de entorno:**

Crea un archivo `.env` en la raíz del proyecto:
```
SECRET_KEY=tu-clave-secreta-aqui
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
EMAIL_HOST_USER=tu-email@gmail.com
EMAIL_HOST_PASSWORD=tu-contraseña-app
PAYPAL_CLIENT_ID=tu-paypal-client-id
PAYPAL_SECRET=tu-paypal-secret
```

5. **Ejecutar migraciones:**
```bash
python manage.py migrate
```

6. **Crear superusuario (admin):**
```bash
python manage.py createsuperuser
```

7. **Ejecutar servidor de desarrollo:**
```bash
python manage.py runserver
```

Accede a: **http://127.0.0.1:8000/**

---

## 📖 Uso y Acceso

### Para Usuarios
1. Navega a **http://127.0.0.1:8000/**
2. Registrate con tu email
3. Verifica tu cuenta (revisa tu email)
4. Inicia sesión
5. Explora destinos y agrega paquetes al carrito
6. Completa la compra

### Para Administradores
Accede al panel: **http://127.0.0.1:8000/admin/**

Usa las credenciales creadas con `createsuperuser`.

En el admin podrás:
- Crear/editar/eliminar paquetes turísticos
- Ver reseñas de clientes
- Gestionar órdenes
- Administrar usuarios

---

## 🏗️ Estructura del Proyecto

```
viaja-conmigo/
├── accounts/           # Gestión de cuentas y autenticación
│   ├── models.py       # Modelos de usuario y perfil
│   ├── views.py        # Vistas de login/registro
│   └── templates/
├── store/              # Tienda y catálogo de viajes
│   ├── models.py       # Productos (paquetes turísticos)
│   ├── views.py        # Vistas de productos
│   └── templates/
├── carts/              # Carrito de compras
│   ├── models.py       # Modelo del carrito
│   └── views.py
├── orders/             # Órdenes y reservas
│   ├── models.py       # Modelo de órdenes
│   └── views.py
├── category/           # Categorías de viajes
├── static/             # CSS, JS, imágenes
│   ├── css/
│   ├── js/
│   └── images/
├── templates/          # Plantillas HTML
├── media/              # Fotos de paquetes (subidas)
│   └── photos/products/
├── db.sqlite3          # Base de datos
├── manage.py           # Gestor de Django
├── requirements.txt    # Dependencias
└── .env                # Variables de entorno (no versionado)
```

---

## 🎨 Personalización

### Cambiar Nombre de la Tienda
- Edita `settings.py` para el nombre
- Modifica `templates/base.html` para el navbar
- Actualiza `templates/includes/footer.html`

### Cambiar Colores
- Edita `static/css/custom.css`
- Paleta actual: Azul (#0066CC) + Turquesa (#00BCD4) + Blanco

### Agregar Nuevos Paquetes
1. Ve al admin: `/admin/store/product/`
2. Haz clic en "Agregar producto"
3. Completa información del destino
4. Sube imagen del lugar
5. Guarda

---

## 🔧 Configuración de Email (Gmail)

Para que funcione el envío de emails:

1. Activa "Contraseñas de aplicación" en tu cuenta Google
2. Genera una contraseña de app para Gmail
3. Actualiza `.env`:
```
EMAIL_HOST_USER=tu-email@gmail.com
EMAIL_HOST_PASSWORD=tu-contraseña-app-generada
```

---

## 💳 Configuración de PayPal

Para testing con PayPal Sandbox:

1. Crea cuenta en [PayPal Developer](https://developer.paypal.com)
2. Obtén tu `Client ID` y `Secret`
3. Actualiza `.env`:
```
PAYPAL_CLIENT_ID=tu-client-id
PAYPAL_SECRET=tu-secret
```

---

## 🐛 Solución de Problemas

### Las imágenes no cargan
```bash
python manage.py collectstatic
```

### Error de módulo faltante
```bash
pip install -r requirements.txt
```

### Error de base de datos
```bash
python manage.py migrate
```

---

## 📝 Notas de Seguridad

⚠️ **IMPORTANTE:**
- Nunca compartas tu archivo `.env` en GitHub
- Cambia `SECRET_KEY` en producción
- Establece `DEBUG=False` en producción
- Usa variables de entorno para credenciales
- Habilita HTTPS en producción

---

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si encuentras bugs o tienes mejoras:

1. Fork el proyecto
2. Crea una rama (`git checkout -b feature/AmazingFeature`)
3. Commit cambios (`git commit -m 'Add AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

## 📄 Licencia

Este proyecto está bajo licencia MIT. Ver archivo `LICENSE` para detalles.

---

## 👨‍💻 Autor

**Luciana Ramirez**

- Email: lucianaramirez3012@gmail.com
- Portfolio: https://lucianaramirezsystems.lovable.app

---

## 📞 Soporte

¿Preguntas o problemas? Contáctame:
- Email: lucianaramirez3012@gmail.com


---

**¡Que disfrutes creando experiencias de viaje increíbles! 🌴✈️🏖️**
