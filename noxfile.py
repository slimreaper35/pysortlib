import nox
from nox.sessions import Session

nox.options.reuse_venv = "always"


def _sync_dependencies(session: Session) -> None:
    session.run("uv", "sync", "--active", "--all-groups", silent=True)


@nox.session(python="3.13")
def ruff(session: Session) -> None:
    """Run ruff to perform static code analysis."""
    _sync_dependencies(session)
    session.run("ruff", "check", "src/pysortlib", "tests", "noxfile.py", silent=True)


@nox.session(python="3.13")
def ty(session: Session) -> None:
    """Run mypy to perform static type checking."""
    _sync_dependencies(session)
    session.run("ty", "check", "src/pysortlib", "tests", "noxfile.py", silent=True)


@nox.session(python="3.13")
def pytest(session: Session) -> None:
    """Run pytest to execute unit tests."""
    _sync_dependencies(session)
    session.run("pytest", "--cov", "--rich")
    session.run("coverage", "report")
