import Main
import pygame
import textwrap 
import time

white = Main.white
screen = Main.screen 
display_text = Main.display_text
font = Main.font
black = Main.black
dark_blue = Main.dark_blue
width = Main.width
height = Main.height
screen = Main.screen 
event_data = Main.event_data


'''
def get_multiple_line_numeric_input(line1, line2, line3):
    input_text = ""
    max_width = width - 20  # Maximum width for wrapped text
    lines = textwrap.wrap(line1 + " " + line2 + " " + line3, width=40)  # Wrap the question into lines

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    try:
                        result = int(input_text)
                        return result
                    except ValueError:
                        print("Error: Not a valid number")
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                elif event.key == pygame.K_ESCAPE:
                    return None
                else:
                    input_text += event.unicode

        screen.fill(white)

        y = (height - len(lines) * font.get_linesize()) // 2

        for line in lines:
            display_text(line, (width // 2, y), color=(0, 0, 0))
            y += font.get_linesize()

        # Display the entered text in dark blue
        display_text(input_text, (width // 2, y + font.get_linesize()), color=dark_blue)

        pygame.display.flip()
'''

def get_multiple_line_numeric_input(line1, line2, line3):

    input_text = ""
    while True: 
        screen.fill(white)
        display_text(line1, (width//2, 150))
        display_text(line2, (width//2, 180))
        display_text(line3, (width//2, 210))
        display_text(input_text, (width // 2, 250), color=dark_blue)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    try:
                        return int(input_text)
                    except ValueError:
                        print("Error: Not a valid number")
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                elif event.key == pygame.K_ESCAPE:
                    return None
                else:
                    input_text += event.unicode

            pygame.display.flip()


def get_numeric_input(question):
    input_text = ""
    max_width = width - 20  # Maximum width for wrapped text
    lines = textwrap.wrap(question, width=40)  # Wrap the question into lines

    while True:
        screen.fill(white)
        y = (height - len(lines) * font.get_linesize()) // 2

        for line in lines:
            display_text(line, (width // 2, y), font_size=36)
            y += font.get_linesize()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    try:
                        result = int(input_text)
                        return result
                    except ValueError:
                        print("error")
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode


def get_numeric_input_other(question1, question2, question3):
    input_text = ""
    while True:
        screen.fill(white)

        display_text(question1, (width // 2, height // 2 - 100), font_size=50)
        display_text(question2, (width // 2, height // 2 - 50), font_size=50)
        display_text(question3, (width // 2, height // 2), font_size=50)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    try:
                        result = int(input_text)
                        return result
                    except ValueError:
                        print("error")
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode
        screen.fill((255, 255, 255))
        text_surface = font.render(": " + input_text, True, (0, 0, 0))
        screen.blit(text_surface, (10, 10))
        pygame.display.update()





def display_event_data(event_data, start_index=0):
    page_size = 3  # Number of elements to display per page
    current_index = start_index
    max_text_width = width - 20  # Maximum width for wrapped text
    
    while True:
        screen.fill(white)
        display_text("Event Data", (width // 2, 120), font_size=40)

        # Display the event data for the current page
        y_position = 200
        for i in range(current_index, min(current_index + page_size, len(event_data))):
            event = event_data[i]

        
            event_text_one = f"{i + 1}: "  # Event number in dark blue and large font

            # Wrap the event text to prevent it from going off the screen
            wrapped_text = textwrap.fill(event_text_one, width=max_text_width, break_long_words=False)
            lines = wrapped_text.split('\n')
            
            for line in lines:
                display_text(line, (width // 2, y_position), color=dark_blue, font_size=40 if "1:" in line else 30)
                y_position += 40 if "1:" in line else 30  # Adjust the vertical spacing between lines

            # Additional event information
            if event[0] == "10 and under": 
                age = "10 & U"
            else: 
                age = event[0]
        
            if event[3] == "Butterfly": 
                stroke = "Fly"
            elif event[3] == "Freestyle": 
                stroke = "Free"
            elif event[3] == "Breastroke": 
                stroke = "Breast"
            elif event[3] == "Backstroke": 
                stroke = "Back"
            else: 
                stroke = "IM"

            length = event[2]
            heats = event[4]
            gender = event[1]

            # Display the additional event information in black and smaller font
            display_text(f"{age} {gender}" , (width // 2, y_position), color=black, font_size=30)
            y_position += 30
            display_text(f"{length} Y {stroke}", (width // 2, y_position), color=black, font_size=30)
            y_position += 30
            display_text(f"{heats} heats", (width // 2, y_position), color=black, font_size=30)
            y_position += 30

        # Display navigation buttons
        if current_index > 0:
            pygame.draw.rect(screen, dark_blue, (25, height - 70, 100, 40))
            display_text("Up", (75, height - 50), color=white)
        if current_index + page_size < len(event_data):
            pygame.draw.rect(screen, dark_blue, (width-125, height - 70, 100, 40))
            display_text("Down", (width-75, height - 50), color=white)
        pygame.draw.rect(screen, dark_blue, (width - 125, 20, 100, 40))
        display_text("Back", (width - 75, 40), color=white)
        pygame.draw.rect(screen, dark_blue, (25, 20, 100, 40))
        display_text("Edit Event", (75, 40), color=white)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 25 <= event.pos[0] <= 125 and height - 70 <= event.pos[1] <= height - 30:
                    # Up arrow clicked, go to the previous page
                    if current_index > 0:
                        current_index -= page_size
                elif width-125 <= event.pos[0] <= width-25 and height - 70 <= event.pos[1] <= height - 30:
                    # Down arrow clicked, go to the next page
                    if current_index + page_size < len(event_data):
                        current_index += page_size
                elif width - 125 <= event.pos[0] <= width - 25 and 20 <= event.pos[1] <= 60:
                    # Back button clicked
                    return "back"
                elif 25 <= event.pos[0] <= 125 and 20 <= event.pos[1] <= 60:
                    return "Edit Event"












def button_dialog_special(question, options, font_size_input=65):
    selected_option = None
    delay_start_time = None

    while True:
        screen.fill(white)
        display_text(question, (width // 2, height // 2 - 100), font_size=font_size_input)

        button_spacing = height // 10
        y_position = height // 2
        for index, option in enumerate(options):
            button_rect = pygame.Rect((width // 2) - 100, y_position, 200, 50)

            # Check if the button is selected (dark blue color)
            if option == selected_option:
                pygame.draw.rect(screen, dark_blue, button_rect)  # Change color to dark blue
            else:
                pygame.draw.rect(screen, black, button_rect)

            display_text(option, button_rect.center, white)
            y_position += button_spacing

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for index, option in enumerate(options):
                    button_rect = pygame.Rect((width // 2) - 100, (height // 2) + index * button_spacing, 200, 50)
                    if button_rect.collidepoint(event.pos):
                        selected_option = option
                        delay_start_time = time.time()

        if selected_option is not None:
            current_time = time.time()
            if current_time - delay_start_time >= 0.1:
                return selected_option

        pygame.display.flip()

def button_dialog_other(questionp1, questionp2, questionp3, options, Bspacing=80):
    selected_option = None
    delay_start_time = None

    while True:
        screen.fill(white)
        display_text(questionp1, (width // 2, height // 2 - 100))
        display_text(questionp2, (width // 2, height // 2 - 80))
        display_text(questionp3, (width // 2, height // 2 - 60))

        button_spacing = Bspacing
        y_position = height // 2
        for index, option in enumerate(options):
            button_rect = pygame.Rect((width // 2) - 100, y_position, 200, 50)

            # Check if the button is selected (dark blue color)
            if option == selected_option:
                pygame.draw.rect(screen, dark_blue, button_rect)  # Change color to dark blue
            else:
                pygame.draw.rect(screen, black, button_rect)

            display_text(option, button_rect.center, white)
            y_position += button_spacing

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for index, option in enumerate(options):
                    button_rect = pygame.Rect((width // 2) - 100, (height // 2) + index * button_spacing, 200, 50)
                    if button_rect.collidepoint(event.pos):
                        selected_option = option
                        delay_start_time = time.time()

        if selected_option is not None:
            current_time = time.time()
            if current_time - delay_start_time >= .1:
                return selected_option

        pygame.display.flip()


def button_dialog_spaced(question, options, Bspacing=55):
    wordSpacing = 30
    numberOfWords = 3
    scale = 0

    selected_option = None
    delay_start_time = None

    while True:
        screen.fill(white)
        display_text(question, (width // 2, 100))
        button_spacing = Bspacing
        y_position = height // 2 - 100
        heightOfRectangle = 50
        widthOfRectangle = 200
        for index, option in enumerate(options):
            button_rect = pygame.Rect((width // 2) - 100, y_position, widthOfRectangle, heightOfRectangle)

            # Check if the button is selected (dark blue color)
            if option == selected_option:
                pygame.draw.rect(screen, dark_blue, button_rect)  # Change color to dark blue
            else:
                pygame.draw.rect(screen, black, button_rect)

            display_text(option, button_rect.center, white)
            y_position += (button_spacing)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for index, option in enumerate(options):
                    button_rect = pygame.Rect((width // 2) - 100, height // 2 - 100 + index * (button_spacing), 200, 50)
                    if button_rect.collidepoint(event.pos):
                        selected_option = option
                        delay_start_time = time.time()

        if selected_option is not None:
            current_time = time.time()
            if current_time - delay_start_time >= .25:
                return selected_option

        pygame.display.flip()


def button_dialog(question, options, Bspacing = 30):
    wordSpacing = 30 
    numberOfWords = 3
    scale = 0

    while True:
        screen.fill(white)
        display_text(question, (width//2, height//2 - 100))

        button_spacing = Bspacing
        y_position = height // 2
        heightOfRectangle = 50
        widthOfRectangle = 200
        for option in options:
            button_rect = pygame.Rect((width//2) - 100, y_position, widthOfRectangle,heightOfRectangle)
            pygame.draw.rect(screen, black, button_rect)
            display_text(option, button_rect.center, white)
            y_position += (button_spacing)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for index, option in enumerate(options):
                    button_rect = pygame.Rect((width//2) - 100, (height//2) + index * (button_spacing), 200, 50)
                    if button_rect.collidepoint(event.pos):
                        return option


def button_dialog_columns(question, options_left, options_right):
    while True:
        screen.fill(white)
        display_text(question, (width//2, height//2 - 100))

        button_spacing = 100
        y_position = height // 2
        for left, right in zip(options_left, options_right):
            button_rect_left = pygame.Rect((width//2) - 200, y_position, 150, 50)
            pygame.draw.rect(screen, black, button_rect_left)
            display_text(left, button_rect_left.center, white)

            button_rect_right = pygame.Rect((width//2) + 50, y_position, 150, 50)
            pygame.draw.rect(screen, black, button_rect_right)
            display_text(right, button_rect_right.center, white)

            y_position += button_spacing

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for index, option in enumerate(options_left):
                    button_rect_left = pygame.Rect((width//2) - 200, (height//2) - 100 + index * button_spacing, 150, 50)
                    button_rect_right = pygame.Rect((width//2) + 50, (height//2) - 100 + index * button_spacing, 150, 50)
                    if button_rect_left.collidepoint(event.pos):
                        return option, options_right[index]
                    
