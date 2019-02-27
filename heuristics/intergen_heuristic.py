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

    inscape = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-inscape_run-{item:02d}_bold')

    math = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-math_run-{item:02d}_bold')

    read = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-read_run-{item:02d}_bold')

    line = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-line_run-{item:02d}_bold')
    

    info[rest]=[]
    info[inscape]=[]
    info[math]=[]
    info[read]=[]
    info[line]=[]

    for idx, s in enumerate(seqinfo):
       
        if ('rsfMRI' in (s.series_description).strip()) and (s.dim4==232):
            info[inscape].append({'item': s.series_id})
                    
        elif ('math' in (s.series_description).strip()) and (s.dim4==244):
            info[math].append({'item': s.series_id})            
        
        elif ('read' in (s.series_description).strip()) and (s.dim4==244):
            info[read].append({'item': s.series_id})

        elif ('line' in (s.series_description).strip()) and (s.dim4==244):
            info[line].append({'item': s.series_id})
        
        elif ('restingState' in (s.series_description).strip()) and (s.dim4==360):
            info[rest].append({'item': s.series_id})


    return info