import sys
import pandas as pd

def task1(training_data):
    # Read training data
    df = pd.read_csv(training_data, names=['B', 'G', 'C', 'F'], sep='\\s+')
    
    # Calculate probabilities
    p_B = df['B'].value_counts(normalize=True).sort_index().tolist()
    p_C = df['C'].value_counts(normalize=True).sort_index().tolist()
    p_G_given_B = df.groupby('B')['G'].apply(lambda x: x.value_counts(normalize=True).sort_index()).unstack().fillna(0).values.tolist()
    p_F_given_G_C = df.groupby(['G', 'C'])['F'].apply(lambda x: x.value_counts(normalize=True).sort_index()).unstack().fillna(0).values.tolist()
    
    # Display probabilities
    print(f'B : {p_B}')
    print(f'G : {p_G_given_B[0]}')
    print(f'     {p_G_given_B[1]}')
    print(f'C : {p_C}')
    print(f'F : {p_F_given_G_C[0]}')
    print(f'     {p_F_given_G_C[1]}')
    print(f'     {p_F_given_G_C[2]}')
    print(f'     {p_F_given_G_C[3]}')
    
    

def task2(training_data, B, G, C, F):
    # Read training data
    df = pd.read_csv(training_data, names=['B', 'G', 'C', 'F'], sep='\\s+')
    
    # Calculate probabilities
    p_B = df['B'].value_counts(normalize=True).sort_index().tolist()
    p_C = df['C'].value_counts(normalize=True).sort_index().tolist()
    p_G_given_B = df.groupby('B')['G'].apply(lambda x: x.value_counts(normalize=True).sort_index()).unstack().fillna(0).values.tolist()
    p_F_given_G_C = df.groupby(['G', 'C'])['F'].apply(lambda x: x.value_counts(normalize=True).sort_index()).unstack().fillna(0).values.tolist()
    
    # Display probabilities
    print(f'B : {p_B}')
    print(f'G : {p_G_given_B[0]}')
    print(f'     {p_G_given_B[1]}')
    print(f'C : {p_C}')
    print(f'F : {p_F_given_G_C[0]}')
    print(f'     {p_F_given_G_C[1]}')
    print(f'     {p_F_given_G_C[2]}')
    print(f'     {p_F_given_G_C[3]}')
    
    # Calculate JPD
    B_val = 1 if B == 'Bt' else 0
    G_val = 1 if G == 'Gt' else 0
    C_val = 1 if C == 'Ct' else 0
    F_val = 1 if F == 'Ft' else 0
    
    jpd = p_B[B_val] * p_G_given_B[B_val][G_val] * p_C[C_val] * p_F_given_G_C[G_val*2 + C_val][F_val]
    
    # Display JPD
    print(f'JPD for B={B_val}, G={G_val}, C={C_val}, F={F_val} is {jpd}')


def task3(training_data, query_variables, evidence_variables=None):
    # Read training data
    df = pd.read_csv(training_data, names=['B', 'G', 'C', 'F'], sep='\\s+')
    
    # Calculate probabilities
    p_B = df['B'].value_counts(normalize=True).sort_index().tolist()
    p_C = df['C'].value_counts(normalize=True).sort_index().tolist()
    p_G_given_B = df.groupby('B')['G'].apply(lambda x: x.value_counts(normalize=True).sort_index()).unstack().fillna(0).values.tolist()
    p_F_given_G_C = df.groupby(['G', 'C'])['F'].apply(lambda x: x.value_counts(normalize=True).sort_index()).unstack().fillna(0).values.tolist()
    
    # Display probabilities
    print(f'B : {p_B}')
    print(f'G : {p_G_given_B[0]}')
    print(f'     {p_G_given_B[1]}')
    print(f'C : {p_C}')
    print(f'F : {p_F_given_G_C[0]}')
    print(f'     {p_F_given_G_C[1]}')
    print(f'     {p_F_given_G_C[2]}')
    print(f'     {p_F_given_G_C[3]}')
    
    # Calculate JPD
    B_val = 1 if query_variables.get('B') == 't' else 0
    
    G_val = 1 if query_variables.get('G') == 't' else 0
    C_val = 1 if query_variables.get('C') == 't' else 0
    F_val = 1 if query_variables.get('F') == 't' else 0
    
    jpd = p_B[B_val] * p_G_given_B[B_val][G_val] * p_C[C_val] * p_F_given_G_C[G_val*2 + C_val][F_val]
    
    # Display JPD
    print(f'JPD for B={B_val}, G={G_val}, C={C_val}, F={F_val} is {jpd}')
    
    # Calculate conditional probability using inference by enumeration
    if evidence_variables:
        # Calculate JPD for evidence variables
        B_evidence = 1 if evidence_variables.get('B') == 't' else 0
        G_evidence = 1 if evidence_variables.get('G') == 't' else 0
        C_evidence = 1 if evidence_variables.get('C') == 't' else 0
        F_evidence = 1 if evidence_variables.get('F') == 't' else 0
        
        jpd_evidence = p_B[B_evidence] * p_G_given_B[B_evidence][G_evidence] * p_C[C_evidence] * p_F_given_G_C[G_evidence*2 + C_evidence][F_evidence]
        
        # Calculate conditional probability
        conditional_probability = jpd / jpd_evidence
        
        # Display conditional probability
        print(f'Conditional probability for B={B_val}, G={G_val}, C={C_val}, F={F_val} given B={B_evidence}, G={G_evidence}, C={C_evidence}, F={F_evidence} is {conditional_probability}')
        


    
if(len(sys.argv) == 6 and ('given' not in sys.argv)):
    task2(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])

    
elif(not len(sys.argv) == 2):
    query_variables = {}
    evidence_variables = {}

    for i in range(2, len(sys.argv)):
        
        if sys.argv[i] == 'given':
            break
        
        variable, value = sys.argv[i][:1], sys.argv[i][1:]
        query_variables[variable] = value

    for i in range(i+1, len(sys.argv)):
        variable, value = sys.argv[i][:1], sys.argv[i][1:]
        evidence_variables[variable] = value

    task3(sys.argv[1], query_variables, evidence_variables)
    
else:
    task1(sys.argv[1])