# electric fail fleet processing
import sys
import pandas as pd

if __name__ == '__main__':
    flag = sys.argv[1]
# from expert knowledge
colnames = ["exclude", "exclude", "componentoperatingseconds", "exclude", "exclude", "exclude", "exclude", "exclude",
            "error_occurred_timestamp", "exclude", "exclude", "exclude", "exclude", "exclude", "exclude", "exclude",
            "vehicle_serialnumber", "exclude", "errorviewdetaildata_id", "exclude", "exclude", "exclude", "exclude",
            "exclude", "exclude", "exclude", "exclude", "exclude", "exclude", "exclude", "exclude", "error_description",
            "exclude", "exclude", "exclude", "s_errorcode"]
if flag:
    path_to_file = '/media/vasy/Data/Doksik/Learn/thesis/fault_pred/xtra_All_errors_with_metainfo.txt'
else:
    path_to_file = '/home/vassb/fault_pred_data/xtra_All_errors_with_metainfo.txt'

if flag:
    electric_errors = pd.read_csv(path_to_file,
                              sep="\t", nrows=5000, error_bad_lines=False, parse_dates=True, names=colnames, skiprows=1)
else:
    electric_errors = pd.read_csv(path_to_file,
                                  sep="\t", error_bad_lines=False, parse_dates=True, names=colnames, skiprows=1)

#print electric_errors.head()

cols = [c for c in electric_errors.columns if c.lower()[:7] != 'exclude']

electric_errors = electric_errors[cols]

#print electric_errors.columns
print electric_errors.describe()

if flag:
    electric_errors.to_csv("/media/vasy/Data/Doksik/Learn/thesis/fault_pred/electric_errors.csv")
else:
    electric_errors.to_csv("/home/vassb/fault_pred_data/electric_errors.csv")