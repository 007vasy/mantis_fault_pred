# electric fail fleet processing
import pandas as pd

# from expert knowledge
colnames = ["exclude", "exclude", "componentoperatingseconds", "exclude", "exclude", "exclude", "exclude", "exclude",
            "error_occurred_timestamp", "exclude", "exclude", "exclude", "exclude", "exclude", "exclude", "exclude",
            "vehicle_serialnumber", "exclude", "errorviewdetaildata_id", "exclude", "exclude", "exclude", "exclude",
            "exclude", "exclude", "exclude", "exclude", "exclude", "exclude", "exclude", "exclude", "error_description",
            "exclude", "exclude", "exclude", "s_errorcode"]

electric_errors = pd.read_csv('/media/vasy/Data/Doksik/Learn/thesis/fault_pred/xtra_All_errors_with_metainfo.txt',
                              sep="\t", nrows=5000, error_bad_lines=False, parse_dates=True, names=colnames, skiprows=1)

print electric_errors.head()

cols = [c for c in electric_errors.columns if c.lower()[:7] != 'exclude']

electric_errors = electric_errors[cols]

print electric_errors.columns

electric_errors.to_csv("/media/vasy/Data/Doksik/Learn/thesis/fault_pred/electric_errors.csv")

