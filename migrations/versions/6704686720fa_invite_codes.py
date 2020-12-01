"""invite codes

Revision ID: 6704686720fa
Revises: c77061c72a59
Create Date: 2020-11-06 13:17:45.111761

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "6704686720fa"
down_revision = "c77061c72a59"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "invite_code",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("date_created", sa.DateTime(), nullable=True),
        sa.Column("date_modified", sa.DateTime(), nullable=True),
        sa.Column("code", sa.String(length=36), nullable=False),
        sa.Column("description", sa.String(length=255), nullable=False),
        sa.Column("remaining_uses", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_invite_code_code"), "invite_code", ["code"], unique=True)
    op.create_table(
        "invite_role",
        sa.Column("invite_id", sa.Integer(), nullable=False),
        sa.Column("role_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["invite_id"],
            ["invite_code.id"],
        ),
        sa.ForeignKeyConstraint(
            ["role_id"],
            ["role.id"],
        ),
        sa.PrimaryKeyConstraint("invite_id", "role_id"),
    )
    op.add_column("user", sa.Column("invite_code_id", sa.Integer(), nullable=True))
    op.create_foreign_key(
        "user_ibfk_1", "user", "invite_code", ["invite_code_id"], ["id"]
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("user_ibfk_1", "user", type_="foreignkey")
    op.drop_column("user", "invite_code_id")
    op.drop_table("invite_role")
    op.drop_index(op.f("ix_invite_code_code"), table_name="invite_code")
    op.drop_table("invite_code")
    # ### end Alembic commands ###
