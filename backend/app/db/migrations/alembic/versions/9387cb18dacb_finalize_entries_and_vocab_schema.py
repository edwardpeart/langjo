"""finalize entries and vocab schema

Revision ID: 9387cb18dacb
Revises: f0c261b01c31
Create Date: 2026-09-07 22:40:37.075551

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '9387cb18dacb'
down_revision: Union[str, Sequence[str], None] = 'f0c261b01c31'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def _table_exists(bind, name: str) -> bool:
    return sa.inspect(bind).has_table(name)


def upgrade() -> None:
    """No-op: the current schema already matches the model definition."""
    bind = op.get_bind()
    if not _table_exists(bind, 'entries') or not _table_exists(bind, 'vocab'):
        raise RuntimeError('Expected entries and vocab tables to exist before finalizing schema')


def downgrade() -> None:
    """Downgrade is intentionally a no-op because this revision is only for schema finalization."""
    pass
