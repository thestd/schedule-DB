# Schedule DB

[![Build Status](http://ci.pnu-bot.pp.ua/buildStatus/icon?job=schedule-DB%2Fmaster&style=flat-square)](http://ci.pnu-bot.pp.ua/job/schedule-DB/job/master/)
[![Coverage Status](https://coveralls.io/repos/github/thestd/schedule-DB/badge.svg?branch=master)](https://coveralls.io/github/thestd/schedule-DB?branch=master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/7467308c638c4501b30e8c53338a6566)](https://www.codacy.com/app/rostIvan/schedule-DB?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=thestd/schedule-DB&amp;utm_campaign=Badge_Grade)
[![CodeFactor](https://www.codefactor.io/repository/github/thestd/schedule-db/badge/master)](https://www.codefactor.io/repository/github/thestd/schedule-db/overview/master)

Deploy application
```bash
inv deploy
```

Stop containers
```bash
inv down
```

Show running containers
```bash
inv ps
```

Up mongo database for development / tests
```bash
inv up-mongo
```

Run tests
```bash
inv tests
```

Create .env file in project root:
```.env
DB_NAME=pnu_schedule
DB_USER=user
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=27011

TORNADO_PORT=8000

MONGO_EXPRESS_PORT=8083
```

Recommend to install 
[EnvFile](https://plugins.jetbrains.com/plugin/7861-envfile) 
plugin for pycharm
