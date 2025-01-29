# AKK Tasks Project

## Clone project on local

Clone project on your local by executing following command in shell.

```shell
git clone https://github.com/waqas-ali-pk/tasks.git
cd tasks
```


## Create virtual environment

Execute following command in shell to create virtual environment.

```shell
virtualenv venv
```

<i><b>Note</b>: If virtualenv does not exist, then install it first using following command in shell. </i>

```shell
pip install virtualenv
```

## Activate virtual environment.

Activate following command in shell, to activate virtual environment.

```shell
.\venv\Scripts\activate
```

<i><b>Note:</b> this command is for Windows 10, use alternate commands if you are on different operating system.</i>

## Install dependencies

Execute following command to install dependencies from requirements.txt file.

```shell
pip install -r requirements.txt
```

## Create migrations

Execute following command to create migrations file (if any).

```shell
python manage.py makemigrations
```

## Migrate database changes

Execute following command to migrate database changes.

```shell
python manage.py migrate
```

## Create superuser.

Execute following command to create a superuser in database.

```shell
python manage.py createsuperuser
```

<i>Enter following values (or your own values as per your choice) to create superuser.</i>

```shell
username: admin
email: admin@aak.com
password: admin
```

## Create file  for environment variables.

There is a file exists <b>.env.example</b> at the root of project, create a new file <b>.env</b> and copy all the environment variables from <b>.env.example</b> file and paste in <b>.env</b> file, change environment variables values as per your choice.

## Start development server

Execute following command to start django development server.

```shell
python manage.py runserver 0.0.0.0:8000
```

Open following URL in browser:

http://localhost:8000

Swagger UI can be access at this URL:

http://localhost:8000/apis/schema/swagger-ui/

<i>Note: To view admin panel, open following URL in browser.</i>

http://localhost:8000/admin
