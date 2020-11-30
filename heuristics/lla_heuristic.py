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

    activeRtKnee = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-activeRtKnee_run-{item:02d}_bold')
    activeRtKnee_sbref = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-activeRtKnee_run-{item:02d}_sbref')
    activeRtKnee_phase = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-activeRtKnee_run-{item:02d}_phase')

    activeLtKnee = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-activeLtKnee_run-{item:02d}_bold')
    activeLtKnee_sbref = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-activeLtKnee_run-{item:02d}_sbref')
    activeLtKnee_phase = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-activeLtKnee_run-{item:02d}_phase')

    imaginedRtKnee = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-imaginedRtKnee_run-{item:02d}_bold')
    imaginedRtKnee_sbref = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-imaginedRtKnee_run-{item:02d}_sbref')
    imaginedRtKnee_phase = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-imaginedRtKnee_run-{item:02d}_phase')
    
    imaginedLtKnee = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-imaginedLtKnee_run-{item:02d}_bold')
    imaginedLtKnee_sbref = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-imaginedLtKnee_run-{item:02d}_sbref')
    imaginedLtKnee_phase = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-imaginedLtKnee_run-{item:02d}_phase')
    
    imaginedWalk = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-imaginedWalk_run-{item:02d}_bold')
    imaginedWalk_sbref = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-imaginedWalk_run-{item:02d}_sbref')
    imaginedWalk_phase = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-imaginedWalk_run-{item:02d}_phase')


    info[activeRtKnee]=[]
    info[activeRtKnee_sbref]=[]
    info[activeRtKnee_phase]=[]
    info[activeLtKnee]=[]
    info[activeLtKnee_sbref]=[]
    info[activeLtKnee_phase]=[]
    info[imaginedRtKnee]=[]
    info[imaginedRtKnee_sbref]=[]
    info[imaginedRtKnee_phase]=[]
    info[imaginedLtKnee]=[]
    info[imaginedLtKnee_sbref]=[]
    info[imaginedLtKnee_phase]=[]
    info[imaginedWalk]=[]
    info[imaginedWalk_sbref]=[]
    info[imaginedWalk_phase]=[]

    for idx, s in enumerate(seqinfo):
       
        if ('ActiveRtKnee' in (s.series_description).strip().lower()):
            if (s.dim4>300):
                    info[activeRtKnee].append({'item': s.series_id})
            elif (s.dim4==1 and 'S' in (s.series_description).strip().lower()):
                    info[activeRtKnee_sbref].append({'item': s.series_id})
            elif (s.dim4==1 and 'P' in (s.series_description).strip().lower()):
                    info[activeRtKnee_phase].append({'item': s.series_id})
                    
        elif ('ActiveLtKnee' in (s.series_description).strip().lower()):
            if (s.dim4>300):
                    info[activeLtKnee].append({'item': s.series_id}) 
            elif (s.dim4==1 and 'S' in (s.series_description).strip().lower()):
                    info[activeLtKnee_sbref].append({'item': s.series_id})
            elif (s.dim4==1 and 'P' in (s.series_description).strip().lower()):
                    info[activeLtKnee_phase].append({'item': s.series_id})

        elif ('ImaginedRtKnee' in (s.series_description).strip().lower()):
            if (s.dim4>300):
                    info[imaginedRtKnee].append({'item': s.series_id}) 
            elif (s.dim4==1 and 'S' in (s.series_description).strip().lower()):
                    info[imaginedRtKnee_sbref].append({'item': s.series_id})
            elif (s.dim4==1 and 'P' in (s.series_description).strip().lower()):
                    info[imaginedRtKnee_phase].append({'item': s.series_id})
             
        elif ('ImaginedLtKnee' in (s.series_description).strip().lower()):
            if (s.dim4>300):
                    info[imaginedLtKnee].append({'item': s.series_id}) 
            elif (s.dim4==1 and 'S' in (s.series_description).strip().lower()):
                    info[imaginedLtKnee_sbref].append({'item': s.series_id})
            elif (s.dim4==1 and 'P' in (s.series_description).strip().lower()):
                    info[imaginedLtKnee_phase].append({'item': s.series_id})    

        elif ('ImaginedWalk' in (s.series_description).strip().lower()):
            if (s.dim4>300):
                    info[imaginedWalk].append({'item': s.series_id}) 
            elif (s.dim4==1 and 'S' in (s.series_description).strip().lower()):
                    info[imaginedWalk_sbref].append({'item': s.series_id})
            elif (s.dim4==1 and 'P' in (s.series_description).strip().lower()):
                    info[imaginedWalk_phase].append({'item': s.series_id})           
                    
    return info
