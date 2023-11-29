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

    prod = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-prod_run-{item:02d}_bold')
    prod_sbref = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-prod_run-{item:02d}_sbref')

    percep = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-percep_run-{item:02d}_bold')
    percep_sbref = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-percep_run-{item:02d}_sbref')

    ntfd = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-ntfd_run-{item:02d}_bold')
    ntfd_sbref = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-ntfd_run-{item:02d}_sbref')

    fmap_sbref = create_key('{bids_subject_session_dir}/fmap/{bids_subject_session_prefix}_acq-EPI_dir-{dir}_epi')

    se_pa = create_key('{bids_subject_session_dir}/fmap/{bids_subject_session_prefix}_acq-SE_dir-{dir}_epi')
    se_ap = create_key('{bids_subject_session_dir}/fmap/{bids_subject_session_prefix}_acq-SE_dir-{dir}_epi')


    info[prod]=[]
    info[prod_sbref]=[]
    info[percep]=[]
    info[percep_sbref]=[]
    info[ntfd]=[]
    info[ntfd_sbref]=[]
    info[fmap_sbref]=[]
    info[se_pa]=[]
    info[se_ap]=[]


    for idx, s in enumerate(seqinfo):
       
        if ('prod' in (s.series_description).strip()):
            if (s.dim4==1 and  'SBRef' in (s.series_description).strip()):
                    info[prod_sbref].append({'item': s.series_id})
            elif (s.dim4>10):
                    info[prod].append({'item': s.series_id})
                    
        elif ('percep' in (s.series_description).strip()):
            if (s.dim4==1 and  'SBRef' in (s.series_description).strip()):
                    info[percep_sbref].append({'item': s.series_id})
            elif (s.dim4>10):
                    info[percep].append({'item': s.series_id})            
        
        elif ('ntfd' in (s.series_description).strip()):
            if (s.dim4==1 and 'SBRef' in (s.series_description).strip()):
                    info[ntfd_sbref].append({'item': s.series_id})
            elif (s.dim4>10):
                    info[ntfd].append({'item': s.series_id})
        
        elif ('ep_bold_mb3_p2_AP' in (s.series_description).strip()):
            info[fmap_sbref].append({'item': s.series_id,'dir': 'AP'})    

        elif ('SpinEchoFieldMap_PA' in (s.series_description).strip()):
            if (s.dim4==1):
                #if 'SBRef' in (s.series_description).strip():
                info[se_pa].append({'item': s.series_id,'dir': 'PA'})

        elif ('SpinEchoFieldMap_AP' in (s.series_description).strip()):
            if (s.dim4==1):
                #if 'SBRef' in (s.series_description).strip():
                info[se_ap].append({'item': s.series_id,'dir': 'AP'})                


    return info

