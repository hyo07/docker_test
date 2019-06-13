FROM python:latest

#COPY test_dir/test.py /
RUN git clone https://github.com/hyo07/docker_test.git

WORKDIR /docker_test

CMD ["python", "server.py"]
