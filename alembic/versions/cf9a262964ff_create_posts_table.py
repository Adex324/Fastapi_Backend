"""create posts table

Revision ID: cf9a262964ff
Revises: 
Create Date: 2024-12-27 14:35:06.730896

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cf9a262964ff'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() :
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable =False, primary_key=True), sa.Column('title', sa.String(),nullable=False))
    pass


def downgrade() :
    op.drop_table('posts')
    pass
