# meeting_organizer

## set up
clone the repository <br>
git clone https://github.com/ozanguvenwebdev/meeting_organizer<br>
<br>
python version is 'Python 3.12.0'<br>
<br>
virtual environnment is ready. to run the API;<br>
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


