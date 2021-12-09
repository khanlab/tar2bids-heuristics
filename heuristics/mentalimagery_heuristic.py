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

    #fmap = create_key('{bids_subject_session_dir}/fmap/{bids_subject_session_prefix}_dir-{dir}_epi')
    fmap_sbref = create_key('{bids_subject_session_dir}/fmap/{bids_subject_session_prefix}_dir-{dir}_epi')

    

    info[rest]=[]
    info[rest_sbref]=[]
    info[movie]=[]
    info[movie_sbref]=[]
    info[cuereactivity]=[]
    info[cuereactivity_sbref]=[]
    info[green]=[]
    info[green_sbref]=[]
    #info[fmap]=[]
    info[fmap_sbref]=[]

    for idx, s in enumerate(seqinfo):
       
        if ('perception' in (s.series_description).strip()):
            if (s.dim4==1 and  'SBRef' in (s.series_description).strip()):
                    info[movie_sbref].append({'item': s.series_id})
            elif (s.dim4==370):
                    info[movie].append({'item': s.series_id})
                    
        elif ('loc' in (s.series_description).strip()):
            if (s.dim4==1 and  'SBRef' in (s.series_description).strip()):
                    info[movie_sbref].append({'item': s.series_id})
            elif (s.dim4==434):
                    info[movie].append({'item': s.series_id})            
        
        elif ('visual' in (s.series_description).strip()):
            if (s.dim4==1 and 'SBRef' in (s.series_description).strip()):
                    info[cuereactivity_sbref].append({'item': s.series_id})
            elif (s.dim4>199):
                    info[cuereactivity].append({'item': s.series_id})

        elif ('auditory' in (s.series_description).strip()):
            if (s.dim4==1 and 'SBRef' in (s.series_description).strip()):
                    info[green_sbref].append({'item': s.series_id})
            elif (s.dim4>75):
                    info[green].append({'item': s.series_id})
        
        elif ('bold' in (s.series_description).strip()):
            if ('topup' in (s.series_description).strip()):
                if (s.dim4==1):
                    if 'SBRef' in (s.series_description).strip():
                        info[fmap_sbref].append({'item': s.series_id,'dir': 'PA'})
 #                   else:
 #                       info[fmap].append({'item': s.series_id,'dir': 'PA'})


    return info
