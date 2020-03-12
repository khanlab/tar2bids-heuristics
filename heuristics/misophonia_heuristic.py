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
    video = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-video_run-{item:02d}_bold')

    info[rest]=[]


    for idx, s in enumerate(seqinfo):
       
        if ('RESTING' in (s.series_description).strip()) and (s.dim4==310):
            info[rest].append({'item': s.series_id})
        elif ('run' in (s.series_description).strip()) or 'video' in (s.series_description.strip()) and (s.dim4==352):
            info[rest].append({'item': s.series_id})


    return info