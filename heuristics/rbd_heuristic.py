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

    movie = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-movie_run-{item:02d}_bold')
    movie_sbref = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-movie_run-{item:02d}_sbref')

    green = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-green_run-{item:02d}_bold')
    green_sbref = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-green_run-{item:02d}_sbref')

    mag_echo_GRE = create_key('{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_acq-svd_part-mag_echo_GRE')
    phase_echo_GRE = create_key('{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_acq-svd_part-phase_echo_GRE')

    
    info[rest]=[]
    info[rest_sbref]=[]
    info[movie]=[]
    info[movie_sbref]=[]
    info[green]=[]
    info[green_sbref]=[]
    info[mag_echo_GRE]=[]
    info[phase_echo_GRE]=[]
    

    for idx, s in enumerate(seqinfo):
       
        if ('Hitchcock' in (s.series_description).strip()):
            if (s.dim4==1 and  'SBRef' in (s.series_description).strip()):
                    info[movie_sbref].append({'item': s.series_id})
            elif (s.dim4==246):
                    info[movie].append({'item': s.series_id})
                    
        elif ('chaplain' in (s.series_description).strip()):
            if (s.dim4==1 and  'SBRef' in (s.series_description).strip()):
                    info[movie_sbref].append({'item': s.series_id})
            elif (s.dim4==215):
                    info[movie].append({'item': s.series_id})            

        elif ('greengame' in (s.series_description).strip()):
            if (s.dim4==1 and 'SBRef' in (s.series_description).strip()):
                    info[green_sbref].append({'item': s.series_id})
            elif (s.dim4>75):
                    info[green].append({'item': s.series_id})
        
        elif ('restingstate' in (s.series_description).strip()):
            if (s.dim4==1 and  'SBRef' in (s.series_description).strip()):
                info[rest_sbref].append({'item': s.series_id})
            elif (s.dim4==340):
                info[rest].append({'item': s.series_id})
                
        elif ('gre_svd' in s.series_description and 't1_fl3d_p4_iso' in s.series_description ):
            if ('M' in (s.image_type[2].strip())):
                if ('ND' in (s.image_type[3].strip())):
                    info[mag_echo_GRE] =  [s.series_id]
        
            if ('P' in (s.image_type[2].strip())):
            	if ('ND' in (s.image_type[3].strip())):
                    info[phase_echo_GRE] =  [s.series_id]
                    


    return info