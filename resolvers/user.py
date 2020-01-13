from ariadne import ObjectType
from services.post import get_user_posts

user = ObjectType('User')


@user.field('id')
def resolve_user_id(user_obj, info):
    return user_obj['_id']


@user.field('posts')
def resolve_posts(user_obj, info):
    user_id = str(user_obj['_id'])
    return get_user_posts(user_id)
