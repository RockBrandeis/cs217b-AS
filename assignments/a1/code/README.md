# Assignment 1 - Web Services

Follow the below instruction to test Fast API Flask webserver Streamlit



### Fast API test

Firstly load the fastapi with the below command
```bash
$ uvicorn app_fastapi:app --reload
```
then, in another terminal, test the following.

```bash
$ curl http://127.0.0.1:8000
$ curl http://127.0.0.1:8000/ner -H "Content-Type: application/json" -d@input.txt
$ curl http://127.0.0.1:8000/dep -H "Content-Type: application/json" -d@input.txt
```

```bash
$ curl http://127.0.0.1:8000?pretty=true
$ curl http://127.0.0.1:8000/ner?pretty=true -H "Content-Type: application/json" -d@input.json
$ curl http://127.0.0.1:8000/dep?pretty=true -H "Content-Type: application/json" -d@input.json
```
You can use Ctrl + c to quit. 

### Flask webserver

```bash
$ python app_flask.py
```
You can use Ctrl + c to quit. 

### Streamlit

```bash
$ python app_flask.py
```
You can use Ctrl + c to quit. 