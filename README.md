Welcome to the Online-Scientific-Journalism-Platform wiki!

# Online-Scientific-Journalism-Platform
this is about an online scientific journalism platform that allow writer to write an article and send it to Editorial Board to do there revision then deciding to publish or reject it, and it is fully supported for Arabic and English language

# supporting Arabic(RTL) and English(LTR) languages

![](https://i.imgur.com/nJr9vUA.png)

# to use this web app, you have to follow these steps:

### at the beginning we recommend you to make virtual environment for this project
`virtualenv <environment_name> --no-site-packages`

**environment_name **=> name it what ever you want

### activate the environment

### back to the <environment_name> file. Now get this project py downloading or cloning it but the unzipped folder that directly contain project folders and files here

### Now run this to get all dependencies
`pip install -r requirements.txt`

### then make migrations and migrate it run this
`python manage.py makemigrations`
then
`python manage.py migrate`

now create super user to get to admin site
`python manage.py createsuperuser`

### finally run server
`python manage.py runserver`
