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

    #pa = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-rest_dir-{dir}_run-{item:02d}_bold')
    #pa_sbref = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-rest_dir-{dir}_run-{item:02d}_sbref')

    

    info[rest]=[]
    info[rest_sbref]=[]
    #info[pa]=[]
    #info[pa_sbref]=[]

    for idx, s in enumerate(seqinfo):

        if ('rs' in (s.series_description).strip()):
            if (s.dim4==1):
                info[rest_sbref].append({'item'})
            else:
                info[rest].append({'item'})
       
    #    if ('bold' in (s.series_description).strip()):           
            #if ('PA' in (s.series_description).strip()):
            #    if 'SBRef' in (s.series_description).strip():
            #        info[pa_sbref].append({'item': s.series_id,'dir': 'PA'})
            #    else:
            #        info[pa].append({'item': s.series_id,'dir': 'PA'})

    #        if ('rs' in (s.series_description).strip()):
    #            if (s.dim4==1):
    #                if 'SBRef' in (s.series_description).strip():
    #                    info[rest_sbref].append({'item'})
    #                else:
    #                    info[rest].append({'item'})


    return info
