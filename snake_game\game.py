import pygame
import sys
import random

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()
        self.snake = [(200, 200), (220, 200), (240, 200)]
        self.direction = 'RIGHT'
        self.apple = self.set_apple()

    def set_apple(self):
        return (random.randint(0, 790) // 10 * 10, random.randint(0, 590) // 10 * 10)

    def play(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.direction != 'DOWN':
                        self.direction = 'UP'
                    elif event.key == pygame.K_DOWN and self.direction != 'UP':
                        self.direction = 'DOWN'
                    elif event.key == pygame.K_LEFT and self.direction != 'RIGHT':
                        self.direction = 'LEFT'
                    elif event.key == pygame.K_RIGHT and self.direction != 'LEFT':
                        self.direction = 'RIGHT'

            self.move_snake()
            self.check_collision()
            self.draw_game()

    def move_snake(self):
        head = self.snake[0]
        if self.direction == 'UP':
            new_head = (head[0], head[1] - 10)
        elif self.direction == 'DOWN':
            new_head = (head[0], head[1] + 10)
        elif self.direction == 'LEFT':
            new_head = (head[0] - 10, head[1])
        elif self.direction == 'RIGHT':
            new_head = (head[0] + 10, head[1])

        self.snake.insert(0, new_head)
        if self.snake[0] == self.apple:
            self.apple = self.set_apple()
        else:
            self.snake.pop()

    def check_collision(self):
        if (self.snake[0][0] < 0 or self.snake[0][0] > 790 or
            self.snake[0][1] < 0 or self.snake[0][1] > 590 or
            self.snake[0] in self.snake[1:]):
            pygame.quit()
            sys.exit()

    def draw_game(self):
        self.screen.fill((0, 0, 0))
        for pos in self.snake:
            pygame.draw.rect(self.screen, (0, 255, 0), pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(self.apple[0], self.apple[1], 10, 10))
        pygame.display.update()
        self.clock.tick(10)

if __name__ == '__main__':
    game = SnakeGame()
    game.play()