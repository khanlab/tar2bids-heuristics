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
    #info = cfmminfodict(seqinfo)

    task1 = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-task1_run-{item:02d}_bold')
    task2 = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-task2_run-{item:02d}_bold')
    task3 = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-task3_run-{item:02d}_bold')

    rest = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-rest_run-{item:02d}_bold')

    dwi_ap = create_key('{bids_subject_session_dir}/dwi/{bids_subject_session_prefix}_dir_{dir}_run-{item:02}_dwi')
    dwi_pa = create_key('{bids_subject_session_dir}/dwi/{bids_subject_session_prefix}_dir-{dir}_run-{item:02}_dwi')

    t13d = create_key('{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_acq-MPRAGE_run-{item:02d}_T1w')

    fmap_diff = create_key('{bids_subject_session_dir}/fmap/{bids_subject_session_prefix}_phasediff')
    fmap_magnitude = create_key('{bids_subject_session_dir}/fmap/{bids_subject_session_prefix}_magnitude')

    info = {task1:[], task2:[], task3:[], rest:[], dwi_ap:[], dwi_pa:[], t13d:[], fmap_diff:[], fmap_magnitude:[]}

    for idx, s in enumerate(seqinfo):
       
        if ('task1' in (s.series_description).strip()):
            if (s.dim4>100):
                info[task1].append({'item': s.series_id})

        elif ('task2' in (s.series_description).strip()):
            if (s.dim4>100):
                info[task2].append({'item': s.series_id})

        elif ('task3' in (s.series_description).strip()):
            if (s.dim4>90):
                info[task3].append({'item': s.series_id})
        
        elif ('restingState' in (s.series_description).strip()):
            if (s.dim4>100):
                info[rest].append({'item': s.series_id})

        elif ('PA' in (s.series_description).strip()):
            if ('diff' in (s.series_description).strip()):
                info[dwi_pa].append({'item': s.series_id, 'dir': 'PA'}) 

        elif ('ep2d_diff_mb2_p2_64dirs' in (s.series_description).strip()):
            if (s.dim4==68):
                info[dwi_ap].append({'item': s.series_id, 'dir': 'AP'})

        elif ('MPRAGE' in (s.series_description).strip()):
            info[t13d].append({'item': s.series_id}) 

        elif ('field_mapping' in s.protocol_name):   
            if (s.dim4 == 1) and ('gre_field_mapping' == (s.series_description).strip()):
                if('P' in (s.image_type[2].strip()) ):
                    info[fmap_diff].append({'item': s.series_id})
                if('M' in (s.image_type[2].strip()) ):
                    info[fmap_magnitude].append({'item': s.series_id})       

    return info


