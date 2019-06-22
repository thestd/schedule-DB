# Schedule DB

[![Build Status](http://ci.pnu-bot.pp.ua/buildStatus/icon?job=schedule-DB/master)](http://ci.pnu-bot.pp.ua/blue/organizations/jenkins/schedule-DB/activity)
[![Coverage Status](https://coveralls.io/repos/github/thestd/schedule-DB/badge.svg?branch=master)](https://coveralls.io/github/thestd/schedule-DB?branch=master)

Run mongo, mongo-express in docker container
```bash
docker-compose up -d
docker-compose logs -f
```

Add .env file in project root like this:
```.env
DB_NAME=pnu_schedule
DB_USER=user
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=27017
APP_PORT=8086
SECRET=ABCDEF!@#$%#
AUTH_KEY=123456
```
Recommend to install 
[EnvFile](https://plugins.jetbrains.com/plugin/7861-envfile) 
plugin for pycharm

For those who coding only in vim:
```bash
export $(cat .env | xargs echo)
```