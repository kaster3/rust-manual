from abc import ABC

import customtkinter as ctk
from PIL import Image

from abstract_class_home import BoxMixin
from images.CTkImages import image_only_tc, cube_1x1


class Kiba4(BoxMixin, ABC):
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

    def __init__(self, name, home, placement_image, wood, stone, placement_image_2):
        super().__init__(name, home, placement_image, wood, stone)
        self.placement_2 = None
        self.placement_image_2 = placement_image_2
        self.home = home

        only_tc_button = ctk.CTkButton(
            master=self.frame,
            text='Only TC',
            command=self.only_tc,
        )

        tc_stash_button = ctk.CTkButton(
            master=self.frame,
            text='Cube',
            command=self.cube,
        )

        classical_kiba = ctk.CTkButton(
            master=self.frame,
            text='Classical',
            command=self.classical,
        )

        self.create_placement_2()

        self.video_create(stash=False, tc=True)

        only_tc_button.grid(row=12, column=0, columnspan=2, padx=(80, 0), pady=10)
        tc_stash_button.grid(row=12, column=2, columnspan=2, padx=(0, 120))
        classical_kiba.grid(row=13, column=0, columnspan=4, pady=(10, 0))

    def only_tc(self) -> None:
        if self.flag != 'Only tc':

            if self.flag == 'Cube':
                self.subtraction(wood=273, stone=1635)
            elif self.flag == 'Classical':
                self.subtraction(wood=1397, stone=7755)

            self.placement_delete()
            self.placement_2.destroy()
            self.edition(name='Only tc', image=image_only_tc)

    def cube(self) -> None:
        if self.flag != 'Cube':

            if self.flag == 'Only tc':
                self.addition(wood=273, stone=1635)
            elif self.flag == 'Classical':
                self.subtraction(wood=1124, stone=6120)
                self.placement_delete()
                self.placement_2.destroy()

            self.edition(name='Cube', image=cube_1x1)

    def classical(self) -> None:
        if self.flag != 'Classical':

            if self.flag == 'Only tc':
                self.addition(wood=1397, stone=7755)
            elif self.flag == 'Cube':
                self.addition(wood=1124, stone=6120)

            self.placement_create()
            self.create_placement_2()
            self.edition(name='Classical', image=self.home)

    def create_placement_2(self) -> None:

        self.placement_2 = ctk.CTkLabel(
            master=self.frame,
            text='',
            image=self.placement_image_2
        )

        self.placement_2.grid(row=24, column=0, columnspan=4)
