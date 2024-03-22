# inerG
inerG - interview - task
------------------------

STEP:01
python -m venv venv

STEP:02
pip install -r requirements.txt

STEP:03
flask run

STEP:04
flask db init

STEP:05
flask db migrate

STEP:06
flask db upgrade

STEP:07
(HIT THIS API TO LOAD CALCULATED DATA TO DB)

http://localhost:5000/v1/test

STEP:08
(HIT THIS API TO GET CALCULATED DATA TO DB)

http://localhost:8080/v1/data?well=34013214540000

