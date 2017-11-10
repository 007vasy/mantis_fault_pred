# making edges data
#    # edges
#        # directed in path which truck when arrived to that stage (accommulate from the three files)
import pandas as pd

import_edges_unordered = '/home/vassb/fault_pred_data/edges_unoredered.csv'
export_edges_ordered = '/home/vassb/fault_pred_data/edges_ordered.csv'

export_vehicle = '/home/vassb/fault_pred_data/'

#big file dropping
chunksize = 10 ** 6

print "boo!"


edges_df = pd.read_csv(import_edges_unordered, parse_dates=True, chunksize=chunksize)

edges_df = edges_df.groupby(["vehicle_serialnumber",'timestamp'],sort = True)
edges_df.to_csv(export_edges_ordered,index=False)

vehicles = edges_df[["vehicle_serialnumber"]].drop_duplicates("vehicle_serialnumber",keep='first')

for vehicle in vehicles:
    edges_df.get_group(vehicle).to_csv(export_vehicle + vehicle + "_edges.csv",index=False)
    print vehicles + "'s path is saved"
print "grouping and ordering is ready"
