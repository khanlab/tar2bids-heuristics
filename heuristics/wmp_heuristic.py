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
    
    #gre_diff = create_key('{bids_subject_session_dir}/fmap/{bids_subject_session_prefix}_run-{item:02d}_phasediff')
    #gre_magnitude = create_key('{bids_subject_session_dir}/fmap/{bids_subject_session_prefix}_run-{item:02d}_magnitude')
    

    #fmap = create_key('{bids_subject_session_dir}/fmap/{bids_subject_session_prefix}_dir-{dir}_epi')
    fmap_sbref = create_key('{bids_subject_session_dir}/fmap/{bids_subject_session_prefix}_dir-{dir}_epi')

    info[task]=[]
    info[task_sbref]=[]
    #info[fmap]=[]
    info[fmap_sbref]=[]

    for idx, s in enumerate(seqinfo):
       
        if ('bold' in (s.series_description).strip()):
            if (s.dim4==1 and 'SBRef' in (s.series_description).strip()):
                info[task_sbref].append({'item': s.series_id})
            elif (s.dim4>1):
                info[task].append({'item': s.series_id})
                
        elif ('PA' in (s.series_description).strip()):
            if (s.dim4==1):
                if 'SBRef' in (s.series_description).strip():
                    info[fmap_sbref].append({'item': s.series_id,'dir': 'PA'})
                #else:
                #    info[fmap].append({'item': s.series_id,'dir': 'PA'})


                    
    return info
