from sys import argv

def build_dictionary(opened_file):
    ratings = {}

    for line in opened_file:
        line = line.rstrip().split(':')
        ratings[line[0]] = line[1]
    return ratings

def sortandprint(opened_file):
    input_dictionary = build_dictionary(opened_file)
    
    sorted_rest_ratings = sorted(input_dictionary)
    for name in sorted_rest_ratings:
        print 'Restaurant %s is rated at %s' % (name, input_dictionary[name])


def main():
    script, filename = argv
    opened_file = open(filename, 'r')
    sortandprint(opened_file)

    opened_file.close()

if __name__ == '__main__':
    main()
