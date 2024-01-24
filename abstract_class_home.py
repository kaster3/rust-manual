import webbrowser
from abc import ABC, abstractmethod

import customtkinter as ctk
from PIL import Image

from images.CTkImages import (
    image_wooden_door, image_metal_door, image_wooden_double_door, image_metal_double_door,
    image_lock, image_codelock, image_stone, image_metal, image_wood, image_box, image_box_1, image_box_2, image_box_3,
)


class Frame(ABC):

    """
    Абстрактный базовый класс для домов
    """

    def __init__(self, name, home, placement_image, wood, stone) -> None:
        self.name = name
        self.home = home
        self.placement_image = placement_image
        self.wood = wood
        self.stone = stone
        self.metal = 0
        self.wooden_door = 0
        self.double_wooden = 0
        self.metal_door = 0
        self.double_metal = 0
        self.lock = 0
        self.codelock = 0
        self.flag = 'Classical'

        kiba = ctk.CTkToplevel()
        kiba.title(name)
        kiba.geometry('700x800')
        kiba.resizable(False, False)

        self.frame = ctk.CTkScrollableFrame(
            master=kiba,
            width=550,
            height=800,
            border_width=2,
        )

        label_1 = ctk.CTkLabel(
            master=self.frame,
            text='Chose a door',
            width=400,
            height=40,
            corner_radius=10,
            font=ctk.CTkFont('Arial', 20, 'bold', slant='italic'),
            fg_color='#3f3f3f',
        )

        label_2 = ctk.CTkLabel(
            master=self.frame,
            width=200,
            height=40,
            text='Press a picture to choose.',
            font=ctk.CTkFont('Arial', 10, slant='italic'),
        )

        chose_wooden_label = ctk.CTkButton(
            master=self.frame,
            command=self.click_wooden_door,
            text='',
            width=80,
            image=image_wooden_door,
            fg_color='#2a2b2b',
            hover_color='#2f2f2f',
        )

        self.label_for_wooden = ctk.CTkLabel(
            master=self.frame,
            text=f'x 0',
            width=60,
            font=ctk.CTkFont('Arial', 30, 'bold'),
        )

        self.label_for_metal = ctk.CTkLabel(
            master=self.frame,
            text='x 0',
            width=60,
            font=ctk.CTkFont('Arial', 30, 'bold')
        )

        chose_metal_label = ctk.CTkButton(
            master=self.frame,
            command=self.click_metal_door,
            text='',
            width=80,
            image=image_metal_door,
            fg_color='#2a2b2b',
            hover_color='#2f2f2f'
        )

        self.label_for_double_wooden = ctk.CTkLabel(
            master=self.frame,
            text='x 0',
            width=60,
            font=ctk.CTkFont('Arial', 30, 'bold')
        )

        chose_double_wooden_label = ctk.CTkButton(
            master=self.frame,
            command=self.click_double_wooden,
            text='',
            width=80,
            image=image_wooden_double_door,
            fg_color='#2a2b2b',
            hover_color='#2f2f2f'
        )

        self.label_for_double_metal = ctk.CTkLabel(
            master=self.frame,
            text='x 0',
            width=60,
            font=ctk.CTkFont('Arial', 30, 'bold')
        )

        chose_double_metal_label = ctk.CTkButton(
            master=self.frame,
            command=self.click_double_metal,
            text='',
            width=80,
            image=image_metal_double_door,
            fg_color='#2a2b2b',
            hover_color='#2f2f2f'
        )

        label_3 = ctk.CTkLabel(
            master=self.frame,
            width=400,
            height=40,
            corner_radius=10,
            text='Chose a lock',
            font=ctk.CTkFont('Arial', 20, 'bold', slant='italic'),
            fg_color='#3f3f3f',
        )

        self.label_for_lock = ctk.CTkLabel(
            master=self.frame,
            text='x 0',
            width=60,
            font=ctk.CTkFont('Arial', 30, 'bold')
        )

        chose_lock_button = ctk.CTkButton(
            master=self.frame,
            command=self.click_lock,
            text='',
            width=80,
            image=image_lock,
            fg_color='#2a2b2b',
            hover_color='#2f2f2f'
        )

        self.label_for_codelock = ctk.CTkLabel(
            master=self.frame,
            text=f'x {self.codelock}',
            width=60,
            font=ctk.CTkFont('Arial', 30, 'bold')
        )

        chose_codelock_button = ctk.CTkButton(
            master=self.frame,
            command=self.click_codelock,
            text='',
            width=80,
            image=image_codelock,
            fg_color='#2a2b2b',
            hover_color='#2f2f2f'
        )

        label_cost = ctk.CTkLabel(
            master=self.frame,
            width=400,
            height=40,
            corner_radius=10,
            text='Cost',
            font=ctk.CTkFont('Arial', 20, 'bold', slant='italic'),
            fg_color='#3f3f3f',
        )

        self.stone_text = ctk.CTkLabel(
            master=self.frame,
            text=f'x {self.stone}',
            font=ctk.CTkFont('Arial', 30, 'bold', slant='italic'),
        )

        label_stone = ctk.CTkLabel(
            master=self.frame,
            text='',
            image=image_stone,
        )

        label_wood = ctk.CTkLabel(
            master=self.frame,
            text='',
            image=image_wood,
        )

        self.wood_text = ctk.CTkLabel(
            master=self.frame,
            text=f'x {self.wood}',
            font=ctk.CTkFont('Arial', 30, 'bold', slant='italic'),
        )

        self.kiba_name = ctk.CTkLabel(
            master=self.frame,
            width=420,
            height=40,
            corner_radius=10,
            text=name,
            font=ctk.CTkFont('Arial', 20, 'bold', slant='italic'),
            fg_color='#3f3f3f',
        )

        self.image_home = ctk.CTkLabel(
            master=self.frame,
            text='',
            image=home,
        )

        exit_btn = ctk.CTkButton(
            master=self.frame,
            command=lambda: kiba.destroy(),
            text='Okay',
        )

        self.placement_create()

        self.frame.pack(pady=(20, 20))

        label_1.grid(row=0, columnspan=4, pady=(20, 0))
        label_2.grid(row=1, columnspan=4)
        chose_wooden_label.grid(row=2, column=0, sticky='E', padx=(100, 0))
        self.label_for_wooden.grid(row=2, column=1, sticky='W', padx=(0, 50))

        chose_metal_label.grid(row=2, column=2, sticky='E')
        self.label_for_metal.grid(row=2, column=3, padx=(0, 100), sticky='W')
        chose_double_wooden_label.grid(row=3, column=0, sticky='E', padx=(100, 0))
        self.label_for_double_wooden.grid(row=3, column=1, sticky='W', padx=(0, 50))
        chose_double_metal_label.grid(row=3, column=2, sticky='E')
        self.label_for_double_metal.grid(row=3, column=3, padx=(0, 100), sticky='W')

        label_3.grid(row=4, column=0, columnspan=4, pady=(20, 0))
        chose_lock_button.grid(row=5, column=0, sticky='E', padx=(100, 0))
        self.label_for_lock.grid(row=5, column=1, sticky='W', padx=(0, 50))
        chose_codelock_button.grid(row=5, column=2, sticky='E', )
        self.label_for_codelock.grid(row=5, column=3, padx=(0, 100), sticky='W')

        label_cost.grid(row=8, column=0, columnspan=4)
        label_wood.grid(row=9, column=0, columnspan=2, padx=(120, 0))
        self.wood_text.grid(row=9, column=1, columnspan=2, padx=(40, 0))
        label_stone.grid(row=10, column=0, columnspan=2, padx=(120, 0))
        self.stone_text.grid(row=10, column=1, columnspan=2, padx=(40, 0))

        self.kiba_name.grid(row=14, column=0, columnspan=4, pady=(20, 0))
        self.image_home.grid(row=15, column=0, columnspan=4)

        exit_btn.grid(row=25, column=0, columnspan=4, pady=(20, 15))

    @abstractmethod
    def click_lock(self) -> None:
        self.lock += 1
        self.wood += 75
        self.label_for_lock.configure(text=f'x {self.lock}')
        self.wood_text.configure(text=f'x {self.wood}')

    @abstractmethod
    def click_codelock(self) -> None:
        if not self.metal:
            self.metal_placement()
        self.metal += 100
        self.codelock += 1
        self.label_for_codelock.configure(text=f'x {self.codelock}')
        self.metal_text.configure(text=f'x {self.metal}')

    @abstractmethod
    def click_wooden_door(self) -> None:
        self.wooden_door += 1
        self.wood += 300
        self.label_for_wooden.configure(text=f'x {self.wooden_door}')
        self.wood_text.configure(text=f'x {self.wood}')

    @abstractmethod
    def click_metal_door(self) -> None:
        if not self.metal:
            self.metal_placement()
        self.metal += 150
        self.metal_door += 1
        self.label_for_metal.configure(text=f'x {self.metal_door}')
        self.metal_text.configure(text=f'x {self.metal}')

    @abstractmethod
    def click_double_metal(self) -> None:
        if not self.metal:
            self.metal_placement()
        self.double_metal += 1
        self.metal += 200
        self.label_for_double_metal.configure(text=f'x {self.double_metal}')
        self.metal_text.configure(text=f'x {self.metal}')

    @abstractmethod
    def click_double_wooden(self) -> None:
        self.double_wooden += 1
        self.wood += 350
        self.label_for_double_wooden.configure(text=f'x {self.double_wooden}')
        self.wood_text.configure(text=f'x {self.wood}')

    @abstractmethod
    def metal_placement(self) -> None:
        self.label_metal = ctk.CTkLabel(
            master=self.frame,
            text='',
            image=image_metal,
        )

        self.metal_text = ctk.CTkLabel(
            master=self.frame,
            text=f'x {self.metal}',
            font=ctk.CTkFont('Arial', 30, 'bold', slant='italic'),
        )

        self.label_metal.grid(row=11, column=0, columnspan=2, padx=(120, 0))
        self.metal_text.grid(row=11, column=1, columnspan=2, padx=(40, 0))

    @abstractmethod
    def placement_create(self) -> None:
        self.placement_text = ctk.CTkLabel(
            master=self.frame,
            text='The best placement',
            width=420,
            height=40,
            corner_radius=10,
            font=ctk.CTkFont('Arial', 20, 'bold', slant='italic'),
            fg_color='#3f3f3f',
        )

        self.placement = ctk.CTkLabel(
            master=self.frame,
            text='',
            image=self.placement_image,
        )

        self.placement_text.grid(row=22, column=0, columnspan=4, pady=(20, 0))
        self.placement.grid(row=23, column=0, columnspan=4)

    @abstractmethod
    def placement_delete(self) -> None:
        self.placement_text.destroy()
        self.placement.destroy()

    @abstractmethod
    def addition(self, wood: int, stone: int) -> None:
        self.wood += wood
        self.stone += stone

    @abstractmethod
    def subtraction(self, wood: int, stone: int) -> None:
        self.wood -= wood
        self.stone -= stone

    @abstractmethod
    def edition(self, name: str, image: Image) -> None:
        self.flag: str = name
        self.wood_text.configure(text=f'x {self.wood}')
        self.stone_text.configure(text=f'x {self.stone}')
        self.kiba_name.configure(text=name)
        self.image_home.configure(image=image)


class BoxMixin(Frame, ABC):
    def __init__(self, name, home, placement_image, wood, stone) -> None:
        super().__init__(name, home, placement_image, wood, stone)
        self.boxes = 0
        self.image_box_1 = image_box_1
        self.image_box_2 = image_box_2
        self.image_box_3 = image_box_3

        self.video_text = ctk.CTkLabel(
            master=self.frame,
            width=420,
            height=40,
            corner_radius=10,
            text='Stash building manual',
            font=ctk.CTkFont('Arial', 20, 'bold', slant='italic'),
            fg_color='#3f3f3f',
        )

        self.video_text.grid(row=16, column=0, columnspan=4, pady=(20, 0))

    def click_box(self) -> None:
        if not self.metal:
            self.metal_placement()
        self.wood += 250
        self.metal += 50
        self.boxes += 1
        self.label_for_boxes.configure(text=f'x {self.boxes}')
        self.metal_text.configure(text=f'x {self.metal}')
        self.wood_text.configure(text=f'x {self.wood}')

    def create_boxes(self) -> None:

        self.text_boxes = ctk.CTkLabel(
            master=self.frame,
            width=400,
            height=40,
            corner_radius=10,
            text='How many boxes?',
            font=ctk.CTkFont('Arial', 20, 'bold', slant='italic'),
            fg_color='#3f3f3f',
        )

        self.box_button = ctk.CTkButton(
            master=self.frame,
            command=self.click_box,
            text='',
            width=80,
            image=image_box,
            fg_color='#2a2b2b',
            hover_color='#2f2f2f'
        )

        self.label_for_boxes = ctk.CTkLabel(
            master=self.frame,
            text=f'x {self.boxes}',
            width=60,
            font=ctk.CTkFont('Arial', 30, 'bold')
        )

        self.box_explanation = ctk.CTkLabel(
            master=self.frame,
            width=420,
            height=40,
            corner_radius=10,
            text='placement of 4 boxes',
            font=ctk.CTkFont('Arial', 20, 'bold', slant='italic'),
            fg_color='#3f3f3f',
        )

        self.box_1 = ctk.CTkLabel(
            master=self.frame,
            text='',
            image=image_box_1,
        )

        self.box_2 = ctk.CTkLabel(
            master=self.frame,
            text='',
            image=image_box_2,
        )

        self.box_3 = ctk.CTkLabel(
            master=self.frame,
            text='',
            image=image_box_3,
        )

        self.text_boxes.grid(row=6, column=0, columnspan=4)
        self.box_button.grid(row=7, column=0, columnspan=3, padx=(100, 0))
        self.label_for_boxes.grid(row=7, column=1, columnspan=2, padx=(60, 0))

        self.box_explanation.grid(row=18, column=0, columnspan=4, pady=(20, 0))
        self.box_1.grid(row=19, column=0, columnspan=4)
        self.box_2.grid(row=20, column=0, columnspan=4)
        self.box_3.grid(row=21, column=0, columnspan=4)

    @classmethod
    def watch_stash(cls) -> None:
        url = 'https://youtu.be/MiTUdXo3cns?si=ID3K2yuavx49WhM0&t=733'
        webbrowser.open(url)

    def create_stash_button(self) -> None:
        self.stash_video_button = ctk.CTkButton(
            master=self.frame,
            text='Stash Video',
            command=self.watch_stash,
        )

    @classmethod
    def watch_tc(cls) -> None:
        url = 'https://youtu.be/iKmTHJ7jCOE?si=KpRDsBxoPuYtEF97&t=120'
        webbrowser.open(url)

    def create_tc_button(self) -> None:
        self.tc_video_button = ctk.CTkButton(
            master=self.frame,
            text='TC Video',
            command=self.watch_tc,
        )

    def placement_video_buttons(self) -> None:
        self.tc_video_button.grid(row=17, column=0, columnspan=2, padx=(80, 0), pady=(20, 0))
        self.stash_video_button.grid(row=17, column=2, columnspan=2, padx=(0, 120), pady=(20, 0))

    def video_create(self, stash: bool, tc: bool) -> None:
        if stash and not tc:
            self.create_stash_button()
            self.video_text.configure(text='Stash manual building')
            self.stash_video_button.grid(row=17, column=0, columnspan=4, pady=(20, 0))
        elif tc and not stash:
            self.video_text.configure(text='TC manual building')
            self.create_tc_button()
            self.tc_video_button.grid(row=17, column=0, columnspan=4, pady=(20, 0))
        elif stash and tc:
            self.video_text.configure(text='TC and Stash manual building')
            self.create_tc_button()
            self.create_stash_button()
            self.placement_video_buttons()



