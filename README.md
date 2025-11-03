Sistema de Citas Médicas - Clínica

Este proyecto implementa un sistema web para la gestión de citas médicas, desarrollado con Django y Bootstrap 5. Incluye autenticación de usuarios, control de acceso y diseño responsivo.

Módulo de Autenticación
- Registro de nuevos usuarios con formulario personalizado
- Inicio y cierre de sesión
- Redirección automática al login tras cerrar sesión
- Vistas protegidas con login_required

Diseño con Bootstrap
- Formularios limpios y centrados
- Estilo profesional con card, btn, form-label, etc.
- Navegación dinámica según estado de sesión
- Plantilla base (base.html) con navbar adaptable
  
Control de Acceso
- Vistas internas protegidas para usuarios autenticados
- Redirección automática al login si no hay sesión activa
