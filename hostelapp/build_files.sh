echo "building started"
python -m pip install --upgrade pip
pip install -r requirements.txt
# Run Django commands
python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate

echo "build completed"