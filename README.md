# meeting_organizer

myproject folder is the API itself. I used Django REST Framework to create it.<br> it should be run at localhost (which I explained in the following paragraphs)<br>
one-page application is the 'client.html' file. I used 'fetch' in JS to show clearly which methods I used to GET, POST, PUT and DELETE data, although I do not generally use JS for requests and responses.<br>
I also used bootstrap modals to design it as much as I could in a limited time.

!!! <b>algorithm_tasks</b> folder includes external py tasks<br>
!!! that folder is unrelated to the meeting_organizer project<br>
<br>

## set up
clone the repository <br>
git clone https://github.com/ozanguvenwebdev/meeting_organizer<br>
<br>
python version is 'Python 3.12.0'<br>
<br>
create a virtual environnment to run the API;<br>
virtualenv env
activate the environment with '. env/Scripts/activate' in linux, 'env\Scripts\activate' in windows (in the directory which includes env folder)<br>
after creating and activating env, run 'pip install -r requirements.txt'<br>
change directory to the folder which includes 'manage.py' (/meeting_organizer/myproject)<br>
then run command 'python manage.py runserver'<br>

<br>
API should run at localhost (http://127.0.0.1:8000/)<br>
it is important because I fetched the data from 'http://127.0.0.1:8000/'<br>
<br>
then, open client.html (/meeting_organizer)
<br>

## meeting_organizer
there is an "Add" button on the top right-hand corner<br>
you can add a new meeting by using <b>POST method</b><br>
<br>
after adding a new meeting, the page will refresh itself<br>
the meeting data will be fetch when the page is loaded by <b>GET method</b><br>
<br>
there are "Edit" buttons on the right-hand of the list items<br>
you can update the selected data by clicking them by <b>PUT method</b><br>
<br>
there are "Delete" buttons on the right-hand of the list items<br>
you can delete the selected data by clicking them by <b>DELETE method</b><br>
<br>


