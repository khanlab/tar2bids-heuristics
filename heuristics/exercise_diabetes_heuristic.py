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

    # BOLD
    rest = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-rest_run-{item:02d}_bold')
    rest_sbref = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-rest_run-{item:02d}_sbref')
    rest_pa_sbref = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-rest_run-{item:02d}_dir-{dir}_sbref')
    

    # ASPIRE
    #aspire_mag_echo_GRE = create_key('{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_acq-ASPIRE_part-mag_echo_GRE')
    #aspire_phase_echo_GRE = create_key('{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_acq-ASPIRE_part-phase_echo_GRE')
    #aspire_T2_star_GRE = create_key('{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_acq-ASPIRE_T2star')
    #aspire_R2_star_GRE = create_key('{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_acq-ASPIRE_R2star')

    # T1w and T2w
    t1w = create_key('{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_acq-tfl3dRMS_run-{item}_T1w')
    t1w_me = create_key('{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_acq-tfl3d_run-{item}_echo_MEMPRAGE')
    t1w_norm = create_key('{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_acq-tfl3dRMS_run-{item}_T1w')
    t1w_me_norm = create_key('{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_acq-tfl3d_run-{item}_echo_MEMPRAGE')
    t1w_vnavs = create_key('{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_acq-ABCD3d1_run-{item}_vNav')

    t2w = create_key('{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_acq-SPCvNavRMS_run-{item}_T2w')
    t2w_norm = create_key('{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_acq-SPCvNavNormRMS_run-{item}_T2w')
    t2w_vnavs = create_key('{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_acq-ABCD3d1_run-{item}_vNav')

    #t1w_basic = create_key('{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_acq-MPRAGE_run-{item}_T1w')
    #t2w_basic = create_key('{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_acq-SPACE_run-{item}_T2w')

    #Diffusion
    dwi = create_key('{bids_subject_session_dir}/dwi/{bids_subject_session_prefix}_run-{item:02d}_dir-{dir}_dwi')
    dwi_pa = create_key('{bids_subject_session_dir}/dwi/{bids_subject_session_prefix}_run-{item:02d}_dir-{dir}_dwi')

    #GRE phase diff 
    fmap_diff = create_key('{bids_subject_session_dir}/fmap/{bids_subject_session_prefix}_phasediff')
    fmap_magnitude = create_key('{bids_subject_session_dir}/fmap/{bids_subject_session_prefix}_magnitude')
    rest_pa = create_key('{bids_subject_session_dir}/fmap/{bids_subject_session_prefix}_acq-EPI_dir-{dir}_epi')

    info = {rest:[],rest_sbref:[],rest_pa_sbref:[],rest_pa:[],
        t1w_me:[],t1w_me_norm:[],t1w_vnavs:[],t1w:[],
        t1w_norm:[],t2w_vnavs:[],t2w:[],t2w_norm:[],
        dwi:[],dwi_pa:[],fmap_diff:[],fmap_magnitude:[]}

    for idx, s in enumerate(seqinfo):

        # ASPIRE 3T images
        #if ('ASPIRE' in (s.series_description).strip()):
        #    if ('R2star' in (s.series_description).strip()):
        #        info[aspire_R2_star_GRE].append({'item': s.series_id})
        #    elif ('TSstar' in (s.series_description).strip()):
        #        info[aspire_T2_star_GRE].append({'item': s.series_id})
        #    elif len(s.image_type) > 3:
        #        if (('M' in (s.image_type[2].strip())) and ('ASPIRE' not in s.image_type)):
        #            info[aspire_mag_echo_GRE].append({'item': s.series_id})
        #        if ('P' in (s.image_type[2].strip()) and len(s.image_type) > 4):
        #            info[aspire_phase_echo_GRE].append({'item': s.series_id}) 

        # T1w images
        if ('T1w' in (s.series_description).strip()):
            if ('vNav' in (s.series_description).strip()):
                if ('setter' in (s.series_description).strip()):
                    if ('MOSAIC' in s.image_type):
                        info[t1w_vnavs].append({'item': s.series_id})
                else:
                    if ('OTHER' in s.image_type): 
                        if ('NORM' in s.image_type):
                            print('skipping pre-scan norm RMS combined T1w')
                            #info[t1w_norm].append({'item': s.series_id})
                        else:
                            print('skipping no pre-scan norm RMS combined T1w')
                            #info[t1w].append({'item': s.series_id})
                    if ('M' in s.image_type): 
                        if ('NORM' in s.image_type):
                            print('skipping pre-scan norm separated echo T1w')
                            #info[t1w_me_norm].append({'item': s.series_id})
                        else:
                            info[t1w_me].append({'item': s.series_id})
                        
            else:
                info[t1w_basic].append({'item': s.series_id})


        #T2w images
        if ('T2w_vNav_setter' in s.series_description):
            if ('MOSAIC' in s.image_type):
                info[t2w_vnavs].append({'item': s.series_id})
        elif ('T2w_space_800iso_vNav' in s.series_description):
            if ('NORM' in s.image_type):
                print('skipping pre-scan norm T2w')
#                info[t2w_norm].append({'item': s.series_id}) 
            else:
                info[t2w].append({'item': s.series_id}) 
        #elif ('T2w' in s.series_description):
        #    info[t2w_basic].append({'item': s.series_id}) 

        #dwi
        if ('diff_mb2_95dir_b2000' in s.series_description):
            if (s.dim4 == 96):
                info[dwi].append({'item': s.series_id,'dir': 'AP'})
            elif (s.dim4 == 7):
                info[dwi_pa].append({'item': s.series_id,'dir': 'PA'})

        #gre field map   
        if ('field_mapping' in s.protocol_name):   
            if (s.dim4 == 1) and ('gre_field_mapping' == (s.series_description).strip()):
                if('P' in (s.image_type[2].strip()) ):
                    info[fmap_diff].append({'item': s.series_id})
                if('M' in (s.image_type[2].strip()) ):
                    info[fmap_magnitude].append({'item': s.series_id})          

        #bold
        if ('REST_AP' in (s.series_description).strip()):
            if (s.dim4 == 1):
                info[rest_sbref].append({'item': s.series_id})
            elif (s.dim4 == 780):
                info[rest].append({'item': s.series_id})
                    
        if ('REST_PA' in (s.series_description).strip()):
            if ('SBRef' in (s.series_description).strip()):
                info[rest_pa_sbref].append({'item': s.series_id,'dir': 'PA'})
            else:
                info[rest_pa].append({'item': s.series_id,'dir': 'PA'}) 

    return info

