def create_dictionary(filename):

    ratings = open(filename)
    restaurants = {}

    for line in ratings:
        name, rating = line.rstrip().split(":")
        restaurants[name] = rating

    ratings.close()

    return restaurants


def sort_and_print(filename):

    input_dict = create_dictionary(filename)

    rest_list = input_dict.keys()
    rest_list.sort()

    for item in rest_list:
        print "Restaurant %s is rated at %s" % (item, input_dict[item])


def main():

    sort_and_print("scores.txt")

if __name__ == "__main__":
    main()