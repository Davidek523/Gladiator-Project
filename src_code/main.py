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
        self.armor_shop.fill("red")

        self.weapon_shop = pygame.Surface((100, 200))
        self.weapon_shop.fill("red")

        self.magic_shop = pygame.Surface((100, 200))
        self.magic_shop.fill("red")

        ENTER_ARMOR = Button(image=self.armor_shop, pos=(800, 550), text_input="Armor Shop", font=self.get_font(40), base_color="red", hovering_color="red3")
        ENTER_WEAPON = Button(image=self.weapon_shop, pos=(200, 300), text_input="Weapon Shop", font=self.get_font(40), base_color="red", hovering_color="red3")
        ENTER_MAGIC = Button(image=self.magic_shop, pos=(100, 550), text_input="Magic Shop", font=self.get_font(40), base_color="red", hovering_color="red3")

        for button in [ENTER_ARMOR, ENTER_MAGIC, ENTER_WEAPON]:
            button.changeColor(CITY_MOUSE_POS)
            button.update(screen)

        return ENTER_ARMOR, ENTER_WEAPON, ENTER_MAGIC
    
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
                    ENTER_ARMOR, ENTER_WEAPON, ENTER_MAGIC = self.main_city()
                    if ENTER_ARMOR.checkForInput(pygame.mouse.get_pos()):
                        self.state = "armor_shop"
                    if ENTER_WEAPON.checkForInput(pygame.mouse.get_pos()):
                        self.state = "weapon_shop"
                    if ENTER_MAGIC.checkForInput(pygame.mouse.get_pos()):
                        self.state = "magic_shop"
            

        if self.state == "main_city":
            self.main_city()    
        elif self.state == "armor_shop":
            print("You are in the Armor Shop!")
        elif self.state == "weapon_shop":
            print("You are in the Weapon Shop!")
        elif self.state == "magic_shop":
            print("You are now in the Magic Shop!")
        pygame.display.flip()
    # pygame.quit()

if __name__=="__main__":
    game = Gameloop(None, None, None, None)
    game.run()