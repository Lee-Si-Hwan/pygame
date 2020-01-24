import pygame 

pygame.init()#pygame 초기화

#pygame에서 사용할 전역변수 선언 (주로 색깔,위치,화면설정 등을 사용)
#사용할 색깔 RGB 
black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)
green = (0,255,0)
red = (255,0,0)

#맵의 사이즈와 실행
size = [400,300]#[x,y]
screen = pygame.display.set_mode(size)#GUI창 만들어줌

pygame.display.set_caption("Game Title")#창의 이름을 설정해줌

done = False
clock = pygame.time.Clock()#화면을 초당 몆 번 출력하는가를 설정해줌

###########################

while not done:
    clock.tick(10)#clock함수를 통해 초당 프레임을 설정해주는 라인
                    # 이 뜻은 초당 10번의 화면을 출력해주겠다는 의미
                     #보통 10 혹은 30 혹은 60이 가장 좋음

    for event in pygame.event.get(): #pygame.event.get()함수를 통해 게임 중간에 어떤 이벤트가 발생했는지 for문을 통해 검사하는 구조
        if event.type == pygame.QUIT:#QIUT값은 창의 'X'를 누르면 발생하는 이벤트
            done = True #메인루프의 while 문이 더이상 돌아가지 않도록 바꿈 (일종의 안전장치)



    screen.fill(white)#fill함수는 화면전체를 특정 색깔로 채워줌
    pygame.draw.polygon(screen, green, [[30,150], [125,100], [220,150]], 5)
    pygame.draw.polygon(screen, green, [[30,150], [125,100], [220,150]], 0)
    pygame.draw.lines(screen, red, False, [[50,150], [50,250], [200,250], [200,150]], 5)
    pygame.draw.rect(screen, black, [75, 175, 75, 50], 5)
    pygame.draw.rect(screen, blue, [75, 175, 75, 50], 0)
    pygame.draw.line(screen, black, [112, 175], [112, 225], 5)
    pygame.draw.line(screen, black, [75, 200], [150, 200], 5)


    pygame.display.update()#현제 작성한 모든 행위를 업데이트 해주는 함수(반드시 써야함)



pygame.quit()









    
