import sys
sys.path.append('../..')

from SALib.sample import fast_sampler
from SALib.analyze import extended_fast
from SALib.test_functions import Ishigami
import numpy as np

# Read the parameter range file and generate samples
param_file = '../../SALib/test_functions/params/Ishigami.txt'

# Generate samples
param_values = fast_sampler.sample(2048, param_file)

# Run the "model" and save the output in a text file
# This will happen offline for external models
Y = Ishigami.evaluate(param_values)
np.savetxt("model_output.txt", Y, delimiter=' ')

# Perform the sensitivity analysis using the model output
# Specify which column of the output file to analyze (zero-indexed)
Si = extended_fast.analyze(param_file, 'model_output.txt', column = 0)
#Returns a dictionary with keys 'S1' and 'ST'
# e.g. Si['S1'] contains the first-order index for each parameter, in the same order as the parameter file
