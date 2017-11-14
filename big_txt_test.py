# bit txt test
import pandas as pd


path_to_file = '/media/vasy/Data/Doksik/Learn/thesis/fault_pred/xtra_All_errors_with_metainfo.txt'



chunk = pd.read_csv(path_to_file,
                         sep="\t", error_bad_lines=False, nrows= 1000)


print chunk["vehicleserialnumber"].head()
print chunk.head()

chunk.columns