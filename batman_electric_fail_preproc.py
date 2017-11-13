# electric fail fleet processing batman
import pandas as pd

# from expert knowledge
colnames = ["exclude", "exclude", "componentoperatingseconds", "exclude", "exclude", "exclude", "exclude", "exclude",
            "error_occurred_timestamp", "exclude", "exclude", "exclude", "exclude", "exclude", "exclude", "exclude",
            "vehicle_serialnumber", "exclude", "errorviewdetaildata_id", "exclude", "exclude", "exclude", "exclude",
            "exclude", "exclude", "exclude", "exclude", "exclude", "exclude", "exclude", "exclude", "error_description",
            "exclude", "exclude", "exclude", "s_errorcode"]
path_to_file = '/home/vassb/fault_pred_data/xtra_All_errors_with_metainfo.txt'

flag = 0
nrow = 10 ** 5

print "boo!"

i = 1
# TODO NROWS
for chunk in pd.read_csv(path_to_file,
                         sep="\t", error_bad_lines=False, parse_dates=True, names=colnames, skiprows=1,
                         nrow=nrow):
    print "chunk "+str(i)+" processing started!"
    if flag == 0:
        cols = [c for c in chunk.columns if c.lower()[:7] != 'exclude']
        chunk = chunk[cols]
        chunk.to_csv("/home/vassb/fault_pred_data/electric_errors.csv",index=False)
        flag = 1
    else:
        cols = [c for c in chunk.columns if c.lower()[:7] != 'exclude']
        chunk = chunk[cols]
        chunk.to_csv('/home/vassb/fault_pred_data/electric_errors.csv', mode='a', header=False,index=False)
    print "chunk "+str(i)+" has processed!"
    i = i+1
print "process ready"
#print electric_errors.head()
