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
        cols = [c for c in chunk.columns if c.lower()[:7] != 'exclude']
        chunk = chunk[cols]
        #chunk.to_csv(export_electric_erros_distinct_errors_codes)
        flag = 1
        edges_df = chunk
    else:
        cols = [c for c in chunk.columns if c.lower()[:7] != 'exclude']
        chunk = chunk[cols]
        #chunk.to_csv(export_electric_erros_distinct_errors_codes, mode='a', header=False)
        edges_df = pd.concat([edges_df,chunk],ignore_index=True)
    print "chunk " + str(i) + " has processed!"
    i = i + 1
edges_df = edges_df.groupby(["vehicle_serialnumber",'timestamp'],sort = True)
edges_df.to_csv(export_edges_ordered,index=False)

vehicles = edges_df[["vehicle_serialnumber"]].drop_duplicates("vehicle_serialnumber",keep='first')

for vehicle in vehicles:
    edges_df.get_group(vehicle).to_csv(export_vehicle + "_edges.csv",index=False)
    print vehicles + "'s path is saved"
print "grouping and ordering is ready"
