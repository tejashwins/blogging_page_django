pip3 install -r requirements.txt

echo "***********creating migrations*****************"
python manage.py makemigrations

echo "***********Applying*****************"
python manage.py migrate


echo "***********collecting static*****************"
python manage.py collectstatic

