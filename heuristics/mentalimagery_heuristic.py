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

    perception = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-perception_run-{item:02d}_bold')
    perception_sbref = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-perception_run-{item:02d}_sbref')

    localizer = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-localizer_run-{item:02d}_bold')
    localizer_sbref = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-localizer_run-{item:02d}_sbref')

    visual = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-visualimagery_run-{item:02d}_bold')
    visual_sbref = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-visualimagery_run-{item:02d}_sbref')

    auditory = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-auditoryimagery_run-{item:02d}_bold')
    auditory_sbref = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-auditoryimagery_run-{item:02d}_sbref')

    fmap_sbref = create_key('{bids_subject_session_dir}/fmap/{bids_subject_session_prefix}_dir-{dir}_epi')

    t13d = create_key('{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_acq-MPRAGE_run-{item:02d}_T1w')

    

    info[perception]=[]
    info[perception_sbref]=[]
    info[localizer]=[]
    info[localizer_sbref]=[]
    info[visual]=[]
    info[visual_sbref]=[]
    info[auditory]=[]
    info[auditory_sbref]=[]
    info[fmap_sbref]=[]
    info[t13d]=[]

    for idx, s in enumerate(seqinfo):
       
        if ('Perception' in (s.series_description).strip()):
            if (s.dim4==1 and  'SBRef' in (s.series_description).strip()):
                    info[perception_sbref].append({'item': s.series_id})
            elif (s.dim4>300):
                    info[perception].append({'item': s.series_id})
                    
        elif ('Loc' in (s.series_description).strip()):
            if (s.dim4==1 and  'SBRef' in (s.series_description).strip()):
                    info[localizer_sbref].append({'item': s.series_id})
            elif (s.dim4>300):
                    info[localizer].append({'item': s.series_id})            
        
        elif ('VisualImagery' in (s.series_description).strip()):
            if (s.dim4==1 and 'SBRef' in (s.series_description).strip()):
                    info[visual_sbref].append({'item': s.series_id})
            elif (s.dim4>199):
                    info[visual].append({'item': s.series_id})

        elif ('AuditoryImagery' in (s.series_description).strip()):
            if (s.dim4==1 and 'SBRef' in (s.series_description).strip()):
                    info[auditory_sbref].append({'item': s.series_id})
            elif (s.dim4>75):
                    info[auditory].append({'item': s.series_id})
        
        elif ('Topup' in (s.series_description).strip()):
            if (s.dim4==1):
                #if 'SBRef' in (s.series_description).strip():
                info[fmap_sbref].append({'item': s.series_id,'dir': 'PA'})

        elif ('T1_3D' in (s.series_description).strip()):
            info[t13d].append({'item': s.series_id})        


    return info
