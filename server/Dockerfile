FROM python:3.7

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/

WORKDIR /opt/project/server
ADD . /opt/project/server

EXPOSE 8000
