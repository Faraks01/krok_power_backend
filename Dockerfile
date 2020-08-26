FROM python:3
RUN mkdir /krok_power_backend
WORKDIR /krok_power_backend
ADD requirements.txt /krok_power_backend/
RUN pip install -r requirements.txt
ADD . /krok_power_backend/
EXPOSE 8000
