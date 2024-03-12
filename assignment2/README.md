# Assignment 2 - Flask SQLAlchemy

Haochen Lin
haochenlin@brandeis.edu

The following pip command is required

```bash
$ pip install Flask==3.0.1
$ pip install Flask-SQLAlchemy==3.1.1
```


By using the following command you should be able to enter the website.
If not, manually enter http://127.0.0.1:5000/ in your browser
```bash
$ python myblog.py
```

You can use Ctrl + c to quit page server. 

There are three pages in this website, by entering a sentence in the begining page and submit, you will save correponding entities and dependencies of your sentence to the database. You can check the Processing result in the second page when your submit your sentence. By clicking button "View Database", you will enter the third page which contains everything in database, including Post table and Dependency table. You can delete everything by clicking the delete button. You can always go back to the first page by clicking "Go back to enter new texts".

Remember, repeat data won't be saved.