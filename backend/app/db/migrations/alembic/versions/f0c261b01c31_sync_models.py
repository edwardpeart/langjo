"""sync models

Revision ID: f0c261b01c31
Revises: 0c79669e0a14
Create Date: 2026-08-25 12:14:27.975960

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f0c261b01c31'
down_revision: Union[str, Sequence[str], None] = '0c79669e0a14'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def _table_exists(bind, name: str) -> bool:
    return sa.inspect(bind).has_table(name)


def upgrade() -> None:
    """Ensure the final journal schema exists without recreating what is already there."""
    bind = op.get_bind()
    if not _table_exists(bind, 'entries'):
        op.create_table(
            'entries',
            sa.Column('id', sa.Integer(), nullable=False),
            sa.Column('body', sa.String(), nullable=False),
            sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
            sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
            sa.PrimaryKeyConstraint('id'),
        )
    if not _table_exists(bind, 'vocab'):
        op.create_table(
            'vocab',
            sa.Column('id', sa.Integer(), nullable=False),
            sa.Column('dict_form', sa.String(), nullable=False),
            sa.Column('reading', sa.String(), nullable=False),
            sa.Column('entry_id', sa.Integer(), nullable=True),
            sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
            sa.ForeignKeyConstraint(['entry_id'], ['entries.id']),
            sa.PrimaryKeyConstraint('id'),
            sa.UniqueConstraint('dict_form', 'reading', name='uq_dict_form_reading'),
        )


def downgrade() -> None:
    """Drop the journal tables if the migration is rolled back."""
    bind = op.get_bind()
    if _table_exists(bind, 'vocab'):
        op.drop_table('vocab')
    if _table_exists(bind, 'entries'):
        op.drop_table('entries')
