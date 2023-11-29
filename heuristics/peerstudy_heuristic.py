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
    rest_sbref = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-rest_run-{item:02d}_sbref')

    feedback = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-feedback_run-{item:02d}_bold')
    feedback_sbref = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-feedback_run-{item:02d}_sbref')

    info[rest]=[]
    info[rest_sbref]=[]
    info[feedback]=[]
    info[feedback_sbref]=[]

    for idx, s in enumerate(seqinfo):
       
        if ('resting' in (s.series_description).strip()):
            if (s.dim4==1 and  'SBRef' in (s.series_description).strip()):
                    info[rest_sbref].append({'item': s.series_id})
            elif (s.dim4>500):
                    info[rest].append({'item': s.series_id})
                    
        elif ('feedback' in (s.series_description).strip()):
            if (s.dim4==1 and  'SBRef' in (s.series_description).strip()):
                    info[feedback_sbref].append({'item': s.series_id})
            elif (s.dim4>700):
                    info[feedback].append({'item': s.series_id})            

    return info
