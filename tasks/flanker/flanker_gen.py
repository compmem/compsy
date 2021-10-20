import random 
import copy

# define the conditions
conds = [{'condition': 'congruent',
          'direction': 'left',
          'stimulus': '<<<<<<<'
         },
         {'condition': 'congruent',
          'direction': 'right',
          'stimulus': '>>>>>>>'
         },
         {'condition': 'incongruent',
          'direction': 'left',
          'stimulus': '>>><>>>'
         },
         {'condition': 'incongruent',
          'direction': 'right',
          'stimulus': '<<<><<<'
         },
         {'condition': 'mix',
          'direction': 'left',
          'stimulus': '<>><>><'
         },
         {'condition': 'mix',
          'direction': 'right',
          'stimulus': '><<><<>'
         },]

def gen_blocks(num_reps, num_blocks):
    # loop and create the blocks
    blocks = []
    for b in range(num_blocks):
        # loop and create the list
        trials = []
        for i in range(num_reps):
            # extend the trials with copies of the conditions
            trials.extend(copy.deepcopy(conds))
            
        # shuffle the trials
        random.shuffle(trials)
        
        # append the trials to the blocks
        blocks.append(trials)
    return blocks
