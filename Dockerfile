FROM ubuntu:20.04
ENV DEBIAN_FRONTEND=noninteractive
ENV LC_ALL=C.UTF-8
RUN apt-get update && apt-get install -y curl build-essential checkinstall \
    libreadline-gplv2-dev libncursesw5-dev libssl-dev \
    libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev

RUN curl -sL https://www.python.org/ftp/python/3.6.10/Python-3.6.10.tgz -O && \
    tar xzf Python-3.6.10.tgz
WORKDIR /Python-3.6.10
RUN ./configure --enable-optimizations && make install

WORKDIR /usr/app
COPY . .
RUN pip3 install -r requirements.txt
ENV FLASK_APP=run
ENV FLASK_ENV=development
CMD [ "flask", "run", "--host", "0.0.0.0"]

EXPOSE 5000
