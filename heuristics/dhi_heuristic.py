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
    motion = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-motion_run-{item:02d}_bold')
    face = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-face_run-{item:02d}_bold')

    info[rest]=[]
    info[motion]=[]
    info[face]=[]


    for idx, s in enumerate(seqinfo):
       
        if ('RESTING' in (s.series_description).strip()) and (s.dim4==310):
            info[rest].append({'item': s.series_id})
        elif ('MOTION' in (s.series_description).strip()) and (s.dim4==360):
            info[motion].append({'item': s.series_id})
        elif ('FACE' in (s.series_description).strip()) and (s.dim4==360):
            info[face].append({'item': s.series_id})


    return info