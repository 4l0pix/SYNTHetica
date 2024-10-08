import pandas as pd
import numpy as np
from scipy.stats import norm, uniform, expon
import os

def convert_to_csv(file_path):
    """Convert Excel or JSON to CSV if needed, and return the CSV file path."""
    file_ext = os.path.splitext(file_path)[1].lower()
    if file_ext == '.csv':
        return file_path
    elif file_ext == '.xlsx':
        df = pd.read_excel(file_path)
        csv_path = file_path.replace('.xlsx', '.csv')
        df.to_csv(csv_path, index=False)
        return csv_path
    elif file_ext == '.json':
        df = pd.read_json(file_path)
        csv_path = file_path.replace('.json', '.csv')
        df.to_csv(csv_path, index=False)
        return csv_path
    else:
        raise ValueError("Unsupported file format. Only .csv, .xlsx, and .json files are allowed.")

def calculate_statistics(df):
    """Calculate the mean and standard deviation for each numeric column in the DataFrame."""
    stats = {}
    for col in df.select_dtypes(include=[np.number]).columns:
        mean = df[col].mean()
        std_dev = df[col].std()
        if std_dev == 0:  # Handle columns with zero standard deviation
            std_dev = 1e-5  # Set a small positive value to avoid errors
        stats[col] = {'mean': mean, 'std_dev': std_dev}
        print(f"Column: {col}, Mean: {mean}, Standard Deviation: {std_dev}")
    return stats

def generate_synthetic_data(df, stats, distribution='normal', num_samples=None):
    """Generate synthetic data based on the specified distribution and calculated statistics."""
    synthetic_data = pd.DataFrame()
    num_samples = num_samples or len(df)  # Default to original data length if not specified
    for col, stat in stats.items():
        if distribution == 'normal':
            synthetic_data[col] = norm.rvs(loc=stat['mean'], scale=stat['std_dev'], size=num_samples)
        elif distribution == 'uniform':
            min_val = stat['mean'] - (stat['std_dev'] * np.sqrt(3))
            max_val = stat['mean'] + (stat['std_dev'] * np.sqrt(3))
            synthetic_data[col] = uniform.rvs(loc=min_val, scale=(max_val - min_val), size=num_samples)
        elif distribution == 'exponential':
            synthetic_data[col] = expon.rvs(scale=stat['mean'], size=num_samples)
        else:
            raise ValueError("Unsupported distribution type. Choose from 'normal', 'uniform', or 'exponential'.")
    return synthetic_data

def save_synthetic_data(original_df, synthetic_data, output_file, append=False):
    """Save synthetic data to a new file, either by itself or appended to the original data."""
    if append:
        # Append synthetic data to the original data
        combined_data = pd.concat([original_df, synthetic_data], ignore_index=True)
    else:
        # Save only synthetic data
        combined_data = synthetic_data
    combined_data.to_csv(output_file, index=False)

def synthetica(file_path, distribution='normal', append=False, samples=None):
    # Step 1: Convert file to CSV if needed
    csv_path = convert_to_csv(file_path)
    
    # Step 2: Load CSV and calculate statistics
    df = pd.read_csv(csv_path)
    stats = calculate_statistics(df)
    
    # Step 3: Generate synthetic data using calculated statistics
    synthetic_data = generate_synthetic_data(df, stats, distribution=distribution, num_samples=samples)
    
    # Step 4: Save synthetic data based on user's choice (append or brand new file)
    output_file = file_path.replace('.csv', '_synthetic.csv')
    save_synthetic_data(df, synthetic_data, output_file, append=append)
    
    # Provide feedback to the user
    if append:
        print(f"Synthetic data appended to original data and saved to {output_file}")
    else:
        print(f"New synthetic data file saved to {output_file}")


