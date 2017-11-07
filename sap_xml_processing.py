# SAP xml processing method
import pandas as pd

sap_fault = pd.read_csv('/media/vasy/Data/Doksik/Learn/thesis/fault_pred/ServiceReportSAPExtrakt_FLMxFahrzeuge.txt',
                        sep="\t", nrows=200, error_bad_lines=False)
# print sap_fault

print sap_fault.describe()
print sap_fault.head()
