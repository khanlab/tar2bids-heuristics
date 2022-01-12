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
    humour = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-humour_run-{item:02d}_bold')
    seinfelde1 = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-seinfeldE1_run-{item:02d}_bold')
    seinfelde2 = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-seinfeldE2_run-{item:02d}_bold')
    hitchcock = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-hitchcock_run-{item:02d}_bold')
    rest = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-rest_run-{item:02d}_bold')
    chaplin = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-chaplin_run-{item:02d}_bold')

    # ASPIRE
    aspire_mag_echo_GRE = create_key('{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_acq-ASPIRE_part-mag_echo_GRE')
    aspire_phase_echo_GRE = create_key('{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_acq-ASPIRE_part-phase_echo_GRE')
    aspire_T2_star_GRE = create_key('{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_acq-ASPIRE_T2star')
    aspire_R2_star_GRE = create_key('{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_acq-ASPIRE_R2star')

    # T1w and T2w
    t1w = create_key('{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_acq-MPRvNav4eRMS_run-{item}_T1w')
    t1w_me = create_key('{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_acq-MPRvNav4e_run-{item}_echo_MEMPRAGE')
    t1w_norm = create_key('{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_acq-MPRvNavNorm4eRMS_run-{item}_T1w')
    t1w_me_norm = create_key('{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_acq-MPRvNavNorm4e_run-{item}_echo_MEMPRAGE')
    t1w_vnavs = create_key('{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_acq-MPRvNav_run-{item}_vNav')

    t2w = create_key('{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_acq-SPCvNavRMS_run-{item}_T2w')
    t2w_norm = create_key('{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_acq-SPCvNavNormRMS_run-{item}_T2w')
    t2w_vnavs = create_key('{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_acq-SPCvNav_run-{item}_vNav')

    t1w_basic = create_key('{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_acq-MPRAGE_run-{item}_T1w')
    t2w_basic = create_key('{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_acq-SPACE_run-{item}_T2w')

    #Diffusion
    dwi = create_key('{bids_subject_session_dir}/dwi/{bids_subject_session_prefix}_run-{item:02d}_dwi')

    #GRE phase diff 
    fmap_diff = create_key('{bids_subject_session_dir}/fmap/{bids_subject_session_prefix}_phasediff')
    fmap_magnitude = create_key('{bids_subject_session_dir}/fmap/{bids_subject_session_prefix}_magnitude')

    info = {humour:[],seinfelde1:[],seinfelde2:[],hitchcock:[],rest:[],chaplin:[],
        aspire_mag_echo_GRE:[],aspire_phase_echo_GRE:[],aspire_T2_star_GRE:[],
        aspire_R2_star_GRE:[],t1w_me:[],t1w_me_norm:[],t1w_vnavs:[],t1w:[],
        t1w_norm:[],t2w_vnavs:[],t2w:[],t2w_norm:[],t1w_basic:[],t2w_basic:[],
        dwi:[],fmap_diff:[],fmap_magnitude:[]}

    for idx, s in enumerate(seqinfo):

        # ASPIRE 3T images
        if ('ASPIRE' in (s.series_description).strip()):
            if ('R2star' in (s.series_description).strip()):
                info[aspire_R2_star_GRE].append({'item': s.series_id})
            elif ('TSstar' in (s.series_description).strip()):
                info[aspire_T2_star_GRE].append({'item': s.series_id})
            elif len(s.image_type) > 3:
                if (('M' in (s.image_type[2].strip())) and ('ASPIRE' not in s.image_type)):
                    info[aspire_mag_echo_GRE].append({'item': s.series_id})
                if ('P' in (s.image_type[2].strip()) and len(s.image_type) > 4):
                    info[aspire_phase_echo_GRE].append({'item': s.series_id}) 

        # T1w images
        if ('T1w_MPR' in (s.series_description).strip()):
            if ('vNav' in (s.series_description).strip()):
                if ('setter' in (s.series_description).strip()):
                    if ('MOSAIC' in s.image_type):
                        info[t1w_vnavs].append({'item': s.series_id})
                else:
                    if ('OTHER' in (s.image_type).strip()): 
                        if ('NORM' in s.image_type):
                            print('skipping pre-scan norm RMS combined T1w')
                            #info[t1w_norm].append({'item': s.series_id})
                        else:
                            print('skipping no pre-scan norm RMS combined T1w')
                            #info[t1w].append({'item': s.series_id})
                    if ('M' in (s.image_type).strip()): 
                        if ('NORM' in s.image_type):
                            print('skipping pre-scan norm separated echo T1w')
                            #info[t1w_me_norm].append({'item': s.series_id})
                        else:
                            info[t1w_me].append({'item': s.series_id})
                        
            else:
                info[t1w_basic].append({'item': s.series_id})


        #T2w images
        if ('T2w_SPC_vNav_setter' in s.series_description):
            if ('MOSAIC' in s.image_type):
                info[t2w_vnavs].append({'item': s.series_id})
        elif ('T2w_SPC_800iso_vNav' in s.series_description):
            if ('NORM' in s.image_type):
                print('skipping pre-scan norm T2w')
#                info[t2w_norm].append({'item': s.series_id}) 
            else:
                info[t2w].append({'item': s.series_id}) 
        elif ('T2w_SPC' in s.series_description):
            info[t2w_basic].append({'item': s.series_id}) 

        #dwi
        if len(s.image_type) > 2 :
            if (('DIFFUSION' in s.image_type[2].strip()) and ('ORIGINAL' in s.image_type[0].strip())):
                if ('cb_ep2d_diff_C26' in s.series_description):
                    info[dwi_ogse].append({'item': s.series_id})
                elif ('UFA' in s.series_description ):
                    info[dwi_ufa].append({'item': s.series_id})
                else:
                    info[dwi].append({'item': s.series_id})

        #gre field map   
        if ('field_mapping' in s.protocol_name):   
            if (s.dim4 == 1) and ('gre_field_mapping' == (s.series_description).strip()):
                if('P' in (s.image_type[2].strip()) ):
                    info[fmap_diff].append({'item': s.series_id})
                if('M' in (s.image_type[2].strip()) ):
                    info[fmap_magnitude].append({'item': s.series_id})          

        if ('Humour' in (s.series_description).strip()):
            info[humour].append({'item': s.series_id})
                    
        if ('SeinfeldE1' in (s.series_description).strip()):
            info[seinfelde1].append({'item': s.series_id})

        if ('SeinfeldE2' in (s.series_description).strip()):
            info[seinfelde2].append({'item': s.series_id})    

        if ('Hitchcock' in (s.series_description).strip()):
            info[hitchcock].append({'item': s.series_id}) 

        if ('rs' in (s.series_description).strip()):
            info[rest].append({'item': s.series_id})  

        if ('Chaplain' in (s.series_description).strip()):
            info[chaplin].append({'item': s.series_id})      

    return info
