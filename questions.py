import pygame

class question:
    ques_num = 0

    def __init__ (self, ques_no):
        self.ques_num = ques_no
    
    def load_image(self):
        img_location = "images//" + str(self.ques_num) + ".png"
        image = pygame.image.load(img_location)
        return image
    
    def show_txt(self, string):
        font = pygame.font.Font('freesansbold.ttf', 20)
        text = font.render(string, True, (0,0,0))
        return text   
    
    def gen_ques(self):
        req_img = self.load_image()
        req_str = ("Q" + str(self.ques_num) + ". Identify the person.")
        req_txt = self.show_txt(req_str)
        return req_img, req_txt