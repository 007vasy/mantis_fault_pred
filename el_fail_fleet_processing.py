#electric fail fleet processing
import pandas as pd

electric_errors = pd.read_csv('/media/vasy/Data/Doksik/Learn/thesis/fault_pred/xtra_All_errors_with_metainfo.txt',
                              sep="\t", nrows=20, error_bad_lines=False)
# print electric_errors


print electric_errors.describe()
print electric_errors.head()