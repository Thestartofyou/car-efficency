class Vehicle:
    def __init__(self, fuel_tank_capacity, fuel_consumption_rate):
        self.fuel_tank_capacity = fuel_tank_capacity  # in liters
        self.fuel_consumption_rate = fuel_consumption_rate  # in liters per kilometer
        self.fuel_level = fuel_tank_capacity  # initialize fuel level to full

    def consume_fuel(self, distance):
        fuel_needed = distance * self.fuel_consumption_rate
        if fuel_needed <= self.fuel_level:
            self.fuel_level -= fuel_needed
            return True  # Fuel was enough for the distance
        else:
            return False  # Not enough fuel

class Route:
    def __init__(self, topography_data):
        self.topography_data = topography_data

    def calculate_distance(self):
        return len(self.topography_data)  # For simplicity, each data point represents 1 km

    def simulate_route(self, vehicle):
        total_distance = self.calculate_distance()
        for elevation in self.topography_data:
            if not vehicle.consume_fuel(1):
                print("Out of fuel!")
                break
            # Simulate the effect of elevation on fuel efficiency
            if elevation > 0:
                vehicle.fuel_consumption_rate *= 1.1  # Increase consumption uphill
            else:
                vehicle.fuel_consumption_rate *= 0.9  # Decrease consumption downhill
        return vehicle.fuel_level

def main():
    vehicle = Vehicle(fuel_tank_capacity=50, fuel_consumption_rate=0.1)  # Example values
    topography_data = [0, 50, 100, -20, -50, 30, 0]  # Example elevation data
    route = Route(topography_data)

    remaining_fuel = route.simulate_route(vehicle)
    if remaining_fuel > 0:
        print(f"Route completed! Remaining fuel: {remaining_fuel:.2f} liters")
    else:
        print("Route not completed due to insufficient fuel.")

if __name__ == "__main__":
    main()
