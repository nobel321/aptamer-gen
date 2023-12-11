import re

def extract_between_constant_regions(pool_type, full_sequence):
    # Extract the constant regions from the pool type
    constant_regions = re.split(r'-N\d+-', pool_type)
    
    # Find the start and end positions of the constant regions in the full sequence
    start_position = full_sequence.find(constant_regions[0]) + len(constant_regions[0])
    end_position = full_sequence.find(constant_regions[1])
    
    # Extract the segment between the constant regions
    segment_between_constant_regions = full_sequence[start_position:end_position]
    
    # Exclude the part you want to omit
    part_to_exclude = constant_regions[1].split('-')[0]  # Extract the part to exclude
    segment_between_constant_regions = segment_between_constant_regions.replace(part_to_exclude, '')

    segment_between_constant_regions = ''.join([i for i in segment_between_constant_regions if not i.isdigit()])
    
    return constant_regions, segment_between_constant_regions

# Example usage
pool_type = "5'-GGGAGAUACCAGCUUAUUCAAUU-N71-AGAUAGUAAGUGCAAUCU-3'"
full_sequence = "5'GGGAGAUACCAGCUUAUUCAAUUUCUAGUCAAGUUGCAAUCUCCGGUGGGGUGGUAACCGAGGAACACGUUUCGGGUGUAUAGGCUAGCGAGAUAGUAAGUGCAAUCU3'"

constant_regions, segment_between_constant_regions = extract_between_constant_regions(pool_type, full_sequence)
print("Constant Regions:", constant_regions)
print("Segment Between Constant Regions:", segment_between_constant_regions)
