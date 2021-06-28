FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR .
COPY requirements.txt .
RUN pip3 install -r requirements.txt

ENV WAIT_VERSION 2.7.2
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/$WAIT_VERSION/wait /wait
RUN chmod +x /wait

#COPY database/create.py database/create.py
#RUN python3 database/create.py
COPY . .