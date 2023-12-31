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

    task = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-task_run-{item:02d}_bold')
    task_sbref = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-task_run-{item:02d}_sbref')

    info[task]=[]
    info[task_sbref]=[]

    for idx, s in enumerate(seqinfo):
       
        if ('bold' in (s.series_description).strip()) and ('M' in (s.image_type[2].strip()) ):
            if (s.dim4==1 and 'SBR' in (s.series_description).strip()):
                info[task_sbref].append({'item': s.series_id})
            elif (s.dim4>1):
                info[task].append({'item': s.series_id})
                    
    return info
