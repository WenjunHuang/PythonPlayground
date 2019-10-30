import collections
import dependency_injector.providers as providers

User = collections.namedtuple('User',[])
users_factory = providers.Factory(User)

user1 = users_factory()
user2 = users_factory()