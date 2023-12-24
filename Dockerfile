FROM python:3
WORKDIR /krok_power_backend

ADD requirements.txt /krok_power_backend/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ADD . /krok_power_backend/
RUN python manage.py migrate

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
