import pygame
import pygame_textinput
from questions import question
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 550
QUES_WIDTH = (SCREEN_WIDTH//2) + 30
QUES_HEIGHT = SCREEN_HEIGHT - (SCREEN_HEIGHT-32)
COLOR_WHITE = (255,255,255)
COLOR_BLACK = (0,0,0)
COLOR_RED = (255, 0, 0)
ans = ['bill gates', 'elon musk', 'satya nadella', 'sundar pichai', 'mukesh ambani', 'lloyd blankfein', 'larry page', 'sergey brin','valentina tereshkova', 'yuri gagarin']

hints = ['Founder of Microsoft',
         'CEO of Tesla, SpaceX, The Boring Company',
         'CEO of Microsoft',
         'CEO of Google',
         'CEO of Reliance Industries',
         'ex-CEO of Goldman Sachs',
         'Founder of Google',
         'Co-Founder of Google',
         'First Woman in space',
         'First Man in Space'
         ]

score = 0


def load_image(num):
    image = pygame.image.load("images//1.png")
    return image

def show_txt(string):
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render(string, True, COLOR_BLACK)
    return text

def text_objects(text, font, surf, color):
    surf = pygame.Surface(font.size(text))
    surf.fill(COLOR_WHITE)
    textSurface = font.render(text, True, color, surf)
    return textSurface, textSurface.get_rect()


def main():
    global score
    end = False
    correct = ""
    curr_ques = 1
    pygame.init()
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    pygame.display.set_caption("Image Quiz!")

    ques = question(curr_ques)

    answer = pygame_textinput.TextInput()

    score_txt = show_txt("Score: " + str(score))
    hint = ""

    running = True

    img, txt = ques.gen_ques()

    sub_button = pygame.Rect(QUES_WIDTH, QUES_HEIGHT + 100, 150, 50)
    hint_btn = pygame.Rect(QUES_WIDTH, QUES_HEIGHT + 350, 150, 50)

    while running:
        smallText = pygame.font.Font("freesansbold.ttf",20)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                if sub_button.collidepoint(mouse_pos):

                    usr_answer = (answer.get_text()).lower()
                    if ans[curr_ques-1] == usr_answer:
                        curr_ques += 1
                        if curr_ques <= 10: 
                            hint = ""
                            print("Correct")
                            correct = "Correct!"                     
                            score += 1
                            score_txt = ("Score: " + str(score))
                            textSurf2, textRect2 = text_objects(correct, smallText, screen, (0, 200, 0))
                            textRect2.center = (QUES_WIDTH + 40, QUES_HEIGHT + 300)
                            screen.blit(textSurf2, textRect2)
                            ques = question(curr_ques)
                            img, txt = ques.gen_ques()                           
                        else:
                            hint = ""
                            print("Correct")
                            correct = "Correct!"                     
                            score += 1
                            score_txt = ("Score: " + str(score))
                            textSurf2, textRect2 = text_objects(correct, smallText, screen, (0, 200, 0))
                            textRect2.center = (QUES_WIDTH + 40, QUES_HEIGHT + 300)
                            screen.blit(textSurf2, textRect2)
                            end = True
                            break
                            # running = False                                                       
                    else:
                        if curr_ques <= 10:
                            hint = ""
                            print("Wrong")
                            correct = "Wrong!"
                            time.sleep(0.5)
                            curr_ques += 1                      
                            ques = question(curr_ques)
                            img, txt = ques.gen_ques()
                        else:
                            hint = ""
                            print("Wrong")
                            correct = "Wrong!"                     
                            score += 1
                            score_txt = ("Score: " + str(score))
                            textSurf2, textRect2 = text_objects(correct, smallText, screen, (200, 0, 0))
                            textRect2.center = (QUES_WIDTH + 40, QUES_HEIGHT + 300)
                            screen.blit(textSurf2, textRect2)
                            end = True
                            break   

                if hint_btn.collidepoint(mouse_pos):
                    hint = hints[curr_ques-1]
                    print(hint)     

            
        screen.fill(COLOR_WHITE)
        screen.blit(img, (0,0))

        screen.blit(txt, (QUES_WIDTH, QUES_HEIGHT))
        pygame.draw.rect(screen, (0, 100, 0), sub_button)
        pygame.draw.rect(screen, (0, 0, 200), hint_btn)


        if answer.update(events):
            print(answer.get_text())
            usr_answer = (answer.get_text()).lower()
                # time.sleep(40)
                # running = False            
            if ans[curr_ques-1] == usr_answer:
                curr_ques += 1
                hint = ""
                if curr_ques <= 10: 
                    print("Correct")
                    correct = "Correct!"                     
                    score += 1
                    score_txt = ("Score: " + str(score))
                    textSurf2, textRect2 = text_objects(correct, smallText, screen, (0, 200, 0))
                    textRect2.center = (QUES_WIDTH + 40, QUES_HEIGHT + 300)
                    screen.blit(textSurf2, textRect2)
                    ques = question(curr_ques)
                    img, txt = ques.gen_ques()                          
                else:
                    print("Correct")
                    correct = "Correct!"                     
                    score += 1
                    score_txt = ("Score: " + str(score))
                    textSurf2, textRect2 = text_objects(correct, smallText, screen, (0, 200, 0))
                    textRect2.center = (QUES_WIDTH + 40, QUES_HEIGHT + 300)
                    screen.blit(textSurf2, textRect2)
                    end = True
                    
            else:
                curr_ques += 1
                hint = ""
                if curr_ques <= 10:
                    print("Wrong")
                    correct = "Wrong!"
                    time.sleep(0.5)                        
                    ques = question(curr_ques)
                    img, txt = ques.gen_ques()
                else:
                    print("Wrong")
                    correct = "Wrong!"                     
                    score += 1
                    score_txt = ("Score: " + str(score))
                    textSurf2, textRect2 = text_objects(correct, smallText, screen, (200, 0, 0))
                    textRect2.center = (QUES_WIDTH + 40, QUES_HEIGHT + 300)
                    screen.blit(textSurf2, textRect2)
                    end = True
                                                    

        screen.blit(answer.get_surface(), (QUES_WIDTH, QUES_HEIGHT + 50))                                    


        textSurf, textRect = text_objects("Check", smallText, screen, COLOR_WHITE)
        textRect.center = (QUES_WIDTH + 70, QUES_HEIGHT+125)
        screen.blit(textSurf, textRect)

        textSurf3, textRect3 = text_objects(hint, smallText, screen, (200, 200, 200))
        textRect3.center = (SCREEN_WIDTH//2, (SCREEN_HEIGHT//2) + 200)
        screen.blit(textSurf3, textRect3)          

        textSurf, textRect = text_objects("Hint?", smallText, screen, COLOR_WHITE)
        textRect.center = (QUES_WIDTH + 70, QUES_HEIGHT+375)
        screen.blit(textSurf, textRect)

        textSurf2, textRect2 = text_objects(("Score: "+ str(score)), smallText, screen, COLOR_BLACK)
        textRect2.center = (QUES_WIDTH + 40, QUES_HEIGHT + 200)
        screen.blit(textSurf2, textRect2)

        if(end):
            time.sleep(1)
            running = False            

        if(correct == "Correct!"):
            textSurf2, textRect2 = text_objects(correct, smallText, screen, (0, 200, 0))
            textRect2.center = (QUES_WIDTH + 40, QUES_HEIGHT + 300)
            screen.blit(textSurf2, textRect2)
        elif(correct == "Wrong!"):
            textSurf2, textRect2 = text_objects(correct, smallText, screen, (200, 0, 0))
            textRect2.center = (QUES_WIDTH + 40, QUES_HEIGHT + 300)
            screen.blit(textSurf2, textRect2)
        else:
            textSurf2, textRect2 = text_objects(correct, smallText, screen, COLOR_BLACK)
            textRect2.center = (QUES_WIDTH + 40, QUES_HEIGHT + 300)
            screen.blit(textSurf2, textRect2)          

        pygame.display.update()
        clock.tick(30)
    
    pygame.quit()


if __name__ == "__main__":
    main()
