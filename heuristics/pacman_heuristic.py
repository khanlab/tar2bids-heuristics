import os
import numpy
from cfmm_base import infotodict as cfmminfodict
from cfmm_base import create_key

def infotodict(seqinfo):
    """Heuristic evaluator for determining which runs belong where
    allowed template fields - follow python string module:
    item: index within category
    subject: participant id
    seqitem: run number during scanning
    subindex: sub index within group
    """

    # call cfmm for general labelling and get dictionary
    info = cfmminfodict(seqinfo)

    rest = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-rest_run-{item:02d}_bold')
    task = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-task_run-{item:02d}_bold')
    replay = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-replay_run-{item:02d}_bold')
    replaypassive = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-replaypassive_run-{item:02d}_bold')
    replayactive = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-replayactive_run-{item:02d}_bold')

    #task_PA = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-task_dir-PA_run-{item:02d}_bold')
    

    info[rest]=[]
    info[task]=[]
    info[replay]=[]
    info[replaypassive]=[]
    info[replayactive]=[]
    #info[task_PA]=[]

    for idx, s in enumerate(seqinfo):
       
        if ('task' in (s.series_description).strip()) and (s.dim4>1):
            info[task].append({'item': s.series_id})
                    
        elif ('replay' in (s.series_description).strip()) and (s.dim4>1):
            info[replay].append({'item': s.series_id})   

        elif ('replay_active' in (s.series_description).strip()) and (s.dim4>1):
            info[replayactive].append({'item': s.series_id}) 

        elif ('replay_passive' in (s.series_description).strip()) and (s.dim4>1):
            info[replaypassive].append({'item': s.series_id})          
        
        elif ('rest' in (s.series_description).strip()) and (s.dim4>1):
            info[rest].append({'item': s.series_id})

        #elif ('PA' in (s.series_description).strip()):
            #info[task_PA].append({'item': s.series_id})


    return info
