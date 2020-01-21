import sys
import pygame

pygame.init()

# create a display
display_w = 640
display_h = 480
screen = pygame.display.set_mode((display_w, display_h), pygame.FULLSCREEN, 32)

# name the window
pygame.display.set_caption('Magnet Attorney!')

# define some colors
blue = [0, 0, 128]
green = [0, 255, 0]
white = [255, 255, 255]

# store the text file into a list
with open('lines.txt', 'r') as fin:
    lines_raw = list(map(lambda x: x.strip().split(': '), fin.readlines()))
    lines = []
    for line in lines_raw:
        if line == ['']:
            lines.append(None)
        elif line == ['END']:
            lines.append('END')
        else:
            lines.append({'nick': line[0], 'line': line[1]})


# draw some text into an area of a surface
# automatically wraps words
# returns any text that didn't get blitted
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


class Background(pygame.sprite.Sprite):
    def __init__(self, image, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


class Textbox:
    def __init__(self, size, color=blue, name_color=blue):
        self.width, self.height = size
        self.color = color
        self.name_color = name_color

        text_font_size = int(7 * self.height / 24)
        name_font_size = int(7 * self.height / 24)
        self.text_font = pygame.font.Font('freesansbold.ttf', text_font_size)
        self.name_font = pygame.font.Font('freesansbold.ttf', name_font_size)

        # declare variables which will later store text surfaces
        self.x = None
        self.y = None
        self.text = None
        self.name = None

    def draw(self, location, with_name=True):
        self.x, self.y = location
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, self.color, rect)
        if with_name:
            name_x = self.x
            name_y = self.y - self.height / 3
            name_width = self.width / 4
            name_height = self.height / 3
            name_rect = pygame.Rect(name_x, name_y, name_width, name_height)
            pygame.draw.rect(screen, self.color, name_rect)

    def write(self, with_name=True):
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
        textbox.text = text
        if with_name:
            textbox.name = self.name


def draw_scene(scene_number):
    current_line = lines[scene_number]
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

    global someone_speaking
    someone_speaking = True

protag = Character('Protag', 'P')
larry = Character('Larry', 'C')
mystery = Character('???', '???')

keys = set()
just_pressed = set()


def get_keys(new_event):
    if new_event.type == pygame.KEYDOWN:
        keys.add(pygame.key.name(new_event.key))
        just_pressed.add(pygame.key.name(new_event.key))
    elif new_event.type == pygame.KEYUP:
        keys.remove(pygame.key.name(new_event.key))


# define images
pixel_magnet = Background('img/PixelMagnet.jpg', [0, 0])
pixel_magnet.image = pygame.transform.scale(pixel_magnet.image, (display_w, display_h))
opening_classroom = Background('img/opening_classroom.jpg', [0, 0])
opening_classroom.image = pygame.transform.scale(opening_classroom.image, (display_w, display_h))
black = Background('img/black.jpg', [0, 0])
black.image = pygame.transform.scale(black.image, (display_w, display_h))

done = False

enter = False

scene = 0
someone_speaking = False

while not done:

    # draw the background
    current_background = pixel_magnet

    screen.blit(current_background.image, current_background.rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

        get_keys(event)

    if 'escape' in keys:
        pygame.quit()
        quit()

    # draw the textbox
    textbox1.draw((0, display_h * 2 / 3))

    if 'return' in just_pressed:
        scene += 1
        if lines[scene] is None:
            current_line = None
            current_nick = None
            current_text = None
            current_character = None

            someone_speaking = False

        elif lines[scene] == 'END':
            pygame.quit()
            quit()

        else:
            draw_scene(scene)

    if someone_speaking:
        textbox1.write()

    pygame.display.flip()

    just_pressed.clear()
