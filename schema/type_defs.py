type_defs = '''
type Query {
    getPost(id: ID!): Post!
    getPosts: [Post!]!
    getUser(id: ID!): User!
    getUsers: [User!]!
}

type Mutation {
    addUser(name: String!): User!
    addPost(user_id: ID!, title: String!, body: String!): Post!
    deleteUser(id: ID!): Boolean!
    updatePost(id: ID!, title: String, body: String): Post!
    deletePost(id: ID!): Boolean!
}

type User {
    id: ID!
    name: String!
    posts: [Post!]!
}

type Post {
    id: ID
    title: String
    body: String
    user: User
}

'''