from pyrogram_patch.fsm import StatesGroup, StateItem


class VortexStates(StatesGroup):
    first_iteration = StateItem()
    second_iteration = StateItem()
    third_iteration = StateItem()
