from modules.generator import NetflixESNGenerator
import pyfiglet
import os
import platform

def clear_screen():
    """Clear the console screen."""
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def main():
    clear_screen()
    title = pyfiglet.figlet_format("ESN Generator")
    print(title)
    generator = NetflixESNGenerator()
    generator.run()

if __name__ == "__main__":
    main()
