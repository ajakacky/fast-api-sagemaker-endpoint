FROM python:3.8-alpine

RUN ln -s /usr/bin/python3 /usr/bin/python & \
    ln -s /usr/bin/pip3 /usr/bin/pip

RUN pip install fastapi uvicorn

ENV PATH="/opt/program:${PATH}"
COPY code /opt/program

RUN chmod 755 /opt/program
WORKDIR /opt/program
RUN chmod 755 serve

EXPOSE 8080