from app.utils.db_actions import finish_user


async def find_messages(client, message):
    async for found_message in client.search_messages(
        message.from_user.id, from_user="me"
    ):
        if any(
            stop_word in found_message.text.lower()
            for stop_word in ["прекрасно", "ожидать"]
        ):
            await finish_user(message.from_user.id)
            return True
