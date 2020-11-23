# KTP Validation Image

[Demo](https://dev-komik.pojokan.my.id/)

## Installation

* Clone the Repo
* Create the environment first
```bash
python -m venv env
```
* Activate the environment
```bash
env\Scripts\activate.bat
```
* Install all library needed to environment by using command
```bash
pip install -r requirements.txt
```


## Usage

* (For Windows) set the flask app
```bash
set FLASK_APP=app.py
```
* Start server with command:
```bash
python -m flask run
```

Then open [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## API

| Url        | Params           | Type |
| ------------- |:-------------:| :-----:| 
| /v1/valid      | ktp | Files | 

---

## Develop By Muhammad Zakir Ramadhan