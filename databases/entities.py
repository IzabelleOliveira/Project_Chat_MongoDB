#classes User e Message
class User:
    def __init__(self,
                 nickname:str,
                 password:str,
                 email:str,):
        self.nickname = nickname
        self.email = email
        self.password = password

class Message:
    def __init__(self,
                 nickname_from:str,
                 nickname_to:str,
                 message:str):
        self.nickname_from = nickname_from
        self.nickname_to = nickname_to
        self.message = message