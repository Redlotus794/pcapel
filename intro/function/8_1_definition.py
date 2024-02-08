def greet_user(username):
    """Display a simple greeting."""
    print("Hello!" + username.title() + "!")


def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    

if __name__ == '__main__':
    greet_user('jesse')
    pass;