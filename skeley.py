import pygame

class Game(object):
	def main(self, screen):
		clock = pygame.time.Clock()

		skeley = pygame.image.load('greenSkeleton.png')
		image = pygame.image.load('darksoldier.png')
		image_x = 400
		image_y = 240
		skeley_x = 200
		skeley_y = 240

		while 1:
			clock.tick(30)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return
				if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
					return

			#image_x += 1

			skeley_x += 10
			
			if skeley_x == 600:
				skeley_x -= 10
			
			if skeley_x == 10:
				skeley_x += 10
			

			key = pygame.key.get_pressed()
			if key[pygame.K_LEFT]:
				image_x -= 10
			if key[pygame.K_RIGHT]:
				image_x += 10
			if key[pygame.K_UP]:
				image_y -= 10
			if key[pygame.K_DOWN]:
				image_y += 10

			screen.fill((200, 200, 200))
			#screen.blit(image, (320, 240))
			screen.blit(skeley, (skeley_x, skeley_y))
			screen.blit(image, (image_x, image_y))
			pygame.display.flip()

if __name__ == '__main__':
	pygame.init()
	screen = pygame.display.set_mode((640, 480))
	Game().main(screen)