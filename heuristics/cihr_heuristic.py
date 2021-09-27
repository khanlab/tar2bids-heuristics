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

    humour = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-humour_run-{item:02d}_bold')
    seinfeld = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-seinfeld_run-{item:02d}_bold')

    info[humour]=[]
    info[seinfeld]=[]

    for idx, s in enumerate(seqinfo):
       
        if ('Humour' in (s.series_description).strip()):
            info[humour].append({'item': s.series_id})
                    
        elif ('Seinfeld' in (s.series_description).strip()):
            info[seinfeld].append({'item': s.series_id})         

    return info
