import sys
import pygame
from pygame.locals import QUIT

pygame.init()# 시작하기 전 무조건 위에 적어야 함

SURFACE = pygame.display.set_mode((400,300))#
pygame.display.set_caption("Just Window")

FPSCLOCK = pygame.time.Clock()

def main():
    """main roution"""
    sysfont = pygame.font.SysFont(None, 36)#글자 폰트 설정
    counter = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:#X버튼 눌렀을 때 끄는 조건문
                pygame.quit()
                sys.exit()

        counter += 1
        SURFACE.fill((0,0,0)) #배경 색칠
        count_image = sysfont.render(
            "count is {}".format(counter), True, (255, 255, 255))#글자 적는 함수
        SURFACE.blit(count_image, (50, 50)) #글자 배치
        
        pygame.display.update()
        FPSCLOCK.tick(100) #1초에 100번 출력

if __name__ == '__main__':
    main()
