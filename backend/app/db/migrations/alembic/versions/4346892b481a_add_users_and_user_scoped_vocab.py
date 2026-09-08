"""add users and user-scoped vocab

Revision ID: 4346892b481a
Revises: 9387cb18dacb
Create Date: 2026-09-08 14:02:24.319178

"""
from __future__ import annotations

from typing import Sequence, Union
from uuid import uuid4

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '4346892b481a'
down_revision: Union[str, Sequence[str], None] = '9387cb18dacb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def _table_exists(bind, name: str) -> bool:
    return sa.inspect(bind).has_table(name)


def _column_exists(bind, table: str, column: str) -> bool:
    return column in {c['name'] for c in sa.inspect(bind).get_columns(table)}


def upgrade() -> None:
    """Create the users table and add user ownership to entries and vocab."""
    bind = op.get_bind()

    if not _table_exists(bind, 'users'):
        op.create_table(
            'users',
            sa.Column('id', sa.Uuid(), nullable=False),
            sa.Column('username', sa.String(), nullable=False),
            sa.Column('email', sa.String(), nullable=False),
            sa.Column('password_hash', sa.String(), nullable=False),
            sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
            sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
            sa.PrimaryKeyConstraint('id'),
            sa.UniqueConstraint('username', name='uq_users_username'),
            sa.UniqueConstraint('email', name='uq_users_email'),
        )

    if not _table_exists(bind, 'entries'):
        raise RuntimeError('entries table must exist before adding user_id foreign key')
    if not _column_exists(bind, 'entries', 'user_id'):
        op.add_column('entries', sa.Column('user_id', sa.Uuid(), nullable=True))
        legacy_user_id = str(uuid4())
        op.execute(
            sa.text(
                "INSERT INTO users (id, username, email, password_hash) VALUES (:id, :username, :email, :password_hash)"
            ),
            {
                'id': legacy_user_id,
                'username': 'legacy_user',
                'email': 'legacy_user@example.com',
                'password_hash': 'legacy-user',
            },
        )
        op.execute(
            sa.text("UPDATE entries SET user_id = :user_id WHERE user_id IS NULL"),
            {'user_id': legacy_user_id},
        )
        op.create_foreign_key('fk_entries_user_id_users', 'entries', 'users', ['user_id'], ['id'])
        op.alter_column('entries', 'user_id', nullable=False)

    if not _table_exists(bind, 'vocab'):
        raise RuntimeError('vocab table must exist before adding user_id foreign key')
    if not _column_exists(bind, 'vocab', 'user_id'):
        op.add_column('vocab', sa.Column('user_id', sa.Uuid(), nullable=True))
        legacy_user_id = bind.execute(sa.text("SELECT id FROM users ORDER BY created_at LIMIT 1")).scalar_one()
        op.execute(
            sa.text("UPDATE vocab SET user_id = :user_id WHERE user_id IS NULL"),
            {'user_id': legacy_user_id},
        )
        op.create_foreign_key('fk_vocab_user_id_users', 'vocab', 'users', ['user_id'], ['id'])
        op.alter_column('vocab', 'user_id', nullable=False)

    existing_unique = [constraint['name'] for constraint in sa.inspect(bind).get_unique_constraints('vocab')]
    if 'uq_user_dict_form_reading' not in existing_unique:
        op.create_unique_constraint(
            'uq_user_dict_form_reading',
            'vocab',
            ['user_id', 'dict_form', 'reading'],
        )


def downgrade() -> None:
    """Remove the user-owned schema additions in reverse order."""
    bind = op.get_bind()

    existing_unique = [constraint['name'] for constraint in sa.inspect(bind).get_unique_constraints('vocab')]
    if 'uq_user_dict_form_reading' in existing_unique:
        op.drop_constraint('uq_user_dict_form_reading', 'vocab', type_='unique')

    if 'user_id' in [c['name'] for c in sa.inspect(bind).get_columns('vocab')]:
        op.drop_constraint('fk_vocab_user_id_users', 'vocab', type_='foreignkey')
        op.drop_column('vocab', 'user_id')
    if 'user_id' in [c['name'] for c in sa.inspect(bind).get_columns('entries')]:
        op.drop_constraint('fk_entries_user_id_users', 'entries', type_='foreignkey')
        op.drop_column('entries', 'user_id')
    if _table_exists(bind, 'users'):
        op.drop_table('users')
