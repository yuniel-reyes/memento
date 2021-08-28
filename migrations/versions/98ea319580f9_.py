"""empty message

Revision ID: 98ea319580f9
Revises: ecb8e2b6db54
Create Date: 2021-08-20 19:39:47.029535

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98ea319580f9'
down_revision = 'ecb8e2b6db54'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('title', sa.Text(), nullable=True))
    op.add_column('posts', sa.Column('body', sa.Text(), nullable=True))
    op.add_column('posts', sa.Column('timestamp', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_posts_timestamp'), 'posts', ['timestamp'], unique=False)
    op.drop_column('posts', 'post')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('post', sa.TEXT(), nullable=True))
    op.drop_index(op.f('ix_posts_timestamp'), table_name='posts')
    op.drop_column('posts', 'timestamp')
    op.drop_column('posts', 'body')
    op.drop_column('posts', 'title')
    # ### end Alembic commands ###
