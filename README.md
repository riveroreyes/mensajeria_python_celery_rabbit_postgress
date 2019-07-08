# Cola Asincronica de Envio Masivo de Correos. Realizado en Python-Django
Desarrollo en Python-DJango para el envio de correos asincronico a N cantidad de usuarios.

Herramientas relacionadas utilizadas:
    - Docker
    - Django
    - Celery
    - RabbitMQ
    - Postgres

Instalacion:
    
Clonar el repositorio: git clone https://github.com/riveroreyes/mensajeria_python_celery_rabbit_postgress.git

Construir los contenedores: docker-compose build

Levantar los contenedores: docker-compose up

Abrir una nueva consola y migrar la base de datos: docker-compose run --rm python python  manage.py migrate

Crear un super usuario: docker-compose run --rm python python  manage.py createsuperuser

Probar la aplicacion: http://127.0.0.1:8000/, ATENCION: Posiblemente requiera modificar algun archivo del projecto (modifica tasks.py) para que docker active el servidor

Ingresar a administracion: http://127.0.0.1:8000/admin, colocar los datos del usuario recien creado.

Ir a usuarios: http://127.0.0.1:8000/admin/auth/user/


Crear un numero determinado de usuarios: Ejemplo: 500

docker-compose run --rm python python  manage.py shell_plus
        
    carlos@carlos:~/Documents/mensajeria_python_celery_rabbit_postgress/app/aplicaciones/tareas(master)$ docker-compose run --rm python python  manage.py shell_plus
    Starting mensajeria_python_celery_rabbit_postgress_postgres_1_42dc9c118430 ... done
    Starting mensajeria_python_celery_rabbit_postgress_rabbitmq_1_2f1dc5cfb726 ... done
    Starting mensajeria_python_celery_rabbit_postgress_celery_worker_1_726e3127c15b ... done
    Create user 'user'
    Running command 'python manage.py shell_plus'
    # Shell Plus Model Imports
    from django.contrib.admin.models import LogEntry
    from django.contrib.auth.models import Group, Permission, User
    from django.contrib.contenttypes.models import ContentType
    from django.contrib.sessions.models import Session
    # Shell Plus Django Imports
    from django.core.cache import cache
    from django.conf import settings
    from django.contrib.auth import get_user_model
    from django.db import transaction
    from django.db.models import Avg, Case, Count, F, Max, Min, Prefetch, Q, Sum, When, Exists, OuterRef, Subquery
    from django.utils import timezone
    from django.urls import reverse
    Python 3.6.8 (default, Jun 11 2019, 01:16:11) 
    [GCC 6.3.0 20170516] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    (InteractiveConsole)
    
    >>> from aplicaciones.tareas.views import create_user_random
    >>> create_user_random(500)
    'Fueron 500 usuarios creados correctamente'

Enviar los correos asincronicamente con celery:

Ir a http://127.0.0.1:8000/admin/auth/user/

En Actions: Seleccionar la opcion: Send email actions

Marcar todos los usuarios de esa pagina y presionar Go o Ir

Observar la consola de docker para ver el envio, La salida esta direccionada a la consola segun la configuracion en settings:

    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

    Respuesta:

    celery_worker_1_726e3127c15b | From: 785c549069e596
    celery_worker_1_726e3127c15b | To: usuario_qPdUs@msa.com.ve
    celery_worker_1_726e3127c15b | Date: Mon, 08 Jul 2019 01:06:38 -0000
    celery_worker_1_726e3127c15b | Message-ID: <156254799898.32.15727822216615144901@b709362b32e4>
    celery_worker_1_726e3127c15b | 
    celery_worker_1_726e3127c15b | Bienvenido, este es un mensaje de prueba CELERY, RABBITMQ Y DJANGO
    celery_worker_1_726e3127c15b | [2019-07-08 01:06:38,991: WARNING/ForkPoolWorker-8] -------------------------------------------------------------------------------
    celery_worker_1_726e3127c15b | [2019-07-08 01:06:39,994: WARNING/ForkPoolWorker-8] Content-Type: text/plain; charset="utf-8"
    celery_worker_1_726e3127c15b | MIME-Version: 1.0
    celery_worker_1_726e3127c15b | Content-Transfer-Encoding: 7bit
    celery_worker_1_726e3127c15b | Subject: Mensaje de prueba
    celery_worker_1_726e3127c15b | From: 785c549069e596
    celery_worker_1_726e3127c15b | To: usuario_CbJJO@msa.com.ve
    celery_worker_1_726e3127c15b | Date: Mon, 08 Jul 2019 01:06:39 -0000
    celery_worker_1_726e3127c15b | Message-ID: <156254799999.32.4275792355309631938@b709362b32e4>
    celery_worker_1_726e3127c15b | 
    celery_worker_1_726e3127c15b | Bienvenido, este es un mensaje de prueba CELERY, RABBITMQ Y DJANGO
    celery_worker_1_726e3127c15b | [2019-07-08 01:06:39,994: WARNING/ForkPoolWorker-8] -------------------------------------------------------------------------------
    celery_worker_1_726e3127c15b | [2019-07-08 01:06:40,996: WARNING/ForkPoolWorker-8] Content-Type: text/plain; charset="utf-8"
    celery_worker_1_726e3127c15b | MIME-Version: 1.0
    celery_worker_1_726e3127c15b | Content-Transfer-Encoding: 7bit
    celery_worker_1_726e3127c15b | Subject: Mensaje de prueba
    celery_worker_1_726e3127c15b | From: 785c549069e596
    celery_worker_1_726e3127c15b | To: usuario_zXdCZ@msa.com.ve
    celery_worker_1_726e3127c15b | Date: Mon, 08 Jul 2019 01:06:40 -0000
    celery_worker_1_726e3127c15b | Message-ID: <156254800099.32.11410617150659821030@b709362b32e4>
    celery_worker_1_726e3127c15b | 
    celery_worker_1_726e3127c15b | Bienvenido, este es un mensaje de prueba CELERY, RABBITMQ Y DJANGO
    celery_worker_1_726e3127c15b | [2019-07-08 01:06:40,996: WARNING/ForkPoolWorker-8] ----------------------------