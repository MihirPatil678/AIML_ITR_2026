class MobilePhone:
    def __init__(self, brand, model, battery_percentage):
        self.brand = brand
        self.model = model
        self.battery_percentage = battery_percentage
 
    def charge(self, percent):
        self.battery_percentage = min(100, self.battery_percentage + percent)
        print("Charging... Battery Now At", self.battery_percentage, "%")
 
    def use_phone(self, minutes):
        drain = minutes // 10   # 1% Battery Drained Per 10 Minutes
        self.battery_percentage = max(0, self.battery_percentage - drain)
        print("Used For", minutes, "Mins. Battery:", self.battery_percentage, "%")
 
    def show_status(self):
        print(self.brand, self.model, "Battery:", self.battery_percentage, "%")

phone = MobilePhone("Samsung", "Galaxy S23", 40)
phone.show_status()
phone.use_phone(60)     # Drains 6%
phone.charge(30)        # Charges To 64%
phone.show_status()