import customtkinter as ctk

import utils
from images.CTkImages import (
    image_classical_1, image_placement_1, image_placement_2, image_deep, image_placement_3,
    image_classical_3, image_1x1, image_placement_4, image_placement_5
)
from windows.kiba_1_window import Kiba1
from windows.kiba_2_window import Kiba2
from windows.kiba_3_window import Kiba3
from windows.kiba_4_window import Kiba4
from windows.rustrician_window import auto_furnaces, auto_craft


class TopLeftFrame:

    def __init__(self) -> None:
        self.frame1 = ctk.CTkFrame(
            master=root,
            border_width=1,
            border_color='black',
        )

        text1 = ctk.CTkLabel(
            master=self.frame1,
            text='Press a button to copy parms.',
            pady=10,
            width=100,
            font=('Arial', 10,),
            text_color='white',
        )

        btn1 = ctk.CTkButton(
            master=self.frame1,
            command=utils.under_work_bench,
            text='Under bench',
            font=ctk.CTkFont('Arial', 12, slant='italic'),
            text_color='white',
            border_color='black',
            border_width=1,
            width=100,
            height=20,
        )

        btn2 = ctk.CTkButton(
            master=self.frame1,
            command=utils.trash,
            text='Trash',
            font=ctk.CTkFont('Arial', 12, slant='italic'),
            text_color='white',
            border_color='black',
            border_width=1,
            width=100,
            height=20,
        )
        btn3 = ctk.CTkButton(
            master=self.frame1,
            command=utils.resources,
            text='Recourses',
            font=ctk.CTkFont('Arial', 12, slant='italic'),
            text_color='white',
            border_color='black',
            border_width=1,
            width=100,
            height=20,
        )
        btn4 = ctk.CTkButton(
            master=self.frame1,
            command=utils.ore,
            text='Furnace ore',
            font=ctk.CTkFont('Arial', 12, slant='italic'),
            text_color='white',
            border_color='black',
            border_width=1,
            width=100,
            height=20,
        )

        self.frame1.grid(row=1, column=0, padx=(10, 0), pady=(20, 0), sticky='N')
        text1.pack(pady=(5, 0), padx=20)
        btn1.pack(padx=20, pady=2)
        btn2.pack(padx=20, pady=2)
        btn3.pack(padx=20, pady=2)
        btn4.pack(padx=20, pady=(2, 15))


class RightFrame:

    def __init__(self) -> None:
        self.frame2 = ctk.CTkFrame(
            master=root,
            border_width=1,
            border_color='black',
        )

        text4 = ctk.CTkLabel(
            master=self.frame2,
            text='Houses',
            width=200,
            font=('Arial', 17, 'bold'),
            fg_color='#3f3f3f',
            corner_radius=10,
        )

        text2 = ctk.CTkLabel(
            master=self.frame2,
            text='Press a button to manual.',
            text_color='white',
        )

        btn1frame2 = ctk.CTkButton(
            master=self.frame2,
            command=self.run_kiba_1,
            text='Kiba 1.0',
            font=('Arial', 17),
            text_color='white',
            border_color='black',
            border_width=1,
            width=200,
            height=38,
        )

        btn2frame2 = ctk.CTkButton(
            master=self.frame2,
            command=self.run_kiba_2,
            text='Kiba 2.0',
            font=('Arial', 17),
            text_color='white',
            border_color='black',
            border_width=1,
            width=200,
            height=38,
        )

        btn3frame2 = ctk.CTkButton(
            master=self.frame2,
            command=self.run_kiba_3,
            text='Kiba 3.0',
            font=('Arial', 17),
            text_color='white',
            border_color='black',
            border_width=1,
            width=200,
            height=38,
        )

        btn4frame2 = ctk.CTkButton(
            master=self.frame2,
            command=self.run_1x1,
            text='1x1',
            font=('Arial', 17),
            text_color='white',
            border_color='black',
            border_width=1,
            width=200,
            height=38,
        )

        self.frame2.grid(row=1, column=1, padx=(5, 10), pady=(27, 12), rowspan=2, sticky='N')
        text4.pack(padx=10, pady=(10, 20), side='top')
        text2.pack(pady=(0, 3), side='top')
        btn1frame2.pack(pady=3)
        btn2frame2.pack(pady=3)
        btn3frame2.pack(pady=3)
        btn4frame2.pack(pady=(3, 15))

    @classmethod
    def run_kiba_1(cls) -> None:
        Kiba1(
            name='Kiba 1.0',
            home=image_classical_1,
            placement_image=image_placement_1,
            wood=1678,
            stone=3345,
        )

    @classmethod
    def run_kiba_2(cls) -> None:
        Kiba2(
            name='Kiba 2.0',
            home=image_deep,
            placement_image=image_placement_2,
            wood=2378,
            stone=6195,
        )

    @classmethod
    def run_kiba_3(cls) -> None:
        Kiba3(
            name='Kiba 3.0',
            home=image_classical_3,
            placement_image=image_placement_3,
            wood=3108,
            stone=9405,
        )

    @classmethod
    def run_1x1(cls) -> None:
        Kiba4(
            name='1x1',
            home=image_1x1,
            placement_image=image_placement_4,
            placement_image_2=image_placement_5,
            wood=2943,
            stone=9180,
        )


class BottomLeftFrame:

    def __init__(self) -> None:
        self.frame3 = ctk.CTkFrame(
            master=root,
            border_width=1,
            border_color='black',
        )

        text5 = ctk.CTkLabel(
            master=self.frame3,
            text='Manual about industrial schemes.',
            pady=0,
            width=50,
            font=('Arial', 10,),
            text_color='white',
        )

        btn1frame3 = ctk.CTkButton(
            master=self.frame3,
            command=auto_furnaces,
            text='Auto-furnaces',
            font=ctk.CTkFont('Arial', 12, slant='italic'),
            text_color='white',
            border_color='black',
            border_width=1,
            width=100,
            height=20,
        )

        btn2frame3 = ctk.CTkButton(
            master=self.frame3,
            command=auto_craft,
            text='Auto-craft',
            font=ctk.CTkFont('Arial', 12, slant='italic'),
            text_color='white',
            border_color='black',
            border_width=1,
            width=100,
            height=20,
        )

        btn3frame3 = ctk.CTkButton(
            master=self.frame3,
            # command=,
            text='-',
            font=ctk.CTkFont('Arial', 12, slant='italic'),
            text_color='white',
            border_color='black',
            border_width=1,
            width=100,
            height=20,
        )

        btn4frame3 = ctk.CTkButton(
            master=self.frame3,
            # command=,
            text='-',
            font=ctk.CTkFont('Arial', 12, slant='italic'),
            text_color='white',
            border_color='black',
            border_width=1,
            width=100,
            height=20,
        )

        self.frame3.grid(row=2, column=0, padx=(10, 0), sticky='N')
        text5.pack(pady=(5, 0), padx=12)
        btn1frame3.pack(padx=20, pady=2)
        btn2frame3.pack(padx=20, pady=2)
        btn3frame3.pack(padx=20, pady=2)
        btn4frame3.pack(padx=20, pady=(2, 15))


class BottomText:
    def __init__(self) -> None:
        self.text3 = ctk.CTkLabel(
            master=root,
            text='',
            height=40,
            width=350,
            font=ctk.CTkFont('Arial', 15, 'bold'),
            fg_color='#3f3f3f',
            text_color='white',
            corner_radius=10,
        )

        self.text3.grid(row=3, column=0, padx=30, pady=20, columnspan=2, sticky='S')


ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')

root = ctk.CTk()
root.title('RUST')
root.geometry('418x400+400+200')
root.iconbitmap('images/Conv.icns')

TopLeftFrame()
RightFrame()
BottomLeftFrame()
bottom_text = BottomText()
