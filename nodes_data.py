#making nodes_df from distinct errors and fails

import pandas as pd
import numpy as np

#for batman
# import_electric_erros_distinct_errors_codes = "/home/vassb/fault_pred_data/distinct_electric_errors.csv"
#
# import_sap_distinct_values = "/home/vassb/fault_pred_data/distinct_sap_fails.csv"
#
# export_distinct_nodes = "/home/vassb/fault_pred_data/nodes.csv"
#for pc
import_electric_erros_distinct_errors_codes = "/media/vasy/Data/Doksik/Learn/thesis/fault_pred/tidy_data/distinct_electric_errors.csv"

import_sap_distinct_values = "/media/vasy/Data/Doksik/Learn/thesis/fault_pred/tidy_data/distinct_sap_fails.csv"

export_distinct_nodes = "/media/vasy/Data/Doksik/Learn/thesis/fault_pred/tidy_data/nodes.csv"

el_er_df = pd.read_csv(import_electric_erros_distinct_errors_codes,index_col=False)
sap_fails_df = pd.read_csv(import_sap_distinct_values,index_col=False)

el_er_df = pd.DataFrame(el_er_df["s_errorcode"])
sap_fails_df = pd.DataFrame(sap_fails_df["exchange part number"])

el_er_df.columns = ['node_name']
sap_fails_df.columns = ['node_name']

el_er_df = el_er_df.assign(node_type_e_or_f = np.zeros(len(el_er_df.index),dtype=bool))
sap_fails_df = sap_fails_df.assign(node_type_e_or_f = np.ones(len(sap_fails_df.index),dtype=bool))

nodes_df = pd.concat([el_er_df,sap_fails_df],ignore_index = True)

nodes_df.to_csv(export_distinct_nodes)