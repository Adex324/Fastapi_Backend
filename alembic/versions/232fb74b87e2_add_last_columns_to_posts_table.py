"""add_last_columns_to_posts_table

Revision ID: 232fb74b87e2
Revises: 3071f65d90ae
Create Date: 2024-12-30 11:31:55.531254

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '232fb74b87e2'
down_revision: Union[str, None] = '3071f65d90ae'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() :
   op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default="TRUE"),)
   op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
  
   pass


def downgrade() :
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
