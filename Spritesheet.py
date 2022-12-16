import pygame

class Spritesheet(pygame.sprite.Sprite):
    def __init__(self, filename, cols, rows, anim_speed, color_key = None):
        super().__init__()

        self.sheet = pygame.image.load(filename)
        if color_key:
            self.sheet = self.sheet.convert()
            self.sheet.set_colorkey(color_key)
        else:
            self.sheet = self.sheet.convert_alpha()

        w = self.sheet.get_width() / cols
        h = self.sheet.get_height() / rows

        self.counter = 0
        self.anim_speed = anim_speed
        self.index = 0
        self.cells = list([pygame.Rect(i % cols * w, (i // cols) * h, w, h) for i in range(cols * rows)])
        self.rect = self.cells[self.index]

        self.image = self.get_image()


    def get_image(self, colorkey=None):
        image = pygame.Surface(self.rect.size, pygame.SRCALPHA)
        image.blit(self.sheet, (0, 0), self.rect)

        return image

    def animate(self):
        self.counter += 1
        if self.counter >= self.anim_speed:
            self.counter = 0
            self.rect = self.cells[self.index % len(self.cells)]
            self.image = self.get_image()
            self.index += 1

    def animate_full(self, is_animated, iterations=1):
        self.counter += 1
        if (is_animated):
            if self.counter >= self.anim_speed:
                self.counter = 0
                if 0 <= self.index <= iterations * (2*len(self.cells) - 2):
                    if 0 <= self.index < len(self.cells):  
                        self.rect = self.cells[self.index % len(self.cells)]
                    else:
                        self.rect = self.cells[len(self.cells) + 3  - self.index]
                    self.image = self.get_image()
                    self.index += 1

                    print(self.index)
                    return True
                else:
                    self.index = 0
                    return False


    def draw(self, surface, x, y):
        surface.blit(self.sheet, (x, y), self.rect)