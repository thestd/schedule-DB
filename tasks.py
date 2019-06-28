from invoke import run, task


@task
def ps(c):
    run('docker ps --format="table {{.Names}}\t{{.Ports}}\t{{.Status}}"')


@task(post=[ps])
def local_deploy(c):
    print('Local deploy running...')
    execute('docker-compose up -d --build')


@task
def up_mongo(c):
    execute('docker-compose up -d --build mongo mongo-express')


@task
def down(c):
    execute('docker-compose down')


@task(pre=[up_mongo])
def tests(c):
    execute('nosetests --with-coverage')


def execute(*commands):
    commands = ' &&'.join(commands)
    run(f'export $(cat .env | xargs echo) && {commands}')
