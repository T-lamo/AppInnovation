## Introduction
_{This project is designed to connect a robot pepper, google recognition and rasa technology. In this section is the database part and rasa. We've chosen sqlite3 database, sqlalchemy ORM and duckling to extract dates.}
## Installing dependancies
_{ These following should be installed (latest version is preferred unless the version is precised): }
*_Python 3.7+ ou 3.9-
*_sqlalchemy
*_duckling (implemented in rasa)

## Steps 
*_Run ducking server: sudo docker run -p 8008:8000 (please change 8008 to an available port in your computer)
*_Run: rasa run actions 
*_Run: rasa shell (to test the to discuss with the bot)

## Stories
_{ Please follow the stories in stories file }