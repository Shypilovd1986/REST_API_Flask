FROM ubuntu
RUN apt-get update
RUN apt-get install python3 -y
RUN apt-get install pip -y
WORKDIR app
ADD . /app
EXPOSE 3000
RUN pip install -r requirements.txt
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "3000"]
