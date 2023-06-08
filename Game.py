"""Fruit Catcher Game | Game.py

This file is responsible for all the graphics and game mechanics.

General Cite
------------
https://stackoverflow.com/questions/10261774/pygame-error-video-system-not-initialized
    used to help solve exiting issue
"""

import pygame
import random
import ObjectDetection
import cv2

pygame.init()
webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# AESTHETICS
black = (0, 0, 0)
white = (255, 255, 255)
dark_red = (200, 0, 0)
dark_green = (0, 200, 0)
dark_yellow = (200, 200, 0)
bright_yellow = (255, 255, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
smFont = pygame.font.SysFont("comicsansms", 25)
medFont = pygame.font.SysFont("comicsansms", 33)
lFont = pygame.font.SysFont("comicsansms", 50)

# DISPLAY
display_width = 500
display_height = 800
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("FRUIT CATCHER")

# IMAGES
basket_img = pygame.image.load('basket.png')
basket_img = pygame.transform.scale(basket_img, (125, 150))
bg = pygame.image.load('background.jpg')
clock = pygame.time.Clock()


class Basket(object):
    """


    Basket Class

    Attributes
    ----------
    x : float
    x position of basket

    y : float
    y position of basket

    vel : int
    Speed of basket

    hitbox : tuple
    Tuple of integer values of hitbox around basket

    Methods
    ----------
    draw(screens)
        draws/displays the basket on screen

    Cites
    -----
    https://www.tutorialspoint.com/What-is-difference-between-self-and-init-methods-in-python-Class
        used to help understand Python coding again
    """

    vel = 10

    def __init__(self, x, y):
        """


        Basket object constructor

        Parameters
        ----------
        x : float
        x position of basket

        y : float
        y position of basket

        """
        self.x = x
        self.y = y
        self.hitbox = (x, y + 20, 125, 130)

    def draw(self, screens):
        """


        Drawing/displaying basket onto screen

        Parameters
        ----------
        screens : screen
        screen to draw/display basket on

        """
        screens.blit(basket_img, (int(self.x), int(self.y)))
        self.hitbox = (self.x, self.y + 20, 125, 130)


class Fruit(object):
    """


    Fruit super class

    Attributes
    ----------
    x : float
    x position of fruit

    y : float
    y position of fruit

    vel : int
    Speed of fruit

    Methods
    ----------
    draw(screens)
        draws/displays the fruit on screen

    Cites
    ----------
    https://www.digitalocean.com/community/tutorials/understanding-class-inheritance-in-python-3

    """

    vel = 10

    def __init__(self, x, y):
        """


        Fruit object constructor

        Parameters
        ----------
        x : float
        x position of fruit

        y : float
        y position of fruit

        """
        self.x = x
        self.y = y


    def draw(self, screens):
        """


        Drawing/displaying fruit onto screen

        Parameters
        ----------
        screens : screen
        screen to draw/display fruit on

        """
        pass


class Strawberry(Fruit):
    """


    Strawberry sub class of Fruit

    Attributes
    ----------
    x : float
    x position of strawberry inherited from Fruit

    y : float
    y position of strawberry inherited from Fruit

    vel : int
    Speed of strawberry inherited from Fruit

    points : int
    Points worth of strawberry

    hitbox : tuple
    Integer values for hitbox around strawberry

    Methods
    ----------
    draw(screens)
        draws/displays the strawberry on screen

    Cites
    ----------
    https://www.digitalocean.com/community/tutorials/understanding-class-inheritance-in-python-3

    """
    points = 1

    def draw(self, screens):
        """


        Drawing/displaying strawberry onto screen

        Parameters
        ----------
        screens : screen
        screen to draw/display strawberry on

        """
        fruit = pygame.image.load('strawberry.png')

        fruit = pygame.transform.scale(fruit, (100, 100))
        screens.blit(fruit, (self.x, self.y))
        self.hitbox = (self.x, self.y, 100, 100)


class Apple(Fruit):
    """


    Apple sub class of Fruit

    Attributes
    ----------
    x : float
    x position of apple inherited from Fruit

    y : float
    y position of apple inherited from Fruit

    vel : int
    Speed of apple inherited from Fruit

    points : int
    Points worth of apple

    hitbox : tuple
    Integer values for hitbox around apple

    Methods
    ----------
    draw(screens)
        draws/displays the apple on screen

    Cites
    ----------
    https://www.digitalocean.com/community/tutorials/understanding-class-inheritance-in-python-3

    """

    points = 2

    def draw(self, screens):
        """


        Drawing/displaying apple onto screen

        Parameters
        ----------
        screens : screen
        screen to draw/display apple on

        """
        fruit = pygame.image.load('apple.png')

        fruit = pygame.transform.scale(fruit, (100, 100))
        screens.blit(fruit, (self.x, self.y))
        self.hitbox = (self.x, self.y, 100, 100)


class Pineapple(Fruit):
    """


    Pineapple sub class of Fruit

    Attributes
    ----------
    x : float
    x position of pineapple inherited from Fruit

    y : float
    y position of pineapple inherited from Fruit

    vel : int
    Speed of pineapple inherited from Fruit

    points : int
    Points worth of pineapple

    hitbox : tuple
    Integer values for hitbox around pineapple

    Methods
    ----------
    draw(screens)
        draws/displays the pineapple on screen

    Cites
    ----------
    https://www.digitalocean.com/community/tutorials/understanding-class-inheritance-in-python-3

    """
    points = 3

    def draw(self, screens):
        """


        Drawing/displaying pineapple onto screen

        Parameters
        ----------
        screens : screen
        screen to draw/display pineapple on

        """
        fruit = pygame.image.load('pineapple.png')

        fruit = pygame.transform.scale(fruit, (100, 100))
        screens.blit(fruit, (self.x, self.y))
        self.hitbox = (self.x, self.y, 100, 100)


def text_objects(text, color, size):
    """


    Font sizes for messages and texts

    Allows for messages and texts to be of a certain size

    Parameters
    ----------
        text : str
        Message of text

        color : tuple
        Tuple of integer values for rgb of text

        size : str, optional
        To indicate size of text

    Cites
    -----
    https://www.youtube.com/playlist?list=PL6gx4Cwl9DGAjkwJocj7vlc_mFU-4wXJq
    """
    if size == "small":
        text_surface = smFont.render(text, True, color)
    elif size == "medium":
        text_surface = medFont.render(text, True, color)
    elif size == "large":
        text_surface = lFont.render(text, True, color)
    return text_surface, text_surface.get_rect()


def text_to_button(msg, color, x, y, width, height, size="small"):
    """


    Displaying text to button

    Function helps display text onto buttons. By default text is small, but can be changed when calling the function.

    Parameters
    ----------
        msg : str
        Message of text

        color: tuple
        Tuple of integer values for rgb of text

        x : int
        x position of text

        y : int
        y position of text

        width : int
        Width of text

        height : int
        Height of text

        size : str, optional
        To indicate size of text

    Cites
    -----
    https://www.youtube.com/playlist?list=PL6gx4Cwl9DGAjkwJocj7vlc_mFU-4wXJq
    """
    text_surf, text_rect = text_objects(msg, color, size)
    text_rect.center = (int(x + (width / 2)), int(y + (height / 2)))
    screen.blit(text_surf, text_rect)


def message_to_screen(msg, y_displace=0, size="small", color=black,):
    """


    Displaying text on screen

    Function helps display text onto screen. By default text is black, centered and small, but can be changed when calling the
    function.

    Parameters
    ----------
        msg : str
        Message of text

        y_displace : int, optional
        How much to displace he text by from the middle

        size : str, optional
        To indicate size of text

        color: tuple, optional
        Tuple of integer values for rgb of text

    """

    text_surf, text_rect = text_objects(msg, color, size)
    text_rect.center = int(display_width / 2), int((display_height / 2) + y_displace)
    screen.blit(text_surf, text_rect)


def score(scores):
    """


    Displaying of scores

    Function for displaying score on screen as it changes

    Parameters
    ----------
        scores : int
        Score of player

    """

    text = smFont.render("Score: " + str(scores), True, black)
    screen.blit(text, [0, 0])


def life(lives):
    """


    Displaying of lives

    Function for displaying lives on screen as it changes

    Parameters
    ----------
        lives : int
        Lives of player

    """
    text = smFont.render("Lives: " + str(lives), True, black)
    screen.blit(text, [380, 0])


def pause():
    """


    In game pause screen

    Displays options (continue or quit). Continue closes the pause screen and continues the game where it
    left off. Quit option closes pause menu and calls game_intro() function.

    Cites
    -----
    https://www.youtube.com/playlist?list=PL6gx4Cwl9DGAjkwJocj7vlc_mFU-4wXJq
    """
    paused = True

    message_to_screen("Paused", -100, "large")
    message_to_screen("Press C to Continue or Q to Quit", 50, "medium")
    pygame.display.update()

    while paused:

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    paused = False
                    game_intro()
                elif event.key == pygame.K_c:
                    paused = False
            if event.type == pygame.QUIT:
                exit()
                paused = False
                break

        clock.tick(5)


def button(msg, x, y, width, height, inactive, active, action=None):
    """


    Button maker

    Funtion for making the buttons that are used throughout the game. Includes visual properties as well as indicators
    for what the button does which then calls specific functions.

    Parameters
    ----------
        msg : str
        The text to be placed in the button

        x : int
        x position of button on screen

        y : int
        y position of button on screen

        width : int
        width of button

        height : int
        height of button

        inactive : tuple
        Tuple of integer values for rgb of button when mouse is not hovering over it

        active : tuple
        Tuple of integer values for rgb of button when mouse is hovering over it

        action: str, optional
        String to indicate what the button would do

    Cites
    -----
    https://www.youtube.com/playlist?list=PL6gx4Cwl9DGAjkwJocj7vlc_mFU-4wXJq
    """

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(screen, active, (x, y, width, height))
        if click[0] == 1 and action != None:
            if action == "Info":
                information()
            if action == "Play":
                modes()
            if action == "Back":
                game_intro()
            if action == "Quit":
                exit()
            if action == "Normal":
                normal()
            if action == "Hard":
                hard()
    else:
        pygame.draw.rect(screen, inactive, (x, y, width, height))
    text_to_button(msg, black, x, y, width, height)


def game_intro():
    """


    Home Screen Page

    Page with options for what the player can do. Has buttons for quitting,
    play (calls the modes() function) and information (calls the information() function)
    """
    intro = True
    while intro:
        screen.blit(bg, (0, 0))
        message_to_screen("FRUIT CATCHER", -100, "large", dark_green)

        button("PLAY", 50, 500, 100, 50, dark_green, bright_green, action="Play")
        button("INFO", 200, 500, 100, 50, dark_yellow, bright_yellow, action="Info")
        button("QUIT", 350, 500, 100, 50, dark_red, bright_red, action="Quit")
        pygame.display.update()
        clock.tick(15)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
                intro = False
                break


def information():
    """


    Information Page

    Page with instructions on how the game works. Button for back calls the game_intro() function
    """
    info = True
    while info:
        screen.blit(bg, (0, 0))
        message_to_screen("INFORMATION", -300, "large", dark_green,)
        message_to_screen("Objective", -200, "medium")
        message_to_screen("Catch as many Fruits as you can", -150)
        message_to_screen("by moving the Basket", -100)
        message_to_screen("But Watch Out! You only get 3 LIVES!", -50)
        message_to_screen("Controls", 0, "medium")
        message_to_screen("Move Left: Move Marker Left", 50)
        message_to_screen("Move Right: Move Marker Right", 100)
        message_to_screen("Pause: Press P", 150)

        button("BACK", 200, 600, 100, 50, dark_yellow, bright_yellow, action="Back")
        pygame.display.update()
        clock.tick(15)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
                info = False
                break


def modes():
    """


    Game mode selector

    Selector screen for Normal and Hard modes. Menu with buttons and descriptions of each gamemode. Clicking button
    calls the specified game mode's function (normal() and hard()).
    """
    mode = True
    while mode:
        screen.blit(bg, (0, 0))
        message_to_screen("CHOOSE MODE", -300, "large", dark_green, )
        message_to_screen("Normal mode is plain at regular speed", -150)
        message_to_screen("with basic controls", -100)
        message_to_screen("All controls are now flipped", 50)
        message_to_screen("Move Left: Move Marker Right", 100)
        message_to_screen("Move Right: Move Marker Left", 150)
        message_to_screen("Everything is also FASTER", 200)
        message_to_screen("GOOD LUCK!", 250)

        button("NORMAL", 190, 175, 120, 50, dark_green, bright_green, action="Normal")
        button("HARD", 200, 375, 100, 50, dark_red, bright_red, action="Hard")
        pygame.display.update()
        clock.tick(15)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
                mode = False
                break


def normal():
    """


    Normal game mode

    Video input determines move value. Based on move value, the basket moves in the direction of the value.
    Random fruits (apples, strawberries, pineapples) are generated and put into the fruit list. When fruit hits
    basket, it is removed from the list and score is added to total score. When fruit hits the floor, it is taken out
    of the list and lives is decreased. When game is lost, there is an option to restart the game or go back to main
    menu.

    Cites
    -----
    https://codereview.stackexchange.com/questions/73847/simple-random-falling-object-animation-in-java
        used as example when making falling code in Python
    https://stackoverflow.com/questions/20102075/move-car-horizontal-python-classes
        used for basket movement
    https://www.youtube.com/playlist?list=PLlEgNdBJEO-lwI_F15DAQmgmqh5E7OYt_
        used for collisions and walls
    https://www.youtube.com/watch?v=K9qMm3JbOH0
        used for hitboxes and movement
    """

    scores = 0
    lives = 3
    fruits = []
    fruit_counter = 0
    add_fruit_rate = 75
    basket = Basket(display_width * 0.35, display_height - 160)
    play = True
    restart = False

    while play:

        if restart:
            message_to_screen("GAME OVER", -50, "large")
            message_to_screen("YOU ARE BAD", 0, "large")
            message_to_screen("Press R to Restart or Q to Quit", 50, "medium")
            pygame.display.update()

        while restart:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        play = False
                        restart = False
                        game_intro()
                    if event.key == pygame.K_r:
                        normal()
                if event.type == pygame.QUIT:
                    exit()
                    play = False
                    break

        direction = ObjectDetection.get_move(webcam)
        keys = pygame.key.get_pressed()

        if direction == 1 and basket.x > basket.vel - 5:
            basket.x -= .3 * basket.vel
        elif direction == 2 and basket.x < 500 - 150 - basket.vel:
            basket.x += .3 * basket.vel

        elif keys[pygame.K_p]:
            pause()

        screen.blit(bg, (0, 0))
        fruit_counter += 1

        if fruit_counter == add_fruit_rate:
            fruit_counter = 0
            f_startx = random.randrange(100, display_width - 100)
            f_starty = 0
            f_type = random.randrange(0, 3)

            if f_type == 0:
                new_fruit = Strawberry(f_startx, f_starty)
            elif f_type == 1:
                new_fruit = Apple(f_startx, f_starty)
            else:
                new_fruit = Pineapple(f_startx, f_starty)

            fruits.append(new_fruit)

        for item in fruits:
            item.draw(screen)
            item.y += .5 * item.vel

        for item in fruits[:]:
            if (item.hitbox[0] >= basket.hitbox[0] - 90) and (item.hitbox[0] <= basket.hitbox[0] + 90):
                if basket.hitbox[1] - 50 <= item.hitbox[1] <= basket.hitbox[1] - 20:
                    fruits.remove(item)
                    scores += item.points

            if (item.y >= display_height - 50) and (item.y <= display_height + 100):
                if display_height - 150 <= item.y <= display_height - 40:
                    if lives >= 2:
                        fruits.remove(item)
                        lives -= 1

                    else:
                        restart = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
                play = False

        score(scores)
        life(lives)
        basket.draw(screen)
        pygame.display.update()
        clock.tick(60)


def hard():
    """


    Hard game mode

    Video input determines move value. Based on move value, the basket moves in the opposite direction to the value.
    Random fruits (apples, strawberries, pineapples) are generated and put into the fruit list. When fruit hits basket,
    it is removed from the list and score is added to total score. When fruit hits the floor, it is taken out of the
    list and lives is decreased. When game is lost, there is an option to restart game or go back to main menu.

    Cites
    -----
    https://codereview.stackexchange.com/questions/73847/simple-random-falling-object-animation-in-java
        used as example when making falling code in Python
    https://stackoverflow.com/questions/20102075/move-car-horizontal-python-classes
        used for basket movement
    https://www.youtube.com/playlist?list=PLlEgNdBJEO-lwI_F15DAQmgmqh5E7OYt_
        used for collisions and walls
    https://www.youtube.com/watch?v=K9qMm3JbOH0
        used for hitboxes and movement
    """

    scores = 0
    lives = 3
    fruits = []
    fruit_counter = 0
    add_fruit_rate = 45
    basket = Basket(display_width * 0.35, display_height - 160)
    play = True
    restart = False

    while play:

        if restart:
            message_to_screen("GAME OVER", -50, "large")
            message_to_screen("YOU ARE BAD", 0, "large")
            message_to_screen("Press R to Restart or Q to Quit", 50, "medium")
            pygame.display.update()

        while restart:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        play = False
                        restart = False
                        game_intro()
                    if event.key == pygame.K_r:
                        hard()
                if event.type == pygame.QUIT:
                    exit()
                    play = False
                    break

        direction = ObjectDetection.get_move(webcam)
        keys = pygame.key.get_pressed()

        if direction == 2 and basket.x > basket.vel - 5:
            basket.x -= basket.vel
        elif direction == 1 and basket.x < 500 - 150 - basket.vel:
            basket.x += basket.vel
        elif keys[pygame.K_p]:
            pause()

        screen.blit(bg, (0, 0))
        fruit_counter += 1

        if fruit_counter == add_fruit_rate:
            fruit_counter = 0
            f_startx = random.randrange(100, display_width - 100)
            f_starty = 0
            f_type = random.randrange(0, 3)

            if f_type == 0:
                new_fruit = Strawberry(f_startx, f_starty)
            elif f_type == 1:
                new_fruit = Apple(f_startx, f_starty)
            else:
                new_fruit = Pineapple(f_startx, f_starty)

            fruits.append(new_fruit)

        for item in fruits:
            item.draw(screen)
            item.y += 1.13 * item.vel

        for item in fruits[:]:
            if (item.hitbox[0] >= basket.hitbox[0] - 90) and (item.hitbox[0] <= basket.hitbox[0] + 90):
                if basket.hitbox[1] - 50 <= item.hitbox[1] <= basket.hitbox[1] - 20:
                    fruits.remove(item)
                    scores += item.points

            if (item.y >= display_height - 50) and (item.y <= display_height + 100):
                if display_height - 150 <= item.y <= display_height - 40:
                    if lives >= 2:
                        fruits.remove(item)
                        lives -= 1

                    else:
                        restart = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
                play = False

        score(scores)
        life(lives)
        basket.draw(screen)
        pygame.display.update()
        clock.tick(60)


game_intro()
normal()