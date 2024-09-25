from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from utils.states import From
from keyboards.builders import profile
from keyboards.reply import rmk 

router = Router()

@router.message(Command('profile')) #! перехват командды настройки профиля
async def fill_profile(message: Message, state: FSMContext):
    await state.set_state(From.name)
    await message.answer('Введи свое имя', reply_markup=profile(message.from_user.first_name), resize_keyboard=True)

@router.message(From.name)
async def From_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(From.age)
    await message.answer('Введи свой возраст', reply_markup=rmk)


@router.message(From.age)
async def from_age(message: Message, state: FSMContext):
    if message.text.isdigit() == True:
        await state.update_data(age=message.text)
        await state.set_state(From.sex)
        await message.answer('Выбери пол', reply_markup=profile(['Парень', 'Девушка'])) #! создали кнопки с помощью билдера
    else:
        await message.answer('Введи число еще раз!')

#! тут сразу создали перехват
@router.message(From.sex, F.text.casefold().in_(['парень', 'девушка']))
async def from_sex(message: Message, state: FSMContext):
    await state.update_data(sex=message.text)
    await state.set_state(From.about)
    await message.answer('Расскажи о себе', reply_markup=rmk) #! тут удалили предыдущую клавиатуру - КНОПКИ


#! это если чел даун и не нажмет кнопку
@router.message(From.sex)
async def incorrect_from_sex(message: Message, state: FSMContext):
    await message.answer('Нажмите на кнопку!')


@router.message(From.about)
async def from_about(message: Message, state: FSMContext):
    if len(message.text) < 5:
        await message.answer('Напиши больше о себе!')
    else:
        await state.update_data(about=message.text)
        await state.set_state(From.photo)
        await message.answer('Теперь определимся с фото!')

@router.message(From.photo, F.photo) 
async def from_photo(message: Message, state: FSMContext):
    photo_file_id = message.photo[-1].file_id #* взял фото с лучшим качеством
    data = await state.get_data() #? сохранил все данные как словарь
    await state.clear() #? закончил работу со стейтом

#!  Я тут завершил стейты и мне нужно будет их вывести

    formatted_text = []
    [
        formatted_text.append(f'{key}: {value}')
        for key, value in data.items()
    ]

    await message.answer_photo(
        photo_file_id, 
        '\n'.join(formatted_text)
    )


@router.message(From.photo, ~F.photo)
async def incorrect_from_photo(message: Message, state: FSMContext):
    await message.answer('Отправь фото')
