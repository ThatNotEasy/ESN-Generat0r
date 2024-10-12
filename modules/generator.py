import random
from modules.utils import Utils
from modules.model import DeviceType, DeviceSubType

class NetflixESNGenerator:
    def __init__(self):
        self.device_type = ""
        self.device_subtype = ""
        self.device_manufacturer = ""
        self.device_model = ""
        self.device_system_id = ""
        self.uhd = False
        self.esn_output = ""

    def select_device_type(self):
        print("Select Device Type:\n1. Android\n2. Browser")
        choice = input("Enter your choice (1/2): ")
        if choice == '1':
            self.device_type = "Android"
        elif choice == '2':
            self.device_type = "Browser"
        else:
            print("Invalid choice. Please select again.")
            self.select_device_type()

    def select_device_subtype(self):
        print("Select Device Sub Type:\n1. Phone\n2. Tablet\n3. TV")
        choice = input("Enter your choice (1/2/3): ")
        if choice == '1':
            self.device_subtype = "Phone"
        elif choice == '2':
            self.device_subtype = "Tablet"
        elif choice == '3':
            self.device_subtype = "TV"
        else:
            print("Invalid choice. Please select again.")
            self.select_device_subtype()

    def input_device_info(self):
        self.device_manufacturer = input("Enter Device Manufacturer: ")
        self.device_model = input("Enter Device Model: ")
        self.device_system_id = input("Enter Device System ID (e.g., 123456): ")

        uhd_choice = input("Is this device 4K? (y/n): ")
        self.uhd = uhd_choice.lower() == 'y'

    def generate_esn(self):
        if self.device_type == "Browser":
            self.esn_output = DeviceType.Chrome + Utils.random_string(30)
            return

        random_number = random.randint(1000000000, 9999999999)
        esn_parts = [
            DeviceType.AndroidUHD if self.uhd else DeviceType.AndroidFHD,
            DeviceSubType.AndroidPhone if self.device_subtype == "Phone" else 
            DeviceSubType.AndroidTablet if self.device_subtype == "Tablet" else 
            DeviceSubType.AndroidTV,
            self.device_manufacturer[:3].upper(),
            self.device_model[:3].upper(),
            str(random_number)
        ]
        self.esn_output = '-'.join(esn_parts)

    def copy_esn(self):
        print(f"ESN Output: {self.esn_output}")

    def run(self):
        self.select_device_type()
        self.select_device_subtype()
        self.input_device_info()
        self.generate_esn()
        self.copy_esn()
