import nox
from nox.sessions import Session

nox.options.reuse_venv = "always"


@nox.session(python="3.13")
def ruff(session: Session) -> None:
    """Run ruff to perform static code analysis."""
    deps = ["ruff"]
    session.install(*deps)
    session.run("ruff", "check", "pysortlib", "tests", "noxfile.py", silent=True)


@nox.session(python="3.13")
def mypy(session: Session) -> None:
    """Run mypy to perform static type checking."""
    deps = ["mypy"]
    session.install(*deps)
    session.run("mypy", "pysortlib", "tests", "noxfile.py", silent=True)


@nox.session(python="3.13")
def pytest(session: Session) -> None:
    """Run pytest to execute unit tests."""
    deps = ["hypothesis", "pytest", "pytest-cov", "pytest-rich"]
    session.install(*deps)
    session.run("pytest", "--cov", "--rich")
    session.run("coverage", "report")
