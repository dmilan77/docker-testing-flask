FROM python:3.13.0b1-slim

MAINTAINER Milan Das "milan.das77@gmail.com"
ENV APP_HOME /dockerapp
COPY ./app/ $APP_HOME/app/
COPY requirements.txt $APP_HOME/
WORKDIR $APP_HOME
RUN pip install -r requirements.txt
ENV PYTHONPATH=$PYTHONPATH:$APP_HOME

ENTRYPOINT ["python"]
CMD ["app/main.py"]
