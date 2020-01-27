"""
Magnet Attorney!!!!!!!!

By editing the lines.txt file, you can change what the characters say, when background change,
the choice a player makes, and how these choices impact the rest of the story.

--------SYNTAX--------

DIALOGUE

[nickname]: [text]

EXAMPLE

P: hello world
This will make the character nicknamed "P" say, "hello world"



BACKGROUNDS

{[background_name]}


EXAMPLE

{my_wonderful_background}
This will display the background called my_wonderful_background



CHOICES

CHOICE n
- [choice 1] ([name 1])
- [choice 2] ([name 2])
...
- [choice n] [name n]


EXAMPLE

CHOICE 2
- study for midterms (study)
- go to sleep (sleep)
This will give the player a choice between studying and sleeping.

"""

import pygame

pygame.init()

# create a display
display_w = 640
display_h = 480
screen = pygame.display.set_mode((display_w, display_h), pygame.FULLSCREEN, 32)

# name the window
pygame.display.set_caption('Magnet Attorney!')

# define some colors
orange = [245, 138, 66]
green = [0, 255, 0]
white = [255, 255, 255]

# this will change when the code encounters a CHOICE in the text file
choices_to_read = 0


def line_to_code(line):
    """
    Reads the lines.txt file and returns a dictionary that translates the line into code.
    All returned dictionaries contain...
    a 'type' (whatever type of action it is)
    a 'condition' (if a certain condition is required before the action can be taken)
    and possibly more, depending on the 'type' of action
    """
    global choices_to_read
    line = line.strip()
    # first test if the action has a condition, indicated by brackets
    if len(line) > 0 and line[0] == '[':
        # if so, store the condition in a variable, then trash everything that was in brackets and continue as usual
        line = line[1:].split(']')
        condition = line[0]
        line = ']'.join(line[1:]).strip()
    else:
        condition = None

    # individual options within a choice
    if choices_to_read > 0:
        text, name = line.split('(')
        text = text[1:].strip()
        name = name[:-1]
        code = {'type': 'option', 'condition': condition, 'text': text, 'name': name}
        choices_to_read -= 1

    # blank line
    elif line == '':
        code = {'type': None, 'condition': condition}

    # end of file
    elif line == 'END':
        code = {'type': 'END', 'condition': condition}

    # background (indicated with braces)
    elif line[0] == '{':
        code = {'type': 'background', 'condition': condition, 'image': line[1:-1]}

    # a CHOICE. when this happens, store the number of options into a global variable
    elif line[0:6] == 'CHOICE':
        choices_to_read = int(line[7:])
        code = {'type': 'choice', 'condition': condition, 'num_options': choices_to_read}

    else:
        components = line.split(': ')
        code = {'type': 'speech', 'condition': condition, 'nick': components[0], 'line': components[1]}

    return code


# store the text file into a list
with open('lines.txt', 'r') as fin:
    lines = list(map(line_to_code, fin.readlines()))


# draw some text into an area of a surface
# automatically wraps words
# returns any text that didn't get blitted
# NOTE: THIS IS NOT MY CODE, SEE CITATIONS
def draw_text(surface, text, color, rect, font, aa=False, bkg=None):
    rect = pygame.Rect(rect)
    y = rect.top
    line_spacing = -2

    # get the height of the font
    font_height = font.size("Tg")[1]

    while text:
        i = 1

        # determine if the row of text will be outside our area
        if y + font_height > rect.bottom:
            break

        # determine maximum width of line
        while font.size(text[:i])[0] < rect.width and i < len(text):
            i += 1

        # if we've wrapped the text, then adjust the wrap to the last word
        if i < len(text):
            i = text.rfind(" ", 0, i) + 1

        # render the line and blit it to the surface
        if bkg:
            image = font.render(text[:i], 1, color, bkg)
            image.set_colorkey(bkg)
        else:
            image = font.render(text[:i], aa, color)

        surface.blit(image, (rect.left, y))
        y += font_height + line_spacing

        # remove the text we just blitted
        text = text[i:]

    return text


def draw_speech():
    """
    Read the current dictionary, assuming it's dialogue, and call the "say" function on the given character
    Note that characters are referred to by their nicknames, which are part of the dictionary and indicated before the
    colon.
    """
    global someone_speaking

    current_line = lines[scene]
    current_nick = current_line['nick']
    current_text = current_line['line']

    current_character = None

    for character in characters:
        if character.nick == current_nick:
            current_character = character
            break

    if current_character is None:
        print('You messed up, there\'s no valid speaker')
        pygame.quit()
        quit()

    else:
        current_character.say(current_text)

    someone_speaking = True


def change_background(background_name):
    """
    Iterate through the Background instances until one of the names matches the background_name paramter
    Then, set the current_background to that Background object.
    """
    global current_background
    for background in backgrounds:
        if background.name == background_name:
            current_background = background


backgrounds = []


# Background class is not completely my own code, SEE CITATIONS
class Background(pygame.sprite.Sprite):
    def __init__(self, name, image, location):
        pygame.sprite.Sprite.__init__(self)
        backgrounds.append(self)
        self.name = name
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


class Textbox:
    """
    Textbox objects start out with a size, but not a location
    Location is specificed in the Textbox.draw() function
    """
    def __init__(self, size, text=None, color=orange, name_color=orange):
        self.width, self.height = size
        self.color = color
        self.name_color = name_color

        text_font_size = int(7 * self.height / 24)
        name_font_size = int(7 * self.height / 48)
        self.text_font = pygame.font.Font('fnt/nasalization-rg.ttf', text_font_size)
        self.name_font = pygame.font.Font('fnt/nasalization-rg.ttf', name_font_size)

        # declare variables which will later store text surfaces
        self.x = None
        self.y = None
        self.text = text
        self.name = None
        self.rect = None

    def draw(self, location, with_name=True):
        """
        Draw the textbox at the given location.
        If the textbox should have a name, include one as well.
        """
        self.x, self.y = location
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, self.color, self.rect)
        if with_name:
            name_x = self.x
            name_y = self.y - self.height / 3
            name_width = self.width / 4
            name_height = self.height / 3
            name_rect = pygame.Rect(name_x, name_y, name_width, name_height)
            pygame.draw.rect(screen, self.color, name_rect)

    def write(self, with_name=True):
        """
        Write the Textbox.text string on the textbox.
        If a Textbox.name should be included, write that as well.
        """
        text_x = self.x + self.width/16
        text_y = self.y + self.height/16
        text_w = self.width * 7 / 8
        text_h = self.height
        text_rect = pygame.Rect(text_x, text_y, text_w, text_h)

        draw_text(screen, self.text, white, text_rect, self.text_font)
        if with_name:
            name_x = self.x + self.width/16
            name_y = self.y - 13 * self.height / 48
            name_w = self.width / 4
            name_h = self.height / 3
            name_rect = pygame.Rect(name_x, name_y, name_w, name_h)
            draw_text(screen, self.name, white, name_rect, self.name_font)


textbox1 = Textbox([display_w, display_h / 6])

characters = []


class Character:
    def __init__(self, name, nick):
        characters.append(self)
        self.name = name
        self.nick = nick

    def say(self, text, textbox=textbox1, with_name=True):
        """
        Send the specified text to the specified textbox.
        If the name should be displayed, tell the textbox who's speaking.
        """
        textbox.text = text
        if with_name:
            textbox.name = self.name


mouse_pressed = False


class Button:
    """
    All of the buttons in the game (so far) are just clickable textboxes, so the button boundaries are defined by
    their corresponding textboxes.
    All buttons are initialized with an 'output' message, which will be returned when they are clicked to identify them.
    """
    def __init__(self, textbox, output):
        self.textbox = textbox
        self.output = output

    def is_pressed(self):
        """
        if the button is onscreen and the mouse clicks on it, return the 'output' message
        otherwise, return None
        """
        mouse = pygame.mouse.get_pos()

        if self.textbox.rect != None and self.textbox.rect.collidepoint(mouse) and mouse_pressed == True:
            return self.output

        else:
            return None


class Choice:
    def __init__(self, num_options):
        self.num_options = num_options
        self.buttons = []

    def add_option(self, text, name):
        """
        add a new button to the current choice's list, to represent the new option.
        """
        button_textbox = Textbox([5 / 6 * display_w, 1 / 6 * display_h], text)
        output = name

        button = Button(button_textbox, output)
        self.buttons.append(button)


def change_scene():
    """
    go to the next dictionary, and draw/write anything that needs to be drawn/written.
    """
    global scene
    global option_bools
    global current_choice
    global enter_pressable

    mode = None

    # keep going until speech or dialogue
    while mode is None:

        # this is just to switch to the next dictionary
        # however, if the condition of the current dictionary is not met, skip it.
        while True:

            scene += 1
            code = lines[scene]

            if code['condition'] is None or code['condition'] in option_bools and option_bools[code['condition']]:
                break

        # change the background without pausing for input
        if code['type'] == 'background':
            change_background(code['image'])
            scene += 1
            code = lines[scene]

        # wait for user input on a black line
        if code['type'] == None:
            mode = 'pause'

        # end the game when 'END' is found
        if code['type'] == 'END':
            pygame.quit()
            quit()

        # draw speech. also, change the current 'mode' so that the game waits for an enter press to continue.
        if code['type'] == 'speech':
            draw_speech()

            mode = 'speech'

        # create a choice. also, change the current 'mode' so that the game waits for the player to choose an option.
        if code['type'] == 'choice':

            current_choice = Choice(code['num_options'])

            max_options = 3

            for i in range(max_options):
                scene += 1
                code = lines[scene]

                current_choice.add_option(code['text'], code['name'])
                option_bools[code['name']] = False

                next_code = lines[scene+1]

                if next_code['type'] != 'option':
                    break

            mode = 'choice'
            enter_pressable = False

    return mode




protag = Character('Protag', 'P')
larry = Character('Larry', 'C')
mystery = Character('???', '???')

keys = set()
just_pressed = set()



def get_keys(new_event):
    # when the user presses a key, add that key to the unordered set "keys"
    if new_event.type == pygame.KEYDOWN:
        keys.add(pygame.key.name(new_event.key))
        just_pressed.add(pygame.key.name(new_event.key))
    elif new_event.type == pygame.KEYUP:
        keys.remove(pygame.key.name(new_event.key))


# define images (okay this looks inefficient but i'll change it later)
pixel_magnet = Background('pixel_magnet', 'img/PixelMagnet.jpg', [0, 0])
pixel_magnet.image = pygame.transform.scale(pixel_magnet.image, (display_w, display_h))
opening_classroom = Background('opening_classroom', 'img/opening_classroom.jpg', [0, 0])
opening_classroom.image = pygame.transform.scale(opening_classroom.image, (display_w, display_h))
black = Background('black', 'img/black.jpg', [0, 0])
black.image = pygame.transform.scale(black.image, (display_w, display_h))
clock = Background('clock', 'img/clock.jpg', [0,0])
clock.image = pygame.transform.scale(clock.image, (display_w, display_h))

done = False

enter = False
enter_pressable = True

option_bools = {}
current_choice = None

scene = 0
scene_type = None
force_next_scene = False

current_background = pixel_magnet


while not done:

    # draw the background
    screen.blit(current_background.image, current_background.rect)

    for event in pygame.event.get():
        # stop running the code when the window is closed
        if event.type == pygame.QUIT:
            quit()

        # when the player left-clicks, change this boolean
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pressed = True
        else:
            mouse_pressed = False

        get_keys(event)  # see if the user is pressing any keys

    if 'escape' in keys:
        pygame.quit()
        quit()

    # go to the next scene if the player presses enter and they're allowed to continue
    if 'return' in just_pressed and enter_pressable or force_next_scene:
        scene_type = change_scene()
        force_next_scene = False

    # draw dialogue if the game is in "speech mode" (see the change_scene() function)
    if scene_type == 'speech':
        textbox1.draw((0, display_h * 2 / 3))
        textbox1.write()

    # draw options and test for a decision if the game is in "choice mode" (see the change_scene() function)
    elif scene_type == 'choice':
        for button in current_choice.buttons:
            option_textbox = button.textbox

            option_textbox_index = current_choice.buttons.index(button)

            option_textbox_x = 1/12 * display_w
            option_textbox_y = 1/4 * display_h * option_textbox_index + 1/6 * display_h

            option_textbox.draw([option_textbox_x, option_textbox_y], False)
            option_textbox.write(False)

            button_output = button.is_pressed()

            # if one of the options is clicked, immediately go to the next scene and allow the player to continue again.
            # plus, the boolean for the option they clicked gets set to True
            if button_output is not None:
                option_bools[button_output] = True
                force_next_scene = True
                enter_pressable = True
                break

    # flip the display
    pygame.display.flip()

    # ensures that some things only happen when a button was JUST pressed, (not held down)
    just_pressed.clear()
