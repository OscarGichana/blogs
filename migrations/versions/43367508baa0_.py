""".

Revision ID: 43367508baa0
Revises: 1f679b541154
Create Date: 2021-03-08 22:45:05.710909

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '43367508baa0'
down_revision = '1f679b541154'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_subscribers_email', table_name='subscribers')
    op.drop_table('subscribers')
    op.drop_table('post_like')
    op.drop_table('comments')
    op.add_column('posts', sa.Column('name', sa.String(), nullable=True))
    op.add_column('posts', sa.Column('post', sa.String(), nullable=True))
    op.add_column('posts', sa.Column('title', sa.String(), nullable=True))
    op.drop_column('posts', 'upvotes')
    op.drop_column('posts', 'posted_at')
    op.drop_column('posts', 'downvotes')
    op.drop_column('posts', 'post_content')
    op.drop_column('posts', 'post_title')
    op.drop_column('posts', 'post_by')
    op.add_column('users', sa.Column('pass_secure', sa.String(length=255), nullable=True))
    op.drop_constraint('users_username_key', 'users', type_='unique')
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=False)
    op.drop_column('users', 'bio')
    op.drop_column('users', 'last_name')
    op.drop_column('users', 'first_name')
    op.drop_column('users', 'avatar_path')
    op.drop_column('users', 'password_hash')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_hash', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('avatar_path', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('first_name', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('last_name', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('bio', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.create_unique_constraint('users_username_key', 'users', ['username'])
    op.drop_column('users', 'pass_secure')
    op.add_column('posts', sa.Column('post_by', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('posts', sa.Column('post_title', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('posts', sa.Column('post_content', sa.TEXT(), autoincrement=False, nullable=True))
    op.add_column('posts', sa.Column('downvotes', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('posts', sa.Column('posted_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column('posts', sa.Column('upvotes', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('posts', 'title')
    op.drop_column('posts', 'post')
    op.drop_column('posts', 'name')
    op.create_table('comments',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('comment', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('comment_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('comment_by', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('like_count', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('post_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], name='comments_post_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='comments_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='comments_pkey')
    )
    op.create_table('post_like',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('post_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], name='post_like_post_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='post_like_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='post_like_pkey')
    )
    op.create_table('subscribers',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='subscribers_pkey')
    )
    op.create_index('ix_subscribers_email', 'subscribers', ['email'], unique=True)
    # ### end Alembic commands ###
