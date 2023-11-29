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
    t13d = create_key('{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_acq-MPRAGE_run-{item:02d}_T1w')

    info[rest]=[]
    info[t13d]=[]

    for idx, s in enumerate(seqinfo):
       
        if ('RS' in (s.series_description).strip()):
            info[rest].append({'item': s.series_id})

        elif ('3DT1' in (s.series_description).strip()):
            info[t13d].append({'item': s.series_id})        
              

    return info
