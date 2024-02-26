import requests
from config import BASE_URL
from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton

verify = Router()


class UserReg(StatesGroup):
    user_data = State()


@verify.message(CommandStart())
async def start(msg: Message):
    opt_btn = [
        InlineKeyboardButton(text='Получить токен', callback_data='opt_token'),
        InlineKeyboardButton(text='Регистрация', callback_data='opt_reg')
    ]
    opt_builder = InlineKeyboardBuilder().row(*opt_btn, width=1)
    await msg.answer(
        text='Выберите опцию',
        reply_markup=opt_builder.as_markup()
    )


@verify.callback_query(F.data.startswith("opt_"))
async def opt_action(call: CallbackQuery, state: FSMContext):
    call_data = call.data.split("_")[1]
    if call_data == 'token':
        token = requests.get(f'{BASE_URL}/checkToken?tg_id={call.from_user.id}')
        if token.json() == "404":
            opt_builder = InlineKeyboardBuilder().row(
                InlineKeyboardButton(text='Регистрация', callback_data='opt_reg'), width=1)

            await call.message.answer(
                text='К сожалению, мы не смогли найти Вас в базе. Попробуйте зарегистрироваться',
                reply_markup=opt_builder.as_markup()
            )
        elif token.json() == "200":
            await call.message.answer(
                text=f'Ваш токен:\n<code>{token}</code>'
            )

    elif call_data == 'reg':
        await state.set_state(UserReg.user_data)
        await call.message.answer(
            text='Отправьте Ваш username, email и пароль через запятую\n\nПример:\nAlex, Alex@mail.com, 1234'
        )

    await call.answer()


@verify.message(UserReg.user_data)
async def registration(msg: Message, state: FSMContext):
    tg_id = msg.from_user.id
    user_data_list = msg.text.split(",")
    user_data = {
        "username": user_data_list[0],
        "email": user_data_list[1],
        "password": user_data_list[2],
        "tg_id": tg_id
    }
    register = requests.post(f"{BASE_URL}/register", json=user_data)
    if register.json() == "200":
        token = requests.get(f"{BASE_URL}/getToken?tg_id={str(tg_id)}")
        await msg.answer(
            text=f'{user_data_list[0]}, Вы успешно зарегистрированы!\n\nВаш токен:\n<code>{token.json()}</code>'
        )
    elif register.json() == "404":
        await msg.answer(
            text=f'REGISTRATION FAILED!'
        )
    await state.clear()
