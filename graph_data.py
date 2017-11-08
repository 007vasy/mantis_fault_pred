#pilot graph build with graph data collection
#nodes
    #from electric_errors.csv all truck distinct all good phase (after sap state too)
    #first phase
        #from electric_errors.csv   distinct error codes
        #from sap_txt.csv           distinct exchange part codes
        #from sap_xml.csv           distinct exchange part codes
    #second phase
        #from sap_txt.csv           where is no exchange part number technical worker comment text mining
        #from sap_xml.csv           where is no exchange part number technical worker comment text mining
#paths
    #directed in path which truck when arrived to that stage (accommulate from the three files)
