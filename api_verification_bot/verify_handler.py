from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton

from laplayer_api.services.user_service import token_by_username, create_user

verify = Router()


class UserReg(StatesGroup):
    user_data = State()


class User(StatesGroup):
    username = State()


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
        await state.set_state(User.username)
        await call.message.answer(text='Отправьте Ваш username')
    elif call_data == 'reg':
        await state.set_state(UserReg.user_data)
        await call.message.answer(
            text='Отправьте Ваш username, email и пароль через запятую\n\nПример:\nAlex, Alex@mail.com, 1234'
        )

    await call.answer()


@verify.message(User.username)
async def return_token(msg: Message, state: FSMContext):
    token = token_by_username(msg.text)
    if token is None:
        opt_builder = InlineKeyboardBuilder().row(
            InlineKeyboardButton(text='Регистрация', callback_data='opt_reg'), width=1)

        await msg.answer(
            text='К сожалению, мы не смогли найти Вас в базе. Попробуйте зарегистрироваться',
            reply_markup=opt_builder.as_markup()
        )
    else:
        await msg.answer(
            text=f'Ваш токен:\n<code>{token[0]}</code>'
        )
    await state.clear()


@verify.message(UserReg.user_data)
async def registration(msg: Message, state: FSMContext):
    user_data = msg.text.split(",")
    print(user_data)
    create_user(name=user_data[0], email=user_data[1], password=user_data[2])
    token = token_by_username(username=user_data[0])[0]

    await msg.answer(
        text=f'{user_data[0]}, Вы успешно зарегистрированы!\n\nВаш токен:\n<code>{token}</code>'
    )
    await state.clear()
