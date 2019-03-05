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

    lh = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-lh_run-{item:02d}_bold')

    rh = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-rh_run-{item:02d}_bold')
    
    info[lh]=[]
    info[rh]=[]

    for idx, s in enumerate(seqinfo):
       
        if ('LH' in (s.series_description).strip()):
            if (s.dim4>1):
                    info[lh].append({'item': s.series_id})
                    
        elif ('RH' in (s.series_description).strip()):
            if (s.dim4>1):
                    info[rh].append({'item': s.series_id})            
                    
    return info