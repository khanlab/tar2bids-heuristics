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

    prod1 = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-prod1_run-{item:02d}_bold')
    prod1_sbref = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-prod1_run-{item:02d}_sbref')

    percep1 = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-percep1_run-{item:02d}_bold')
    percep1_sbref = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-percep1_run-{item:02d}_sbref')

    ntfd1 = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-ntfd1_run-{item:02d}_bold')
    ntfd1_sbref = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-ntfd1_run-{item:02d}_sbref')

    prod2 = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-prod2_run-{item:02d}_bold')
    prod2_sbref = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-prod2_run-{item:02d}_sbref')

    percep2 = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-percep2_run-{item:02d}_bold')
    percep2_sbref = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-percep2_run-{item:02d}_sbref')

    ntfd2 = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-ntfd2_run-{item:02d}_bold')
    ntfd2_sbref = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-ntfd2_run-{item:02d}_sbref')

    fmap_sbref = create_key('{bids_subject_session_dir}/fmap/{bids_subject_session_prefix}_acq-EPI_dir-{dir}_epi')

    se_pa = create_key('{bids_subject_session_dir}/fmap/{bids_subject_session_prefix}_acq-SE_dir-{dir}_epi')
    se_ap = create_key('{bids_subject_session_dir}/fmap/{bids_subject_session_prefix}_acq-SE_dir-{dir}_epi')


    info[prod1]=[]
    info[prod1_sbref]=[]
    info[percep1]=[]
    info[percep1_sbref]=[]
    info[ntfd1]=[]
    info[ntfd1_sbref]=[]
    info[prod2]=[]
    info[prod2_sbref]=[]
    info[percep2]=[]
    info[percep2_sbref]=[]
    info[ntfd2]=[]
    info[ntfd2_sbref]=[]
    info[fmap_sbref]=[]
    info[se_pa]=[]
    info[se_ap]=[]


    for idx, s in enumerate(seqinfo):
       
        if ('prod1' in (s.series_description).strip()):
            if (s.dim4==1 and  'SBRef' in (s.series_description).strip()):
                    info[prod1_sbref].append({'item': s.series_id})
            elif (s.dim4>10):
                    info[prod1].append({'item': s.series_id})
                    
        elif ('percep1' in (s.series_description).strip()):
            if (s.dim4==1 and  'SBRef' in (s.series_description).strip()):
                    info[percep1_sbref].append({'item': s.series_id})
            elif (s.dim4>10):
                    info[percep1].append({'item': s.series_id})            
        
        elif ('ntfd1' in (s.series_description).strip()):
            if (s.dim4==1 and 'SBRef' in (s.series_description).strip()):
                    info[ntfd1_sbref].append({'item': s.series_id})
            elif (s.dim4>10):
                    info[ntfd1].append({'item': s.series_id})

        elif ('prod2' in (s.series_description).strip()):
            if (s.dim4==1 and  'SBRef' in (s.series_description).strip()):
                    info[prod2_sbref].append({'item': s.series_id})
            elif (s.dim4>10):
                    info[prod2].append({'item': s.series_id})
                    
        elif ('percep2' in (s.series_description).strip()):
            if (s.dim4==1 and  'SBRef' in (s.series_description).strip()):
                    info[percep2_sbref].append({'item': s.series_id})
            elif (s.dim4>10):
                    info[percep2].append({'item': s.series_id})            
        
        elif ('ntfd2' in (s.series_description).strip()):
            if (s.dim4==1 and 'SBRef' in (s.series_description).strip()):
                    info[ntfd2_sbref].append({'item': s.series_id})
            elif (s.dim4>10):
                    info[ntfd2].append({'item': s.series_id})
        
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

