import glfw
from OpenGL.GL import *
import random
import time

if not glfw.init():
    exit()

window = glfw.create_window(800, 600, "Exercício", None, None)
if not window:
    glfw.terminate()
    exit()

glfw.make_context_current(window)

while not glfw.window_should_close(window):
    glfw.poll_events()

    if glfw.get_key(window, glfw.KEY_ESCAPE) == glfw.PRESS:
        glfw.set_window_should_close(window, True)

    # Cores aleatórias
    r, g, b = random.random(), random.random(), random.random()
    glClearColor(r, g, b, 1.0)

    glClear(GL_COLOR_BUFFER_BIT)
    glfw.swap_buffers(window)

    # Pausa de 0.5s para as cores trocarem devagar
    time.sleep(0.5)

glfw.terminate()