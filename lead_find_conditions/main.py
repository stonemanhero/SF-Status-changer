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
    lead_ids = {}

    f = open("output/results.txt", "w")  # opens file with name of "test.txt"



    with open('input/lead_fix.csv', 'rb') as file_lead:
        reader_lead = csv.DictReader(file_lead)

        for row in reader_lead:
            status = False
            for i in range(1, 11):
                if row[CONDITION_TYPE + str(i) + C_SUFFIX] == "Paydown Required" or row[CONDITION_TYPE + str(i) + C_SUFFIX] == "Remove Fraud Alert":
                    status = True
                    break

            if status:
                f.write(row['ID'])

                for i in range(1, 11):
                    f.write(', ' + row[CONDITION_TYPE + str(i) + C_SUFFIX] + '\n')

    f.close()
if __name__ == "__main__":
    main()
