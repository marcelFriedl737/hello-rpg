# Pygame Front Page — pygame v2.6.0 documentation

# Pygame Front Page[¶](#pygame-front-page "Permalink to this headline")

## Quick start[¶](#quick-start "Permalink to this headline")

Welcome to pygame! Once you've got pygame installed (`pip install pygame` or `pip3 install pygame` for most people), the next question is how to get a game loop running. Pygame, unlike some other libraries, gives you full control of program execution. That freedom means it is easy to mess up in your initial steps.

Here is a good example of a basic setup (opens the window, updates the screen, and handles events)--

\# Example file showing a basic pygame "game loop"
import pygame

\# pygame setup
pygame.init()
screen \= pygame.display.set\_mode((1280, 720))
clock \= pygame.time.Clock()
running \= True

while running:
    \# poll for events
    \# pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type \== pygame.QUIT:
            running \= False

    \# fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    \# RENDER YOUR GAME HERE

    \# flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  \# limits FPS to 60

pygame.quit()

Here is a slightly more fleshed out example, which shows you how to move something (a circle in this case) around on screen--

\# Example file showing a circle moving on screen
import pygame

\# pygame setup
pygame.init()
screen \= pygame.display.set\_mode((1280, 720))
clock \= pygame.time.Clock()
running \= True
dt \= 0

player\_pos \= pygame.Vector2(screen.get\_width() / 2, screen.get\_height() / 2)

while running:
    \# poll for events
    \# pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type \== pygame.QUIT:
            running \= False

    \# fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.circle(screen, "red", player\_pos, 40)

    keys \= pygame.key.get\_pressed()
    if keys\[pygame.K\_w\]:
        player\_pos.y \-= 300 \* dt
    if keys\[pygame.K\_s\]:
        player\_pos.y += 300 \* dt
    if keys\[pygame.K\_a\]:
        player\_pos.x \-= 300 \* dt
    if keys\[pygame.K\_d\]:
        player\_pos.x += 300 \* dt

    \# flip() the display to put your work on screen
    pygame.display.flip()

    \# limits FPS to 60
    \# dt is delta time in seconds since last frame, used for framerate-
    \# independent physics.
    dt \= clock.tick(60) / 1000

pygame.quit()

For more in depth reference, check out the [Tutorials](#tutorials-reference-label) section below, check out a video tutorial ([I'm a fan of this one](https://www.youtube.com/watch?v=AY9MnQ4x3zk)), or reference the API documentation by module.

## Documents[¶](#documents "Permalink to this headline")

[Readme](../wiki/about)

Basic information about pygame: what it is, who is involved, and where to find it.

[Install](../wiki/GettingStarted#Pygame%20Installation)

Steps needed to compile pygame on several platforms. Also help on finding and installing prebuilt binaries for your system.

[File Path Function Arguments](filepaths.html)

How pygame handles file system paths.

[Pygame Logos](logos.html)

The logos of Pygame in different resolutions.

[LGPL License](LGPL.txt)

This is the license pygame is distributed under. It provides for pygame to be distributed with open source and commercial software. Generally, if pygame is not changed, it can be used with any type of program.

## Tutorials[¶](#tutorials "Permalink to this headline")

[Introduction to Pygame](tut/PygameIntro.html)

An introduction to the basics of pygame. This is written for users of Python and appeared in volume two of the Py magazine.

[Import and Initialize](tut/ImportInit.html)

The beginning steps on importing and initializing pygame. The pygame package is made of several modules. Some modules are not included on all platforms.

[How do I move an Image?](tut/MoveIt.html)

A basic tutorial that covers the concepts behind 2D computer animation. Information about drawing and clearing objects to make them appear animated.

[Chimp Tutorial, Line by Line](tut/ChimpLineByLine.html)

The pygame examples include a simple program with an interactive fist and a chimpanzee. This was inspired by the annoying flash banner of the early 2000s. This tutorial examines every line of code used in the example.

[Sprite Module Introduction](tut/SpriteIntro.html)

Pygame includes a higher level sprite module to help organize games. The sprite module includes several classes that help manage details found in almost all games types. The Sprite classes are a bit more advanced than the regular pygame modules, and need more understanding to be properly used.

[Surfarray Introduction](tut/SurfarrayIntro.html)

Pygame used the NumPy python module to allow efficient per pixel effects on images. Using the surface arrays is an advanced feature that allows custom effects and filters. This also examines some of the simple effects from the pygame example, arraydemo.py.

[Camera Module Introduction](tut/CameraIntro.html)

Pygame, as of 1.9, has a camera module that allows you to capture images, watch live streams, and do some basic computer vision. This tutorial covers those use cases.

[Newbie Guide](tut/newbieguide.html)

A list of thirteen helpful tips for people to get comfortable using pygame.

[Making Games Tutorial](tut/MakeGames.html)

A large tutorial that covers the bigger topics needed to create an entire game.

[Display Modes](tut/DisplayModes.html)

Getting a display surface for the screen.

[한국어 튜토리얼 (Korean Tutorial)](tut/ko/%EB%B9%A8%EA%B0%84%EB%B8%94%EB%A1%9D%20%EA%B2%80%EC%9D%80%EB%B8%94%EB%A1%9D/%EA%B0%9C%EC%9A%94.html)

빨간블록 검은블록

## Reference[¶](#reference "Permalink to this headline")

[Index](genindex.html)

A list of all functions, classes, and methods in the pygame package.

[pygame.BufferProxy](ref/bufferproxy.html)

An array protocol view of surface pixels

[pygame.Color](ref/color.html)

Color representation.

[pygame.cursors](ref/cursors.html)

Loading and compiling cursor images.

[pygame.display](ref/display.html)

Configure the display surface.

[pygame.draw](ref/draw.html)

Drawing simple shapes like lines and ellipses to surfaces.

[pygame.event](ref/event.html)

Manage the incoming events from various input devices and the windowing platform.

[pygame.examples](ref/examples.html)

Various programs demonstrating the use of individual pygame modules.

[pygame.font](ref/font.html)

Loading and rendering TrueType fonts.

[pygame.freetype](ref/freetype.html)

Enhanced pygame module for loading and rendering font faces.

[pygame.gfxdraw](ref/gfxdraw.html)

Anti-aliasing draw functions.

[pygame.image](ref/image.html)

Loading, saving, and transferring of surfaces.

[pygame.joystick](ref/joystick.html)

Manage the joystick devices.

[pygame.key](ref/key.html)

Manage the keyboard device.

[pygame.locals](ref/locals.html)

Pygame constants.

[pygame.mixer](ref/mixer.html)

Load and play sounds

[pygame.mouse](ref/mouse.html)

Manage the mouse device and display.

[pygame.mixer.music](ref/music.html)

Play streaming music tracks.

[pygame](ref/pygame.html)

Top level functions to manage pygame.

[pygame.PixelArray](ref/pixelarray.html)

Manipulate image pixel data.

[pygame.Rect](ref/rect.html)

Flexible container for a rectangle.

[pygame.scrap](ref/scrap.html)

Native clipboard access.

[pygame.sndarray](ref/sndarray.html)

Manipulate sound sample data.

[pygame.sprite](ref/sprite.html)

Higher level objects to represent game images.

[pygame.Surface](ref/surface.html)

Objects for images and the screen.

[pygame.surfarray](ref/surfarray.html)

Manipulate image pixel data.

[pygame.tests](ref/tests.html)

Test pygame.

[pygame.time](ref/time.html)

Manage timing and framerate.

[pygame.transform](ref/transform.html)

Resize and move images.

[pygame C API](c_api.html)

The C api shared amongst pygame extension modules.

[Search Page](search.html)

Search pygame documents by keyword.

  
  

---

[Edit on GitHub](https://github.com/pygame/pygame/edit/main/docs/reST/index.rst)