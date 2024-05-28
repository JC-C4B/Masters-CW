from BL7 import BL

class PL:
    def __init__(self):
        self.procedures = BL()
        self.running = True

    def run(self):
        while self.running:
            print("Please Select a Query:")
            print("1. Add a New Item to a Room")
            print("2. Move Items to a Different Room")
            print("3. Update an Item's total Amount")
            print("4. Exit")
            
            choice = input("Please enter your choice: ")
            
            if choice == "1":
                self.procedures.add_item()
            elif choice == "2":
                self.procedures.move_items()
            elif choice == "3":
                self.procedures.update_item_amount_in_room()
            elif choice == "4":
                self.running = False
                print("Exiting...")
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    presentation = PL()
    presentation.run()
