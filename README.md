# django-clientes-banco

## Características

- Gestión de clientes: Crear, leer, actualizar y eliminar registros.
- Filtros avanzados: Filtrar clientes por género, estado activo e índice de satisfacción.
- Paginación configurable: Selecciona cuántos registros mostrar por página (10, 20, 50, 100).
- API REST para integraciones externas.
- Análisis inicial de datos con Pandas.
  
---

## Requisitos
- Python 3.12
- Django 5.1
- Pipenv o pip
- Entorno virtual
- instalar dependencias usando pip install -r requirements.txt
## Instalación

Sigue estos pasos para instalar y configurar la aplicación en tu máquina local:

### 1. Clonar el repositorio
Clona el repositorio desde GitHub:
```bash
git clone https://github.com/tu_usuario/django-clientes-banco.git
cd django-clientes-banco
```
### 2. Crear un entorno virtual
Es recomendable usar un entorno virtual para evitar conflictos de dependencias:
```bash
python3 -m venv djangoenv
source ../djangoenv/bin/activate
```
### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```
### 4. Configurar la base de datos
```bash
python manage.py makemigrations
python manage.py migrate
```
### 5. Cargar datos iniciales
Si deseas cargar datos iniciales desde el archivo clientes_banco.csv, ejecuta:
```bash
python manage.py makemigrations
python manage.py migrate
```
### 6. Ejecutar el servidor de desarrollo
```bash
python manage.py runserver
```
### 7. Ejecutar en un servidor Apache2
Asegúrate de que Apache2 y mod_wsgi están instalados:
```bash
sudo apt update
sudo apt install apache2 libapache2-mod-wsgi-py3
```
### 7.1 Configurar Apache2 para Django
Crea un archivo de configuración para el sitio:
```bash
sudo nano /etc/apache2/sites-available/django-clientes-banco.conf
```
Inserta la siguiente configuración:
```bash
<VirtualHost *:80>
    ServerName yourdomain.com
    ServerAdmin admin@yourdomain.com

    DocumentRoot /var/www/django-clientes-banco

    Alias /static /var/www/django-clientes-banco/static
    <Directory /var/www/django-clientes-banco/static>
        Require all granted
    </Directory>

    <Directory /var/www/django-clientes-banco/djangoapi>
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory>

    WSGIDaemonProcess django-clientes-banco python-path=/var/www/django-clientes-banco:/var/www/django-clientes-banco/djangoenv/lib/python3.12/site-packages
    WSGIProcessGroup django-clientes-banco
    WSGIScriptAlias / /var/www/django-clientes-banco/djangoapi/wsgi.py
</VirtualHost>
```
### 7.2 Activar el sitio y reiniciar Apache
```bash
sudo a2ensite django-clientes-banco.conf
sudo systemctl restart apache2
```
### 7.3 Preparar archivos estáticos
```bash
python manage.py collectstatic
```
Asegúrate de que la carpeta /static tiene los permisos correctos:
```bash
sudo chown -R www-data:www-data /var/www/django-clientes-banco/static
```

### Reiniciar servidor apache2
```bash
sudo systemctl restart apache2
```
### Acceder a la aplicación
desde un navegador ingresar a las siguientes urls
```bash
http://<tu.ip>/listar/
http://<tu.ip>/crear/
http://<tu.ip>/estadisticas/
http://<tu.ip>/filtrar/
```

### Comando git
desde un navegador ingresar a las siguientes urls
```bash
git pull
git push
```


### Cargar clientes
Ir a la carpeta raiz del proyecto, luego activar el entorno virtual 
```bash
source ../djangoenv/bin/activate
```
Finalmente ejecutar el script para cargar los clientes en la base de datos
```bash
python manage.py cargar_clientes
```
desactivar entorno virtual
```bash
deactivate
```
Reiniciar el servidor Apache2
```bash
sudo systemctl restart apache2
```
