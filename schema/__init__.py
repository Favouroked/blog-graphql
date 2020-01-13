from ariadne import make_executable_schema

from .type_defs import type_defs
from resolvers.mutations import mutations
from resolvers.queries import query
from resolvers.post import post
from resolvers.user import user

schema = make_executable_schema(type_defs, query, post, user, mutations)
