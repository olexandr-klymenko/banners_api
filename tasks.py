"""Project automation routines."""

from invoke import task


@task
def init(ctx):
    ctx.run("pip install --no-cache-dir -r dev-requirements.txt")
    sync(ctx)


@task()
def sync(ctx):
    """Synchronize all dependencies for the virtual environment."""
    ctx.run("pip-sync requirements.txt")
    ctx.run("pip install --no-cache-dir -r dev-requirements.txt")


@task(help={"upgrade-package": "Particular package that should be upgraded"})
def pin(ctx, upgrade_package=None):
    """Compile dependencies and store to requirements.txt."""
    ctx.run(
        f"""
        CUSTOM_COMPILE_COMMAND='inv pin' pip-compile --no-index \
        {"--upgrade-package=" + upgrade_package if upgrade_package else ""}
    """
    )


@task
def black(ctx):
    """Reformat the code."""
    ctx.run("black ./")


@task
def test(ctx, where="tests"):
    """Run tests with default options."""
    ctx.run(f"nosetests -w {where} --with-doctest")


@task
def run(ctx):
    """Run the app in production mode.

    This task can be run from Docker
    """
    ctx.run("uvicorn app.main:app --reload")


@task
def run_dev(ctx):
    """Run the app in production mode.

    This task can be run from Docker
    """
    ctx.run("uvicorn app.main:app --reload")
