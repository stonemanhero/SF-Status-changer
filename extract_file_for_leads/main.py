import csv


def main():
    total_counter = 0
    founded_counter = 0

    with open('output/lead_missing_files.csv', 'wb') as output_file:
        with open('input/missing_files.csv', 'rb') as input_file:
            input_reader = csv.DictReader(input_file)
            fieldnames = input_reader.fieldnames

            output_writer = csv.DictWriter(output_file, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
            output_writer.writeheader()

            for row in input_reader:
                if row['FirstPublishLocationId']:
                    if row['FirstPublishLocationId'][0:3] == '00Q':
                        output_writer.writerow(row)
                        founded_counter += 1

                total_counter += 1
                print total_counter

    print 'Founded counter: ' + str(founded_counter)

if __name__ == "__main__":
    main()
