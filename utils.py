import pygame

def load_image(filename, transparent=True):
    """Function to reurn a image object."""
    try:
        image = pygame.image.load(filename)
    except pygame.error:
        raise SystemExit
    image = image.convert()
    if transparent:
        color = image.get_at((0, 0))
        image.set_colorkey(color, RLEACCEL)
    return image

def fText(text1, posx, posy, color=(255, 255, 255)):
    """Manage text box in pygame."""
    fuente = pygame.font.Font("images/DroidSans.ttf", 25)
    salida = pygame.font.Font.render(fuente, text1, 1, color)
    salida_rect = salida.get_rect()
    salida_rect.centerx = posx
    salida_rect.centery = posy
    return salida, salida_rect