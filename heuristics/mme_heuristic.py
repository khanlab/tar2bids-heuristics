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

    task_prc = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-prc_run-{item:02d}_bold')
    task_intact = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-intact_run-{item:02d}_bold')

    info[task_prc]=[]
    info[task_intact]=[]

    for idx, s in enumerate(seqinfo):

        if ('PRC' in (s.series_description).strip() and s.dim4>1):
            info[task_prc].append({'item': s.series_id})

        elif ('Intact' in (s.series_description).strip() and s.dim4>1):
            info[task_intact].append({'item': s.series_id})
        
                   
    return info