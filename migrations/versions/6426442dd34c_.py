"""empty message

Revision ID: 6426442dd34c
Revises: a93b99e4ead8
Create Date: 2018-05-22 16:36:20.677192

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6426442dd34c'
down_revision = 'a93b99e4ead8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cancer_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Class', sa.String(length=40), nullable=True),
    sa.Column('age', sa.String(length=10), nullable=True),
    sa.Column('menopause', sa.String(length=10), nullable=True),
    sa.Column('tumor_size', sa.String(length=10), nullable=True),
    sa.Column('inv_nodes', sa.String(length=10), nullable=True),
    sa.Column('node_caps', sa.String(length=10), nullable=True),
    sa.Column('deg_malig', sa.Integer(), nullable=True),
    sa.Column('breast', sa.String(length=10), nullable=True),
    sa.Column('breast_quady', sa.String(length=10), nullable=True),
    sa.Column('irradiat', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_index('ix_CancerData_id', table_name='CancerData')
    op.drop_table('CancerData')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('CancerData',
    sa.Column('id', mysql.BIGINT(display_width=20), autoincrement=False, nullable=True),
    sa.Column('Class', mysql.TEXT(), nullable=True),
    sa.Column('age', mysql.TEXT(), nullable=True),
    sa.Column('menopause', mysql.TEXT(), nullable=True),
    sa.Column('tumor_size', mysql.TEXT(), nullable=True),
    sa.Column('inv_nodes', mysql.TEXT(), nullable=True),
    sa.Column('node_caps', mysql.TEXT(), nullable=True),
    sa.Column('deg_malig', mysql.BIGINT(display_width=20), autoincrement=False, nullable=True),
    sa.Column('breast', mysql.TEXT(), nullable=True),
    sa.Column('breast_quad', mysql.TEXT(), nullable=True),
    sa.Column('irradiat', mysql.TEXT(), nullable=True),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('ix_CancerData_id', 'CancerData', ['id'], unique=False)
    op.drop_table('cancer_data')
    # ### end Alembic commands ###
