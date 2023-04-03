From Python3.8

WORKDIR /Flask

# copy code and database
COPY ./* C:/Users/Adina Dingankar/PycharmProjects/Data-Visualization

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "Web-app.py"]
