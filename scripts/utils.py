import pandas as pd
import os

def load_data(file_path):

    input_file = file_path  
    output_file = "../data/MachineLearningRating_v3.csv"  
     # Ensure the directory exists
    output_dir = os.path.dirname(output_file)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    data = pd.read_csv(input_file, delimiter='|') # Delimeter


    data.to_csv(output_file, index=False)

    print(f"File successfully converted and saved as {output_file}")
    return data


def column_categorize(cg):
    """Categorize columns of a DataFrame into numerical and categorical."""
    column_types = {
        'numerical': [],
        'categorical': [],
        'datetime': [],
        'boolean': []
    }
    
    for column in cg.columns:
        if pd.api.types.is_numeric_dtype(cg[column]):
            column_types['numerical'].append(column)
        elif pd.api.types.is_categorical_dtype(cg[column]) or cg[column].dtype == 'object':
            column_types['categorical'].append(column)
        elif pd.api.types.is_datetime64_any_dtype(cg[column]):
            column_types['datetime'].append(column)
        elif pd.api.types.is_bool_dtype(cg[column]):
            column_types['boolean'].append(column)

    return column_types

# Example usage
# df = pd.read_csv("path/to/your/data.csv")  # Load your DataFrame
