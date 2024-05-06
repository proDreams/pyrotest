import asyncio

from pyrogram_patch import patch

from app.handlers.vortex_handlers import vortex_router
from app.settings import client, redis_storage


# async def start():
#
#     patch_manager = patch(client)
#     patch_manager.set_storage(redis_storage)
#     patch_manager.include_router(vortex_router)
#
#     await client.start()
#
#     # await asyncio.Event().wait()
#
#
# asyncio.run(start())

patch_manager = patch(client)
patch_manager.set_storage(redis_storage)
patch_manager.include_router(vortex_router)

client.run()
