# Arden Boettcher
# Insert date here
# Insert title here

import pygame as pg
import sys
import config as c
from bounce import Square
pg.init()

class Main:
  def __init__(self):
    # Window
    self.screen = pg.display.set_mode((c.WIDTH, c.HEIGHT), pg.RESIZABLE)
    pg.display.set_caption("PLACEHOLDER")

    # Clock
    self.clock = pg.time.Clock()

    # Ship
    self.square = Square([c.WIDTH / 2, c.HEIGHT / 2])

    self.lines = pg.Surface((self.screen.get_width(), self.screen.get_height()))
    self.lines.fill((0, 0, 0))



  def run(self):
    # The bool for the main loop
    self.running = True

    dt = 0
    # Main loop
    while self.running:

      # Call events / update running
      self.main_events()

      new_line = self.square.update(dt)
      if new_line:
        pg.draw.line(self.lines, new_line[2], new_line[0], new_line[1])

      # Fills window
      self.screen.fill(c.BLACK)

      self.screen.blit(self.lines, (0, 0))

      self.square.draw(self.screen)

      # Updates the Display
      pg.display.flip()

      # Limits the framerate
      dt = self.clock.tick(c.FPS) / 1000

    # Close everything
    self.quit()

  def reset(self):
    self.square.go_back()
    self.lines = pg.Surface((self.screen.get_width(), self.screen.get_height()))

  # Event Handling
  def main_events(self):
    for event in pg.event.get():
      # Quits the game when you press the x
      if event.type == pg.QUIT:
        self.running = False
      elif event.type == pg.WINDOWRESIZED:
        self.reset()
      self.square.events(event)


  # Exits the code
  def quit(self):
    pg.quit()
    sys.exit()


if __name__ == "__main__":
  main = Main()
  main.run()
