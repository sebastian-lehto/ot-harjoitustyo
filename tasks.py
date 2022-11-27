from invoke import task
import sys 

pty = sys.platform != 'win32'

@task
def start(ctx):
    ctx.run("python3 src/index.py", pty=pty)

@task
def test(ctx):
    ctx.run("pytest src", pty=pty)

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest", pty=pty)

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=pty)
