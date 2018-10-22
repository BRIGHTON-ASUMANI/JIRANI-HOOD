# __GB-AWWWARDS__
[GB-AWWWARDS](www.gbawwwards.herokuapp.com)
 This is  an application that allows users to post their projects and other people with different profiles are able to rate whatever projects are posted.
> A user will be able to post an image of their project, add a description to that project and lastly a link that redirects a user to the actual project


### __prerequisites__
The app runs on django==1.11 and works with both bootstrap4
and runs currently on >= python3.6 ubuntu 16.04

### __installation__
For the application to work you need some basic installations.
1. install a virtualenv in your root folder
  * sudo apt-get install python3-pip
  * sudo pip3 install virtualenv
  * virtualenv venv
  *after the above process make sure you activate the virtual by writing source virtual/bin/activate*

2. To start a django app you have to install django e.g ***python3.6 -m pip install django==1.11***

3. Then start a django project  -  django-admin startproject projectname
4. Inside the django project start a django-app -  django-admin startapp appname
5. for more info please read the [django documentation](https://docs.djangoproject.com/en/2.1/releases/1.11/)

### __Emerging Errors__
1. ***Error:*** - No module named django. ***Soln:*** install django in this format *python3.6 -m pip install django==1.11*

2. ***Error:***  - Programming Error. ***soln:*** make sure you migrate your database after you make changes ***python3.6 manage.py makemigrations*** and then ***python3.6 manage.py migrate***

> ***__programming is prone to errors therfore make sure ou install everything required in the requirements.txt and you do this by typing *python3.6 pip install -r requirements.txt *__***

3.
### __Running Tests__
> After passing in diferrent functions in this application, one has to write tests
> some of the functions include:
***note tests have to be assigned in the tests.py module***

### __Technologies Used__
1. posgresql
2. django==1.11
3. python3.6
4. bootstrap4
5. javascript
6. uploadcare

### __Deployment to Heroku__
> for deployment in heroku please click on this link and follow the steps very keenly [deployment](https://www.codementor.io/jamesezechukwu/how-to-deploy-django-app-on-heroku-dtsee04d4)


### __Authors__
***fh5co ASUMANI***
* For anyproblem please contact at asumanifh5co@gmail.com

### __Licence__
This project is licensed under the MIT License

***__MIT License__

Copyright (c) 2018 bright

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.***
