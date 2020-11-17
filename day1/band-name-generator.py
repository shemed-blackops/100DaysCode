import sys


def main():
    city_name = input("Where were you born ?: ")
    pet_name = input("What's is your pet's name ?: ")

    band_name = "{} {}".format(city_name, pet_name)

    print("Your band name may be {} ".format(band_name))

if __name__ == "__main__":
    main()
