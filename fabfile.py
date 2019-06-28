import json
from os import environ as env

from fabric import Connection
from fabric import task

REPO_NAME = 'schedule-DB'
REPO_URL = f'https://github.com/thestd/{REPO_NAME}'

APPS_ROOT = '~/application'
PROJECT_ROOT = f'{APPS_ROOT}/{REPO_NAME}'


@task
def staging(ctx):
    ctx.user = env['SSH_USER']
    ctx.host = env['SSH_HOST']
    ctx.connect_kwargs.key_filename = env['SSH_KEY_FILENAME']


@task
def deploy(ctx, webhook_data):
    data = json.loads(webhook_data)
    if should_to_deploy(data):
        print('Run deploy process...')
        run_deploy(ctx, data)
    else:
        print('Skip deploy process...')


def should_to_deploy(data):
    action = data['action']
    prerelease = data['release']['prerelease']
    draft = data['release']['draft']
    return (action == 'published'
            and not prerelease
            and not draft)


def run_deploy(ctx, data):
    with remote_connection(ctx) as c:
        prepare(c)
        with c.cd(PROJECT_ROOT):
            tag = data['release']['tag_name']
            deploy_process(c, tag)


def prepare(c):
    c.run(f'mkdir -p {APPS_ROOT}')
    with c.cd(APPS_ROOT):
        c.run(f'if [ ! -d {PROJECT_ROOT} ] ; then git clone {REPO_URL}; fi')


def deploy_process(c, tag):
    c.run('git fetch --all --tags --prune --prune-tags --progress')
    c.run(f'git checkout -f tags/{tag} -B release/{tag}')
    c.run(f'inv local-deploy')


def remote_connection(ctx):
    return Connection(host=ctx.host, user=ctx.user,
                      connect_kwargs=ctx.connect_kwargs)
