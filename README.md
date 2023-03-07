

### API creada con Django Rest Framework y MySQL.


## Requisitos para correr el proyecto

- Python 3.x
- [Git](https://git-scm.com/)  y Git bash


## Instalacion del proyecto

Usar Git bash para clonar el proyecto:

```bash
git clone https://github.com/locchiato/python-api-restful
```

Entrar al proyecto:
```bash
cd python-api-restful
```

Crear entorno virtual:
```bash
py -m venv venv
```

Activar el entorno virtual:
```bash
source venv/bin/activate
#En cmd es: venv\Scripts\activate.bat
```

Instalar dependecias utilizando el archivo requirements.txt
```bash
pip install -r requirements.txt
```

Crear super usuario
```bash
python manage.py createsuperuser --username=tu_usuario
```

Crear archivo .env en la raiz del proyecto, que contenga las siguientes constantes:
```bash
DB_NAME=uniwebcity
USER=usuario_mysql
PASSWORD=contraseña_mysql
HOST=localhost
SECRET_KEY=secret_key
```


## Modo de uso

Iniciar la API
```bash
python manage.py runserver
```

Por defecto se ejecuta en el puerto 8000 de tu computadora.
Por lo que la ruta de acceso al proyecto sera: 127.0.0.1:8000
A menos que lo aclare al iniciar de la siguiente forma
```bash
python manage.py runserver localhost:9090
```


Las rutas a las que se puede acceder son las siguientes:

| Endpoint | Description |
| --- | --- |
| / | Muestra la pagina principal |
| /departments | Lista los departamentos existentes |
| /professors | Muestra los profesores activos |

