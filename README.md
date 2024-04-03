# inerG
inerG - interview - task
------------------------

STEP:01
python -m venv venv

STEP:02
.\venv\Scripts\Activate
or
.\venv\bin\activate

STEP:03
pip install -r requirements.txt

STEP:04
flask db init

STEP:05
flask db migrate

STEP:06
flask db upgrade

STEP:07
python runserver.py
or
flask run

STEP:08
(HIT THIS API TO LOAD CALCULATED DATA TO DB)

http://localhost:8080/v1/test

STEP:09
(HIT THIS API TO GET CALCULATED DATA TO DB)

http://localhost:8080/v1/data?well=34013214540000

STEP:10
(HIT THIS API TO GET MULTIPLE QUARTER VALUES AS WELL AS SINGLE)

SINGLE:
http://127.0.0.1:8080/v1/data?well=34059243550000&quarter=1

MULTIPLE:
http://127.0.0.1:8080/v1/data?well=34059243550000&quarter=1,2,3,4