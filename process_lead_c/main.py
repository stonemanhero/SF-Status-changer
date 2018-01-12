import csv

C_SUFFIX = '__C'

# Fields
CONDITION_TYPE = 'CONDITION_TYPE'
BANK_NAME = 'BANK_NAME'
CURRENT_BALANCE = 'CURRENT_BALANCE'
CURRENT_DEBT_CREDIT_RATIO = 'CURRENT_DEBT_CREDIT_RATIO'
CURRENT_LIMIT = 'CURRENT_LIMIT'
EQUIFAX = 'EQUIFAX'
EXPERIAN = 'EXPERIAN'
NEW_BALANCE = 'NEW_BALANCE'
PAYDOWN_CONDITIONS_NOTES = 'PAYDOWN_CONDITIONS_NOTES'
PAY_OFF_AMOUNT = 'PAY_OFF_AMOUNT'
REQUIRED_BALANCE = 'REQUIRED_BALANCE'
REQUIRED_PAYDOWN_AMOUNT = 'REQUIRED_PAYDOWN_AMOUNT'
TRANSUNION = 'TRANSUNION'
VENDOR = 'VENDOR'
CONDITIONS_NEEDED = 'CONDITIONS_NEEDED'
CONTAINS_CLIENT_S_NAME = 'CONTAINS_CLIENT_S_NAME'
INDICATES_CURRENT_BALANCE_OF_ACCOUNT = 'INDICATES_CURRENT_BALANCE_OF_ACCOUNT'
MUST_BE_ON_OFFICIAL_BANK_LETTERHEAD = 'MUST_BE_ON_OFFICIAL_BANK_LETTERHEAD'
SHOWS_LAST_FOR_DIGITS_OF_ACCOUNT_NUMBER = 'SHOWS_LAST_FOR_DIGITS_OF_ACCOUNT_NUMBER'


def main():
    counter = 1
    lead_c_ids = {}

    with open('output/lead_c_fix.csv', 'wb') as file_lead_c_fix:
        fieldnames = ['LEAD_ID']

        for i in range(1, 9):
            fieldnames.append(CONTAINS_CLIENT_S_NAME + str(i) + C_SUFFIX)

        for i in range(1, 9):
            fieldnames.append(INDICATES_CURRENT_BALANCE_OF_ACCOUNT + str(i) + C_SUFFIX)

        for i in range(1, 9):
            fieldnames.append(MUST_BE_ON_OFFICIAL_BANK_LETTERHEAD + str(i) + C_SUFFIX)

        for i in range(1, 9):
            fieldnames.append(SHOWS_LAST_FOR_DIGITS_OF_ACCOUNT_NUMBER + str(i) + C_SUFFIX)

        lead_c_writer = csv.DictWriter(file_lead_c_fix, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        lead_c_writer.writeheader()

        with open('input/lead_c.csv', 'rb') as file_lead_c:
            reader_lead_c = csv.DictReader(file_lead_c)

            for row in reader_lead_c:
                if row['LEAD__C'] != "":
                    if row['LEAD__C'] in lead_c_ids:
                        if CONTAINS_CLIENT_S_NAME + '1__C' in row['LEAD__C']:
                            for i in range(1, 9):
                                if CONTAINS_CLIENT_S_NAME + str(i) + C_SUFFIX in row['LEAD__C']:
                                    if row[CONTAINS_CLIENT_S_NAME + str(i) + C_SUFFIX] == "true" and lead_c_ids[row['LEAD__C']][CONTAINS_CLIENT_S_NAME + str(i) + C_SUFFIX] == "false":
                                        lead_c_ids[row['LEAD__C']][CONTAINS_CLIENT_S_NAME + str(i) + C_SUFFIX] = "true"

                                    if row[INDICATES_CURRENT_BALANCE_OF_ACCOUNT + str(i) + C_SUFFIX] == "true" and lead_c_ids[row['LEAD__C']][INDICATES_CURRENT_BALANCE_OF_ACCOUNT + str(i) + C_SUFFIX] == "false":
                                        lead_c_ids[row['LEAD__C']][INDICATES_CURRENT_BALANCE_OF_ACCOUNT + str(i) + C_SUFFIX] = "true"

                                    if row[MUST_BE_ON_OFFICIAL_BANK_LETTERHEAD + str(i) + C_SUFFIX] == "true" and lead_c_ids[row['LEAD__C']][MUST_BE_ON_OFFICIAL_BANK_LETTERHEAD + str(i) + C_SUFFIX] == "false":
                                        lead_c_ids[row['LEAD__C']][MUST_BE_ON_OFFICIAL_BANK_LETTERHEAD + str(i) + C_SUFFIX] = "true"

                                    if row[SHOWS_LAST_FOR_DIGITS_OF_ACCOUNT_NUMBER + str(i) + C_SUFFIX] == "true" and lead_c_ids[row['LEAD__C']][SHOWS_LAST_FOR_DIGITS_OF_ACCOUNT_NUMBER + str(i) + C_SUFFIX] == "false":
                                        lead_c_ids[row['LEAD__C']][SHOWS_LAST_FOR_DIGITS_OF_ACCOUNT_NUMBER + str(i) + C_SUFFIX] = "true"
                        else:
                            for i in range(1, 9):
                                write_status = False

                                if row[CONTAINS_CLIENT_S_NAME + str(i) + C_SUFFIX] == "true" or row[
                                                    INDICATES_CURRENT_BALANCE_OF_ACCOUNT + str(
                                                    i) + C_SUFFIX] == "true" or row[
                                                    MUST_BE_ON_OFFICIAL_BANK_LETTERHEAD + str(
                                                    i) + C_SUFFIX] == "true" or row[
                                                    SHOWS_LAST_FOR_DIGITS_OF_ACCOUNT_NUMBER + str(
                                                    i) + C_SUFFIX] == "true":
                                    write_status = True
                                    break

                            if write_status:
                                lead_c_ids[row['LEAD__C']]['LEAD_ID'] = row['LEAD__C']

                                for i in range(1, 9):
                                    lead_c_ids[row['LEAD__C']][CONTAINS_CLIENT_S_NAME + str(i) + C_SUFFIX] = row[
                                        CONTAINS_CLIENT_S_NAME + str(i) + C_SUFFIX]
                                    lead_c_ids[row['LEAD__C']][
                                        INDICATES_CURRENT_BALANCE_OF_ACCOUNT + str(i) + C_SUFFIX] = row[
                                        INDICATES_CURRENT_BALANCE_OF_ACCOUNT + str(i) + C_SUFFIX]
                                    lead_c_ids[row['LEAD__C']][
                                        MUST_BE_ON_OFFICIAL_BANK_LETTERHEAD + str(i) + C_SUFFIX] = row[
                                        MUST_BE_ON_OFFICIAL_BANK_LETTERHEAD + str(i) + C_SUFFIX]
                                    lead_c_ids[row['LEAD__C']][
                                        SHOWS_LAST_FOR_DIGITS_OF_ACCOUNT_NUMBER + str(i) + C_SUFFIX] = row[
                                        SHOWS_LAST_FOR_DIGITS_OF_ACCOUNT_NUMBER + str(i) + C_SUFFIX]
                    else:
                        lead_c_ids[row['LEAD__C']] = {}

                        for i in range(1, 9):
                            write_status = False

                            if row[CONTAINS_CLIENT_S_NAME + str(i) + C_SUFFIX] == "true" or row[INDICATES_CURRENT_BALANCE_OF_ACCOUNT + str(i) + C_SUFFIX] == "true" or row[MUST_BE_ON_OFFICIAL_BANK_LETTERHEAD + str(i) + C_SUFFIX] == "true" or row[SHOWS_LAST_FOR_DIGITS_OF_ACCOUNT_NUMBER + str(i) + C_SUFFIX] == "true":
                                write_status = True
                                break

                        if write_status:
                            lead_c_ids[row['LEAD__C']]['LEAD_ID'] = row['LEAD__C']

                            for i in range(1, 9):
                                lead_c_ids[row['LEAD__C']][CONTAINS_CLIENT_S_NAME + str(i) + C_SUFFIX] = row[CONTAINS_CLIENT_S_NAME + str(i) + C_SUFFIX]
                                lead_c_ids[row['LEAD__C']][INDICATES_CURRENT_BALANCE_OF_ACCOUNT + str(i) + C_SUFFIX] = row[INDICATES_CURRENT_BALANCE_OF_ACCOUNT + str(i) + C_SUFFIX]
                                lead_c_ids[row['LEAD__C']][MUST_BE_ON_OFFICIAL_BANK_LETTERHEAD + str(i) + C_SUFFIX] = row[MUST_BE_ON_OFFICIAL_BANK_LETTERHEAD + str(i) + C_SUFFIX]
                                lead_c_ids[row['LEAD__C']][SHOWS_LAST_FOR_DIGITS_OF_ACCOUNT_NUMBER + str(i) + C_SUFFIX] = row[SHOWS_LAST_FOR_DIGITS_OF_ACCOUNT_NUMBER + str(i) + C_SUFFIX]

                print counter
                counter += 1

            for key, value in lead_c_ids.iteritems():
                if value:
                    lead_c_writer.writerow(value)

if __name__ == "__main__":
    main()