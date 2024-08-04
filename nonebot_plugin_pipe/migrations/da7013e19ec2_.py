"""empty message

迁移 ID: da7013e19ec2
父迁移:
创建时间: 2024-08-04 20:27:56.264169

"""

from __future__ import annotations

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "da7013e19ec2"
down_revision: str | Sequence[str] | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade(name: str = "") -> None:
    if name:
        return
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "nonebot_plugin_pipe_message",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("message_id", sa.Uuid(), nullable=False),
        sa.Column("src", sa.String(), nullable=False),
        sa.Column("src_id", sa.String(), nullable=False),
        sa.Column("user_id", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_nonebot_plugin_pipe_message")),
        info={"bind_key": "nonebot_plugin_pipe"},
    )
    # ### end Alembic commands ###


def downgrade(name: str = "") -> None:
    if name:
        return
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("nonebot_plugin_pipe_message")
    # ### end Alembic commands ###
