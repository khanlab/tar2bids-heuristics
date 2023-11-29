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

    task = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-rest_run-{item:02d}_bold')
    task_sbref = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-rest_run-{item:02d}_sbref')

    fmap_sbref = create_key('{bids_subject_session_dir}/fmap/{bids_subject_session_prefix}_acq-EPI_dir-{dir}_epi')

    dwi_ap = create_key('{bids_subject_session_dir}/dwi/{bids_subject_session_prefix}_run-{item:02}_dwi')
    dwi_pa = create_key('{bids_subject_session_dir}/fmap/{bids_subject_session_prefix}_acq-DWI_dir-{dir}_epi')

    t13d = create_key('{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_acq-MPRAGE_run-{item:02d}_T1w')

    fmap_diff = create_key('{bids_subject_session_dir}/fmap/{bids_subject_session_prefix}_phasediff')
    fmap_magnitude = create_key('{bids_subject_session_dir}/fmap/{bids_subject_session_prefix}_magnitude')

    info = {task:[], task_sbref:[], fmap_sbref:[], dwi_ap:[], dwi_pa:[], t13d:[], fmap_diff:[], fmap_magnitude:[]}

    for idx, s in enumerate(seqinfo):
       
        if ('resting_state' in (s.series_description).strip()):
            if (s.dim4==1 and  'SBRef' in (s.series_description).strip()):
                    info[task_sbref].append({'item': s.series_id})
            elif (s.dim4>10):
                    info[task].append({'item': s.series_id})
        
        elif ('PE180' in (s.series_description).strip()):
            #if ('bold' in (s.series_description).strip()):
            #    info[fmap_sbref].append({'item': s.series_id,'dir': 'PA'})
            if ('ORIG' in (s.series_description).strip()):
                info[dwi_pa].append({'item': s.series_id, 'dir': 'PA'}) 

        elif (('DIFFUSION' in s.image_type[2].strip()) and ('ORIGINAL' in s.image_type[0].strip())):
            if ('ORIG' in (s.series_description).strip()):
                info[dwi_ap].append({'item': s.series_id})

        elif ('MPRAGE' in (s.series_description).strip()):
            if ('ND' in (s.image_type[3].strip())):
                info[t13d].append({'item': s.series_id}) 

        elif ('field_mapping' in s.protocol_name):   
            if (s.dim4 == 1) and ('gre_field_mapping' == (s.series_description).strip()):
                if('P' in (s.image_type[2].strip()) ):
                    info[fmap_diff].append({'item': s.series_id})
                if('M' in (s.image_type[2].strip()) ):
                    info[fmap_magnitude].append({'item': s.series_id})       

    return info


