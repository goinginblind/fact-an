```markdown
# Factor Analysis Tool

This project provides a simple script for performing factor analysis on a dataset stored in CSV format. It uses Python, NumPy, pandas, matplotlib, and factor_analyzer.

## Features

- Reads a semicolon-separated CSV file with numerical data.
- Computes the correlation matrix and eigenvalues/eigenvectors.
- Plots the eigenvalues and saves the plot as `plot-eigvals.png`.
- Determines the number of factors using the Kaiser criterion (eigenvalues > 1).
- Calculates and prints factor loadings.
- Performs factor analysis with varimax rotation.

## Usage

1. **Install dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

2. **Prepare your data:**

   - Place your data in a CSV file (semicolon-separated, with column headers).
   - An example file is provided as [`example.csv`](example.csv).

3. **Run the script:**

   ```sh
   python factan.py
   ```

   - When prompted, enter the filename (without `.csv` extension).

4. **Output:**

   - The script prints intermediate results to the console.
   - The eigenvalue plot is saved as plot-eigvals.png.

## File Structure

- factan.py: Main script for factor analysis.
- example.csv: Example dataset.
- requirements.txt: Python dependencies.
- plot-eigvals.png: Output plot (generated after running the script).

## Notes

- The script expects the CSV file to use semicolons (`;`) as separators and commas (`,`) as decimal points.
- The script is interactive and requires user input for the filename.

## License

This project is provided as-is for educational purposes.
```
