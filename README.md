1. change_status script uses as input
  - mapping.csv as mapper for old to new statuses
  - lead.csv as data source
  
  and produces new lead_new.csv with updated DISPOSITION statuses
  
2. split_types script uses as input
  - input/types.csv to check which status goes to lead, opportunity or NONE
  - input/lead_new.csv as data source
  
  and produces three files:
  - output/leads_output.csv
  - output/opportunity_output.csv
  - output/nontype_output.csv
  
  -- THINGS MUST TO KNOW --
  *every status witch start with DL will go to Opportunity!!!
  *output folder must be created before script runs
