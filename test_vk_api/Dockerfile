FROM python:3.7

MAINTAINER <berserg2010@gmail.com>

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/test_vk_api

COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY . ./

EXPOSE 80

CMD ["gunicorn", "--bind", ":80", "test_vk_api.wsgi:application"]
