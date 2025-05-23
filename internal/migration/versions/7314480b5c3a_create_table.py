"""create_table

Revision ID: 7314480b5c3a
Revises: 
Create Date: 2025-04-17 23:18:08.319998

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '7314480b5c3a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('app', schema=None) as batch_op:
        batch_op.drop_index('idx_app_account_id')

    op.drop_table('app')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('app',
    sa.Column('id', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('account_id', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=200), autoincrement=False, nullable=False),
    sa.Column('icon', sa.VARCHAR(length=200), autoincrement=False, nullable=False),
    sa.Column('description', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('update_time', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('create_time', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='pk_app_id')
    )
    with op.batch_alter_table('app', schema=None) as batch_op:
        batch_op.create_index('idx_app_account_id', ['account_id'], unique=False)

    # ### end Alembic commands ###
