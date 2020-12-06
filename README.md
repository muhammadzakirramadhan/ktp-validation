# KTP Validation Image

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
| /api/valid      | ktp | Files | 
| /api/extract_ktp	| ktp | Files |
| /api/match	| ktp,nik | Files, Integer |

---

## Develop By Muhammad Zakir Ramadhan