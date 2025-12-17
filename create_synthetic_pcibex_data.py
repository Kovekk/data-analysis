import pandas as pd
from sdv.single_table import GaussianCopulaSynthesizer
from sdv.metadata import Metadata

data = pd.read_csv('./data/datafull.csv')
# print(data.describe())
metadata = Metadata.detect_from_dataframe(data)

synthesizer = GaussianCopulaSynthesizer(metadata)
synthesizer.fit(data)
print("Fitting complete.")
print("Generating synthetic data...")
synthetic_data = synthesizer.sample(num_rows=400000)
print("Synthetic data generation complete.")
synthetic_data.to_csv('synthetic_pcibex_data.csv', index=False)