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
CONDITIONS_NEEDED = 'CONDITIONS_NEEDED' + C_SUFFIX
CONTAINS_CLIENT_S_NAME = 'CONTAINS_CLIENT_S_NAME'
INDICATES_CURRENT_BALANCE_OF_ACCOUNT = 'INDICATES_CURRENT_BALANCE_OF_ACCOUNT'
MUST_BE_ON_OFFICIAL_BANK_LETTERHEAD = 'MUST_BE_ON_OFFICIAL_BANK_LETTERHEAD'
SHOWS_LAST_FOR_DIGITS_OF_ACCOUNT_NUMBER = 'SHOWS_LAST_FOR_DIGITS_OF_ACCOUNT_NUMBER'

MAX_LOOP = 11

def main():
    counter = 1
    bank_ids = {}

    with open('output/bank_fix.csv', 'wb') as file_bank_fix:
        fieldnames = ['LEAD_ID', CONDITIONS_NEEDED]

        for i in range(1, 11):
            fieldnames.append(BANK_NAME + str(i) + C_SUFFIX)

        for i in range(1, MAX_LOOP):
            fieldnames.append(CURRENT_BALANCE + str(i) + C_SUFFIX)

        for i in range(1, MAX_LOOP):
            fieldnames.append(CURRENT_DEBT_CREDIT_RATIO + str(i) + C_SUFFIX)

        for i in range(1, MAX_LOOP):
            fieldnames.append(CURRENT_LIMIT + str(i) + C_SUFFIX)

        for i in range(1, MAX_LOOP):
            fieldnames.append(EQUIFAX + str(i) + C_SUFFIX)

        for i in range(1, MAX_LOOP):
            fieldnames.append(EXPERIAN + str(i) + C_SUFFIX)

        for i in range(1, MAX_LOOP):
            fieldnames.append(NEW_BALANCE + str(i) + C_SUFFIX)

        for i in range(1, MAX_LOOP):
            fieldnames.append(PAYDOWN_CONDITIONS_NOTES + str(i) + C_SUFFIX)

        for i in range(1, MAX_LOOP):
            fieldnames.append(PAY_OFF_AMOUNT + str(i) + C_SUFFIX)

        for i in range(1, MAX_LOOP):
            fieldnames.append(REQUIRED_BALANCE + str(i) + C_SUFFIX)

        for i in range(1, MAX_LOOP):
            fieldnames.append(REQUIRED_PAYDOWN_AMOUNT + str(i) + C_SUFFIX)

        for i in range(1, MAX_LOOP):
            fieldnames.append(TRANSUNION + str(i) + C_SUFFIX)

        for i in range(1, MAX_LOOP):
            fieldnames.append(VENDOR + str(i) + C_SUFFIX)

        bank_writer = csv.DictWriter(file_bank_fix, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        bank_writer.writeheader()

        with open('input/bank_application.csv', 'rb') as file_bank:
            reader_bank = csv.DictReader(file_bank)

            for row in reader_bank:
                if row['LEAD_ID__C'] != "" and row[CONDITIONS_NEEDED] and row['LEAD_ID__C'] != '00Q3600000SZHzkEAH':
                    if row['LEAD_ID__C'] in bank_ids:
                        print "Duplicate: " + row['LEAD_ID__C']

                        # IF there is duplicate logic...
                        if row['LEAD_ID__C'] != bank_ids[row['LEAD_ID__C']]:
                            print "Duplicate: " + row['LEAD_ID__C']
                            """
                            for i in range(1, MAX_LOOP):
                                print BANK_NAME + ': ' + row[BANK_NAME + str(i) + C_SUFFIX] + ' == ' + bank_ids[row['LEAD_ID__C']][BANK_NAME + str(i) + C_SUFFIX]
                                print CURRENT_BALANCE + ': ' + row[CURRENT_BALANCE + str(i) + C_SUFFIX] + ' == ' + bank_ids[row['LEAD_ID__C']][
                                    CURRENT_BALANCE + str(i) + C_SUFFIX]
                                print CURRENT_DEBT_CREDIT_RATIO + ': ' + row[CURRENT_DEBT_CREDIT_RATIO + str(i) + C_SUFFIX] + ' == ' + bank_ids[row['LEAD_ID__C']][
                                    CURRENT_DEBT_CREDIT_RATIO + str(i) + C_SUFFIX]
                                print EQUIFAX + ': ' + row[EQUIFAX + str(i) + C_SUFFIX] + ' == ' + bank_ids[row['LEAD_ID__C']][
                                    EQUIFAX + str(i) + C_SUFFIX]
                                print EXPERIAN + ': ' + row[EXPERIAN + str(i) + C_SUFFIX] + ' == ' + bank_ids[row['LEAD_ID__C']][
                                    EXPERIAN + str(i) + C_SUFFIX]

                                if i not in [7, 8]:
                                    print NEW_BALANCE + ': ' + row[NEW_BALANCE + str(i) + C_SUFFIX] + ' == ' + bank_ids[row['LEAD_ID__C']][
                                    NEW_BALANCE + str(i) + C_SUFFIX]

                                print PAYDOWN_CONDITIONS_NOTES + ': ' + row[PAYDOWN_CONDITIONS_NOTES + str(i) + C_SUFFIX] + ' == ' + bank_ids[row['LEAD_ID__C']][
                                    PAYDOWN_CONDITIONS_NOTES + str(i) + C_SUFFIX]
                                print PAY_OFF_AMOUNT + ': ' + row[PAY_OFF_AMOUNT + str(i) + C_SUFFIX] + ' == ' + bank_ids[row['LEAD_ID__C']][
                                    PAY_OFF_AMOUNT + str(i) + C_SUFFIX]
                                print REQUIRED_BALANCE + ': ' + row[REQUIRED_BALANCE + str(i) + C_SUFFIX] + ' == ' + bank_ids[row['LEAD_ID__C']][
                                    REQUIRED_BALANCE + str(i) + C_SUFFIX]
                                print REQUIRED_PAYDOWN_AMOUNT + ': ' + row[REQUIRED_PAYDOWN_AMOUNT + str(i) + C_SUFFIX] + ' == ' + bank_ids[row['LEAD_ID__C']][
                                    REQUIRED_PAYDOWN_AMOUNT + str(i) + C_SUFFIX]
                                print TRANSUNION + ': ' + row[TRANSUNION + str(i) + C_SUFFIX] + ' == ' + bank_ids[row['LEAD_ID__C']][
                                    TRANSUNION + str(i) + C_SUFFIX]
                                print VENDOR + ': ' + row[VENDOR + str(i) + C_SUFFIX] + ' == ' + bank_ids[row['LEAD_ID__C']][
                                    VENDOR + str(i) + C_SUFFIX]
                            """
                    else:
                        bank_ids[row['LEAD_ID__C']] = {}
                        bank_ids[row['LEAD_ID__C']][CONDITIONS_NEEDED] = row[CONDITIONS_NEEDED]
                        bank_ids[row['LEAD_ID__C']]['LEAD_ID'] = row['LEAD_ID__C']

                        for i in range(1, MAX_LOOP):
                            bank_ids[row['LEAD_ID__C']][BANK_NAME + str(i) + C_SUFFIX] = row[BANK_NAME + str(i) + C_SUFFIX]
                            bank_ids[row['LEAD_ID__C']][CURRENT_BALANCE + str(i) + C_SUFFIX] = row[CURRENT_BALANCE + str(i) + C_SUFFIX]
                            bank_ids[row['LEAD_ID__C']][CURRENT_DEBT_CREDIT_RATIO + str(i) + C_SUFFIX] = row[CURRENT_DEBT_CREDIT_RATIO + str(i) + C_SUFFIX]
                            bank_ids[row['LEAD_ID__C']][EQUIFAX + str(i) + C_SUFFIX] = row[EQUIFAX + str(i) + C_SUFFIX]
                            bank_ids[row['LEAD_ID__C']][EXPERIAN + str(i) + C_SUFFIX] = row[EXPERIAN + str(i) + C_SUFFIX]

                            if i not in [7, 8]:
                                bank_ids[row['LEAD_ID__C']][NEW_BALANCE + str(i) + C_SUFFIX] = row[NEW_BALANCE + str(i) + C_SUFFIX]

                            bank_ids[row['LEAD_ID__C']][PAYDOWN_CONDITIONS_NOTES + str(i) + C_SUFFIX] = row[PAYDOWN_CONDITIONS_NOTES + str(i) + C_SUFFIX]
                            bank_ids[row['LEAD_ID__C']][PAY_OFF_AMOUNT + str(i) + C_SUFFIX] = row[PAY_OFF_AMOUNT + str(i) + C_SUFFIX]
                            bank_ids[row['LEAD_ID__C']][REQUIRED_BALANCE + str(i) + C_SUFFIX] = row[REQUIRED_BALANCE + str(i) + C_SUFFIX]
                            bank_ids[row['LEAD_ID__C']][REQUIRED_PAYDOWN_AMOUNT + str(i) + C_SUFFIX] = row[REQUIRED_PAYDOWN_AMOUNT + str(i) + C_SUFFIX]
                            bank_ids[row['LEAD_ID__C']][TRANSUNION + str(i) + C_SUFFIX] = row[TRANSUNION + str(i) + C_SUFFIX]
                            bank_ids[row['LEAD_ID__C']][VENDOR + str(i) + C_SUFFIX] = row[VENDOR + str(i) + C_SUFFIX]

                        bank_writer.writerow(bank_ids[row['LEAD_ID__C']])
                    print counter
                    counter += 1


if __name__ == "__main__":
    main()