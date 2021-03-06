"""empty message

Revision ID: 738b48d818a8
Revises: aa78a0f129e9
Create Date: 2020-05-27 22:07:37.667836

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '738b48d818a8'
down_revision = 'aa78a0f129e9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('questions_total', sa.Integer(), nullable=False),
    sa.Column('questions_won', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('questions', sa.Column('answer_attempt_count', sa.Integer(), default=0))
    op.add_column('questions', sa.Column('answer_success_count', sa.Integer(), default=0))

    op.execute("UPDATE questions SET answer_attempt_count = 0")
    op.execute("UPDATE questions SET answer_success_count = 0")

    op.alter_column('questions', sa.Column('answer_attempt_count', nullable=False))
    op.alter_column('questions', sa.Column('answer_success_count', nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('questions', 'answer_success_count')
    op.drop_column('questions', 'answer_attempt_count')
    op.drop_table('users')
    # ### end Alembic commands ###
