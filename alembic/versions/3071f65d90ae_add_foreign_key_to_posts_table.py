"""add foreign-key to posts table

Revision ID: 3071f65d90ae
Revises: a6174a8ead0b
Create Date: 2024-12-30 11:25:14.035641

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3071f65d90ae'
down_revision: Union[str, None] = 'a6174a8ead0b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() :
   op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
   op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=["owner_id"], remote_cols=["id"], ondelete="CASCADE")
   pass

def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column("posts", "owner_id")
    pass