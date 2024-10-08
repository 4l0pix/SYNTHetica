# SYNTHetica
A usefull homecooked tool for fast synthetic data generation.
-    Features
  1) File Conversion: Convert .xlsx or .json files to .csv.
  2) Synthetic Data Generation: Generate synthetic data using distributions such as Normal (Gaussian), Uniform, or Exponential.
  3) Customizable Parameters: Control distribution parameters (e.g., mean, standard deviation) for synthetic data generation.
  4) Flexible Output: Choose to create a new file with only synthetic data or append synthetic data to the original dataset in a new file.

-    Installation

Ensure you have Python installed (>=3.6), and install the required packages!
pip install pandas numpy scipy

Use the synthetica() function in synthetic_data_generator.py by providing the following arguments:

    syntehtica(file_path, distribution='normal', mean=0, std_dev=1, scale=1, append=False)

An example as refference:

    from synthetica import synthetica
    file_path = "yourFilew.csv/xlsx/json"
    synthetica(file_path, distribution='normal', append=True, samples=1000)



Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

License: Distributed under the MIT License. See LICENSE for more information.
