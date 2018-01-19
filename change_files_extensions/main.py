import csv


def main():
    counter = 1

    with open('output/changed_file_extensions.csv', 'wb') as file_output:
        with open('input/files_changed_new_ids.csv', 'rb') as file_input:
            reader_input = csv.DictReader(file_input)
            fieldnames = reader_input.fieldnames
            writer_output = csv.DictWriter(file_output, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
            writer_output.writeheader()

            for row in reader_input:
                row['Title'] = row['PathOnClient']
                writer_output.writerow(row)

                print counter
                counter += 1


if __name__ == "__main__":
    main()
