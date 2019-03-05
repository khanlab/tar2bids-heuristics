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

    visual = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-visual_run-{item:02d}_bold')
    visual_sbref = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-visual_run-{item:02d}_sbref')

    somat = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-somat_run-{item:02d}_bold')
    somat_sbref = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-somat_run-{item:02d}_sbref')

    info[rest]=[]
    info[rest_sbref]=[]
    info[visual]=[]
    info[visual_sbref]=[]
    info[somat]=[]
    info[somat_sbref]=[]

    for idx, s in enumerate(seqinfo):
       
        if ('Visual' in (s.series_description).strip()):
            if (s.dim4==1 and  'SBRef' in (s.series_description).strip()):
                    info[movie_sbref].append({'item': s.series_id})
            elif (s.dim4>1):
                    info[movie].append({'item': s.series_id})
                    
        elif ('Somat' in (s.series_description).strip()):
            if (s.dim4==1 and  'SBRef' in (s.series_description).strip()):
                    info[movie_sbref].append({'item': s.series_id})
            elif (s.dim4>1):
                    info[movie].append({'item': s.series_id})            
        
        elif ('rs' in (s.series_description).strip()):
            if (s.dim4==1 and  'SBRef' in (s.series_description).strip()):
                info[rest_sbref].append({'item': s.series_id})
            elif (s.dim4>1):
                info[rest].append({'item': s.series_id})
                    
    return info