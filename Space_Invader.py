import sys
import time
from pygame import Vector2
from settings import settings
import random
from space_ship import Ship
from start_screen import start_screen
from high_score_screen import high_score_screen
from game_over_screen import game_over_screen
from fleet import Fleet
import pygame


class Space_Invader:

    def __init__(self):
        pygame.init()
        # Set up the music
        self.shoot_sound = pygame.mixer.Sound('music/8bit.wav')
        pygame.mixer.music.load('music/09 - Cherry Bomb.mp3')
        pygame.mixer.music.play(-1, 0.0)
        self.music_playing = True

        self.settings = settings()
        self.scene = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height), 0, 32)
        pygame.display.set_caption('Space Invader')
        self.fleet = Fleet(self.settings, self.shoot_sound)
        self.ship = Ship(self.settings)
        self.start_screen = start_screen(self.scene, Vector2(self.settings.screen_width, self.settings.screen_height), self.settings)
        self.high_score_screen = high_score_screen(self.scene, self.settings)
        self.game_over_screen = game_over_screen(self.settings, self.scene)

        # Set up the music
        self.shoot_sound = pygame.mixer.Sound('music/8bit.wav')
        pygame.mixer.music.load('music/09 - Cherry Bomb.mp3')
        pygame.mixer.music.play(-1, 0.0)
        self.music_playing = True

        self.new_game = True
        self.show_scores = False
        self.game_over = False
        self.round_count = 1

        self.scene_count = 0

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        if self.new_game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    button_clicked = self.start_screen.play_game_button.rect.collidepoint(mouse_pos)
                    if button_clicked:
                        self.new_game = False
                        self.show_scores = False
                        self.game_over = False
                    button_clicked = self.start_screen.high_score_button.rect.collidepoint(mouse_pos)
                    if button_clicked:
                        self.new_game = False
                        self.show_scores = True
        elif self.show_scores:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    button_clicked = self.high_score_screen.return_button.rect.collidepoint(mouse_pos)
                    if button_clicked:
                        self.new_game = True
                        self.show_scores = False
                        self.game_over = False
        elif self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    button_clicked = self.game_over_screen.button1.rect.collidepoint(mouse_pos)
                    if button_clicked:
                        self.show_scores = True
                        self.game_over = False
                        self.new_game = False
                        self.fleet = Fleet(self.settings)
                        self.ship = Ship(self.settings)
                    button_clicked = self.game_over_screen.button2.rect.collidepoint(mouse_pos)
                    if button_clicked:
                        self.show_scores = False
                        self.game_over = False
                        self.new_game = False
                        self.fleet = Fleet(self.settings)
                        self.ship = Ship(self.settings)
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
                #elif event.type == pygame.MOUSEBUTTONDOWN:
                 #   mouse_pos = pygame.mouse.get_pos()
                  #  self._check_play_button(mouse_pos)

    def _check_keydown_events(self, event):
        if self.new_game:
            pass
        elif self.show_scores:
            pass
        else:
            """Respond to keypresses."""
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = True
            elif event.key == pygame.K_q:
                sys.exit()
            elif event.key == pygame.K_SPACE:
                self.ship.shoot()
                self.shoot_sound.play()

    def _check_keyup_events(self, event):
        if self.new_game:
            pass
        elif self.show_scores:
            pass
        else:
            """Respond to key releases."""
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = False

    def alien_hit(self):
        for bullet in self.ship.gun.bullet_list:
            for alien in self.fleet.fleet:
                if alien.rect.colliderect(bullet):
                    self.ship.score.add(alien.score)
                    self.ship.gun.remove(bullet)
                    self.fleet.fleet.remove(alien)
                    self.fleet.speedup()
                    break

    def saucer_hit(self):
        for bullet in self.ship.gun.bullet_list:
            if self.fleet.saucer.rect.colliderect(bullet):
                self.ship.score.add(random.randint(self.settings.saucer_score_min, self.settings.saucer_score_max))
                self.ship.gun.remove(bullet)
                self.fleet.saucer.despawned = True

    def ship_hit(self):
        for bullet in self.fleet.gun.bullet_list:
            if self.ship.rect.colliderect(bullet):
                self.ship.life -= 1
                self.fleet.gun.remove(bullet)
            break

    def update(self):
        if self.new_game:
            pass
        elif self.show_scores:
            pass
        elif self.game_over:
            pass
        else:
            if len(self.fleet.fleet) == 0:
                self.ship.gun.reset()
                del self.fleet
                self.fleet = Fleet(self.settings)

            self.ship_hit()
            self.alien_hit()
            self.saucer_hit()
            self.fleet.out_of_bound(self.settings)
            self.fleet.move()
            self.ship.move()

    def draw(self):
        if self.new_game:
            self.scene.fill(self.settings.bg_color)
            self.start_screen.draw(self.scene, self.scene_count)
        elif self.show_scores:
            self.scene.fill(self.settings.bg_color)
            self.high_score_screen.draw()
        elif self.game_over:
            self.game_over_screen.draw()
        else:
            self.scene.fill(self.settings.bg_color)
            self.fleet.draw(self.scene, self.scene_count)
            self.ship.draw(self.scene, self.scene_count)
            self.ship.draw_life(self.scene, self.scene_count)

    def run_game(self):
        while True:
            self._check_events()
            self.update()
            self.draw()
            self.scene_count += 1

            if self.ship.life == 0:
                self.high_score_screen.save_score(self.ship.score.score)
                self.game_over = True

            pygame.display.update()
            time.sleep(0.1)

if __name__ == '__main__':
    # Make a game instance, and run the game.
    SI = Space_Invader()
    SI.run_game()