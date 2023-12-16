import torch
from transformers import DNABertModel, DNABertTokenizer
from torch.utils.data import DataLoader, TensorDataset
import numpy as np

# Load pre-trained DNABERT model and tokenizer
model_name = 'Zhihan1996/DNABERT_2'
tokenizer = DNABertTokenizer.from_pretrained(model_name)
model = DNABertModel.from_pretrained(model_name)

# Inference
input_sequence = "GCUCUUGGGCGCAGCCUCAAUGAGGCUGGUGGUGCAAG3"
tokenized_input = tokenizer.encode(input_sequence, return_tensors="pt", padding=True, truncation=True)
outputs = model(**tokenized_input)
embeddings = outputs.last_hidden_state # model outputs
