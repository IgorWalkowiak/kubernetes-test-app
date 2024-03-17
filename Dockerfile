FROM python:3.12
LABEL Maintainer="igor.w"

WORKDIR /usr/app/src
COPY main.py ./

CMD ["python", "./main.py"]