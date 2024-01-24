from PIL import Image #it has a hard time with Qs
import pytesseract
import pyautogui
from re import sub
from time import sleep
import pygame
from sys import exit
# Rember to install python itself then imstall the following using the termal (pip install pillow pytesseract pyautogui pygame) also you need to download Tesseract set up here https://github.com/UB-Mannheim/tesseract/wiki (idk why its in the wiki part)
# all charater dectecting software credit all goes to TESSERACT tho a side note is that it takes like 10 years to find the setup for windows button
pygame.init()
background = pygame.image.load("screenshot.png")

pytesseract.pytesseract.tesseract_cmd = r'D:\Desktop\tesseract\tesseract.exe' # replace this where you put the tesseract.exe file location otherwise it will fail
filepath = 'D:/Desktop/takepic/fixer.txt'
#you can remove this if you want this is for it to click on area and type the code in
def remove_word(input_string, word_to_remove):
    # Replace the specified word with an empty string
    result_string = input_string.replace(word_to_remove, '')

    return result_string
def clickhandler(_input):
     pattern = r'[^a-zA-Z0-9\s]' 
     with open(filepath , mode='r+') as cont:
        cont.write(f'The X = {x}\nThe Y = {y}')

     result_string = sub(pattern, '', _input)
     result_string = remove_word(result_string,'CODE')
     print(result_string)
     click_x, click_y = 2000, 550
     pyautogui.click(click_x, click_y)
     sleep(0.1)
     click_x,click_y = 2200,940
     pyautogui.click(click_x,click_y)
     sleep(0.1)
     click_x, click_y = 2600, 940
     pyautogui.click(click_x, click_y)
     sleep(0.1)  
     pyautogui.write(result_string)

def take_screenshot_and_check_for_text(x, y, width, height):  
    global background
    pygame.display.flip()
    screenshot = pygame.surfarray.array3d(pygame.display.get_surface())
    screenshot = pyautogui.screenshot(region=(x, y, width, height))

    screenshot.save('screenshot.png')
    screenshot = Image.open('screenshot.png')
    background = pygame.image.load("screenshot.png")
    background = pygame.transform.scale(background, (800, 400))
    text = pytesseract.image_to_string(screenshot)
    screenshot.close()

    has_words = any(word.isalpha() for word in text.split())
    
        
    return has_words,text
x = 833
y = 73
width = 200
height = 100
screen = pygame.display.set_mode((800, 400))
input('start')
while True:
    try:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            y -= 2
            print('going up')
        if keys[pygame.K_DOWN]:
            y += 2
            print('going down')
        if keys[pygame.K_LEFT]:
            x-=2
            print('goingleft')
        if keys[pygame.K_RIGHT]:
            x +=2
            print('going right')
        contains_words, extracted_text = take_screenshot_and_check_for_text(x, y, width, height)
        screen.blit(background, (0, 0))
        if contains_words:
            print(extracted_text)
            clickhandler(extracted_text)
            break
    except KeyboardInterrupt:
         print('stopping')
         break
    except Exception as e:
        print("error at",e)

sleep(5)
pygame.quit()
exit()