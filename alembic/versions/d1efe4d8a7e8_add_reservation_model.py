"""Add Reservation model

Revision ID: d1efe4d8a7e8
Revises: de224590c4d9
Create Date: 2023-04-29 16:02:03.021949

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd1efe4d8a7e8'
down_revision = 'de224590c4d9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reservation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('from_reserve', sa.DateTime(), nullable=True),
    sa.Column('to_reserve', sa.DateTime(), nullable=True),
    sa.Column('meetingroom_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['meetingroom_id'], ['meetingroom.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reservation')
    # ### end Alembic commands ###