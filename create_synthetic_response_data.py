import pandas as pd
from sdv.single_table import GaussianCopulaSynthesizer
from sdv.metadata import Metadata

data = pd.read_csv('./data/data_responses.csv')
metadata = Metadata.detect_from_dataframe(data)

synthesizer = GaussianCopulaSynthesizer(metadata)
synthesizer.fit(data)
synthetic_data = synthesizer.sample(num_rows=12000)
synthetic_data.to_csv('synthetic_data_responses.csv', index=False)