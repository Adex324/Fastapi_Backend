"""add content column to posts table

Revision ID: 33959ebf4c2d
Revises: cf9a262964ff
Create Date: 2024-12-27 21:07:34.500166

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '33959ebf4c2d'
down_revision: Union[str, None] = 'cf9a262964ff'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() :
    op.add_column('posts', sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() :
    op.drop_column('posts', 'content')
    pass
