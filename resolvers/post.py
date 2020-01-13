from ariadne import ObjectType
from services.user import get_user

post = ObjectType('Post')


@post.field('user')
def resolve_user(post_obj, info):
    user_id = post_obj['user_id']
    return get_user(user_id)


@post.field('id')
def resolve_post_id(post_obj, info):
    return str(post_obj['_id'])
