# -*- coding utf-8 -*-

import peewee as pw
from secrets import token_hex

db = pw.SqliteDatabase('users.db')


class Users(pw.Model):
    user_id = pw.PrimaryKeyField()
    token = pw.CharField()
    progress = pw.IntegerField()
    try_count = pw.IntegerField()

    class Meta:
        database = db


def create_tables():
    with db:
        db.create_tables([Users])


def get_user(token):
    try:
        user = Users.get(Users.token == token)
    except pw.DoesNotExist:
        return None
    return user


def create_user(token=None):
    if token is None:
        token = token_hex(16)
    if get_user(token) is None:
        user = Users.create(token=token, progress=0, try_count=1)
        db.commit()
        return user


def count_defuse(user):
    q = (Users.update({Users.progress: user.progress + 1}).where(Users.token == user.token))
    q.execute()


def reset_progress(user):
    q = (Users.update({Users.progress: 0, Users.try_count: user.try_count + 1}).where(Users.token == user.token))
    q.execute()


if __name__ == '__main__':
    create_tables()
