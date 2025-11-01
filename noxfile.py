import nox
from nox.sessions import Session

nox.options.reuse_venv = "always"


@nox.session(python="3.13")
def ruff(session: Session) -> None:
    """Run ruff to perform static code analysis."""
    session.run("uv", "sync", "--active")
    session.run("ruff", "check", "src/pysortlib", "tests", "noxfile.py", silent=True)


@nox.session(python="3.13")
def mypy(session: Session) -> None:
    """Run mypy to perform static type checking."""
    session.run("uv", "sync", "--active")
    session.run("mypy", "src/pysortlib", "tests", "noxfile.py", silent=True)


@nox.session(python="3.13")
def pytest(session: Session) -> None:
    """Run pytest to execute unit tests."""
    session.run("uv", "sync", "--active")
    session.run("pytest", "--cov", "--rich")
    session.run("coverage", "report")
