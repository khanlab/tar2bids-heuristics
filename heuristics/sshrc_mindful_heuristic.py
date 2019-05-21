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

    soundcheck = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-soundcheck_run-{item:02d}_bold')

    mindful = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-mindful_run-{item:02d}_bold')
    
    rest = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-rest_run-{item:02d}_bold')
    
    control1 = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-control1_run-{item:02d}_bold')
    
    control2 = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-control2_run-{item:02d}_bold')
    
    info[soundcheck]=[]
    info[mindful]=[]
    info[rest] = []
    info[control1] = []
    info[control2] = []

    for idx, s in enumerate(seqinfo):
       
        if ('soundcheck' in (s.series_description).strip()):
            if (s.dim4>1):
                    info[soundcheck].append({'item': s.series_id})
                    
        elif ('mindful' in (s.series_description).strip()):
            if (s.dim4>1):
                    info[mindful].append({'item': s.series_id})
        
        elif ('restingState' in (s.series_description).strip()):
            if (s.dim4>1):
                    info[rest].append({'item': s.series_id}) 
                    
        elif ('control1' in (s.series_description).strip()):
            if (s.dim4>1):
                    info[control1].append({'item': s.series_id})
                    
        elif ('control2' in (s.series_description).strip()):
            if (s.dim4>1):
                    info[control2].append({'item': s.series_id})
                    
    return info