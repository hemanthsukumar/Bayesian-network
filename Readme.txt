README


Name: Hemanth Sukumar Vangala
UTA ID: 1002118951


Description:
The code is a Python program that implements a Bayesian network and performs probabilistic inference using enumeration. The program takes as input a training dataset in the form of a text file containing four binary variables 'B', 'G', 'C', and 'F'. The program reads the training dataset using pandas and computes the probabilities of each variable and the joint probability distribution (JPD) of all four variables. 

The program then allows the user to input a query variable and an optional set of evidence variables. If evidence variables are given, the program computes the conditional probability of the query variable given the evidence variables using the JPD and the product rule of probability.

The program takes command-line arguments to specify the training data file, the query variable, and the evidence variables. The program uses the sys.argv array to extract these arguments. 

The main function in the program is `bnet()`, which takes three arguments: `training_data`, `query_variables`, and `evidence_variables`. `training_data` is the path to the text file containing the training dataset. `query_variables` is a dictionary containing the query variable and its value, e.g., {'B': 'Bt'}. `evidence_variables` is an optional dictionary containing the evidence variables and their values, e.g., {'C': 'Cf', 'F': 'Ft'}.

The program first reads the training dataset using pandas and computes the probabilities of each variable and the JPD of all four variables using maximum likelihood estimation. It then displays the probabilities and the JPD to the console.

The program then calculates the JPD for the query variable and the evidence variables (if any) using the probabilities and the product rule of probability. If evidence variables are given, the program also calculates the JPD for the evidence variables. The program then computes the conditional probability of the query variable given the evidence variables using the JPD and the product rule of probability. The program displays the conditional probability to the console.

Overall, the program demonstrates the implementation of a simple Bayesian network and the use of probabilistic inference for reasoning under uncertainty.


Structure:
This code defines a function called `bnet` that takes in three parameters: `training_data`, `query_variables`, and `evidence_variables`. 

The `training_data` parameter is a string representing the path to a CSV file containing training data. The CSV file is assumed to have four columns named 'B', 'G', 'C', and 'F'. 

This code seems to be part of a larger program that implements a Bayesian network. The code contains three functions:

1. `task1(training_data)` - Reads the training data and calculates the probabilities of each variable (B, G, C, and F) as well as the probabilities of G given B and F given G and C. It then displays these probabilities.

2. `task2(training_data, B, G, C, F)` - Reads the training data and calculates the same probabilities as `task1`. It then uses the probabilities to calculate the joint probability distribution (JPD) of B, G, C, and F given specific values of these variables. It displays the JPD.

3. `task3(training_data, query_variables, evidence_variables=None)` - Reads the training data and calculates the same probabilities as `task1`. It then uses the probabilities to calculate the JPD of the variables in `query_variables` given the values of the variables in `evidence_variables`. It displays the JPD.

The `query_variables` parameter is a dictionary containing query variables that represent the variables whose probabilities we are interested in calculating. The keys of the `query_variables` dictionary are variable names and the values are either 'Bt' or 'Bf' for variable B, 'Gt' or 'Gf' for variable G, 'Ct' or 'Cf' for variable C, and 'Ft' or 'Ff' for variable F. 

The `evidence_variables` parameter is an optional dictionary containing evidence variables that represent the variables whose values we are given or assumed to know. The keys of the `evidence_variables` dictionary are variable names and the values are either 'Bt' or 'Bf' for variable B, 'Gt' or 'Gf' for variable G, 'Ct' or 'Cf' for variable C, and 'Ft' or 'Ff' for variable F.

Finally, the code includes an example usage of the `bnet` function that reads the query and evidence variables from the command line arguments and calls the `bnet` function with these variables and the path to the training data file.


Usage:
Run the file “bnet.py”
The command line invocation should follow the following format:

Task 1:
bnet.py <training_data>
	<training_data> text file with training data.
Example:
python bnet.py training_data.txt

Task 2:
bnet.py <training_data> <Bt/Bf> <Gt/Gf> <Ct/Cf> <Ft/Ff>
	<training_data> text file with training data.
	* Bt if B is true, Bf if B is false
	* Gt if G is true, Gf if G is false
	* Ct if C is true, Cf if C is false
	* Ft if F is true, Ff if F is false
Example:
python bnet.py training_data.txt Bt Gf Ct Ff 

Task 3:
bnet.py <training_data> <query variable values> [given <evidence variable values>]
	<training_data> text file with training data.
Example:
python bnet.py training_data.txt Bt Gf given Ff
Python bnet.py training_data.txt Bt Ff


Main Module:
bnet.py
Readme.txt
Note: All files must be in the same folder


Requirements:
OS: Windows or Mac
This program requires Python 3 to run.