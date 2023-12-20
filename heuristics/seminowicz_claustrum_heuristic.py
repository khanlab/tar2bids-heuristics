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

    # Keys
    task_rest = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-rest_dir-{dir}_run-{item:02d}_bold')
    task_rest_sbref = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-rest_dir-{dir}_run-{item:02d}_sbref')
    task_HeatBlock = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-HeatBlock_dir-{dir}_run-{item:02d}_bold')
    task_HeatBlock_sbref = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-HeatBlock_dir-{dir}_run-{item:02d}_sbref')
    task_HeatBlockMSITevent = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-HeatBlockMSITevent_dir-{dir}_run-{item:02d}_bold')
    task_HeatBlockMSITevent_sbref = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-HeatBlockMSITevent_dir-{dir}_run-{item:02d}_sbref')
    task_MSITeventHeatBlock = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-MSITeventHeatBlock_dir-{dir}_run-{item:02d}_bold')
    task_MSITeventHeatBlock_sbref = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-MSITeventHeatBlock_dir-{dir}_run-{item:02d}_sbref')
    task_MSIT = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-MSIT_dir-{dir}_run-{item:02d}_bold')
    task_MSIT_sbref = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-MSIT_dir-{dir}_run-{item:02d}_sbref')
    task_CoolPulse = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-CoolPulse_dir-{dir}_run-{item:02d}_bold')
    task_CoolPulse_sbref = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-CoolPulse_dir-{dir}_run-{item:02d}_sbref')

    fmap_sbref = create_key('{bids_subject_session_dir}/fmap/{bids_subject_session_prefix}_dir-{dir}_epi')
    fmap_diff = create_key('{bids_subject_session_dir}/fmap/{bids_subject_session_prefix}_phasediff')
    fmap_magnitude = create_key('{bids_subject_session_dir}/fmap/{bids_subject_session_prefix}_magnitude')

 

    # Images
    info[task_rest] = []
    info[task_rest_sbref] = []
    info[task_HeatBlock] = []
    info[task_HeatBlock_sbref] = []
    info[task_HeatBlockMSITevent] = []
    info[task_HeatBlockMSITevent_sbref] = []
    info[task_MSITeventHeatBlock] = []
    info[task_MSITeventHeatBlock_sbref] = []
    info[task_MSIT] = []
    info[task_MSIT_sbref] = []
    info[task_CoolPulse] = []
    info[task_CoolPulse_sbref] = []
    info[fmap_sbref] = []
    info[fmap_diff] = []
    info[fmap_magnitude] = []


    for idx, s in enumerate(seqinfo):
        # func
        if "mbep2d_bold_mb3_p2_AP" in (series_description := (s.series_description).strip()):
            # Rest
            if "rsMRI" in series_description:
                if 'SBRef' in series_description:
                    info[task_rest_sbref].append({'item': s.series_id, 'dir': 'AP'})
                else:
                    info[task_rest].append({'item': s.series_id, 'dir': 'AP'})
            
            # HeatBlock
            elif "HeatBlock" in series_description:
                if 'SBRef' in series_description:
                    info[task_HeatBlock_sbref].append({'item': s.series_id, 'dir': 'AP'})
                elif s.dim4 == 308:
                    info[task_HeatBlock].append({'item': s.series_id, 'dir': 'AP'})

            # HeatBlockMSITevent
            elif "HeatBlockMSITevent" in series_description:
                if 'SBRef' in series_description:
                    info[task_HeatBlockMSITevent_sbref].append({'item': s.series_id, 'dir': 'AP'})
                elif s.dim4 == 308:
                    info[task_HeatBlockMSITevent].append({'item': s.series_id, 'dir': 'AP'})

            # MSITeventHeatBlock
            elif "MSITeventHeatBlock" in series_description:
                if 'SBRef' in series_description:
                    info[task_MSITeventHeatBlock_sbref].append({'item': s.series_id, 'dir': 'AP'})
                elif s.dim4 == 308:
                    info[task_MSITeventHeatBlock].append({'item': s.series_id, 'dir': 'AP'})

            # MSIT
            elif "MSIT" in series_description:
                if 'SBRef' in series_description:
                    info[task_MSIT_sbref].append({'item': s.series_id, 'dir': 'AP'})
                elif s.dim4 == 308:
                    info[task_MSIT].append({'item': s.series_id, 'dir': 'AP'})

            # CoolPulse
            elif "CoolPulse" in series_description and s.dim4 == 288:
                if 'SBRef' in series_description:
                    info[task_CoolPulse_sbref].append({'item': s.series_id, 'dir': 'AP'})
                elif s.dim4 == 288:
                    info[task_CoolPulse].append({'item': s.series_id, 'dir': 'AP'})

        # fmap
        elif ('Topup' in (s.series_description).strip()):
            if (s.dim4==1):
                info[fmap_sbref].append({'item': s.series_id, 'dir': 'PA'})

        elif ('field_mapping' in s.protocol_name):   
            if (s.dim4 == 1) and ('gre_field_mapping' == (s.series_description).strip()):
                if('P' in (s.image_type[2].strip()) ):
                    info[fmap_diff].append({'item': s.series_id})
                if('M' in (s.image_type[2].strip()) ):
                    info[fmap_magnitude].append({'item': s.series_id})  

    return info 
