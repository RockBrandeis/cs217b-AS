# Assignment 1 - Web Services

Follow the below instruction to test Fast API, Flask webserver, and Streamlit.

If you're not using any editor terminal, open the Windows power shell by searching it through the Windows search tab. Otherwise, Press the windows button + x, then press i to open the window power shell. If you are using MacOS, click the Launchpad icon in the Dock, type Terminal in the search field, and then click Terminal. 

### Fast API test

Firstly load the fastapi with the below command
```bash
$ uvicorn app_fastapi:app --reload
```
Then, in another terminal, test the following.(Don't foreget run it in the same directory as the app)

```bash
$ curl http://127.0.0.1:8000
$ curl http://127.0.0.1:8000/ner -H "Content-Type: application/json" -d@input.json
$ curl http://127.0.0.1:8000/dep -H "Content-Type: application/json" -d@input.json
```
Or, you can try '?pretty' if you want better writing
```bash
$ curl http://127.0.0.1:8000?pretty=true
$ curl http://127.0.0.1:8000/ner?pretty=true -H "Content-Type: application/json" -d@input.json
$ curl http://127.0.0.1:8000/dep?pretty=true -H "Content-Type: application/json" -d@input.json
```
If running successful, you should see something like following in the main terminal.

```bash
INFO:     127.0.0.1:33942 - "GET / HTTP/1.1" 200 OK
INFO:     127.0.0.1:40326 - "POST /ner HTTP/1.1" 200 OK
INFO:     127.0.0.1:36134 - "POST /dep HTTP/1.1" 200 OK
INFO:     127.0.0.1:40848 - "GET /?pretty=true HTTP/1.1" 200 OK
INFO:     127.0.0.1:52024 - "POST /ner?pretty=true HTTP/1.1" 200 OK
INFO:     127.0.0.1:36788 - "POST /dep?pretty=true HTTP/1.1" 200 OK

```

You can use Ctrl + c to quit. 

### Flask webserver
By using the following command you should be able to enter the website.
If not, manually enter http://127.0.0.1:5000/ in your browser
```bash
$ python app_flask.py
```
You can use Ctrl + c to quit. 

### Streamlit
By using the following command you should be able to enter the website. 
If not, manually enter http://127.0.0.1:8501/ in your browser

```bash
$ streamlit run app_streamlit.py
```
You can use Ctrl + c to quit. 