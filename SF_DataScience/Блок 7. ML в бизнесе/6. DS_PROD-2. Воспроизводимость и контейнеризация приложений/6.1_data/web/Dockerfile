FROM python:3.9
WORKDIR /app
COPY ./app ./
COPY ./test ./
COPY ./requirements.txt ./
COPY ./server.py ./ 
RUN pip install -r requirements.txt
CMD [ "python", "./server.py" ]