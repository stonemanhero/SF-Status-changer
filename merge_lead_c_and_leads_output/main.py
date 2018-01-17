import csv


def main():
    base_fieldnames = []
    leads = {}
    counter_leads_output = 1
    counter_prepared = 1
    counter_written = 1

    with open('input/after_opportunity_output.csv', 'rb') as file_leads_output:
        reader_leads_output = csv.DictReader(file_leads_output)
        base_fieldnames = reader_leads_output.fieldnames

        for row in reader_leads_output:
            leads[row['ID']] = {}
            for field in base_fieldnames:
                leads[row['ID']][field] = row[field]

            print counter_leads_output
            counter_leads_output += 1

    with open('input/lead_c_prepared_for_merge.csv', 'rb') as file_lead_c_merge:
        reader_lead_c_merge = csv.DictReader(file_lead_c_merge)
        addon_fieldnames = reader_lead_c_merge.fieldnames
        base_fieldnames += addon_fieldnames

        for row in reader_lead_c_merge:
            if row['LEAD__C'] in leads:
                for field in addon_fieldnames:
                    leads[row['LEAD__C']][field] = row[field]

            print counter_prepared
            counter_prepared += 1

    with open('output/merged_after_opportunity.csv', 'wb') as file_merged_leads:
        writer_merged_leads = csv.DictWriter(file_merged_leads, fieldnames=base_fieldnames, quoting=csv.QUOTE_ALL)
        writer_merged_leads.writeheader()

        for key, value in leads.iteritems():
            writer_merged_leads.writerow(value)
            print counter_written
            counter_written += 1

if __name__ == "__main__":
    main()
