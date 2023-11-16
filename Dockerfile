FROM python:3.9-alpine


COPY . /EFIdevOpsPython
WORKDIR /EFIdevOpsPython

RUN pip install --upgrade pip
RUN pip install -r requirements.txt



EXPOSE 5005



ENV FLASK_APP=app/__init__.py
ENV FLASK_RUN_HOST=0.0.0.0






CMD ["sh", "run.sh"]
