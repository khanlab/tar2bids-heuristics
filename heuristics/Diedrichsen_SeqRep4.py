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

    taskname='sequenceproduction'
    taskvols=340


    task = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-{task}_run-{item:02d}_bold')
    task_sbref = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-{task}_run-{item:02d}_sbref')

    task_psf = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-{task}_acq-psf_run-{item:02d}_bold')
    task_psf_dico = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-{task}_acq-psf_rec-dico_run-{item:02d}_bold')


    discarded = create_key('sourcedata/discarded_bold/{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-{task}_run-{item:02d}_bold')
    discarded_psf = create_key('sourcedata/discarded_bold/{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-{task}_acq-psf_run-{item:02d}_bold')
    discarded_psf_dico = create_key('sourcedata/discarded_bold/{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-{task}_acq-psf_rec-dico_run-{item:02d}_bold')



    info[task]=[]
    info[task_sbref]=[]
    info[task_psf]=[]
    info[task_psf_dico]=[]
    info[discarded]=[]
    info[discarded_psf]=[]
    info[discarded_psf_dico]=[]

    for idx, s in enumerate(seqinfo):
       
        if ('bold' in s.protocol_name or 'tasking_state' in s.series_description or 'mbep2d' in (s.series_description).strip() or 'ep_bold' in (s.series_description).strip() and not ('diff' in s.protocol_name or 'DWI' in s.series_description )):
            
            if ('SBRef' in (s.series_description).strip()):
                print('skipping sbref')



            elif (s.dim4 < taskvols):
                    if ('mi_ep2d' in (s.series_description).strip() ):
                        if ('DICO'  in (s.image_type[4].strip())):
                            info[discarded_psf_dico].append({'item': s.series_id,'task': taskname})
                        else:
                            info[discarded_psf].append({'item': s.series_id,'task': taskname})
                    else:
                        info[discarded].append({'item': s.series_id,'task': taskname})

            elif (s.dim4 == taskvols): 
                if ('mi_ep2d' in (s.series_description).strip() ):
                    if ('DICO'  in (s.image_type[4].strip())):
                        info[task_psf_dico].append({'item': s.series_id,'task': taskname})
                    else:
                        info[task_psf].append({'item': s.series_id,'task': taskname})
                else:
                    info[task].append({'item': s.series_id,'task': taskname})
 
                  
    return info
