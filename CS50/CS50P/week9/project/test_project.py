import pytest  
import pygame  
from project import Screen, Game

# This ensures that any test that requires a Screen object can use this fixture to get a pre-configured screen.
@pytest.fixture  
def screen():
    pygame.init()
    screen = Screen()
    screen.create_screen()
    return screen

# This ensures that any test that requires a Game object will receive a pre-configured game instance with an already set-up screen.
@pytest.fixture  
def game(screen):
    return Game(screen)

def test_create_screen(screen):
    assert screen.screen is not None  
    assert screen.screen.get_width() == screen.screen_width  
    assert screen.screen.get_height() == screen.screen_height

def test_fill(screen):
    screen.fill()
    assert screen.screen.get_at((0, 0)) == screen.background_color

def test_update(screen):
    screen.update()
    # Simply looks for any assertion errors
    assert True

def test_quit(screen):
    screen.quit()
    assert not pygame.get_init()

def test_draw_snake(game):
    game.draw_snake()
    assert game.snake_body[0] == (game.screen_width / 2, game.screen_height / 2)

def test_get_snake_position(game):
    game.x, game.y = game.snake_body[0]
    assert game.get_snake_position() == (game.screen_width / 2, game.screen_height / 2)

def test_draw_food(game):
    game.draw_food()
    assert game.food_x is not None  
    assert game.food_y is not None  
    food_rect = pygame.Rect(game.food_x, game.food_y, 25, 25)
    assert game.screen.get_at((food_rect.x, food_rect.y)) == game.food_color

def test_update_position(game):
    initial_position = game.snake_body[0]

    # Adds a piece of food at the starting position so the snake is guaranteed to move
    game.food_x, game.food_y = initial_position  
    game.update_position()
    
    new_position = game.snake_body[0]
    assert new_position != initial_position

def test_check_collision_with_food(game):
    game.food_x, game.food_y = game.snake_body[0]  # Places a piece of food at the position of the snakes head
    assert game.check_collision_with_food()

def test_check_collision_with_self(game):
    # Makes the snake collide with itself
    game.snake_body.append(game.snake_body[0])
    assert game.check_collision_with_self()
