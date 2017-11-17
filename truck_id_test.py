# pilot graph build with graph data collection
#    # nodes
#        # from electric_errors.csv all truck distinct all good phase (after sap state too)
#        # first phase
#            # from electric_errors.csv   distinct error codes
#            # from sap_txt.csv           distinct exchange part codes
#            # from sap_xml.csv           distinct exchange part codes
#        # second phase
#            # from sap_txt.csv           where is no exchange part number technical worker comment text mining
#            # from sap_xml.csv           where is no exchange part number technical worker comment text mining
#    # edges
#        # directed in path which truck when arrived to that stage (accommulate from the three files)

import pandas as pd

path_to_electric_errors_csv = '/home/vassb/fault_pred_data/electric_errors.csv'
path_to_sap_txt_csv = '/home/vassb/fault_pred_data/sap_txt.csv'
path_to_sap_xml_csv = '/home/vassb/fault_pred_data/sap_xml.csv'

export_electric_erros_distinct_errors_codes = "/home/vassb/fault_pred_data/distinct_electric_errors_truck_ID.csv"
export_sap_txt_fails_codes = "/home/vassb/fault_pred_data/sap_txt_truck_ID.csv"
export_sap_xml_fails_codes = "/home/vassb/fault_pred_data/sap_xml_truck_ID.csv"

#######################################################################################################################
#drop not usefull columns for graph core
#######################################################################################################################
colnames_electric_errors = ["exclude",
            "exclude",
            "vehicle_serialnumber",
            "exclude",
            "exclude",
            "exclude"]

colnames_sap_txt = ["exclude", "serialnumber", "exclude",
            "exclude",   "exclude", "exclude",
            "exclude",  "exclude", "exclude", "exclude",
            "exclude",
            "exclude", "exclude",
            "exclude", "exclude",
             "exclude",
            "exclude", "exclude",
            "exclude", "exclude", "exclude", "exclude",
            "exclude", "exclude"]

colnames_sap_xml = [ "exclude", "serialnumber", "exclude",
            "exclude", "exclude", "exclude", "exclude",
            "exclude", "exclude",
            "exclude", "exclude",   "exclude",
            "exclude", "exclude", "exclude", "exclude",
            "exclude", "exclude"]

#big file dropping
flag = 0
chunksize = 10 ** 6

print "boo!"

i = 1

for chunk in pd.read_csv(path_to_electric_errors_csv, parse_dates=True, names=colnames_electric_errors, skiprows=1,
                         chunksize=chunksize):
    print "chunk " + str(i) + " processing started!"
    if flag == 0:
        cols = [c for c in chunk.columns if c.lower()[:7] != 'exclude']
        chunk = chunk[cols]
        #chunk.to_csv(export_electric_erros_distinct_errors_codes)
        flag = 1
        el_f_df = chunk.dropna(how = "any").drop_duplicates("s_errorcode")
    else:
        cols = [c for c in chunk.columns if c.lower()[:7] != 'exclude']
        chunk = chunk[cols]
        #chunk.to_csv(export_electric_erros_distinct_errors_codes, mode='a', header=False)
        el_f_df = pd.concat([el_f_df,chunk],ignore_index=True).dropna(how = "any").drop_duplicates("s_errorcode",keep='first')
    print "chunk " + str(i) + " has processed!"
    i = i + 1
el_f_df.to_csv(export_electric_erros_distinct_errors_codes,index=False)
print "process ready"
#######################################################################################################################

# big file ready

sap_txt_fault = pd.read_csv(path_to_sap_txt_csv, parse_dates=True, names=colnames_sap_txt, skiprows=1)

cols = [c for c in sap_txt_fault.columns if c.lower()[:7] != 'exclude']

sap_txt_fault = sap_txt_fault[cols]

print sap_txt_fault.columns
#TODO rename na exchange part number in the first phase in second phase use NLP for making sub categories
sap_txt_fault.drop_duplicates(keep='first').dropna(how = "any").to_csv(export_sap_txt_fails_codes,index=False)

#######################################################################################################################

sap_xml_fault = pd.read_csv(path_to_sap_xml_csv,parse_dates=True, names=colnames_sap_xml, skiprows=1)

cols = [c for c in sap_xml_fault.columns if c.lower()[:7] != "exclude"]

sap_xml_fault = sap_xml_fault[cols]

print sap_xml_fault.columns

sap_xml_fault.drop_duplicates(keep='first').to_csv(export_sap_xml_fails_codes)
#######################################################################################################################

