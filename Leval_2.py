import random
import time

class Level2:
    def __init__(self, player_name, collection, time_limit=60):
        """
        Initializes the Level2 class with player name and time limit for the level.
        :param player_name: Name of the player
        :param time_limit: Time limit to complete the level (default is 60 seconds)
        """
        self.player_name = player_name
        self.collection = collection
        self.time_limit = time_limit
        self.time_left = time_limit
        self.level_started = False



    def welcom_page(self):
        """
        Displays the welcome message and instructions for the player.
        """
        print(f"Welcome {self.player_name} to Level 2!")
        print(f"Your task: Survive for {self.time_limit} seconds.")
        print(f"Collection weapon: weapon show {self.collection} is time {self.time_left}")
        print("Be collection all type Weapon to add in the game")
        print("Be careful! Random events may happen during this time.")
        print("Get ready to start!")


    def random_event(self):
        """
        A function to simulate random events that may happen in the level.
        """
        events = ["An asteroid appears!", "A sudden meteor shower!", "You find a power-up!", "A monster spawns!"]
        events1 = ["An gun in the left pop!", "A boom pop-up!", "A monster boom pop-up!", "A missile lunch pop-up!", " missile collect in pop-up !"]
        return random.choice(events+events1)
        

    def start(self):
        """
        Starts the level. Countdown starts and random events occur.
        """
        print(f"\nStarting Level 2... Time Limit: {self.time_limit} seconds")
        self.level_started = True
        
        start_time = time.time()  # Capture the start time
        while self.time_left > 0:
            current_time = time.time()
            self.time_left = self.time_limit - int(current_time - start_time)
            
            # Every 5 seconds, trigger a random event
            if self.time_left % 1 == 0 and self.time_left != 0:
                print(f"Time left: {self.time_left} seconds. Event: {self.random_event()}")
            time.sleep(1)  # Wait for 1 second
                
        # self.end()
        return
        
    def end(self):
        """
        Ends the level and displays a message.
        """
        print(f"\nTime's up! Level 2 is complete. Well done {self.player_name}!")
        if self.time_left >= 0:
            print("You survived the level!")
        else:
            print("You didn't survive,{self.player_name} try again!")
            return

# Main execution:
# if __name__ == "__main__":
    # # Ask for player's name
    # player_name = input("Enter your name: ") 
    # collection = ['item1', 'item2', 'item3']

    # # Create an instance of Level2 with the player's name
    # level_2 = Level2(player_name, collection)

    
    # # Display the welcome message
    # level_2.welcom_page()

    # # Start the level
    # level_2.start()
