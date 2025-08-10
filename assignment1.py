class Television:
    def __init__(self, brand, size, is_smart):
        self.brand = brand
        self.size = size  # in inches
        self.is_smart = is_smart

    def turn_on(self):
        print(f"{self.brand} TV is now ON.")

    def turn_off(self):
        print(f"{self.brand} TV is now OFF.")

    def display_info(self):
        smart_status = "Smart TV" if self.is_smart else "Regular TV"
        print(f"{self.brand} {self.size}\" - {smart_status}")


class SmartTelevision(Television):
    def __init__(self, brand, size, is_smart, streaming_apps):
        super().__init__(brand, size, is_smart)
        self.streaming_apps = streaming_apps  # list of apps

    def open_app(self, app_name):
        if app_name in self.streaming_apps:
            print(f"Opening {app_name} on your {self.brand} Smart TV.")
        else:
            print(f"{app_name} is not installed on your {self.brand} Smart TV.")


# Example usage
tv1 = Television("Sony", 42, False)
tv1.turn_on()
tv1.display_info()
tv1.turn_off()

print()

tv2 = SmartTelevision("Samsung", 55, True, ["Netflix", "YouTube", "Hulu"])
tv2.turn_on()
tv2.display_info()
tv2.open_app("Netflix")
tv2.open_app("Hulu")
tv2.turn_off()
