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

    humour = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-humour_run-{item:02d}_bold')
    seinfeld = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-seinfeld_run-{item:02d}_bold')
    hitchcock = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-hitchcock_run-{item:02d}_bold')

    aspire_mag_echo_GRE = create_key('{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_acq-ASPIRE_part-mag_echo_GRE')
    aspire_phase_echo_GRE = create_key('{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_acq-ASPIRE_part-phase_echo_GRE')
    aspire_T2_star_GRE = create_key('{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_acq-ASPIRE_T2star')
    aspire_R2_star_GRE = create_key('{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_acq-ASPIRE_R2star')

    info[humour]=[]
    info[seinfeld]=[]
    info[hitchcock]=[]

    info[aspire_mag_echo_GRE] = []
    info[aspire_phase_echo_GRE] = []
    info[aspire_T2_star_GRE] = []
    info[aspire_R2_star_GRE] = []

    for idx, s in enumerate(seqinfo):

        if ('ASPIRE' in (s.series_description).strip()):
            if ('R2star' in (s.series_description).strip()):
                info[aspire_R2_star_GRE].append({'item': s.series_id})
            elif ('TSstar' in (s.series_description).strip()):
                info[aspire_T2_star_GRE].append({'item': s.series_id})
            elif len(s.image_type) > 3:
                if (('M' in (s.image_type[2].strip())) and ('ASPIRE' not in s.image_type)):
                    info[aspire_mag_echo_GRE].append({'item': s.series_id})
                if ('P' in (s.image_type[2].strip()) and len(s.image_type) > 4):
                    info[aspire_phase_echo_GRE].append({'item': s.series_id})            

        elif ('Humour' in (s.series_description).strip()):
            info[humour].append({'item': s.series_id})
                    
        elif ('Seinfeld' in (s.series_description).strip()):
            info[seinfeld].append({'item': s.series_id})   

        elif ('Hitchcock' in (s.series_description).strip()):
            info[hitchcock].append({'item': s.series_id})       

    return info
