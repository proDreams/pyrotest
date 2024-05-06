import asyncio

from pyrogram import filters, Client
from pyrogram.types import Message
from pyrogram_patch.fsm import State
from pyrogram_patch.fsm.filter import StateFilter
from pyrogram_patch.router import Router

from app.states.vortex_states import VortexStates
from app.utils.db_actions import get_or_create_user, finish_user
from app.utils.messages import find_messages

vortex_router = Router()


@vortex_router.on_message(filters.private & StateFilter())
async def first_iteration(client: Client, message: Message, state: State):
    if message.outgoing:
        return

    user = await get_or_create_user(message.from_user.id)
    if user.status == "dead" or user.status == "finished":
        await state.finish()
        return

    await asyncio.sleep(1 * 60)
    await message.reply("Ответ на первое сообщение спустя 6 минут.")
    await state.set_state(VortexStates.second_iteration)


@vortex_router.on_message(filters.private & StateFilter(VortexStates.second_iteration))
async def second_iteration(client: Client, message, state: State):
    if await find_messages(client, message):
        await state.finish()
        return
    await asyncio.sleep(1 * 60)
    await client.send_message(
        message.chat.id, "Ответ на второе сообщение спустя 39 минут."
    )
    await state.set_state(VortexStates.third_iteration)


@vortex_router.on_message(filters.private & StateFilter(VortexStates.third_iteration))
async def third_iteration(client: Client, message, state: State):
    if await find_messages(client, message):
        await state.finish()
        return
    await asyncio.sleep(1 * 60)
    await client.send_message(
        message.chat.id,
        "Ответ на второе сообщение спустя 1 день и 2 часа.",
    )
    await finish_user(message.from_user.id)
    await state.finish()
