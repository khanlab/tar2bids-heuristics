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

    info[task_localizer]=[]
    info[task_lifetime]=[]
    info[task_localizerreverse]=[]
    info[task_localizerTE25]=[]

    for idx, s in enumerate(seqinfo):

        if ('bold' in (s.sequence_name).strip() or 'epfid' in (s.sequence_name).strip() or 'mbep2d' in (s.series_name).strip() or 'ep_bold' in (s.sequence_name).strip() and not ('diff' in s.protocol_name or 'DWI' in s.series_description)):
            
            if ('lifetime' in (s.series_description).strip() and s.dim4>150):
                info[task_lifetime].append({'item': s.series_id})

            elif ('PRC_localizer' in (s.series_description).strip().lower() and 'reverse' not in (s.series_description).strip().lower() and 'TE25' not in (s.series_description).strip().lower()):
                info[task_localizer].append({'item': s.series_id})

            elif ('PRC_localizer' in (s.series_description).strip().lower() and 'reverse' in (s.series_description).strip().lower()):
                info[info_localizerreverse].append({'item': s.series_id})

            elif ('PRC_localizer' in (s.series_description).strip().lower() and 'TE25' in (s.series_description).strip().lower()):
                info[task_localizerTE25].append({'item': s.series_id})
                   
    return info