from os import environ as env

from fabric import Connection
from fabric import task


@task
def staging(ctx):
    ctx.user = env['SSH_USER']
    ctx.host = env['SSH_HOST']
    ctx.connect_kwargs.key_filename = env['SSH_KEY_FILENAME']


@task
def deploy(ctx):
    with remote_connection(ctx) as c:
        with c.cd('~/'):
            c.run('ls ../')


def remote_connection(ctx):
    return Connection(host=ctx.host, user=ctx.user,
                      connect_kwargs=ctx.connect_kwargs)
