# SteelEye Data Engineer Technical Assessment

This repository contains my solution for the SteelEye Data Engineer technical assessment.
✅ Downloads DLTINS data from ESMA  
✅ Extracts XML from ZIP  
✅ Parses instrument data into a DataFrame  
✅ Enriches it with custom fields (`a_count`, `contains_a`)  
✅ Exports the result to CSV  

## Requirements

- Python 3.x
- Pandas
- Requests
- pytest

## How to run

1. Clone the repo:
```bash
git clone https://github.com/tanjilh136/steeleye-data-engineer-assessment.git

2.Install dependencies:
    pip install -r requirements.txt

3. Run the pipeline:
    python -m steeleye_assignment.main
4. Run tests :
    python -m unittest discover -s tests

The resulting file will be saved at:
    output/dltins_output.csv
It contains:

-> Instrument ID, Name, Classification

-> Issuer

-> a_count: Number of 'a' in name

-> contains_a: YES/NO

## 📜 Author

- 👤 Tanjil Hasan 
- 🌍 Porto, Portugal
- 🧰 GitHub: [github.com/tanjilh136](https://github.com/tanjilh136)
