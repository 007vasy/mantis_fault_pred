# making edges data
#    # edges
#        # directed in path which truck when arrived to that stage (accommulate from the three files)
import pandas as pd

import_edges_unordered = '/home/vassb/fault_pred_data/edges_unoredered.csv'
export_edges_ordered = '/home/vassb/fault_pred_data/edges_ordered.csv'

export_vehicle = '/home/vassb/fault_pred_data/'

#big file dropping
flag = 0
chunksize = 10 ** 6

print "boo!"

i = 1

for chunk in pd.read_csv(import_edges_unordered, parse_dates=True, chunksize=chunksize):
    print "chunk " + str(i) + " processing started!"
    if flag == 0:
        edges_df = chunk
        flag = 1
    else:
        edges_df = pd.concat([edges_df,chunk],ignore_index=True)
    print "chunk " + str(i) + " has processed!"
    i = i + 1
#if it's too large one can read in one row at time and append for the correct vehicle CSV
#POSSIBLE WORKAROUND

vehicles = edges_df[["vehicle_serialnumber"]].drop_duplicates("vehicle_serialnumber",keep='first')

edges_df = edges_df.groupby(["vehicle_serialnumber"],sort = False)
#edges_df.to_csv(export_edges_ordered,index=False)

#TODO solving nan truck id
for index,row in vehicles.iterrows():
    pd.DataFrame(edges_df.get_group(row["vehicle_serialnumber"])).sort('timestamp').to_csv(export_vehicle + row["vehicle_serialnumber"] + "_edges.csv",index=False)
    print row["vehicle_serialnumber"]
print "grouping and ordering is ready"


#get_group?