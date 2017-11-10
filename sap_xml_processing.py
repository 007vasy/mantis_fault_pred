# SAP xml processing method
import pandas as pd

colnames = ["exclude", "customer related STILL Sales Unit", "serialnumber", "service order number", "exclude",
            "contract number", "company", "equipmentnumber", "Operating Hours Value", "exclude",
            "manually entered operatinghours value after operatinghours unit replacement", "service report number",
            "service task(s) begin", "service task(s) end", "exclude", "exclude", "exchange part number",
            "exchange part name", "truck type", "truck year of construction", "truck purchase date",
            "service technician technical comment", "service technician internal comment"]

sap_xml_fault = pd.read_csv(
    '/media/vasy/Data/Doksik/Learn/thesis/fault_pred/Alle-SBs-ProActive_droprows.csv', error_bad_lines=False,
    parse_dates=True, names=colnames, skiprows=1)  # print sap_fault
print sap_xml_fault.columns

cols = [c for c in sap_xml_fault.columns if c.lower()[:7] != "exclude"]

sap_xml_fault = sap_xml_fault[cols]

print sap_xml_fault.columns

sap_xml_fault.to_csv("/media/vasy/Data/Doksik/Learn/thesis/fault_pred/sap_xml.csv",index=False)
