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

    matrix = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-matrix_run-{item:02d}_bold')
    matrix_sbref = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-matrix_run-{item:02d}_sbref')

    endback = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-endback_run-{item:02d}_bold')
    endback_sbref = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-endback_run-{item:02d}_sbref')

    rest = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-rest_run-{item:02d}_bold')
    rest_sbref = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-rest_run-{item:02d}_sbref')

    fmap_sbref = create_key('{bids_subject_session_dir}/fmap/{bids_subject_session_prefix}_dir-{dir}_epi')

    dwi_pa = create_key('{bids_subject_session_dir}/dwi/{bids_subject_session_prefix}_dir-{dir}_run-{item:02}_dwi')

    t13d = create_key('{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_acq-MPRAGE_run-{item:02d}_T1w')

    

    info[matrix]=[]
    info[matrix_sbref]=[]
    info[endback]=[]
    info[endback_sbref]=[]
    info[rest]=[]
    info[rest_sbref]=[]
    info[fmap_sbref]=[]
    info[dwi_pa]=[]
    info[t13d]=[]

    for idx, s in enumerate(seqinfo):
       
        if ('matrix' in (s.series_description).strip()):
            if (s.dim4==1 and  'SBRef' in (s.series_description).strip()):
                    info[matrix_sbref].append({'item': s.series_id})
            elif (s.dim4>100):
                    info[matrix].append({'item': s.series_id})
                    
        elif ('endback' in (s.series_description).strip()):
            if (s.dim4==1 and  'SBRef' in (s.series_description).strip()):
                    info[endback_sbref].append({'item': s.series_id})
            elif (s.dim4>100):
                    info[endback].append({'item': s.series_id})            
        
        elif ('rest' in (s.series_description).strip()):
            if (s.dim4==1 and 'SBRef' in (s.series_description).strip()):
                    info[rest_sbref].append({'item': s.series_id})
            elif (s.dim4>100):
                    info[rest].append({'item': s.series_id})
        
        elif ('ep_bold_mb6_PA' in (s.series_description).strip()):
            if (s.dim4==1):
                #if 'SBRef' in (s.series_description).strip():
                info[fmap_sbref].append({'item': s.series_id,'dir': 'PA'})

        elif ('diff_mb3_b0_PA' in (s.series_description).strip()):
            if (s.dim4==1):
                #if 'SBRef' in (s.series_description).strip():
                info[dwi_pa].append({'item': s.series_id,'dir': 'PA'})

        elif ('T1_3D' in (s.series_description).strip()):
            info[t13d].append({'item': s.series_id})        


    return info

