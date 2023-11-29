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

    play = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-play_run-{item:02d}_bold')
    react = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-react_run-{item:02d}_bold')
    watch = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-watch_run-{item:02d}_bold')
    

    info[play]=[]
    info[react]=[]
    info[watch]=[]

    for idx, s in enumerate(seqinfo):
       
        if ('PLAY' in (s.series_description).strip()) and (s.dim4>1):
            info[play].append({'item': s.series_id})
                    
        elif ('REACT' in (s.series_description).strip()) and (s.dim4>1):
            info[react].append({'item': s.series_id})  

        elif ('WATCH' in (s.series_description).strip()) and (s.dim4>1):
            info[watch].append({'item': s.series_id})             
        

    return info
