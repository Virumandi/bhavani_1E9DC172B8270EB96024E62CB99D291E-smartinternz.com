- Implement a function called sort_students that takes a list of student objects as input and sorts thelist based on their CGPA (Cumulative Grade Point Average) in descending order. Each student object has the following attributes: name (string), roll_number (string), and cgpa (float). Test the function with different input lists of students.
class Player:
    def play(self):
        print("The player is playing cricket.")

class Batsman(Player):
    def play(self):
        print("The batsman is batting.")

class Bowler(Player):
    def play(self):
        print("The bowler is bowling.")

# Main program
while True:
    try:
        choice = int(input("Enter 1 for Batsman, 2 for Bowler, or 0 to exit: "))
        if choice == 0:
            break
        elif choice == 1:
            player = Batsman()
        elif choice == 2:
            player = Bowler()
        else:
            print("Invalid choice. Please enter 1 for Batsman, 2 for Bowler, or 0 to exit.")
            continue

        player.play()
    except ValueError:
        print("Invalid input. Please enter a valid choice.")

print("Exiting the program.")