from abc import ABC

import customtkinter as ctk
from PIL import Image

from abstract_class_home import BoxMixin
from images.CTkImages import image_stash, image_stash_cube, image_without


class Kiba2(BoxMixin, ABC):
    def click_wooden_door(self) -> None:
        super().click_wooden_door()

    def click_double_wooden(self) -> None:
        super().click_double_wooden()

    def click_metal_door(self) -> None:
        super().click_metal_door()

    def click_double_metal(self) -> None:
        super().click_double_metal()

    def click_codelock(self) -> None:
        super().click_codelock()

    def click_lock(self) -> None:
        super().click_lock()

    def metal_placement(self) -> None:
        super().metal_placement()

    def placement_create(self) -> None:
        super().placement_create()

    def placement_delete(self) -> None:
        super().placement_delete()

    def addition(self, wood: int, stone: int) -> None:
        super().addition(wood=wood, stone=stone)

    def subtraction(self, wood: int, stone: int) -> None:
        super().subtraction(wood=wood, stone=stone)

    def edition(self, name: str, image: Image) -> None:
        super().edition(name=name, image=image)

    def __init__(self, name, home, placement_image, wood, stone):
        super().__init__(name, home, placement_image, wood, stone)
        self.home = home

        only_stash_btn = ctk.CTkButton(
            master=self.frame,
            text='Only stash',
            command=self.only_stash,
        )

        stash_cube = ctk.CTkButton(
            master=self.frame,
            text='Stash and cube',
            command=self.cube,
        )

        classical_kiba = ctk.CTkButton(
            master=self.frame,
            text='Classical',
            command=self.classical,
        )

        without = ctk.CTkButton(
            master=self.frame,
            text='without triangle',
            command=self.without_triangle,
        )

        self.create_boxes()
        self.video_create(stash=True, tc=False)

        only_stash_btn.grid(row=12, column=0, columnspan=2, padx=(80, 0), pady=10)
        stash_cube.grid(row=12, column=2, columnspan=2, padx=(0, 120))
        without.grid(row=13, column=0, columnspan=2, padx=(80, 0))
        classical_kiba.grid(row=13, column=2, columnspan=2, padx=(0, 120))

        self.stash_video_button.grid(row=17, column=0, columnspan=4, pady=(20, 0))

    def only_stash(self) -> None:
        if self.flag != 'Only Stash':
            if self.flag == 'Cube':
                self.subtraction(wood=1200, stone=1200)
            elif self.flag == 'Without triangle':
                self.subtraction(wood=1360, stone=2160)
                self.placement_delete()
            elif self.flag == 'Classical':
                self.subtraction(wood=1533, stone=3495)
                self.placement_delete()

            self.edition(name='Only Stash', image=image_stash)

    def cube(self):
        if self.flag != 'Cube':
            if self.flag == 'Only Stash':
                self.addition(wood=1200, stone=1200)
            elif self.flag == 'Without triangle':
                self.subtraction(wood=160, stone=960)
                self.placement_delete()
            elif self.flag == 'Classical':
                self.subtraction(wood=333, stone=2295)
                self.placement_delete()

            self.edition(name='Cube', image=image_stash_cube)

    def without_triangle(self) -> None:
        if self.flag != 'Without triangle':
            if self.flag == 'Only Stash':
                self.addition(wood=1360, stone=2160)
                self.placement_create()
            elif self.flag == 'Cube':
                self.addition(wood=160, stone=960)
                self.placement_create()
            elif self.flag == 'Classical':
                self.subtraction(wood=173, stone=1335)

            self.edition(name='Without triangle', image=image_without)

    def classical(self) -> None:
        if self.flag != 'Classical':
            if self.flag == 'Only Stash':
                self.addition(wood=1533, stone=3495)
                self.placement_create()
            elif self.flag == 'Cube':
                self.addition(wood=333, stone=2295)
                self.placement_create()
            elif self.flag == 'Without triangle':
                self.addition(wood=173, stone=1335)

            self.edition(name='Classical', image=self.home)
