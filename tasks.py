from invoke import task


@task
def ps(c):
    table = 'table {{.Names}}\t{{.Ports}}\t{{.Status}}'
    execute(c, f'docker ps --format="{table}"')


@task
def down(c):
    execute(c, 'docker-compose down')


@task(post=[ps])
def deploy(c):
    execute(c, 'docker-compose up -d --build')


@task(pre=[down], post=[ps])
def redeploy(c):
    deploy(c)


@task
def up_mongo(c):
    execute(c, 'docker-compose up -d --build mongo mongo-express')


@task(pre=[up_mongo])
def tests(c):
    execute(c, 'nosetests --with-coverage')


def execute(c, *commands):
    commands = ' &&'.join(commands)
    c.run(f'export $(cat .env | xargs echo) && {commands}')
