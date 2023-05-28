from view.main_menu import show_main_menu
from view.add_animal_menu import add_animal_menu
from view.animal_view import list_of_animals, animal_details, select_animal_id, add_commands_to_animal
from date_store.AnimalsRepository import read_all


def main():
    running = True
    while running:
        show_main_menu()
        user_input = input()
        if user_input == "1":
            list_of_animals(read_all())
        elif user_input == "2":
            add_animal_menu()
        elif user_input == "3":
            animal_details(select_animal_id())
        elif user_input == "4":
            add_commands_to_animal(select_animal_id())
        elif user_input == "0":
            running = False


if __name__ == '__main__':
    main()
