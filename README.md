## Que Management in Django with Real time chat
[![Twitter](https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Ftwitter.com%2Ffeytonf)](https://twitter.com/intent/tweet?text=Wow:&url=https%3A%2F%2Fgithub.com%2Ffeyton%2Fque_manager) [![GitHub issues](https://img.shields.io/github/issues/feyton/que_manager)](https://github.com/feyton/que_manager/issues) [![GitHub stars](https://img.shields.io/github/stars/feyton/que_manager)](https://github.com/feyton/que_manager/stargazers)

## Introduction
This is a full fledged application that can be used for que management. Your customers will not be bored with this cue management.
With outstanding features, this application allow people in a que to chat with one another while also receiving real time updates from the teller. A list of all features is below. This is a fork of a project by **[Delyce Twizeyimana](https://github.com/Delyc)** . Let me give credit where they are due and check out the original work **[linked here](https://github.com/Delyc/customer_queue_management_django)**

## Deployment
This project has been deployed on heroku. Check the link below to test the features.
- [Heroku Project](https://customer-que-management.herokuapp.com)

## Technologies
- Django (Python web framework)
- Redis
- Django channels
- HTML CSS 
- Javascript
- jQuery

## Features:
- Real time chat 
- Real time updates for all customers waiting for the same teller
## Getting started at local development
To get you up and running on your laptop. Check the pre-requisites and the commands.
### Pre-requisites
To use and develop upon this project, you need to have a good understanding of the technologies used. This project is for advanced beginners. All documentations I believe to be helpful will be linked below but for now these is what you need
- Django - Intermediate
- HTML-CSS-JS - Intermediate
- Docker - Have it installed
- Redis - Beginner
- Heroku - If you will need to deploy

### Instructions
These instructions are written to allow you to copy and paste them and get started. Each command will be explained afterward.
Assuming you have **Git, Docker, Python** installed. Open the terminal and change to the folder you want save the project.
```
git clone https://github.com/feyton/que_manager.git
cd que_manager
python -m venv env
cd env
.\Scripts\activate
cd ..
python -m pip install --upgrade pip
pip install -r requirements.txt
docker run --name redis-server -p 6379:6379 -d redis
python manage.py migrate
python manage.py runserver
// Follow the link in your terminal
```
From command **`4 to 6`** these are system dependent. 
The other command would be about launching a docker container to run redis. **Redis** is required to use channels.

## How to contribute
Just start by forking the project

## About author
[Fabrice Hafashimana](https://github.com/feyton)- A happy traveller and a software developer by passion. If you see me around, say hi and we can talk tech over a cup of coffee. 
Remember to follow me on my socials.

### Resources/ Debugging/ Documentation
- [Django channels](https://channels.readthedocs.io/en/stable/)

<footer>

Good things come to those who never stop dreaming.

</footer>