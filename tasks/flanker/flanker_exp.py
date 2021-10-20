from smile.common import *
from smile.scale import scale as s

import flanker_gen

# config section

# specify number of reps of the conditions
num_reps = 8
num_blocks = 4

font_size = 75
resp_keys = ['F', 'J']

resp_map = {'left': 'F', 'right': 'J'}
ISI_dur = 0.5
ISI_jitter = 0.5
LOC_X_jitter = 300
LOC_Y_jitter = 100

inst_title_font_size = 40
inst_font_size = 25
inst_text = """[u][size={}]FLANKER INSTRUCTIONS[/size][/u]

In this task, you must indicate what direction the MIDDLE arrow is pointing, while ignoring the flanking stimuli.

Press {} to indicate that the arrow is pointing left, or {} to indicate that the arrow is pointing right. 

Please answer as quickly and as accurately as possible.
    
Press the ENTER key to continue."""



@Subroutine
def Instruct(self, resp_map):
    # show the instructions
    Label(text=Ref(inst_text.format, Ref(int, s(inst_title_font_size)),
                   resp_map['left'], resp_map['right']), 
          font_size=s(inst_font_size),
          text_size=(self.exp.screen.width*0.75, None),
          markup=True)
    with UntilDone():
        KeyPress(keys=['ENTER'])

@Subroutine
def Trial(self, block_num, trial_num, cur_trial, resp_map):
    # pick the new stimulus location
    self.location = (jitter(self.exp.screen.center_x-s(LOC_X_jitter),
                            s(LOC_X_jitter)*2),
                     jitter(self.exp.screen.center_y-s(LOC_Y_jitter),
                            s(LOC_Y_jitter)*2))
    # present the stimulus
    stim = Label(text=cur_trial['stimulus'],
                 font_size=s(font_size),
                 center=self.location)
    with UntilDone():
        # make sure the stimulus has appeared on the screen
        Wait(until=stim.appear_time)
        
        # collect a response (with no timeout)
        kp = KeyPress(keys=resp_keys, 
                      base_time=stim.appear_time['time'],
                      correct_resp=resp_map[cur_trial['direction']])
    # wait the ISI with jitter
    Wait(ISI_dur, jitter=ISI_jitter)

    # log the result of the trial
    Log(name='flanker', 
        log_dict=cur_trial,
        resp_map=resp_map,
        block_num=block_num,
        trial_num=trial_num,
        stim_on=stim.appear_time,
        resp=kp.pressed,
        resp_time=kp.press_time,
        rt=kp.rt,
        correct=kp.correct,
        location=self.location
       )

@Subroutine
def FlankerExp(self, blocks):
    # show the instructions
    self.resp_map = resp_map
    Instruct(self.resp_map)
    Wait(0.5)
    
    # loop over the blocks
    with Loop(blocks) as block:
        # make sure they are ready to continue
        Label(text='Press the ENTER key to\nstart the next block.', 
              font_size=s(inst_title_font_size), halign='center')
        with UntilDone():
            KeyPress(keys=['ENTER'])

        # add in some delay before the start of the block
        Wait(ISI_dur*3, jitter=ISI_jitter)
        
        # loop over the trials
        with Loop(block.current) as trial:
            Trial(block.i, trial.i, cur_trial=trial.current,
                  resp_map=self.resp_map)


if __name__ == "__main__":

    # generate blocks
    fblocks = flanker_gen.gen_blocks(num_reps, num_blocks)
    
    # instantiate exp with scaling
    exp = Experiment(name='Flanker', show_splash=True, 
                     #fullscreen=False, debug=False,
                     #resolution=(1024, 768), 
                     scale_up=True, scale_down=True,
                     scale_box=(1024, 768))

    Wait(0.5)

    # run the task
    FlankerExp(fblocks)

    Label(text='You are all done!!!\nPress the ENTER key to go celebrate.', 
          font_size=s(font_size), halign='center')
    with UntilDone():
        KeyPress(keys=['ENTER'])
    
    exp.run()
