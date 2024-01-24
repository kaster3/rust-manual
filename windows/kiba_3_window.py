from abc import ABC

import customtkinter as ctk
from PIL import Image

from abstract_class_home import BoxMixin
from images.CTkImages import image_only_tc, image_tc_stash


class Kiba3(BoxMixin, ABC):
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

        only_tc_button = ctk.CTkButton(
            master=self.frame,
            text='Only TC',
            command=self.only_tc,
        )

        tc_stash_button = ctk.CTkButton(
            master=self.frame,
            text='TC and stash',
            command=self.tc_stash,
        )

        classical_kiba = ctk.CTkButton(
            master=self.frame,
            text='Classical',
            command=self.classical,
        )

        self.create_boxes()
        self.video_create(stash=True, tc=True)

        only_tc_button.grid(row=12, column=0, columnspan=2, padx=(80, 0), pady=10)
        tc_stash_button.grid(row=12, column=2, columnspan=2, padx=(0, 120))
        classical_kiba.grid(row=13, column=0, columnspan=4, pady=(10, 0))

    def only_tc(self) -> None:
        if self.flag != 'Only tc':
            if self.boxes:
                self.metal -= self.boxes * 50
                self.wood -= self.boxes * 250
                self.boxes = 0
                self.metal_text.configure(text=f'x {self.metal}')
                if not self.metal:
                    self.metal_text.destroy()
                    self.label_metal.destroy()

            self.text_boxes.destroy()
            self.box_button.destroy()
            self.label_for_boxes.destroy()
            self.stash_video_button.destroy()
            self.box_explanation.destroy()
            self.box_1.destroy()
            self.box_2.destroy()
            self.box_3.destroy()

            self.tc_video_button.grid(row=17, column=0, columnspan=4, padx=0, pady=(20, 0))

            if self.flag == 'TC and Stash':
                self.subtraction(wood=630, stone=2700)
            elif self.flag == 'Classical':
                self.subtraction(wood=1562, stone=7980)

            self.placement_delete()
            self.video_text.configure(text='TC building manual')
            self.edition(name='Only TC', image=image_only_tc)

    def tc_stash(self):
        if self.flag != 'TC and Stash':
            if self.flag == 'Only TC':
                self.addition(wood=630, stone=2700)
                self.create_boxes()
                self.video_create(stash=True, tc=False)
                self.placement_video_buttons()
            elif self.flag == 'Classical':
                self.wood -= 932
                self.stone -= 5280
                self.placement_delete()

            self.edition(name='TC and Stash', image=image_tc_stash)

    def classical(self) -> None:
        if self.flag != 'Classical':
            if self.flag == 'Only TC':
                self.addition(wood=1562, stone=7980)
                self.create_boxes()
                self.video_create(stash=True, tc=False)
                self.placement_video_buttons()
            elif self.flag == 'TC and Stash':
                self.addition(wood=932, stone=5280)

            self.placement_create()
            self.edition(name='Classical', image=self.home)
