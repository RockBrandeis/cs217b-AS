# COSI 217b - NLP Systems Assignments

Haochen Lin
haochenlin@brandeis.edu

This is a homework assignment repository base on the forked sample repository.
New function was added in order fullfill the requirement of assignment while redundant files and folders are removed.

Under you user terminal or powershell,

Navigate to asssigment1 where the program is running.(Previous:AS1)

```bash
$ cd assignment1
```

Navigate to asssigment2 where the program is running.(Previous:AS2)

```bash
$ cd assignment2
```

Navigate to asssigment3 where the program is running.

```bash
$ cd assignment3
```

Before entering the program, make sure you complete the Installation guide.(Not required for assignemnt3 unless you want to run individual programs.)


# Installation & dependency requirements Guide:

- Make sure you have Python 3.8(or above) installed .

- Make sure you have Docker setup and ready to run.

- Use the following commands to download require packges(For assignment3 only, you won't need the following since those are already downloaded through Dockerfile):

```bash
$ pip install fastapi
$ pip install uvicorn
$ pip install jupyter
$ pip install spacy
$ python -m spacy download en_core_web_sm
$ pip install flask flask-restful flask-sqlalchemy
$ pip install streamlit graphviz
$ pip install mypy
```


# Create a virtual environment in the current directory

VS code CodeSpace environment is recommended.

For those who do not using Github codespace as virtual environment, you can manually create one(Recommended but optional)
```bash
$ python3 -m venv venv
```
On Windows
```bash
$ .\venv\Scripts\activate
```
On macOS and Linux
```bash
$ source venv/bin/activate
```


------------------------------------------------------------------------

You will see more instruction on the README.md under the corresponding assignment folder
