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

    # key definitions
    # anat
    t1w = create_key('{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_T1w')
    flair  = create_key('{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_FLAIR')
    t2w = create_key('{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_T2w')
    
    # dwi. added _acq-mde as a key to identify this as a MDE scan
    dwi = create_key('{bids_subject_session_dir}/dwi/{bids_subject_session_prefix}_acq-mde_dir-AP_dwi')
    # Save the RPE (reverse phase-encode) B0 image as a fieldmap (fmap).
    fmap_rev_phase =  create_key('{bids_subject_session_dir}/fmap/{bids_subject_session_prefix}_dir-PA_epi')
    
    # MTS collection
    mt_off = create_key('{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_flip-1_mt-off_MTS')
    mt_on  = create_key('{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_flip-1_mt-on_MTS')
    mt_t1w  = create_key('{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_flip-2_mt-off_MTS')
    
    # Fill data dictionary
    info[t1w]=[]
    info[flair]=[]
    info[t2w]=[]
    info[dwi]=[]
    info[mt_off]=[]
    info[mt_on]=[]
    info[mt_t1w]=[]
    info[fmap_rev_phase]=[]

    # Criteria
    for idx, s in enumerate(seqinfo):
        # anat
        if ('T1w_MPR**' in s.series_description):
            info[t1w].append(s.series_id)
        if ('t2_space_dark-fluid_sag_p2_iso' in s.protocol_name):
            info[flair].append(s.series_id)
        if ('T2w_SPC' in s.protocol_name):
            info[t2w].append(s.series_id)

        #  dwi
        if ('UFA_AP' in s.protocol_name):
            info[dwi].append(s.series_id)
        if ('UFA_PA_B0' in s.protocol_name):
            info[fmap_rev_phase] = [s.series_id]

        # MTS collection. Only for magnitude Images
        # use == operator to disentangle shared gre3D_mtOFF string case
        if ('gre3D_mtOFF' == s.series_description) and ('M' in s.image_type[2].strip() ):
            info[mt_off] = [s.series_id]

        if ('gre3D_mtON' == s.series_description) and ('M' in s.image_type[2].strip() ):
            info[mt_on] = [s.series_id]
                
        if ('gre3D_mtOFF_TR12' == s.series_description) and ('M' in s.image_type[2].strip() ):
            info[mt_t1w] = [s.series_id]
                    
    return info
