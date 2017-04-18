# example-api-DRF
This is a example of project create with Django Rest Framework, for generate a simple API

##Requeriments
You requires the following:

* Python 2.7
* Django
* djangorestframework

##Installation
First you need clone the project in your workspace:

```sh
git clone https://github.com/jroaes/example-api-DRF
```


For the installation you can create a Virtual environment:

```sh
virtualenv tutorial
source tutorial/bin/activate  # On Windows use `env\Scripts\activate`
```

Once we have created and activated our virtual environment, we proceed to install the necessary packages:

```sh
pip install django
pip install djangorestframework
```

Now, we are ready to test. Move to the folder telefonica and first migrate the models, and run the server:

```sh
cd your-workspace/telefonica
python manage.py makemigrations postulacion
python manage.py migrate
python manage.py runserver 0.0.0.0:8080
```
You can test this in yout browser in localhost:8080 and localhost:8080/persona/ for get API
