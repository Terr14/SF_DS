FROM python:latest
WORKDIR /src/app
COPY ./src/ ./
COPY ./requirements.txt ./
RUN pip install -r requirements.txt
CMD [ "python", "./plot.py" ]