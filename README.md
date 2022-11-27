# AWSChaliceDemo
Simple demo for creating a serverless AWS app using Chalice

## Requisitos
- Tener instalado Python3.6, Python3.7, Python3.8 o Python3.9.
- Tener configuradas las credenciales de AWS en el equipo.
  - Debes tener creado el directorio ~/.aws
  - Las credenciales deben estar configuradas de la siguiente forma:
  $ cat >> ~/.aws/config
  [default]
  aws_access_key_id=YOUR_ACCESS_KEY_HERE
  aws_secret_access_key=YOUR_SECRET_ACCESS_KEY
  region=YOUR_REGION

## Primeros pasos
1. Iniciar un entorno virtual e instalar chalice dentro:
$ python3 -m venv .env
$ source .env/bin/activate
(.env) $ pip install -r requirements-dev.txt

2. Desplegar servicio de prueba y probar la API desplegada
$ chalice deploy
(.env) $ curl *url de API Gateway recibida*

Opcionalmente, se puede ejecutar chalice delete para liberar los recursos
creados en AWS, como lo son el rol de IAM, la función lambda y la API Rest de
API Gateway de la siguiente forma:
(.env) $ chalice delete

Opcionalmente, puedes desplegar la aplicación localmente con el siguiente
comando:
$ chalice local --autoreload

Para mostrar la url publicada por API Gateway:
$ chalice url

## La aplicación que montaremos

Para crear la base de datos, ejecutaremos el siguiente comando:
$ aws dynamodb create-table --table-name chalice-demo-table-dev \
  --attribute-definitions AttributeName=first_name,AttributeType=S \
  --key-schema AttributeName=first_name,KeyType=HASH \
  --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1
