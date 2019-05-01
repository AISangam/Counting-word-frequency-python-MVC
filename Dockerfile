FROM ubuntu:16.04
RUN apt-get update
RUN apt-get install -y python3-pip python3-dev build-essential
WORKDIR /freq_count
COPY . /freq_count
RUN pip3 install -r requirements.txt

