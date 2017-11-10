# making edges data
#    # edges
#        # directed in path which truck when arrived to that stage (accommulate from the three files)
import pandas as pd
import numpy as np

path_to_electric_errors_csv = '/home/vassb/fault_pred_data/electric_errors.csv'
path_to_sap_txt_csv = '/home/vassb/fault_pred_data/sap_txt.csv'
path_to_sap_xml_csv = '/home/vassb/fault_pred_data/sap_xml.csv'

edges_unordered = '/home/vassb/fault_pred_data/edges_unoredered.csv'

#big file dropping
flag = 0
chunksize = 10 ** 6

print "boo!"

i = 1

for chunk in pd.read_csv(path_to_electric_errors_csv, parse_dates=True, chunksize=chunksize):
    print "chunk " + str(i) + " processing started!"
    if flag == 0:
        chunk = chunk[["error_occurred_timestamp","s_errorcode","vehicle_serialnumber"]]
        chunk.columns = ['timestamp','to_go_node',"vehicle_serialnumber"]
        chunk = chunk.assign(fail_in=np.zeros(len(chunk.index), dtype=bool))
        chunk = chunk.assign(fail_out=np.zeros(len(chunk.index), dtype=bool))
        chunk.to_csv(edges_unordered,index=False)
        flag = 1
    else:
        chunk = chunk[["error_occurred_timestamp","s_errorcode","vehicle_serialnumber"]]
        chunk.columns = ['timestamp', 'to_go_node', "vehicle_serialnumber"]
        chunk = chunk.assign(fail_in=np.zeros(len(chunk.index), dtype=bool))
        chunk = chunk.assign(fail_out=np.zeros(len(chunk.index), dtype=bool))
        chunk.to_csv(edges_unordered, mode='a', header=False,index=False)
    print "chunk " + str(i) + " has processed!"
    i = i + 1
print chunk.columns
print "process ready"

#######################################################################################################################

sap_txt_fault = pd.read_csv(path_to_sap_txt_csv, parse_dates=True)

sap_txt_fault_edges_in = sap_txt_fault[["service task(s) begin","exchange part number","serialnumber"]]
sap_txt_fault_edges_in.columns = ['timestamp','to_go_node',"vehicle_serialnumber"]
sap_txt_fault_edges_in = sap_txt_fault_edges_in.assign(fail_in=np.ones(len(sap_txt_fault_edges_in.index), dtype=bool))
sap_txt_fault_edges_in = sap_txt_fault_edges_in.assign(fail_out=np.zeros(len(sap_txt_fault_edges_in.index), dtype=bool))

sap_txt_fault_edges_out = sap_txt_fault[["service task(s) end","exchange part number","serialnumber"]]
sap_txt_fault_edges_out.columns = ['timestamp','to_go_node',"vehicle_serialnumber"]
sap_txt_fault_edges_out = sap_txt_fault_edges_out.assign(fail_in=np.zeros(len(sap_txt_fault_edges_out.index), dtype=bool))
sap_txt_fault_edges_out = sap_txt_fault_edges_out.assign(fail_out=np.ones(len(sap_txt_fault_edges_out.index), dtype=bool))

#######################################################################################################################

sap_xml_fault = pd.read_csv(path_to_sap_xml_csv, parse_dates=True)

sap_xml_fault_edges_in = sap_xml_fault[["service task(s) begin","exchange part number","serialnumber"]]
sap_xml_fault_edges_in.columns = ['timestamp','to_go_node',"vehicle_serialnumber"]
sap_xml_fault_edges_in = sap_xml_fault_edges_in.assign(fail_in=np.ones(len(sap_xml_fault_edges_in.index), dtype=bool))
sap_xml_fault_edges_in = sap_xml_fault_edges_in.assign(fail_out=np.zeros(len(sap_xml_fault_edges_in.index), dtype=bool))

sap_xml_fault_edges_out = sap_xml_fault[["service task(s) end","exchange part number","serialnumber"]]
sap_xml_fault_edges_out.columns = ['timestamp','to_go_node',"vehicle_serialnumber"]
sap_xml_fault_edges_out = sap_xml_fault_edges_out.assign(fail_in=np.zeros(len(sap_xml_fault_edges_out.index), dtype=bool))
sap_xml_fault_edges_out = sap_xml_fault_edges_out.assign(fail_out=np.ones(len(sap_xml_fault_edges_out.index), dtype=bool))

#######################################################################################################################
sap_edges = pd.concat([sap_txt_fault_edges_in,sap_txt_fault_edges_out,sap_xml_fault_edges_in,sap_xml_fault_edges_out],ignore_index = True)
sap_edges.to_csv(edges_unordered, mode='a', header=False,index=False)

print sap_edges.columns