FROM python:3.10

ADD .  /proxy/

WORKDIR /proxy/
RUN pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
RUN pip install --upgrade pip
RUN pip install -r /proxy/requirements.txt
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN echo 'Asia/Shanghai' >/etc/timezone

CMD ["python", "/proxy/main.py"]
