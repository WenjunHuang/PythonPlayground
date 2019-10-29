import collections
import dependency_injector.providers as providers

CreditCard = collections.namedtuple('CreditCard', [])
Photo = collections.namedtuple('Photo', [])
User = collections.namedtuple('User', ['uid', 'main_photo', 'credit_card'])

# User, Photo and CreditCard factories:
credit_cards_factory = providers.Factory(CreditCard)
photos_factory = providers.Factory(Photo)
users_factory = providers.Factory(User, main_photo=photos_factory, credit_card=credit_cards_factory)

user1 = users_factory(1)
user2 = users_factory(2)

main_photo = Photo()
credit_card = CreditCard()
user3 = users_factory(3, main_photo=main_photo, credit_card=credit_card)
