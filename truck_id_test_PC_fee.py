import pandas as pd
path_to_file = '/media/vasy/Data/Doksik/Learn/thesis/fault_pred/xtra_All_errors_with_metainfo.txt'
#                         sep="\t", error_bad_lines=False, parse_dates=True, names=colnames, skiprows=1)
# sap_fault_fee = pd.read_csv(
#     '/media/vasy/Data/Doksik/Learn/thesis/fault_pred/SAP_data/UTF8-tabseperated-ServiceReportSAPExtrakt_FLMxFahrzeuge.txt',
#     sep="\t", error_bad_lines=False)
#
# el_err = pd.read_csv('/media/vasy/Data/Doksik/Learn/thesis/fault_pred/tidy_data/distinct_electric_errors_truck_ID.csv')
#
# pd.merge(el_err, pd.DataFrame(sap_fault_fee["Serialnummer"]).drop_duplicates(),left_on = 'serialnumber',right_on = 'Serialnummer').to_csv(
#     '/media/vasy/Data/Doksik/Learn/thesis/fault_pred/tidy_data/fee_check_truck_ID.csv',index=False)
#
# sap_fault_fee.columns
#
#
# sap_fault_fee_all = pd.read_csv(
#     '/media/vasy/Data/Doksik/Learn/thesis/fault_pred/SAP_data/UTF8-tabseperated-ALL-ServiceReportSAPExtrakt_FLMxFahrzeuge.txt',
#     sep="\t", error_bad_lines=False)
#
# pd.merge(el_err, pd.DataFrame(sap_fault_fee["Serialnummer"]).drop_duplicates(),left_on = 'serialnumber',right_on = 'Serialnummer').to_csv(
#     '/media/vasy/Data/Doksik/Learn/thesis/fault_pred/tidy_data/fee_check_all_truck_ID.csv',index=False)

flag = 0
nrow = 10 ** 5

print "boo!"

i = 1
# TODO NROWS
for chunk in pd.read_csv(path_to_file,
                         sep="\t", error_bad_lines=False, nrows=nrow):
    if flag == 0:
        pd.DataFrame(chunk).loc["vehicleserialnumber"].drop_duplicates().to_csv("/home/vassb/fault_pred_data/truck_ID_fee_check_format_electric_errors.csv",index=False)
        flag = 1
    else:
        pd.DataFrame(chunk).loc["vehicleserialnumber"].drop_duplicates().to_csv("/home/vassb/fault_pred_data/truck_ID_fee_check_format_electric_errors.csv",mode='a',index=False)
print "process ready"