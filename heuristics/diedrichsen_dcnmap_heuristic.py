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

    task_prefix = '{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-task_run-{item:02d}'
    task = create_key(f'{task_prefix}_bold')
    task_sbref = create_key(f'{task_prefix}_sbref')

    info[task] = []
    info[task_sbref] = []

    for idx, s in enumerate(seqinfo):
        if (s.dim4 == 1 and 'SBRef' in (s.series_description).strip()):
            info[task_sbref].append({'item': s.series_id})
        elif (s.dim4 > 1):
            info[task].append({'item': s.series_id})

    return info
