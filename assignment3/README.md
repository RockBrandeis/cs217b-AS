# Assignment 3 - Docker image

Haochen Lin
haochenlin@brandeis.edu

The following was run on a docker file which has pre-built configs, before using the below, make sure that you have successfully setup the Docker. You can do this either through VS code Docker plugin (If you're using VS code) or manually download it in the official website. Docker plugin   

In the assignment3 directory, run the following the build a docker image in your terminal.(solo_blog is my image name, change it to anything you like.)

```bash
$ docker build -t solo_blog .
```

After successfully build tge image, runs this command to run the image.
```bash
$ docker run -d -p 8000:8000 -p 5000:5000 -p 8501:8501 solo_blog

```

Then you should be able to acess http://127.0.0.1:8000 http://127.0.0.1:5000/ http://127.0.0.1:8501/ at the same time.


Use the following commmands if you want to check the container status

Show the status of all container/running container
```bash
docker image ls
docker ps
```

Delete the container.(Replace CONTAINER_ID_OR_NAME to the actual id or name, you're able to find it through the above command)
```bash
docker rm CONTAINER_ID_OR_NAME
```

----------


The following are the way the run individual files without docker image, and you may not need it.

------------------------------

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

### Flask webserver with SQL Database


By using the following command you should be able to enter the website.
If not, manually enter http://127.0.0.1:5000/ in your browser
```bash
$ python myblog.py
```

You can use Ctrl + c to quit page server. 

There are three pages in this website, by entering a sentence in the begining page and submit, you will save correponding entities and dependencies of your sentence to the database. You can check the Processing result in the second page when your submit your sentence. By clicking button "View Database", you will enter the third page which contains everything in database, including Post table and Dependency table. You can delete everything by clicking the delete button. You can always go back to the first page by clicking "Go back to enter new texts".

Remember, repeat data won't be saved.


### Streamlit
By using the following command you should be able to enter the website. 
If not, manually enter http://127.0.0.1:8501/ in your browser

```bash
$ streamlit run app_streamlit.py
```
You can use Ctrl + c to quit. 