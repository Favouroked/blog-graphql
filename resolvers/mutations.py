from ariadne import ObjectType
from services.user import add_user, delete_user
from services.post import add_post, update_post, delete_post

mutations = ObjectType('Mutation')


@mutations.field('addUser')
def resolve_add_user(*_, name):
    return add_user(name)


@mutations.field('addPost')
def resolve_add_post(*_, user_id, title, body):
    return add_post(user_id, title, body)


@mutations.field('deleteUser')
def resolve_delete_user(*_, id):
    return delete_user(id)


@mutations.field('updatePost')
def resolve_update_post(*_, id, **update):
    return update_post(id, update)


@mutations.field('deletePost')
def resolve_delete_post(*_, id):
    return delete_post(id)
