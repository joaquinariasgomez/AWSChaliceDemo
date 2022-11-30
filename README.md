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
1. Iniciar un entorno virtual con la versión de [Python requerida](#requisitos):
$ python3 -m venv .env
$ source .env/bin/activate

2. Moverse hacia directorio de la demo e instalar las dependencias:
(.env) $ cd chalice-demo
(.env) $ pip install -r requirements-dev.txt

3. Desplegar servicio de prueba y probar la API desplegada. Primero,
   renombraremos a *app.py* el fichero que contendrá la clase principal, para
que Chalice lo localice. Después, probaremos a desplegar usando *chalice
deploy*:
$ mv hello_world.py app.py
$ chalice deploy
(.env) $ curl $(chalice url)

4. Por último, probaremos a liberar recursos de AWS con *chalice delete*. Este comando liberará los recursos
creados en AWS, como lo son el rol de IAM, la función lambda y la API Rest de
API Gateway de la siguiente forma:
(.env) $ chalice delete

Opcionalmente, puedes desplegar la aplicación localmente con el siguiente
comando:
$ chalice local --autoreload

## La aplicación que montaremos

![Alt text](./arquitectura.svg "Arquitectura del sistema")

Para crear la base de datos, ejecutaremos el siguiente comando:
$ aws dynamodb create-table --table-name chalice-demo-table-dev \
  --attribute-definitions AttributeName=first_name,AttributeType=S \
  --key-schema AttributeName=first_name,KeyType=HASH \
  --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1

Ejemplo de curl para realizar peticiones a nuestro API Gateway:
$ curl -X POST $(chalice url)/signup -d '{
    "first_name": "joaquin",
    "email": "joaquinarias@gmail.com",
    "age": 27
}' -H 'Content-Type: application/json'

Politica a meter en .chalice/policy-dev.json:
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": "arn:aws:logs:*:*:*",
            "Effect": "Allow"
        },
        {
            "Action": [
                "dynamodb:PutItem",
                "dynamodb:DeleteItem",
                "dynamodb:UpdateItem",
                "dynamodb:GetItem",
                "dynamodb:Scan",
                "dynamodb:Query"
            ],
            "Resource": [
                "arn:aws:dynamodb:*:*:table/chalice-demo-table-dev"
            ],
            "Effect": "Allow"
        }
    ]
}

Añadir "autogen_policy": false
en .chalice/config.json