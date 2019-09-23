#*******************************#
#                               #
#   Random_Friend_Generator     #
#   by M. E. Rasmussen          #
#   Started 09. sep. 2019       #
#   Finished 18. sep. 2019      #
#                               #
#*******************************#

from data import Text
import random
import os

class Generator:
    def __init__ (self):
        self.dt = Text()
        self.random_ep = False
        self.episode = 0
        self.season = 0

    def s_1(self):
        self.season = 1
        if self.random_ep == True:
            self.episode = random.randint(1,24)
        else:
            self.episode = int(input('Input a number bettween 1 and 24, to select an episode in season 1:\n'))
            if self.episode < 1 or self.episode > 24:
                print("Invalid input")
                self.s_1()
        print(" ")
        print("Season 1, Episode " +str(self.episode))
        print("Episode Overall: " +str(self.episode))
        print("Title: " +str(self.dt.s_1_titles[self.episode -1]))
        print("Original Airdate: " +str(self.dt.s_1_original_airdate[self.episode -1]))
        print("Summary: " +str(self.dt.s_1_summary[self.episode -1]))
        print("Title, airdate and summery taken from friends.fandom.com")
        print(" ")
        self.play()
            

    def s_2(self):
        self.season = 2
        if self.random_ep == True:
            self.episode = random.randint(1,24)
        else:
            self.episode = int(input('Input a number bettween 1 and 24, to select an episode in season 2:\n'))
            if self.episode < 1 or self.episode > 24:
                print("Invalid input")
                self.s_2()
        print(" ")
        print("Season 2, Episode " +str(self.episode))
        print("Episode Overall: " +str(self.episode+24))
        print("Title: " +str(self.dt.s_2_titles[self.episode -1]))
        print("Original Airdate: " +str(self.dt.s_2_original_airdate[self.episode -1]))
        print("Summary: " +str(self.dt.s_2_summary[self.episode -1]))
        print("Title, airdate and summery taken from friends.fandom.com")
        print(" ")
        self.play()

    def s_3(self):
        self.season = 3
        if self.random_ep == True:
            self.episode = random.randint(1,25)
        else:
            self.episode = int(input('Input a number bettween 1 and 25, to select an episode in season 3:\n'))
            if self.episode < 1 or self.episode > 25:
                print("Invalid input")
                self.s_3()
        print(" ")
        print("Season 3, Episode " +str(self.episode))
        print("Episode Overall: " +str(self.episode+24+24))
        print("Title: " +str(self.dt.s_3_titles[self.episode -1]))
        print("Original Airdate: " +str(self.dt.s_3_original_airdate[self.episode -1]))
        print("Summary: " +str(self.dt.s_3_summary[self.episode -1]))
        print("Title, airdate and summery taken from friends.fandom.com")
        print(" ")
        self.play()

    def s_4(self):
        self.season = 4
        if self.random_ep == True:
            self.episode = random.randint(1,24)
        else:
            self.episode = int(input('Input a number bettween 1 and 24, to select an episode in season 4:\n'))
            if self.episode < 1 or self.episode > 24:
                print("Invalid input")
                self.s_4()
        print(" ")
        print("Season 4, Episode " +str(self.episode))
        print("Episode Overall: " +str(self.episode+24+24+25))
        print("Title: " +str(self.dt.s_4_titles[self.episode -1]))
        print("Original Airdate: " +str(self.dt.s_4_original_airdate[self.episode -1]))
        print("Summary: " +str(self.dt.s_4_summary[self.episode -1]))
        print("Title, airdate and summery taken from friends.fandom.com")
        print(" ")
        self.play()

    def s_5(self):
        self.season = 5
        if self.random_ep == True:
            self.episode = random.randint(1,24)
        else:
            self.episode = int(input('Input a number bettween 1 and 24, to select an episode in season 5:\n'))
            if self.episode < 1 or self.episode > 24:
                print("Invalid input")
                self.s_5()
        print(" ")
        print("Season 5, Episode " +str(self.episode))
        print("Episode Overall: " +str(self.episode+24+24+25+24))
        print("Title: " +str(self.dt.s_5_titles[self.episode -1]))
        print("Original Airdate: " +str(self.dt.s_5_original_airdate[self.episode -1]))
        print("Summary: " +str(self.dt.s_5_summary[self.episode -1]))
        print("Title, airdate and summery taken from friends.fandom.com")
        print(" ")
        self.play()

    def s_6(self):
        self.season = 6
        if self.random_ep == True:
            self.episode = random.randint(1,25)
        else:
            self.episode = int(input('Input a number bettween 1 and 25, to select an episode in season 6:\n'))
            if self.episode < 1 or self.episode > 25:
                print("Invalid input")
                self.s_6()
        print(" ")
        print("Season 6, Episode " +str(self.episode))
        print("Episode Overall: " +str(self.episode+24+24+25+24+24))
        print("Title: " +str(self.dt.s_6_titles[self.episode -1]))
        print("Original Airdate: " +str(self.dt.s_6_original_airdate[self.episode -1]))
        print("Summary: " +str(self.dt.s_6_summary[self.episode -1]))
        print("Title, airdate and summery taken from friends.fandom.com")
        print(" ")
        self.play()

    def s_7(self):
        self.season = 7
        if self.random_ep == True:
            self.episode = random.randint(1,24)
        else:
            self.episode = int(input('Input a number bettween 1 and 24, to select an episode in season 7:\n'))
            if self.episode < 1 or self.episode > 24:
                print("Invalid input")
                self.s_7()
        print(" ")
        print("Season 7, Episode " +str(self.episode))
        print("Episode Overall: " +str(self.episode+24+24+25+24+24+25))
        print("Title: " +str(self.dt.s_7_titles[self.episode -1]))
        print("Original Airdate: " +str(self.dt.s_7_original_airdate[self.episode -1]))
        print("Summary: " +str(self.dt.s_7_summary[self.episode -1]))
        print("Title, airdate and summery taken from friends.fandom.com")
        print(" ")
        self.play()

    def s_8(self):
        self.season = 8
        if self.random_ep == True:
            self.episode = random.randint(1,24)
        else:
            self.episode = int(input('Input a number bettween 1 and 24, to select an episode in season 8:\n'))
            if self.episode < 1 or self.episode > 24:
                print("Invalid input")
                self.s_8()
        print(" ")
        print("Season 8, Episode " +str(self.episode))
        print("Episode Overall: " +str(self.episode+24+24+25+24+24+25+24))
        print("Title: " +str(self.dt.s_8_titles[self.episode -1]))
        print("Original Airdate: " +str(self.dt.s_8_original_airdate[self.episode -1]))
        print("Summary: " +str(self.dt.s_8_summary[self.episode -1]))
        print("Title, airdate and summery taken from friends.fandom.com")
        print(" ")
        self.play()

    def s_9(self):
        self.season = 9
        if self.random_ep == True:
            self.episode = random.randint(1,24)
        else:
            self.episode = int(input('Input a number bettween 1 and 24, to select an episode in season 9:\n'))
            if self.episode < 1 or self.episode > 24:
                print("Invalid input")
                self.s_9()
        print(" ")
        print("Season 9, Episode " +str(self.episode))
        print("Episode Overall: " +str(self.episode+24+24+25+24+24+25+24+24))
        print("Title: " +str(self.dt.s_9_titles[self.episode -1]))
        print("Original Airdate: " +str(self.dt.s_9_original_airdate[self.episode -1]))
        print("Summary: " +str(self.dt.s_9_summary[self.episode -1]))
        print("Title, airdate and summery taken from friends.fandom.com")
        print(" ")
        self.play()

    def s_10(self):
        self.season = 10
        if self.random_ep == True:
            self.episode = random.randint(1,18)
        else:
            self.episode = int(input('Input a number bettween 1 and 18, to select an episode in season 10:\n'))
            if self.episode < 1 or self.episode > 18:
                print("Invalid input")
                self.s_10()
        print(" ")
        print("Season 10, Episode " +str(self.episode))
        print("Episode Overall: " +str(self.episode+24+24+25+24+24+25+24+24+24))
        print("Title: " +str(self.dt.s_10_titles[self.episode -1]))
        print("Original Airdate: " +str(self.dt.s_10_original_airdate[self.episode -1]))
        print("Summary: " +str(self.dt.s_10_summary[self.episode -1]))
        print("Title, airdate and summery taken from friends.fandom.com")
        print(" ")
        self.play()

    def generate_episode(self):
        season = random.randint(1,10)
        if season == 1:
            self.s_1()
        if season == 2:
            self.s_2()
        if season == 3:
            self.s_3()
        if season == 4:
            self.s_4()
        if season == 5:
            self.s_5()
        if season == 6:
            self.s_6()
        if season == 7:
            self.s_7()
        if season == 8:
            self.s_8()
        if season == 9:
            self.s_9()
        if season == 10:
            self.s_10()


    def state_1(self):
        self.random_ep = False
        self.episode = 0
        self.season = 0
        first_imput = (input('Imput "random" to generate a random episode, or imput a number between 1 and 10, to select a season:\n'))

        if first_imput == "random" or first_imput == "tilfældig":
            self.random_ep = True
            self.generate_episode()

        elif first_imput == "1":
            print("Season 1")
            self.s_1()

        elif first_imput == "2":
            print("Season 2")
            self.s_2()

        elif first_imput == "3":
            print("Season 3")
            self.s_3()

        elif first_imput == "4":
            print("Season 4")
            self.s_4()

        elif first_imput == "5":
            print("Season 5")
            self.s_5()

        elif first_imput == "6":
            print("Season 6")
            self.s_6()

        elif first_imput == "7":
            print("Season 7")
            self.s_7()

        elif first_imput == "8":
            print("Season 8")
            self.s_8()

        elif first_imput == "9":
            print("Season 9")
            self.s_9()

        elif first_imput == "10":
            print("Season 10")
            self.s_10()
            
        else:
            print("Invalid input")
            self.state_1()

    def play(self):
        play_or_return = (input('Input "play", to play the episode, or input "return", to go back to start:\n'))
        if play_or_return == "play":
            video = (str(self.season) + "_" + str(self.episode) + ".mp4")
            print(video)
            os.system("start " + video)
            print("If you have the videofile for the episode labeled " + str(video) + " you can play it from this progran")
            print(" ")
        elif play_or_return == "return":
            self.state_1()
        else:
            print("Invalid input")
            self.play()


    def start_program(self):
        print("")
        print("#----------------------------- Marty Rasmussen Presents ----------------------------#")
        print("|       ______    _                _       _____      _               _             |")
        print("|       |  ___|  (_)              | |     |  ___|    (_)             | |            |")
        print("|       | |_ _ __ _  ___ _ __   __| |___  | |__ _ __  _ ___  ___   __| | ___        |")
        print("|       |  _| '__| |/ _ \\ '_ \\ / _` / __| |  __| '_ \\| / __|/ _ \\ / _` |/ _ \\       |")
        print("|       | | | |  | |  __/ | | | (_| \\__ \\ | |__| |_) | \\__ \\ (_) | (_| |  __/       |")
        print("|       \\_| |_|  |_|\\___|_| |_|\\__,_|___/ \\____/ .__/|_|___/\\___/ \\__,_|\\___|       |")
        print("|                                              |_|                                  |")
        print("|  _______  _______  _        _______  _______  _______ _________ _______  _______  |")
        print("| (  ____ \\(  ____ \\( (    /|(  ____ \\(  ____ )(  ___  )\\__   __/(  ___  )(  ____ ) |")
        print("| | (    \\/| (    \\/|  \\  ( || (    \\/| (    )|| (   ) |   ) (   | (   ) || (    )| |")
        print("| | |      | (__    |   \\ | || (__    | (____)|| (___) |   | |   | |   | || (____)| |")
        print("| | | ____ |  __)   | (\\ \\) ||  __)   |     __)|  ___  |   | |   | |   | ||     __) |")
        print("| | | \\_  )| (      | | \\   || (      | (\\ (   | (   ) |   | |   | |   | || (\\ (    |")
        print("| | (___) || (____/\\| )  \\  || (____/\\| ) \\ \\__| )   ( |   | |   | (___) || ) \\ \\__ |")
        print("| (_______)(_______/|/    )_)(_______/|/   \\__/|/     \\|   )_(   (_______)|/   \\__/ |")
        print("#--------------------------------------- 2019 --------------------------------------#")
        print("")
        self.state_1()


g = Generator()
g.start_program()
