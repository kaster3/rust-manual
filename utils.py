import pyperclip

from windows import main_window


def under_work_bench() -> None:
    copy_data(name='work_bench.json')
    main_window.bottom_text.text3.configure(text='"Under bench" was copied successfully!')


def resources() -> None:
    copy_data(name='resources.json')
    main_window.bottom_text.text3.configure(text='"Recourses" was copied successfully!')


def ore() -> None:
    copy_data(name='ore.json')
    main_window.bottom_text.text3.configure(text='"Furnace ore" was copied successfully!')


def trash() -> None:
    copy_data(name='trash.json')
    main_window.bottom_text.text3.configure(text='"Trash" was copied successfully!')


def copy_data(name: str) -> None:
    with open('data/json_data/' + name, 'r', encoding='utf-8') as file:
        data = file.read()
        pyperclip.copy(data)


