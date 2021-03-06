"""users added

Revision ID: d0766a2c62ff
Revises: 16c07dab1a38
Create Date: 2021-03-25 12:08:35.794606

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd0766a2c62ff'
down_revision = '16c07dab1a38'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('newsfeed',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('post', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('NewsFeed')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('NewsFeed',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"NewsFeed_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('username', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('post', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='NewsFeed_pkey')
    )
    op.drop_table('newsfeed')
    # ### end Alembic commands ###
