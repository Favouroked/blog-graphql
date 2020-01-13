from ariadne import ObjectType
from services.post import get_post, get_posts
from services.user import get_user, get_users

query = ObjectType('Query')


@query.field('getPost')
def resolve_get_post(*_, id):
    return get_post(id)


@query.field('getPosts')
def resolve_get_posts(*_):
    return get_posts()


@query.field('getUser')
def resolve_get_user(*_, id):
    return get_user(id)


@query.field('getUsers')
def resolve_get_users(*_):
    return get_users()
