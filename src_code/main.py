import pygame
import sys
from button import Button

pygame.init()

SCREEN_WIDTH = 700
SCREEN_HIGHT = 900

screen = pygame.display.set_mode((SCREEN_HIGHT, SCREEN_WIDTH))
pygame.display.set_caption("Gladiator Project")

class City:
    def __init__(self, armor_shop, weapon_shop, magic_shop, arena) -> None:
        self.armor_shop = armor_shop
        self.weapon_shop = weapon_shop
        self.magic_shop = magic_shop
        self.arena = arena
        self.state = "main_city"

    def get_font(self, size):
        return pygame.font.Font("data/fonts/antiquity-print.ttf", size)

    def main_city(self):
        CITY_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("yellow")

        self.armor_shop = pygame.Surface((100, 200))
        self.armor_shop.fill("red2")

        self.weapon_shop = pygame.Surface((100, 200))
        self.weapon_shop.fill("red2")

        self.magic_shop = pygame.Surface((100, 200))
        self.magic_shop.fill("red2")

        self.arena = pygame.Surface((100, 200))
        self.arena.fill("red2")

        ENTER_ARMOR = Button(image=self.armor_shop, pos=(800, 550), text_input="Armor Shop", font=self.get_font(40), base_color="red", hovering_color="red3")
        ENTER_WEAPON = Button(image=self.weapon_shop, pos=(200, 300), text_input="Weapon Shop", font=self.get_font(40), base_color="red", hovering_color="red3")
        ENTER_MAGIC = Button(image=self.magic_shop, pos=(100, 550), text_input="Magic Shop", font=self.get_font(40), base_color="red", hovering_color="red3")
        ENTER_ARENA = Button(image=self.arena, pos=(600, 150), text_input="Arena", font=self.get_font(40), base_color="red", hovering_color="red3")

        for button in [ENTER_ARMOR, ENTER_MAGIC, ENTER_WEAPON, ENTER_ARENA]:
            button.changeColor(CITY_MOUSE_POS)
            button.update(screen)

        return ENTER_ARMOR, ENTER_WEAPON, ENTER_MAGIC, ENTER_ARENA

    def weaponShop(self):
        WEAPON_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("gray")

        self.weapon = pygame.Surface((100, 200))
        self.weapon.fill("white")

        CHOOSE_WEAPON = Button(image=self.weapon, pos=(200, 400), text_input="Sword 1", font=self.get_font(30), base_color="black", hovering_color="brown")

        for button in [CHOOSE_WEAPON]:
            button.changeColor(WEAPON_MOUSE_POS)
            button.update(screen)

        return CHOOSE_WEAPON
    
class Gameloop(City):
    def run(self) -> None:
        while True:
            self.handle_events()

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.state == "main_city":
                    ENTER_ARMOR, ENTER_WEAPON, ENTER_MAGIC, ENTER_ARENA = self.main_city()
                    if ENTER_ARMOR.checkForInput(pygame.mouse.get_pos()):
                        self.state = "armor_shop"
                    if ENTER_WEAPON.checkForInput(pygame.mouse.get_pos()):
                        self.state = "weapon_shop"
                    if ENTER_MAGIC.checkForInput(pygame.mouse.get_pos()):
                        self.state = "magic_shop"
                    if ENTER_ARENA.checkForInput(pygame.mouse.get_pos()):
                        self.state = "arena"
            

        if self.state == "main_city":
            self.main_city()    
        elif self.state == "armor_shop":
            print("You are in the Armor Shop!")
        elif self.state == "weapon_shop":
            print("You are in the Weapon Shop!")
        elif self.state == "magic_shop":
            print("You are now in the Magic Shop!")
        elif self.state == "arena":
            print("You are in the Mighty Arena!")
        pygame.display.flip()
    # pygame.quit()

if __name__=="__main__":
    game = Gameloop(None, None, None, None)
    game.run()