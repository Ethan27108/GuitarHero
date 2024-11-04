from PIL import ImageGrab
from PIL import Image
import pygame
from Button import Button
import random
import time


def clickedOn(colourClick):
    for i in buttonList:
        if (i.colour==colourClick):
            temp=buttonList.index(i)
            del buttonList[temp]
            break





interval=110
nextButton=0
buttonList=[]
green = (0,255,0)
blue=(0,0,255)
yellow=(255,255,0)
red=(255,0,0)
black=(0,0,0)
white=(255,255,255)

pygame.init() 
font = pygame.font.Font('freesansbold.ttf', 24)
clock = pygame.time.Clock()
window=pygame.display.set_mode((500,500))
streak=0
score=0
streakLim=False
startTime=time.time()
running = True
while running: 
    #stopping process
    for event in pygame.event.get():  
        
            
        if event.type == pygame.QUIT: 
            print(score)
            running=False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                streakLim=False
                # Capture a specific region (left, top, right, bottom) 
                screenshot = ImageGrab.grab(bbox=(710, 290, 1210, 780))

                screenshot.save("testingplace.png")

                img = Image.open('testingplace.png')
                img.convert('RGB')
                
                x, y = pygame.mouse.get_pos()
                if(((x>75)and(x<125))and((y>375)and(y<430))):
                    for i in range(50):
                        for y in range(55):
                            r,g,b=img.getpixel((75+i,375+y))
                            if ((r,g,b)==(green))and(streakLim==False):
                                score+=(1+streak)
                                streak+=1
                                streakLim=True
                            elif ((r,g,b)==(green)):
                                score+=(1+streak)
                    if (streakLim==False):
                        streak=0
                    else:
                        clickedOn(green)
                elif(((x>175)and(x<225))and((y>375)and(y<430))):
                    for i in range(50):
                        for y in range(55):
                            r,g,b=img.getpixel((175+i,375+y))
                            if ((r,g,b)==(red))and(streakLim==False):
                                score+=(1+streak)
                                streak+=1
                                streakLim=True
                            elif ((r,g,b)==(red)):
                                score+=(1+streak)
                    if (streakLim==False):
                        streak=0
                    else:
                        clickedOn(red)
                elif(((x>275)and(x<325))and((y>375)and(y<430))):
                    for i in range(50):
                        for y in range(55):
                            r,g,b=img.getpixel((275+i,375+y))
                            if ((r,g,b)==(yellow))and(streakLim==False):
                                score+=(1+streak)
                                streak+=1
                                streakLim=True
                            elif ((r,g,b)==(yellow)):
                                score+=(1+streak)
                    if (streakLim==False):
                        streak=0
                    else:
                        clickedOn(yellow)
                elif(((x>375)and(x<420))and((y>375)and(y<430))):
                    for i in range(50):
                        for y in range(55):
                            r,g,b=img.getpixel((375+i,375+y))
                            if ((r,g,b)==(blue))and(streakLim==False):
                                score+=(1+streak)
                                streak+=1
                                streakLim=True
                            elif ((r,g,b)==(blue)):
                                score+=(1+streak)
                    if (streakLim==False):
                        streak=0
                    else:
                        clickedOn(blue)

            
            
            # Close the screenshot
            
            screenshot.close()    
    if (time.time()-startTime)>=60:
            print(score)
            running=False
    elif (time.time()-startTime)>=50:
        interval=60
    elif (time.time()-startTime)>=40:
        interval=70
    elif (time.time()-startTime)>=30:
        interval=80
    elif (time.time()-startTime)>=20:
        interval=90
    elif (time.time()-startTime)>=10:
        interval=100        
    pygame.draw.rect(window, (black),[0, 0, 500, 500], 0)  
    pygame.draw.rect(window, (white),[0, 375, 500, 5], 0)   
    pygame.draw.rect(window, (white),[0, 430, 500, 5], 0) 
    
    for i in range (4):
        i+=1
        pygame.draw.circle(window, (white),
                        [100*i, 405], 30, 0)  
        pygame.draw.circle(window, (black),
                        [100*i, 405], 27.5, 0)  
    nextButton+=1
    if (nextButton>=interval):
            nextButton=0
            colour=random.randint(1,4)
            obj=Button(colour)
            buttonList.append(obj)
    for i in buttonList:
        i.y+=1
        pygame.draw.circle(window, (i.colour),
                    [i.x, i.y], 25, 0)
        if i.y>=460:
            temp=buttonList.index(i)
            del buttonList[temp]
            streak=0
    text = font.render("Score: "+str(score), True, white)
    textRect = text.get_rect()
    textRect.center = (250, 25)
    window.blit(text, textRect)       
    text = font.render("Streak: "+str(streak), True, white)
    textRect = text.get_rect()
    textRect.center = (250, 50)
    window.blit(text, textRect)   
        
    pygame.time.delay(10)
    pygame.display.update()
    