"""initial schema

Revision ID: 0c79669e0a14
Revises: 
Create Date: 2026-08-24 15:22:50.404437

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '0c79669e0a14'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def _table_exists(bind, name: str) -> bool:
    return sa.inspect(bind).has_table(name)


def upgrade() -> None:
    """Create the base journal tables if they do not already exist."""
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
    """Drop the base journal tables if they exist."""
    bind = op.get_bind()
    if _table_exists(bind, 'vocab'):
        op.drop_table('vocab')
    if _table_exists(bind, 'entries'):
        op.drop_table('entries')
