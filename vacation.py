def hotel_cost(nights):
    """Define hotel costs."""
    return 140 * nights


def plane_ride_cost(city):
    """Price of ticket."""
    if city == "Charlotte":
        return 183
    if city == "Tampa":
        return 220
    if city == "Pittsburgh":
        return 222
    if city == "Los Angeles":
        return 475


def rental_car_cost(days):
    """Rental Car costs."""
    if days < 3:
        return days * 40
    elif days >= 3 and days < 7:
        return days * 40 - 20
    elif days >= 7:
        return days * 40 - 50


def trip_cost(city, days, spending_money):
    """Trip cost."""
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money


print(trip_cost("Los Angeles", 5, 600))
