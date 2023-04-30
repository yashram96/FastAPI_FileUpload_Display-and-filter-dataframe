FROM python:3.8.10
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["uvicorn" ,"main:app", "--host", "0.0.0.0","--port" ,"8081"]
EXPOSE 8081