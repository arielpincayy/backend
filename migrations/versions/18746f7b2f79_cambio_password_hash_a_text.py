"""Cambio password_hash a Text

Revision ID: 18746f7b2f79
Revises: 575c9ec211c5
Create Date: 2025-06-18 04:00:05.892210

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18746f7b2f79'
down_revision = '575c9ec211c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('published', sa.Boolean(), nullable=True))

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('password_hash',
               existing_type=sa.VARCHAR(length=128),
               type_=sa.String(length=256),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('password_hash',
               existing_type=sa.String(length=256),
               type_=sa.VARCHAR(length=128),
               existing_nullable=False)

    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.drop_column('published')

    # ### end Alembic commands ###
