import pygame
import random
from global_inst import *
from find_area import find_area_num, random_area_num


def Player_vs_AI():
    turn = 1
    area_num = -1
    card_left = 16
    score_player = 0
    score_ai = 0
    comp_list = []
    card_list = []

    # initialize game
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("My game")
    pygame.event.set_blocked(pygame.MOUSEMOTION)
    # load game images
    egg1 = pygame.image.load(os.path.join(img_folder, "egg1.png")).convert()
    egg1 = pygame.transform.scale(egg1, (90, 120))
    egg2 = pygame.image.load(os.path.join(img_folder, "egg2.png")).convert()
    egg2 = pygame.transform.scale(egg2, (90, 120))
    egg3 = pygame.image.load(os.path.join(img_folder, "egg3.png")).convert()
    egg3 = pygame.transform.scale(egg3, (90, 120))
    egg4 = pygame.image.load(os.path.join(img_folder, "egg4.png")).convert()
    egg4 = pygame.transform.scale(egg4, (90, 120))
    egg5 = pygame.image.load(os.path.join(img_folder, "egg5.png")).convert()
    egg5 = pygame.transform.scale(egg5, (90, 120))
    egg6 = pygame.image.load(os.path.join(img_folder, "egg6.png")).convert()
    egg6 = pygame.transform.scale(egg6, (90, 120))
    egg7 = pygame.image.load(os.path.join(img_folder, "egg7.png")).convert()
    egg7 = pygame.transform.scale(egg7, (90, 120))
    bunny = pygame.image.load(os.path.join(img_folder, "bunny.png")).convert()
    bunny = pygame.transform.scale(bunny, (90, 120))
    card_back = pygame.image.load(os.path.join(img_folder, "card.png")).convert()
    card_back = pygame.transform.scale(card_back, (80, 120))
    # load texts and scores on the screen
    font_name = pygame.font.SysFont("Arial", 40, True, False)
    text_player_name = font_name.render("YOU", False, black)
    text_ai_name = font_name.render("AI", False, black)
    font_score = pygame.font.SysFont("Arial", 30, True, False)
    text_player = font_score.render("0", False, black)
    text_ai = font_score.render("0", False, black)
    text_cover = pygame.Surface((100, 50))
    text_cover.fill(white)
    font_win = pygame.font.SysFont("Arial", 100, True, False)
    font_draw = pygame.font.SysFont("Arial", 100, True, False)
    font_lose = pygame.font.SysFont("Arial", 100, True, False)

    # shuffle the cards
    random.shuffle(value_in_area)

    # class for card object
    class Card:
        def __init__(self, value, area):
            self.card_value = value
            self.card_area = area
            self.shown = False
            if self.card_value == 1:
                self.image = egg1
            if self.card_value == 2:
                self.image = egg2
            if self.card_value == 3:
                self.image = egg3
            if self.card_value == 4:
                self.image = egg4
            if self.card_value == 5:
                self.image = egg5
            if self.card_value == 6:
                self.image = egg6
            if self.card_value == 7:
                self.image = egg7
            if self.card_value == 8:
                self.image = bunny

    # add cards to a card list
    for i in range(16):
        card = Card(value_in_area[i], area_list[i])
        card_list.append(card)

    # setup board with 16 cards face down, and texts
    screen.fill(white)
    for coor in area_list:
        screen.blit(card_back, coor)
    screen.blit(text_player_name, (60, 100))
    screen.blit(text_ai_name, (670, 100))
    screen.blit(text_player, (90, 150))
    screen.blit(text_ai, (680, 150))

    running = True
    # game loop
    while running:
        
        # process input (events)
        for event in pygame.event.get():
            print("event loop")
            # check for closing the window
            if event.type == pygame.QUIT:
                running = False
            else:
                windows_focus = pygame.mouse.get_focused()
                if windows_focus == 1:
                    # player's turn
                    if turn == 1:
                        print("player's turn")
                        # if the player has selected two cards:
                        if comp_list.__len__() == 2:
                            print("comparing two cards")
                            # compare two selected cards
                            if comp_list[0].card_value == comp_list[1].card_value:
                                print("matched")
                                # update the score
                                score_player = score_player + 1
                                # user white cover overlap the old score
                                screen.blit(text_cover, (90, 150))
                                # show up the new score text
                                text_player = font_score.render(str(score_player), False, black)
                                screen.blit(text_player, (90, 150))
                                pygame.display.update()
                                # decrease the total fo card by 2
                                card_left = card_left - 2                            
                                # if bunny is found, get extra turn
                                if comp_list[0].card_value == 8:
                                    print("found bunny, get extra turn")
                                    turn = 1
                                else:
                                    turn = 2
                            else:
                                print("missed")
                                comp_list[0].shown = False
                                comp_list[1].shown = False
                                screen.blit(card_back, comp_list[0].card_area)
                                screen.blit(card_back, comp_list[1].card_area)
                                turn = 2
                            # clear the compare list
                            comp_list.clear()
                        # if the player has NOT selected two cards:
                        else:
                            print("pick a card")
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                pos_x, pos_y = pygame.mouse.get_pos()
                                print(pos_x, pos_y)
                                area_num = find_area_num(pos_x, pos_y)
                                print(area_num)
                                if area_num:
                                    if area_num == 1:
                                        print("pick card 1")
                                        if not card_list[0].shown:
                                            screen.blit(card_list[0].image, card_list[0].card_area)
                                            card_list[0].shown = True
                                            comp_list.append(card_list[0])
                                        else:
                                            pass
                                    if area_num == 2:
                                        print("pick card 2")
                                        if not card_list[1].shown:
                                            screen.blit(card_list[1].image, card_list[1].card_area)
                                            card_list[1].shown = True
                                            comp_list.append(card_list[1])
                                        else:
                                            pass
                                    if area_num == 3:
                                        print("pick card 3")
                                        if not card_list[2].shown:
                                            screen.blit(card_list[2].image, card_list[2].card_area)
                                            card_list[2].shown = True
                                            comp_list.append(card_list[2])
                                        else:
                                            pass
                                    if area_num == 4:
                                        print("pick card 4")
                                        if not card_list[3].shown:
                                            screen.blit(card_list[3].image, card_list[3].card_area)
                                            card_list[3].shown = True
                                            comp_list.append(card_list[3])
                                        else:
                                            pass
                                    if area_num == 5:
                                        print("pick card 5")
                                        if not card_list[4].shown:
                                            screen.blit(card_list[4].image, card_list[4].card_area)
                                            card_list[4].shown = True
                                            comp_list.append(card_list[4])
                                        else:
                                            pass
                                    if area_num == 6:
                                        print("pick card 6")
                                        if not card_list[5].shown:
                                            screen.blit(card_list[5].image, card_list[5].card_area)
                                            card_list[5].shown = True
                                            comp_list.append(card_list[5])
                                        else:
                                            pass
                                    if area_num == 7:
                                        print("pick card 7")
                                        if not card_list[6].shown:
                                            screen.blit(card_list[6].image, card_list[6].card_area)
                                            card_list[6].shown = True
                                            comp_list.append(card_list[6])
                                        else:
                                            pass
                                    if area_num == 8:
                                        print("pick card 8")
                                        if not card_list[7].shown:
                                            screen.blit(card_list[7].image, card_list[7].card_area)
                                            card_list[7].shown = True
                                            comp_list.append(card_list[7])
                                        else:
                                            pass
                                    if area_num == 9:
                                        print("pick card 9")
                                        if not card_list[8].shown:
                                            screen.blit(card_list[8].image, card_list[8].card_area)
                                            card_list[8].shown = True
                                            comp_list.append(card_list[8])
                                        else:
                                            pass
                                    if area_num == 10:
                                        print("pick card 10")
                                        if not card_list[9].shown:
                                            screen.blit(card_list[9].image, card_list[9].card_area)
                                            card_list[9].shown = True
                                            comp_list.append(card_list[9])
                                        else:
                                            pass
                                    if area_num == 11:
                                        print("pick card 11")
                                        if not card_list[10].shown:
                                            screen.blit(card_list[10].image, card_list[10].card_area)
                                            card_list[10].shown = True
                                            comp_list.append(card_list[10])
                                        else:
                                            pass
                                    if area_num == 12:
                                        print("pick card 12")
                                        if not card_list[11].shown:
                                            screen.blit(card_list[11].image, card_list[11].card_area)
                                            card_list[11].shown = True
                                            comp_list.append(card_list[11])
                                        else:
                                            pass
                                    if area_num == 13:
                                        print("pick card 13")
                                        if not card_list[12].shown:
                                            screen.blit(card_list[12].image, card_list[12].card_area)
                                            card_list[12].shown = True
                                            comp_list.append(card_list[12])
                                        else:
                                            pass
                                    if area_num == 14:
                                        print("pick card 14")
                                        if not card_list[13].shown:
                                            screen.blit(card_list[13].image, card_list[13].card_area)
                                            card_list[13].shown = True
                                            comp_list.append(card_list[13])
                                        else:
                                            pass
                                    if area_num == 15:
                                        print("pick card 15")
                                        if not card_list[14].shown:
                                            screen.blit(card_list[14].image, card_list[14].card_area)
                                            card_list[14].shown = True
                                            comp_list.append(card_list[14])
                                        else:
                                            pass
                                    if area_num == 16:
                                        print("pick card 16")
                                        if not card_list[15].shown:
                                            screen.blit(card_list[15].image, card_list[15].card_area)
                                            card_list[15].shown = True
                                            comp_list.append(card_list[15])
                                        else:
                                            pass
                                else:
                                    pass

                    # AI's turn
                    if turn == 2:
                        print("AI's turn")
                        # if AI has selected two cards:
                        if comp_list.__len__() == 2:
                            print("comparing two cards")
                            # compare two selected cards
                            if comp_list[0].card_value == comp_list[1].card_value:
                                print("matched")
                                # update the score
                                score_ai = score_ai + 1
                                # user white cover overlap the old score
                                screen.blit(text_cover, (680, 150))
                                # show up the new score text
                                text_ai = font_score.render(str(score_ai), False, black)
                                screen.blit(text_ai, (680, 150))
                                pygame.display.update()
                                # decrease the total fo card by 2
                                card_left = card_left - 2
                                # if bunny is found, get extra turn
                                if comp_list[0].card_value == 8:
                                   print("found bunny, get extra turn")
                                   turn = 2
                                else:
                                    turn = 1
                            else:
                                print("missed")
                                comp_list[0].shown = False
                                comp_list[1].shown = False
                                screen.blit(card_back, comp_list[0].card_area)
                                screen.blit(card_back, comp_list[1].card_area)
                                pygame.time.wait(2000)
                                turn = 1
                            comp_list.clear()
                        # if AI has NOT selected two cards:
                        else:
                            pygame.time.wait(2000)
                            # level 0 AI (pick the two cards randomly)
                            print("AI is choosing card")
                            # GET A RANDOM CARD POSITION FROM A FUNCTION
                            area_num = random_area_num(card_list)
                            if area_num:
                                if area_num == 1:
                                    print("pick card 1")
                                    screen.blit(card_list[0].image, card_list[0].card_area)
                                    card_list[0].shown = True
                                    comp_list.append(card_list[0])
                                if area_num == 2:
                                    print("pick card 2")
                                    screen.blit(card_list[1].image, card_list[1].card_area)
                                    card_list[1].shown = True
                                    comp_list.append(card_list[1])
                                if area_num == 3:
                                    print("pick card 3")
                                    screen.blit(card_list[2].image, card_list[2].card_area)
                                    card_list[2].shown = True
                                    comp_list.append(card_list[2])
                                if area_num == 4:
                                    print("pick card 4")
                                    screen.blit(card_list[3].image, card_list[3].card_area)
                                    card_list[3].shown = True
                                    comp_list.append(card_list[3])   
                                if area_num == 5:
                                    print("pick card 5")
                                    screen.blit(card_list[4].image, card_list[4].card_area)
                                    card_list[4].shown = True
                                    comp_list.append(card_list[4])      
                                if area_num == 6:
                                    print("pick card 6")
                                    screen.blit(card_list[5].image, card_list[5].card_area)
                                    card_list[5].shown = True
                                    comp_list.append(card_list[5])
                                if area_num == 7:
                                    print("pick card 7")
                                    screen.blit(card_list[6].image, card_list[6].card_area)
                                    card_list[6].shown = True
                                    comp_list.append(card_list[6])
                                if area_num == 8:
                                    print("pick card 8")
                                    screen.blit(card_list[7].image, card_list[7].card_area)
                                    card_list[7].shown = True
                                    comp_list.append(card_list[7])
                                if area_num == 9:
                                    print("pick card 9")
                                    screen.blit(card_list[8].image, card_list[8].card_area)
                                    card_list[8].shown = True
                                    comp_list.append(card_list[8])
                                if area_num == 10:
                                    print("pick card 10")
                                    screen.blit(card_list[9].image, card_list[9].card_area)
                                    card_list[9].shown = True
                                    comp_list.append(card_list[9])
                                if area_num == 11:
                                    print("pick card 11")
                                    screen.blit(card_list[10].image, card_list[10].card_area)
                                    card_list[10].shown = True
                                    comp_list.append(card_list[10])
                                if area_num == 12:
                                    print("pick card 12")
                                    screen.blit(card_list[11].image, card_list[11].card_area)
                                    card_list[11].shown = True
                                    comp_list.append(card_list[11])
                                if area_num == 13:
                                    print("pick card 13")
                                    screen.blit(card_list[12].image, card_list[12].card_area)
                                    card_list[12].shown = True
                                    comp_list.append(card_list[12])
                                if area_num == 14:
                                    print("pick card 14")
                                    screen.blit(card_list[13].image, card_list[13].card_area)
                                    card_list[13].shown = True
                                    comp_list.append(card_list[13])
                                if area_num == 15:
                                    print("pick card 15")
                                    screen.blit(card_list[14].image, card_list[14].card_area)
                                    card_list[14].shown = True
                                    comp_list.append(card_list[14])
                                if area_num == 16:
                                    print("pick card 16")
                                    screen.blit(card_list[15].image, card_list[15].card_area)
                                    card_list[15].shown = True
                                    comp_list.append(card_list[15])
                            else:
                                pass

        # exit game when all cards are flipped
        if card_left == 0:
            if score_player > score_ai:
                print("YOU WIN")
                win_window = font_win.render("YOU WIN", False, red)
            elif score_player == score_ai:
                print("DRAW")
                win_window = font_draw.render("DRAW", False, blue)
            else:
                print("YOU LOSE")
                win_window = font_lose.render("YOU LOSE", False, black)
            screen.blit(win_window, (200, 200))
            running = False

        pygame.display.flip()

    # end loop
    print("game will close automatically within 1 second")
    pygame.time.wait(600)
    pygame.quit()
