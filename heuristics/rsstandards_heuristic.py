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

    #fmap = create_key('{bids_subject_session_dir}/fmap/{bids_subject_session_prefix}_dir-{dir}_epi')
    fmap_sbref = create_key('{bids_subject_session_dir}/fmap/{bids_subject_session_prefix}_dir-{dir}_epi')

    

    info[rest]=[]
    info[rest_sbref]=[]
    info[movie]=[]
    info[movie_sbref]=[]
    #info[fmap]=[]
    info[fmap_sbref]=[]

    for idx, s in enumerate(seqinfo):
       
        if ('Hitchcock' in (s.series_description).strip()):
            if (s.dim4==1 and  'SBRef' in (s.series_description).strip()):
                    info[movie_sbref].append({'item': s.series_id})
            elif (s.dim4==480):
                    info[movie].append({'item': s.series_id})
                    
        elif ('chaplain' in (s.series_description).strip()):
            if (s.dim4==1 and  'SBRef' in (s.series_description).strip()):
                    info[movie_sbref].append({'item': s.series_id})
            elif (s.dim4==215):
                    info[movie].append({'item': s.series_id})            
        
        elif ('bold' in (s.series_description).strip()):
            if ('rs' in (s.series_description).strip()):
                if (s.dim4==1 and  'SBRef' in (s.series_description).strip()):
                    info[rest_sbref].append({'item': s.series_id})
                elif (s.dim4>350):
                    info[rest].append({'item': s.series_id})
                    
            if ('PA' in (s.series_description).strip()):
                if (s.dim4==1):
                    if 'SBRef' in (s.series_description).strip():
                        info[fmap_sbref].append({'item': s.series_id,'dir': 'PA'})
 #                   else:
 #                       info[fmap].append({'item': s.series_id,'dir': 'PA'})

            if ('AP' in (s.series_description).strip()):
                if (s.dim4==1):
                    if 'SBRef' in (s.series_description).strip():
                        info[fmap_sbref].append({'item': s.series_id,'dir': 'AP'})
 #                   else:
 #                       info[fmap].append({'item': s.series_id,'dir': 'AP'})


    return info