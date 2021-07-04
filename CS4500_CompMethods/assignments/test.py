import random
from csv import DictReader
import copy

# function to make a study/test block from the pools past in
def gen_block(pools, cond, num_items):
    # fill the study list
    study_list = []
    
    # loop over pools
    for pool in pools:
        # loop over items to add from that pool
        # this will be num_items/num_types for mixed lists
        for i in range(num_items):
            study_item = pool.pop()
            study_item.update({'novelty': 'target', 
                               'cond': cond})
            study_list.append(study_item)

    # shuffle the study_list
    random.shuffle(study_list)
    
    # copy the study list to be the start of the test list
    test_list = copy.deepcopy(study_list)
    
    # loop over pools
    for pool in pools:
        # loop over items to add from that pool
        # this will be num_items/num_types for mixed lists
        for i in range(num_items):
            test_item = pool.pop()
            test_item.update({'novelty': 'lure', 
                              'cond': cond})
            test_list.append(test_item)
    
    # shuffle the test list
    random.shuffle(test_list)
    
    return {'study': study_list, 'test': test_list}

# config variables
indoor_file = 'indoor.csv'
outdoor_file = 'outdoor.csv'

# number of pools
num_pools = 2

# number of items in pure lists (must be evenly divisible by num_pools)
num_items_pure = 10

# number of repetitions of each block type
num_reps = 3       

# verify these numbers make sense
num_items_mixed = int(num_items_pure / num_pools)
assert num_items_mixed * num_pools == num_items_pure


# load in the pools
indoor_pool = [i for i in DictReader(open(indoor_file, 'r'))]
outdoor_pool = [i for i in DictReader(open(outdoor_file, 'r'))]


# shuffle the pools
random.shuffle(indoor_pool)
random.shuffle(outdoor_pool)


# generate the blocks
blocks = []
for r in range(num_reps):
    # generate a pure indoor block
    blocks.append(gen_block([indoor_pool], 'indoor', 
                            num_items_pure))
    
    # generate a pure outdoor block
    blocks.append(gen_block([outdoor_pool], 'outdoor', 
                            num_items_pure))
    
    # generate a mixed indoor/outdoor block
    blocks.append(gen_block([indoor_pool, outdoor_pool], 'mixed', 
                            num_items_mixed))

# shuffle the blocks
random.shuffle(blocks)

# Load in the most common SMILE states
from smile.common import *
from smile.scale import scale as s
from smile.startup import InputSubject
# import os


# enter configuration variables here (including the listgen variables)
font_size = 50
resp_keys = ['T', 'L']
resp_map = {'target': 'T', 'lure': 'L'}
ISI_dur = 0.5
ISI_jitter = 0.25
inst_font_size = 38
inst_text = """[b][u][size=45]SCENE STUDY INSTRUCTIONS[/size][/b][/u]
In this task, you will study a series of images
Afterwards, you must identify whether 
an image shown in a test was studied or not.
Press T if the image was studied
Press L if the image is new
    
Press SPACEBAR to continue."""


# create the experiment
exp = Experiment(name='SceneStudy', show_splash=False, 
                 fullscreen=True)
#                  resolution=(1024, 768))


@Subroutine
def Instruct(self):
    # show the instructions
    Label(text=inst_text, font_size=inst_font_size,
          text_size=(exp.screen.width*0.75, None),
          markup=True, halign='center')
    with UntilDone():
        KeyPress(keys=['SPACEBAR'])

        
@Subroutine
def Study(self, block_num, trial_num, cur_trial):
    Debug(trial_type=cur_trial['in_out'],
            image_path=cur_trial['in_out'] + '/' + cur_trial['filename'])
    stim = Image(source=(cur_trial['in_out'] + "/" + cur_trial['filename']), 
                 width=400, height=400, allow_stretch=True)
#     stim = Image(source=os.path.join(cur_trial['in_out'], cur_trial['filename']), 
#              width=400, height=400, allow_stretch=True)
    with UntilDone():
        Wait(ISI_dur*3)      
# Set up a log file here too     
        
@Subroutine
def Test(self, block_num, trial_num, cur_trial):
    Debug(trial_type=cur_trial['in_out'],
            image_path=cur_trial['in_out'] + '/' + cur_trial['filename'])
    stim = Image(source=(cur_trial['in_out'] + "/" + cur_trial['filename']), 
                 width=400, height=400, allow_stretch=True)
#     stim = Image(source=(os.path.join(cur_trial['in_out'], cur_trial['filename'])), 
#          width=400, height=400, allow_stretch=True)
    with UntilDone():
        Wait(until=stim.appear_time)                  # make sure the stimulus has appeared on the screen
        kp = KeyPress(keys=resp_keys,                 # collect a response (with no timeout)
                      base_time=stim.appear_time['time'],
                      correct_resp=Ref.object(resp_map)[cur_trial['novelty']])
    Wait(ISI_dur)                                     # wait the ISI 
    Log(name='scenestudy',                            # log the result of the trial
        log_dict=cur_trial,
        block_num=block_num,
        trial_num=trial_num,
        stim_on=stim.appear_time,
        resp=kp.pressed,
        resp_time=kp.press_time,
        rt=kp.rt,
        correct=kp.correct,
       )
    

InputSubject('Scene Study')
Instruct()                                            # show the instructions
Wait(0.5)


with Loop(blocks) as block:                           # loop over the blocks
    Label(text='Press the SPACEBAR to\nstart the next block', 
          font_size=font_size, halign='center')
    with UntilDone():
        KeyPress(keys=['SPACEBAR'])
    Wait(ISI_dur, jitter=ISI_jitter)                  # add in some delay before the start of the block
    with Loop(block.current['study']) as study_trial:
        Study(block.i, study_trial.i, study_trial.current)
    Label(text='Remember\nPress T if the image was studied\nPress L if the image is new\n',
          font_size=font_size, halign='center')
    with UntilDone():
        Wait(ISI_dur*4)                               # wait the ISI 
    with Loop(block.current['test']) as test_trial:
        Test(block.i, test_trial.i, test_trial.current)

        
Label(text='Congratulations!\nYou have finished the experiment\n\nPress SPACEBAR to exit', 
      font_size=font_size, halign='center')
with UntilDone():
    KeyPress(keys=['SPACEBAR'])

        
# run the experiment
exp.run()

