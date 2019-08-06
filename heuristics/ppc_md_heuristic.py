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

    task_localizer = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-localizer_run-{item:02d}_bold')
    task_lifetime = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-lifetime_run-{item:02d}_bold')
    task_localizerReverse = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-localizerReverse_run-{item:02d}_bold')
    task_localizerTE25 = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-localizerTE25_run-{item:02d}_bold')
    task_study = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-study_run-{item:02d}_bold')
    task_keyprac = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-keyprac_run-{item:02d}_bold')

    info[task_localizer]=[]
    info[task_lifetime]=[]
    info[task_localizerReverse]=[]
    info[task_localizerTE25]=[]
    info[task_study] = []
    info[task_keyprac] = []

    for idx, s in enumerate(seqinfo):

        if ('lifetime' in (s.series_description).strip() and s.dim4>150):
            info[task_lifetime].append({'item': s.series_id})

        elif ('PRC_localizer' in (s.series_description).strip() and 'reverse' not in (s.series_description).strip() and 'TE25' not in (s.series_description).strip()):
            info[task_localizer].append({'item': s.series_id})

        elif ('PRC_localizer' in (s.series_description).strip() and 'reverse' in (s.series_description).strip()):
            info[task_localizerReverse].append({'item': s.series_id})

        elif ('PRC_localizer' in (s.series_description).strip() and 'TE25' in (s.series_description).strip()):
            info[task_localizerTE25].append({'item': s.series_id})
        
        elif ('study' in (s.series_description).strip() and s.dim4>150):
            info[task_study].append({'item': s.series_id})
            
        elif ('keyprac' in (s.series_description).strip() and s.dim4>150):
            info[task_keyprac].append({'item': s.series_id})
        
                   
    return info