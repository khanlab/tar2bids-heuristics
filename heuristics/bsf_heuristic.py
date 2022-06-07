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

    foodflanker = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-foodflanker_run-{item:02d}_bold')
    foodflanker_sbref = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-foodflanker_run-{item:02d}_sbref')
    rsafood = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-RSAfood_run-{item:02d}_bold')
    rsafood_sbref = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-RSAfood_run-{item:02d}_sbref')
    
    info[foodflanker]=[]
    info[foodflanker_sbref]=[]
    info[rsafood]=[]
    info[rsafood_sbref]=[]

    for idx, s in enumerate(seqinfo):
       
        if ('foodflanker' in (s.series_description).strip()):
            if (s.dim4==1 and 'SBRef' in (s.series_description).strip()):
                info[task_sbref].append({'item': s.series_id})
            elif (s.dim4>2):
                info[task].append({'item': s.series_id})

        if ('RSAfood' in (s.series_description).strip()):
            if (s.dim4==1 and 'SBRef' in (s.series_description).strip()):
                info[task_sbref].append({'item': s.series_id})
            elif (s.dim4>2):
                info[task].append({'item': s.series_id})
                    
    return info
