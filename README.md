# DFT API
[![Build Status](https://travis-ci.org/fnscoder/dft_api.svg?branch=master)](https://travis-ci.org/fnscoder/dft_api)
[![Maintainability](https://api.codeclimate.com/v1/badges/876e5b402d4f470c3fc8/maintainability)](https://codeclimate.com/github/fnscoder/dft_api/maintainability)

[Live on heroku](http://dft-api-fnsouza.herokuapp.com/api/auth/token/)

## How to run the project

1. Clone repository
2. Create a virtualenv python 3.7
3. Activate your virtualenv
4. Install dependencies (gunicorn and psycopg2 are not required for development instance, only for deploy on heroku)
5. Configure the instance with .env file
6. Run the tests

```console
git clone git@github.com:fnscoder/dft_api.git dft_api
cd dft_api
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp contrib/sample-env .env
python manage.py test
```
