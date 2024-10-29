import nox
from nox.sessions import Session


@nox.session(name="ruff", reuse_venv=True, python="3.12")
def ruff(session: Session) -> None:
    """Run ruff to perform static code analysis."""
    deps = ["ruff"]
    for dep in deps:
        session.install(dep)

    session.run("ruff", "check", "pysortlib", "tests", "noxfile.py", silent=True)


@nox.session(name="mypy", reuse_venv=True, python="3.12")
def mypy(session: Session) -> None:
    """Run mypy to perform static type checking."""
    deps = ["mypy"]
    for dep in deps:
        session.install(dep)

    session.run("mypy", "pysortlib", "tests", "noxfile.py", silent=True)


@nox.session(name="pytest", reuse_venv=True, python="3.12")
def pytest(session: Session) -> None:
    """Run pytest to execute unit tests."""
    deps = ["hypothesis", "pytest", "pytest-cov", "pytest-rich"]
    for dep in deps:
        session.install(dep)

    session.run("pytest", "--cov", "--rich")
    session.run("coverage", "report")
