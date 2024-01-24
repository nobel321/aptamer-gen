# Hybridization Aptamer Generation Algorithm (HAGA)

HAGA is an AI program designed to predict the binding affinity between a target and a DNA sequence using aptamer prediction methods. This program leverages deep learning approaches to provide accurate and efficient predictions of aptamer-protein interactions. Though it's still in development, currently the project's basic functionalities can be encapsulated in the phrase: **[BLAST]([url](https://blast.ncbi.nlm.nih.gov/Blast.cgi)) for aptamers**

## Features

- ~~Predicts the binding affinity between a target and a DNA sequence~~
- Utilizes deep learning approaches for aptamer prediction
- Provides accurate and efficient predictions of aptamer-protein interactions

## Installation

To install HAGA, follow these steps:

1. Clone the repository from GitHub:

   ```bash
   git clone https://github.com/nobel321/aptamer-gen.git
   ```

2. Navigate to the project directory:

   ```bash
   cd aptamer-gen
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the program:

   ```bash
   python predict_affinity.py
   ```

## Usage

After installing the program, you can use it to predict the binding affinity by providing the target and the DNA sequence as input. Here's an example of how to use the program:

```python
from aptamer_gen import predict_binding_affinity

target = 'Your Target of Interest'
dna_sequence = 'Your DNA Sequence of Interest'

predicted_affinity = predict_binding_affinity(target, dna_sequence)
print(f"The predicted binding affinity between the target and the DNA sequence is: {predicted_affinity}")
```

## References

- [AptaNet - Deep Learning approach for Aptamer-Protein Interaction Prediction](https://github.com/nedaemami/AptaNet)
- [AptamerBase - Database of Aptamer Experimental Conditions](https://github.com/micheldumontier/aptamerbase)

## License

This program is distributed under the MIT license. See the [LICENSE](https://github.com/nobel321/aptamer-gen/blob/main/LICENSE) file for more details.

For more information, please visit the [Aptamer-Gen](https://github.com/nobel321/aptamer-gen) repository.

Citations:
[1] https://github.com/nobel321/aptamer-gen
[2] https://github.com/micheldumontier/aptamerbase
[3] https://github.com/yq342/Aptamer-predictor
[4] https://github.com/nedaemami/AptaNet
[5] https://github.com/topics/aptamers
