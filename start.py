import election
import lib
import pygame, sys
import buttons

# data = lib.data
# voters = lib.voters


# election.get_election_result("Jednota",data)



# count = 0
# for voter in voters:
#     if voters[voter]["commitment"] == False:
#         count += voters[voter]["quantity"]
#     print(voters[voter]["commitment"])
# print(count)

pygame.init()
pygame.font.init()

my_font = pygame.font.SysFont('Michroma', 30)

screen_width, screen_height = 1280, 720

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Menu")

clock = pygame.time.Clock()

menu_bg = pygame.image.load("img/menu_bg.png")

pygame.display.update()
clock.tick(20)

def get_font_michroma(size):
    return pygame.font.SysFont('Michroma', size)

def main_play():
    pygame.display.set_caption("Game")

    running = True
    while running:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        screen.fill((0, 0, 0))

        play_text = get_font_michroma(90).render("HRA", True, "red")
        play_rect = play_text.get_rect(center=(640, 260))

        screen.blit(play_text, play_rect)

        play_back = buttons.Button(image=None, pos=(640, 460), text_input = "ZPĚT", font = get_font_michroma(50), base_color = "#eaeaea", hover_color = "#ffffff", hover_image=None)

        play_back.change_color(PLAY_MOUSE_POS)
        play_back.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  
                sys.exit()
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    if play_back.check_input(PLAY_MOUSE_POS):
                        game_menu()
        pygame.display.update()
                
def options():
    pygame.display.set_caption("Options")

    running = True
    while running:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        screen.fill((0, 0, 0))

        options_text = get_font_michroma(90).render("NASTAVENÍ", True, "red")
        options_rect = options_text.get_rect(center=(640, 260))

        screen.blit(options_text, options_rect)

        options_back = buttons.Button(image=None, pos=(640, 460), text_input = "ZPĚT", font = get_font_michroma(50), base_color = "#eaeaea", hover_color = "#ffffff", hover_image=None)

        options_back.change_color(OPTIONS_MOUSE_POS)
        options_back.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  
                sys.exit()
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    if options_back.check_input(OPTIONS_MOUSE_POS):
                        game_menu()
        pygame.display.update()

def game_menu():
    pygame.display.set_caption("Menu")

    running = True
    while running:
        screen.blit(menu_bg, (0, 0))

        menu_button = pygame.image.load("img/menu_button.png")
        menu_button_hover = pygame.image.load("img/menu_button_hover.png")

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        menu_text = get_font_michroma(400).render("ARBITER", True, "#660619")
        menu_rect = menu_text.get_rect(center=(640, 245))

        screen.blit(menu_text, menu_rect)

        PLAY_BUTTON = buttons.Button(image=menu_button, pos=(640, 250), text_input = "HRÁT", font = get_font_michroma(50), base_color = "#eaeaea", hover_color = "#ffffff", hover_image=menu_button_hover)
        OPTIONS_BUTTON = buttons.Button(image=menu_button, pos=(640, 400), text_input = "NASTAVENÍ", font = get_font_michroma(50), base_color = "#eaeaea", hover_color = "#ffffff", hover_image=menu_button_hover)
        QUIT_BUTTON = buttons.Button(image=menu_button, pos=(640, 550), text_input = "OPUSTIT", font = get_font_michroma(50), base_color = "#eaeaea", hover_color = "#ffffff", hover_image=menu_button_hover)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.change_color(MENU_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  
                sys.exit()
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    if PLAY_BUTTON.check_input(MENU_MOUSE_POS):
                        main_play()
                    if OPTIONS_BUTTON.check_input(MENU_MOUSE_POS):
                        options()
                    if QUIT_BUTTON.check_input(MENU_MOUSE_POS):
                        pygame.quit()  
                        sys.exit()
                        running = False
        pygame.display.update()

game_menu()