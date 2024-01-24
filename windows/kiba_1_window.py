from abc import ABC

import customtkinter as ctk
from PIL import Image

from images.CTkImages import image_deep, image_cube, image_without, image_explanation
from abstract_class_home import Frame


class Kiba1(Frame, ABC):
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

        self.explanation_image = None
        self.explanation_text = None

        start_cube = ctk.CTkButton(
            master=self.frame,
            text='Cube to start',
            command=self.cube,
        )

        without_triangle = ctk.CTkButton(
            master=self.frame,
            text='Without triangle',
            command=self.without_triangle,
        )

        classical_kiba = ctk.CTkButton(
            master=self.frame,
            text='Classical',
            command=self.classical,
        )

        deep_triangle = ctk.CTkButton(
            master=self.frame,
            text='Deep triangle',
            command=self.deep_triangle,
        )

        start_cube.grid(row=12, column=0, columnspan=2, padx=(80, 0), pady=10)
        without_triangle.grid(row=12, column=2, columnspan=2, padx=(0, 120))
        classical_kiba.grid(row=13, column=0, columnspan=2, padx=(80, 0))
        deep_triangle.grid(row=13, column=2, columnspan=2, padx=(0, 120))

    def cube(self) -> None:
        if self.flag != 'Cube to start':
            if self.flag == 'Without triangle':
                self.subtraction(wood=185, stone=1010)
            elif self.flag == 'Classical':
                self.subtraction(wood=308, stone=1745)
            elif self.flag == 'Deep triangle':
                self.subtraction(wood=408, stone=2345)
                self.delete_explanation_label()

            self.placement_delete()
            self.edition(name='Cube to start', image=image_cube)

    def without_triangle(self) -> None:
        if self.flag != 'Without triangle':
            if self.flag == 'Cube to start':
                self.addition(wood=185, stone=1010)
                self.placement_create()
            elif self.flag == 'Classical':
                self.subtraction(wood=123, stone=735)
            if self.flag == 'Deep triangle':
                self.subtraction(wood=223, stone=1335)
                self.delete_explanation_label()

            self.edition(name='Without triangle', image=image_without)

    def classical(self) -> None:
        if self.flag != 'Classical':
            if self.flag == 'Cube to start':
                self.addition(wood=308, stone=1745)
                self.placement_create()
            elif self.flag == 'Without triangle':
                self.addition(wood=123, stone=735)
            elif self.flag == 'Deep triangle':
                self.subtraction(wood=100, stone=600)
                self.delete_explanation_label()

            self.edition(name='Classical', image=self.home)

    def deep_triangle(self) -> None:
        if self.flag != 'Deep triangle':

            self.create_explanation_label()

            if self.flag == 'Cube to start':
                self.addition(wood=408, stone=2345)
                self.placement_create()
            elif self.flag == 'Without triangle':
                self.addition(wood=223, stone=1335)
            elif self.flag == 'Classical':
                self.addition(wood=100, stone=600)

            self.edition(name='Deep triangle', image=image_deep)

    def create_explanation_label(self) -> None:
        self.explanation_image = ctk.CTkLabel(
            master=self.frame,
            text='',
            image=image_explanation,
        )

        self.explanation_text = ctk.CTkLabel(
            master=self.frame,
            text="""
                        Look at these 2 lines, dark and light, this point is
                        a minimum requirement of double foundation,
                        you can't pull your mouse from this moment,
                        only push from yourself
                        """,
        )

        self.explanation_image.grid(row=16, column=0, columnspan=4, pady=(0, 10))
        self.explanation_text.grid(row=17, column=0, columnspan=5, padx=(0, 70))

    def delete_explanation_label(self) -> None:
        self.explanation_image.destroy()
        self.explanation_text.destroy()
