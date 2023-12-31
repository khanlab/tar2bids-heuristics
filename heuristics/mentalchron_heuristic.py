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

    task = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-vma_run-{item:02d}_bold')
    task_sbref = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-vma_run-{item:02d}_sbref')
    
    gre_diff = create_key('{bids_subject_session_dir}/fmap/{bids_subject_session_prefix}_run-{item:02d}_phasediff')
    gre_magnitude = create_key('{bids_subject_session_dir}/fmap/{bids_subject_session_prefix}_run-{item:02d}_magnitude')
    
    fmap_diff = create_key('{bids_subject_session_dir}/fmap/{bids_subject_session_prefix}_phasediff')
    fmap_magnitude = create_key('{bids_subject_session_dir}/fmap/{bids_subject_session_prefix}_magnitude')
    del info[fmap_diff]
    del info[fmap_magnitude]

    info[task]=[]
    info[task_sbref]=[]
    info[gre_diff]=[]
    info[gre_magnitude]=[]

    for idx, s in enumerate(seqinfo):
       
        if ('bold' in (s.series_description).strip()):
            if (s.dim4==1 and 'SBRef' in (s.series_description).strip()):
                info[task_sbref].append({'item': s.series_id})
            elif (s.dim4==3000):
                info[task].append({'item': s.series_id})
                
        if ('field_mapping' in s.protocol_name):   
            if (s.dim4==1 and 'gre_field_mapping' in (s.series_description).strip()):
                if('P' in (s.image_type[2].strip()) ):
                    info[gre_diff].append({'item': s.series_id})
                if('M' in (s.image_type[2].strip()) ):
                    info[gre_magnitude].append({'item': s.series_id})
                    
    return info
