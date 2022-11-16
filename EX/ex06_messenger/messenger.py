"""Messenger."""


class User:
    """User class."""

    def __init__(self, name):
        """AAAA."""
        self.name = name


class Chat:
    """Chat class."""

    def __init__(self, name, users):
        """AAAA."""
        self.name = name
        self.users = users
        self.messages = []


class Message:
    """Message class."""

    def __init__(self, user, content):
        """AAAA."""
        self.user = user
        self.content = content
        self.reactions = 0


def write_message(user: User, chat: Chat, content: str) -> None:
    """AAAA."""
    if user in chat.users:
        msg = Message(user, content)
        chat.messages.append(msg)

    pass


def get_messages_by_user(user: User, chat: Chat) -> list:
    """AAAA."""
    reslist = []
    for message in chat.messages:
        if user == message.user:
            reslist.append(message)
    print(reslist)

    return reslist


def delete_message(chat: Chat, message: Message) -> None:
    """AAAA."""
    msgcont_list = []
    for msg in chat.messages:
        msgcont_list.append(msg.content)
    for i in msgcont_list:
        if message.content == i:
            indx = msgcont_list.index(i)
            msgcont_list.pop(indx)
            chat.messages.pop(indx)

    pass


def react_to_last_message(chat: Chat) -> None:
    """AAAA."""
    if chat.messages:
        chat.messages[-1].reactions += 1

    pass


def find_most_reacted_message(chat: Chat) -> Message:
    """AAAA."""
    for k, v in enumerate(chat.messages):
        sortedmsgs = sorted(chat.messages, key=lambda x: (v, k))

    return sortedmsgs[-1]


def count_reactions_in_chat(chat: Chat) -> int:
    """AAAA."""
    result = 0
    for msgs in chat.messages:
        result += msgs.reactions

    return result


def count_reactions_by_chat(chats: list) -> dict:
    """AAAA."""
    res_dict = {}
    for c in chats:
        res_dict[c.name] = count_reactions_in_chat(c)

    return res_dict
