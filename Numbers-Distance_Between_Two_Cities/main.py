# Distance Between Two Cities - Calculates the distance between two cities and allows the user to specify a unit of
# distance. This program may require finding coordinates for the cities like latitude and longitude.
import geopy
from geopy.distance import geodesic


def main():
    print("Calculate the distance between 2 cities.")
    city1 = input("Give a first address: street, city: ")
    city2 = input("Give a second address: street, city: ")

    distance = calculate_distance(get_lat_long(city1), get_lat_long(city2))
    print("The distance between %s and %s is %s" % (city1, city2, str(distance)))


def get_lat_long(address):
    geolocator = geopy.Nominatim()
    location = geolocator.geocode(address)
    coordinates = (location.latitude, location.longitude)
    return coordinates


def calculate_distance(coor1, coor2):
    return geodesic(coor1, coor2)


if __name__ == '__main__':
    main()