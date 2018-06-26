
[![Build Status](https://travis-ci.org/johnkegz/ride.svg?branch=api)](https://travis-ci.org/johnkegz/ride)
[![Maintainability](https://api.codeclimate.com/v1/badges/72aafefdd6ecdfc4e366/maintainability)](https://codeclimate.com/github/johnkegz/ride/maintainability)
[![Coverage Status](https://coveralls.io/repos/github/johnkegz/ride/badge.svg)](https://coveralls.io/github/johnkegz/ride)
## Project Title

RIDE MAY WAY

### Prerequisites

You need to be having Heroku for the app to work
Flask==1.0.2
pytest==3.6.2
pylint==1.9.2
post man

### Installing

-load heroku website
-create account
-sign in 
-create an app and give it a unit name
-integrate it with git hub
-allow automatic update

## Running the tests

Tests are run using post man for client end forexample
 -get all rides is run by running the url
 api/v1/rides
 -get all rides is run by running the url
 api/v1/rides/<int:id>
 -for create ride offer this json input data is put in postman
 {"id":4, "time_to_leave":"1:29 pm", "price":"4000 /=", "start":"Gayaza", "destination":"matuga", "Driver_name":"kalyango john"}
 -for join offer this json file is used
 {"id"=4, "passenger_name":"Junior Sara", "phone_number":"078966857"
Unit tests are done in test_views.py using unittest package


## Deployment

The system is deployed on heroku

## Built With

* Flask micro framework 
* tested using unit tests (unittest package)
* plylint and PEP8 standards
* code climate for code maintainability 
* coverall.io for code cverage
* travis for testing whether tests are passing

## Versioning

I use git hub for versioning. 

## Authors

* **KALYANGO JOHN** -(https://github.com/johnkegz)

## Acknowledgments

* Thanks to ASSIIMWE INNOCENT MY Learning FACILITATOR(LFA)


