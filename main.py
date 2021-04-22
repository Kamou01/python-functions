# Functions Handout Task - Sample Solution
def hotel_cost(nights):
    return nights * 140  # in rands


def plane_ride_cost(city):
    if city == "CapeTown":
        return 2500
    elif city == "Durban":
        return 2300
    elif city == "JHB":
        return 2000
    elif city == "BFN":
        return 1800


def rental_car_cost(days):
    cost = 40 * days
    if days >= 7:
        cost = cost - 50
    elif days >= 3 < 7:
        cost = cost - 20
    return cost


def new_sum(*numbers):
    return sum(numbers)


def trip_cost(city, days, spending_money):
    return new_sum(rental_car_cost(days), hotel_cost(days), plane_ride_cost(city), spending_money)


print(trip_cost("CapeTown", 1, 0))
