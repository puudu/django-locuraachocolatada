## Requerimientos

Antes de comenzar, asegúrate de tener instalados los siguientes requerimientos:

- Python y pip
- Node.js y npm
- MySQL

## Instalación

1. Instala los requerimientos de Python utilizando el siguiente comando:

```bash
pip install -r requirements.txt
```

2. Instala Tailwind CSS dentro del proyecto Django ejecutando el siguiente comando:

```bash
npm install -D tailwindcss
```

Nota: Debes tener Node.js instalado en tu sistema.

3. Inicia MySQL y crea una base de datos llamada "locuraachocolatada".

4. Arranca el proyecto Django con el siguiente comando:

```bash
python manage.py runserver
```

5. Opcional: Si necesitas hacer cambios en las clases de los templates y actualizar Tailwind CSS, puedes iniciar el observador de Tailwind con el siguiente comando:

```bash
npx tailwindcss -o locuraachocolatada/static/css/output.css --watch
```

Este comando observa los componentes utilizados en el proyecto y los actualiza en el archivo output.css.

Nota: No es necesario arrancar el observador si no vas a hacer cambios en las clases en los templates.

¡Listo! Ahora deberías tener el proyecto funcionando localmente en tu entorno de desarrollo.
