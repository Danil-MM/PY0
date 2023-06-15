FROM python:3.10.9
COPY ./requirements.txt /code/requirements.txt
WORKDIR /code
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
COPY . /code
CMD ("uvicorn","main:app","--host","0.0.0.0","port","80")