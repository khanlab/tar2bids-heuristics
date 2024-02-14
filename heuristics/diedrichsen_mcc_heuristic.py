from cfmm_base import create_key, infotodict as cfmminfodict

def infotodict(seqinfo):
    """Heuristic evaluator for determining which runs belong where allowed 
    template fields - follow python string module:
    item: index within category
    subject: participant id
    seqitem: run number during scanning
    subindex: sub index within group
    """

    # call cfmm for general labelling and get dictionary
    info = cfmminfodict(seqinfo)

    # Keys & scans associated with scans from 2017
    task_prefix = '{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-{task}_run-{item:02d}'
    task = create_key(f'{task_prefix}_bold')
    task_sbref = create_key(f'{task_prefix}_SBRef')
    task_whole_prefix = '{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-{task}_acq-WholeBrain_run-{item:02d}'
    task_whole = create_key(f'{task_whole_prefix}_bold')
    task_whole_sbref = create_key(f'{task_whole_prefix}_SBRef')

    info[task] = []
    info[task_sbref] = []
    info[task_whole] = []
    info[task_whole_sbref] = []

    for idx, s in enumerate(seqinfo):
        # Functional scans
        if any(seq in s.protocol_name.strip() for seq in ['ep_bold', 'mbep2d_bold']):
            # 2017
            if ('ep_bold' in s.protocol_name.strip() and s.dim4 > 600):
                info[task].append({'item': s.series_id, 'task': "task"})
            # 2021
            # Note: HF scan is excluded
            elif ('mbep2d_bold' in s.protocol_name.strip()):
                if 'WholeBrain' in s.protocol_name.strip():
                    if 'SBRef' in s.series_description.strip():
                        info[task_whole_sbref].append(
                            {'item': s.series_id, 'task': "task"}
                        )
                    elif s.dim4 > 300:
                        info[task_whole].append(
                            {'item': s.series_id, 'task': "task"}
                        )
                else:
                    if 'SBRef' in s.series_description.strip():
                        info[task_sbref].append(
                            {'item': s.series_id, 'task': "task"}
                        )
                    elif s.dim4 > 300:
                        info[task].append({'item': s.series_id, 'task': "task"})

    return info
