import subprocess
import sys


def _run(args):
    command = [sys.executable, "-m", "alembic", *args]
    result = subprocess.run(command, cwd="/home/edward/workspace/langjo")
    raise SystemExit(result.returncode)


def migrate():
    _run(["revision", "--autogenerate", "-m", "migration"])


def upgrade():
    _run(["upgrade", "head"])


def downgrade():
    _run(["downgrade", "-1"])
