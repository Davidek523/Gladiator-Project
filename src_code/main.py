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

        self.weapon = pygame.Surface((75, 75))
        self.weapon.fill("white")
        back_button = pygame.Surface((50, 50))
        back_button.fill("gray")

        CHOOSE_WEAPON = Button(image=self.weapon, pos=(200, 400), text_input="Sword 1", font=self.get_font(30), base_color="black", hovering_color="brown")
        BACK_BUTTON = Button(image=back_button, pos=(100, 100), text_input="< BACK", font=self.get_font(20), base_color="white", hovering_color="black")

        for button in [CHOOSE_WEAPON, BACK_BUTTON]:
            button.changeColor(WEAPON_MOUSE_POS)
            button.update(screen)

        return CHOOSE_WEAPON, BACK_BUTTON
    
    def armorShop(self):
        ARMOR_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("gray")

        armorm_piece = pygame.Surface((75, 75))
        armorm_piece.fill("white")
        back_button = pygame.Surface((75, 75))
        back_button.fill("gray")

        ARMOR_PIECE = Button(image=armorm_piece, pos=(200, 400), text_input="Armor piece 1", font=self.get_font(30), base_color="black", hovering_color="brown")
        BACK_BUTTON = Button(image=back_button, pos=(100, 100), text_input="< BACK", font=self.get_font(20), base_color="white", hovering_color="black")

        for button in [ARMOR_PIECE, BACK_BUTTON]:
            button.changeColor(ARMOR_MOUSE_POS)
            button.update(screen)

        return ARMOR_PIECE, BACK_BUTTON

    def magicShop(self):
        MAGIC_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("gray")

        magic_piece = pygame.Surface((75, 75))
        magic_piece.fill("white")
        back_button = pygame.Surface((75, 75))
        back_button.fill("gray")

        MAGIC_PIECE = Button(image=magic_piece, pos=(200, 400), text_input="Magic spell 1", font=self.get_font(30), base_color="black", hovering_color="brown")
        BACK_BUTTON = Button(image=back_button, pos=(100, 100), text_input="< BACK", font=self.get_font(20), base_color="white", hovering_color="black")

        for button in [MAGIC_PIECE, BACK_BUTTON]:
            button.changeColor(MAGIC_MOUSE_POS)
            button.update(screen)

        return MAGIC_PIECE, BACK_BUTTON

    def arenaArena(self):
        ARENA_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("gray")

        tournament = pygame.Surface((75, 75))
        tournament.fill("white")
        basic_fight = pygame.Surface((75, 75))
        basic_fight.fill("white")
        back_button = pygame.Surface((75, 75))
        back_button.fill("gray")

        TOURNAMENT = Button(image=tournament, pos=(200, 400), text_input="Enter the tournament", font=self.get_font(30), base_color="black", hovering_color="brown")
        BASIC_FIGHT = Button(image=basic_fight, pos=(200, 400), text_input="Enter a fight", font=self.get_font(30), base_color="black", hovering_color="brown")
        BACK_BUTTON = Button(image=back_button, pos=(100, 100), text_input="< BACK", font=self.get_font(20), base_color="white", hovering_color="black")

        for button in [BASIC_FIGHT, TOURNAMENT, BACK_BUTTON]:
            button.changeColor(ARENA_MOUSE_POS)
            button.update(screen)

        return BASIC_FIGHT, TOURNAMENT, BACK_BUTTON
    
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

                elif self.state == "armor_shop":
                    ARMOR_PIECE, BACK_BUTTON = self.armorShop()
                    if BACK_BUTTON.checkForInput(pygame.mouse.get_pos()):
                        self.state = "main_city"

                elif self.state == "weapon_shop":
                    CHOOSE_WEAPON, BACK_BUTTON = self.weaponShop()
                    if BACK_BUTTON.checkForInput(pygame.mouse.get_pos()):
                        self.state = "main_city"

                elif self.state == "magic_shop":
                    MAGIC_SPELL, BACK_BUTTON = self.magicShop()
                    if BACK_BUTTON.checkForInput(pygame.mouse.get_pos()):
                        self.state = "main_city"

                elif self.state == "arena":
                    TOURNAMENT, BASIC_FIGHT, BACK_BUTTON = self.arenaArena()
                    if BACK_BUTTON.checkForInput(pygame.mouse.get_pos()):
                        self.state = "main_city"
            

        if self.state == "main_city":
            self.main_city()    
        elif self.state == "armor_shop":
            self.armorShop()
        elif self.state == "weapon_shop":
            self.weaponShop()
        elif self.state == "magic_shop":
            self.magicShop()
        elif self.state == "arena":
            self.arenaArena()
        pygame.display.flip()
    # pygame.quit()

if __name__=="__main__":
    game = Gameloop(None, None, None, None)
    game.run()