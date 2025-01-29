import pandas as pd

def load_data(complaints_file, kpi_file):
    """
    Load customer complaints and KPI data.
    """
    complaints = pd.read_csv(complaints_file)
    kpi_data = pd.read_csv(kpi_file)
    return complaints, kpi_data
#
