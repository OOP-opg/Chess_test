"""
Users handler module
"""

from history import History
from user import User
from storage import Storage


class UsersHandler:
    storage: Storage

    def __init__(self, storage: Storage):
        self.storage = storage

    def register_user(self, registration_data):
        pass

    def delete_user(self, user_id):
        self.storage.delete_user(user_id)

    def edit_user_meta(self, user_id, delta):
        self.storage.edit_user(user_id, delta)

    def get_user(self, user_id):
        user: User = User(self.storage.get_user(user_id))
        return user
