import openai
from apikey import API_KEY
openai.api_key = API_KEY

ATTRIBUTES = None

usr_input = input("Proompt: ")

output = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content":
               """
               fill out this template each time with the provided input:
               1. Target Molecule: <inputed_affinity>
               2. pH: <inputed_ph>
               3. Affinity: <inputed_affinity>
               4. Buffer: <inputed_buffer>

               don't include parts of the list for which no value was inputed. If it's not provided, don't include that value or section of the list (remove the numbered part). 
               
               Here's an example output:
               1. Target Molecule: T4 DNA polymerase (gp43)
               2. pH: 8.5
               6. Affinity: Kd~600µM

               Stay consistent to the instructions i provided and always follow the template for which the values are mentioned. Never stray from the template.
               """ + usr_input
               }]
)

output_ = output['choices'][0]['message']['content']

# print(output['choices'][0]['message']['content'])

def create_indexed_list(input_string):
    # Split the input string by lines and strip any leading/trailing whitespaces
    lines = [line.strip() for line in input_string.split('\n') if line.strip()]
    
    # Create a dictionary to store the indexed values
    indexed_values = {}
    
    # Iterate over the lines and extract the values
    for line in lines:
        # Split each line by ":" to separate the index and the value
        parts = line.split(":")
        if len(parts) == 2:
            index = parts[0].strip().split('.')[0]  # Extract the index from the line
            value = parts[1].strip()
            indexed_values[index] = value
    
    # Create a list where the values are assigned to the corresponding index
    indexed_list = [indexed_values.get(str(i), None) for i in range(1, 5)]  # Use range(1, 9) to cover indices 1 to 8
    
    return indexed_list

result = create_indexed_list(output_)
print(result)

ATTRIBUTES = result

#objectives
"""
- replace variable region of original sequence
- understand how gene sequences folding - tertiary/secondary structures
- output sequence
- setup binding affinity test
"""

"""
Output, based on the text (and according to the order I list them), what the mentioned 1. Target Molecule, 2. pH, 3. Type of Nucleic Acid, 4. GC Content, 5. Sequence Length, 
               6. Affinity, 7. Molecular Weight, 8. Type of buffer, are. Output everything that you find in the users sentence in order to fill the list I provided with no spaces in between but each parameter
               has a new line. Match output with corresponding numbers for each parameter. Make sure not to make up values and only list what the user gives you.
               If the user doesn\'t give a certain value don\'t include it in the output. Here\'s the user input. Adhere strictly to everything listed:

"""