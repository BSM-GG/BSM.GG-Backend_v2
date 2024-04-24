FROM python:3.9

WORKDIR /bssmgg/

COPY . /bssmgg/

#COPY ./requirements.txt /bssmgg/

RUN pip3 install --no-cache-dir --upgrade -r ./requirements.txt

CMD uvicorn --host=0.0.0.0 --port 9000 main:app
