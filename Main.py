import Methods
import Data
import pygame
import sys
import textwrap
import time

event_data = []

# Initialize pygame
pygame.init()



# Set up display
width, height = 350, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("SwimCalculator")

# Set up colors
white = (255, 255, 255)
black = (100, 255, 204)
dark_blue = (0, 0, 128)

# Set up fonts
font = pygame.font.Font(None, 36)




def main():
    num_events = 0
    
    fontFactor1 = 30

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        newMeet = False
        collect = False

        screen.fill(white)
        display_text("SwimCalculator", (width//2, height//4), font_size=50) # this does not matter at all because of init
        if init() == "Start":
            newMeet = True


        #for event_index in range(num_events):
            #screen.fill(white)
            #display_text(f"Event {event_index + 1}", (width//2, 50), font_size=40)
        if newMeet == True:
            while newMeet == True:
                gender = get_gender_input()
                stroke = get_stroke_input()
                if stroke == "Freestyle": 
                    length = get_length_free()
                elif stroke == "IM":
                    length = get_length_IM()
                else:
                    length  = get_length()
                age_range = get_age_range_input()

                heats = get_numeric_input("How Many Heats Are There?")
                event_data.append((age_range, gender, length, stroke, heats))


                

                print (event_data)

               
                shouldICalculate = continue_or_not()
                if shouldICalculate == "No, Calculate":
                    print("recieved")
                    
                    
                    checkEventsOrCalc = Methods.button_dialog_other("Go directly to", "cacluations or" ,"check events?", ["Check Events", "Calculate"], 60)

                    while checkEventsOrCalc == "Check Events": 
                        backOrEdit = Methods.display_event_data(event_data)
                        if backOrEdit == "back": 
                            checkEventsOrCalc = Methods.button_dialog_other("Go directly to", "cacluations or" ,"check events?", ["Check Events", "Calculate"], 60)

                        elif backOrEdit == "Edit Event": 
                            replacingEventNumber = Methods.get_multiple_line_numeric_input("Enter the Event number" ,"of the event you", "want to replace:")
                            gender = get_gender_input()
                            stroke = get_stroke_input()
                            if stroke == "Freestyle": 
                                length = get_length_free()
                            elif stroke == "IM":
                                length = get_length_IM()
                            else:
                               length  = get_length()
                            age_range = get_age_range_input()

                            heats = get_numeric_input("How Many Heats Are There?")

                            list1 = list(event_data[replacingEventNumber - 1])
                            list1 = (age_range, gender, length, stroke, heats)
                            event_data[replacingEventNumber - 1] = tuple(list1)

                            checkEventsOrCalc = Methods.button_dialog_other("Go directly to", "cacluations or" ,"check events?", ["Check Events", "Calculate"], 60)

                    while checkEventsOrCalc == "Calculate":
                        delay_start_time = time.time()
                        starting_event = Methods.get_multiple_line_numeric_input("To calculate time" ,"interval, enter the", "starting event number:")
                        starting_heat = Methods.get_multiple_line_numeric_input("Now, enter the" ,"starting heat number", "of the first event:")
                        ending_event = Methods.get_multiple_line_numeric_input("To calculate time", "interval, enter" ,"ending event number")
                        ending_heat = Methods.get_multiple_line_numeric_input("Now, enter the last" ,"heat number of the last", "event you want in the calculation:")
                        result = Data.calculate(starting_event, starting_heat, ending_event, ending_heat, event_data)
                        if Methods.button_dialog_other("Your Total is...", f"{int(result/60)} minutes and", f"{int(result % 60)} seconds!!",  ["Great!!"], 40) == "Great!!":
                            shouldICalculate = continue_or_not()

                       
                        current_time = time.time()
                        if current_time - delay_start_time >= 5:
                            checkEventsOrCalc = Methods.button_dialog_other("Go directly to", "cacluations or" ,"check events?", ["Check Events", "Calculate"], 60)
                       
                    


                    screen.fill(white)
                    #pygame.time.delay(4000)
                    display_text("Collected Event Data", (width // 2, 50), font_size=40)

                    pygame.time.delay(5000)
                    y_position = 150
                    for event in event_data:
                        event_text = f"{event[0]} | {event[1]} {event[2]} | Age Range: {event[3]}"
                        display_text(event_text, (width // 2, y_position))
                        y_position += 50
                        pygame.time.delay(1000)
                        


            # Display collected event data

        pygame.display.flip()
        screen.fill(white)
        display_text("Collected Event Data", (width//2, 50), font_size=40)
        y_position = 150
        for event in event_data:
            event_text = f"{event[0]} | {event[1]} {event[2]} | Age Range: {event[3]}"
            display_text(event_text, (width//2, y_position))
            y_position += 50


        pygame.display.flip()

        # Display event data for 5 seconds



def display_text(text, position, color=black, font_size=30):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=position)
    screen.blit(text_surface, text_rect)

def get_numeric_input(question):
    display_text(question, (width//2, height//2 - 100),font_size=70)
    input_value = ""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and input_value:
                    return int(input_value)
                elif event.key == pygame.K_BACKSPACE:
                    input_value = input_value[:-1]
                else:
                    input_value += event.unicode

        screen.fill(white)
        display_text(question + ":" + str(input_value), (width//2, height//2))
        pygame.display.flip()



def init():
    return Methods.button_dialog_special("SwimCalculator", [ "Start"], 40)

def get_gender_input():
    return Methods.button_dialog_other("Women's (w) or" , "men's (m) event?", "", ["Women", "Men"], 55)

def get_stroke_input():
    return Methods.button_dialog_spaced("Stroke", ["Breaststroke", "Freestyle", "Butterfly" , "Backstroke", "IM" ], 55)

def get_length_free():
    return Methods.button_dialog_spaced("Length", ["50", "100", "200" , "400", "500", "1000", "1650"], 55)

def get_length_IM():
    return Methods.button_dialog_spaced("length", ["100", "200" , "400"], 55)

def get_length():
    return Methods.button_dialog_spaced("length", ["50", "100", "200"], 55)

def get_age_range_input():
    return Methods.button_dialog_other("Enter age range", "for event:", "", ["10 and under", "11-12", "13-14", "15-19"], 55)

    return Methods.button_dialog_special("SwimCalculator", ["Info/Help", "Start", "Stored Data"])

def get_gender_input():
    return Methods.button_dialog_other("Is it women's (w)", "or men's (m) event?", "", ["Women", "Men"])

def get_event_type_input():
    return Methods.button_dialog_columns("Select event type:", ["50", "100", "200", "400", "500", "800", "1000", "1650"], ["Breaststroke", "Backstroke", "Freestyle", "Butterfly"])

def get_age_range_input():
    return Methods.button_dialog_other("Enter the,", "age range of", "the swimmers:", ["10 and under", "11-12", "13-14", "15-19"],55)

def continue_or_not():
    return Methods.button_dialog_spaced("Add another event?", ["Yes", "No, Calculate"], 55)




if __name__ == "__main__":
    main()


