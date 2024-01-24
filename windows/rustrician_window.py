import customtkinter as ctk
from PIL import Image
import webbrowser
import pyperclip


class Schemes:
    def __init__(self, text) -> None:
        extra_window = ctk.CTkToplevel()
        extra_window.title('Auto-furnaces')
        extra_window.geometry('500x400')

        image_import = ctk.CTkImage(
            dark_image=Image.open('../images/others/import_xml.png'),
            size=(400, 150)
        )

        text_1 = ctk.CTkLabel(
            master=extra_window,
            text=text,
            height=40,
            width=350,
            font=ctk.CTkFont('Arial', 15, 'bold'),
            fg_color='#3f3f3f',
            text_color='white',
            corner_radius=10,
        )

        text_2 = ctk.CTkLabel(
            master=extra_window,
            text="To open scheme press this site button and there\n click import button to paste data"
        )

        button_link = ctk.CTkButton(
            master=extra_window,
            text='Rician.io',
            command=self.button_link
        )

        text_3 = ctk.CTkLabel(
            master=extra_window,
            text='',
            image=image_import
        )

        button_close = ctk.CTkButton(
            master=extra_window,
            text='Close',
            command=extra_window.destroy
        )

        text_1.pack(pady=20)
        text_2.pack()
        button_link.pack(pady=20)
        text_3.pack()
        button_close.pack(pady=20)

    @classmethod
    def button_link(cls):
        url = 'https://rustrician.io'
        webbrowser.open(url)


def auto_furnaces() -> None:

    with open('../data/xml_data/auto_furnaces.xml', 'r', encoding='utf-8') as file:
        data = file.read()
        pyperclip.copy(data)

    text = '"Auto-furnaces" was copied!'
    Schemes(text=text)


def auto_craft() -> None:

    with open('../data/xml_data/auto_craft.xml', 'r', encoding='utf-8') as file:
        data = file.read()
        pyperclip.copy(data)

    text = '"Auto-craft" was copied!'
    Schemes(text=text)





