from bluer_agent.chat.messages import List_of_Messages


def test_chat_list_of_messages():
    list_of_messages = List_of_Messages()
    assert isinstance(list_of_messages.messages, list)
