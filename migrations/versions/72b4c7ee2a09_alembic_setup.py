"""alembic setup

Revision ID: 72b4c7ee2a09
Revises: 
Create Date: 2024-04-16 22:04:14.807798

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel



# revision identifiers, used by Alembic.
revision: str = '72b4c7ee2a09'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('hero', sa.Column('power', sqlmodel.sql.sqltypes.AutoString(), nullable=False))
    op.create_index(op.f('ix_hero_age'), 'hero', ['age'], unique=False)
    op.create_index(op.f('ix_hero_name'), 'hero', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_hero_name'), table_name='hero')
    op.drop_index(op.f('ix_hero_age'), table_name='hero')
    op.drop_column('hero', 'power')
    # ### end Alembic commands ###
