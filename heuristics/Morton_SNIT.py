import os
import numpy
from cfmm_base import create_key


def infotodict(seqinfo):
    """Heuristic evaluator for determining which runs belong where

    allowed template fields - follow python string module:

    item: index within category
    subject: participant id
    seqitem: run number during scanning
    subindex: sub index within group
    """

    inv1_mp2rage = create_key(
        "{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_inv-1_run-{item:02d}_MP2RAGE"
    )
    inv2_mp2rage = create_key(
        "{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_inv-2_run-{item:02d}_MP2RAGE"
    )
    t1map = create_key(
        "{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_acq-MP2RAGE_run-{item:02d}_T1map"
    )
    t1w = create_key(
        "{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_acq-MP2RAGE_run-{item:02d}_T1w"
    )
    uni_mp2rage = create_key(
        "{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_acq-UNI_run-{item:02d}_MP2RAGE"
    )

    # Dist. corrected versions:
    DIS3D_inv1_mp2rage = create_key(
        "{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_inv-1_rec-DIS3D_run-{item:02d}_MP2RAGE"
    )
    DIS3D_inv2_mp2rage = create_key(
        "{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_inv-2_rec-DIS3D_run-{item:02d}_MP2RAGE"
    )
    DIS3D_t1map = create_key(
        "{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_acq-MP2RAGE_rec-DIS3D_run-{item:02d}_T1map"
    )
    DIS3D_t1w = create_key(
        "{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_acq-MP2RAGE_rec-DIS3D_run-{item:02d}_T1w"
    )
    DIS3D_uni_mp2rage = create_key(
        "{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_acq-UNI_rec-DIS3D_run-{item:02d}_MP2RAGE"
    )

    DIS2D_inv1_mp2rage = create_key(
        "{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_inv-1_rec-DIS2D_run-{item:02d}_MP2RAGE"
    )
    DIS2D_inv2_mp2rage = create_key(
        "{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_inv-2_rec-DIS2D_run-{item:02d}_MP2RAGE"
    )
    DIS2D_t1map = create_key(
        "{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_acq-MP2RAGE_rec-DIS2D_run-{item:02d}_T1map"
    )
    DIS2D_t1w = create_key(
        "{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_acq-MP2RAGE_rec-DIS2D_run-{item:02d}_T1w"
    )
    DIS2D_uni_mp2rage = create_key(
        "{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_acq-UNI_rec-DIS2D_run-{item:02d}_MP2RAGE"
    )

    dwi_ap = create_key(
        "{bids_subject_session_dir}/dwi/{bids_subject_session_prefix}_dir-{dir}_run-{item:02}_dwi"
    )
    dwi_pa = create_key(
        "{bids_subject_session_dir}/fmap/{bids_subject_session_prefix}_acq-DWI_dir-{dir}_run-{item:02}_epi"
    )

    bold_ap = create_key(
        "{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-movie_dir-AP_run-{item:02d}_bold"
    )
    bold_ap_sbref = create_key(
        "{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-movie_dir-AP_run-{item:02d}_sbref"
    )
    bold_pa = create_key(
        "{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-movie_dir-PA_run-{item:02d}_bold"
    )
    bold_pa_sbref = create_key(
        "{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-movie_dir-PA_run-{item:02d}_sbref"
    )

    nm_comb_echo_GRE = create_key(
        "{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_acq-CombEchoNM_run-{item:02d}_GRE"
    )
    nm_DIS2D_comb_echo_GRE = create_key(
        "{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_acq-CombEchoNM_rec-DIS2D_run-{item:02d}_GRE"
    )
    nm_DIS3D_comb_echo_GRE = create_key(
        "{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_acq-CombEchoNM_rec-DIS3D_run-{item:02d}_GRE"
    )

    nm_mag_echo_GRE = create_key(
        "{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_acq-NM_run-{item:02d}_part-mag_GRE"
    )
    nm_phase_echo_GRE = create_key(
        "{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_acq-NM_run-{item:02d}_part-phase_GRE"
    )
    nm_DIS2D_mag_echo_GRE = create_key(
        "{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_acq-NM_rec-DIS2D_run-{item:02d}_part-mag_GRE"
    )
    nm_DIS2D_phase_echo_GRE = create_key(
        "{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_acq-NM_rec-DIS2D_run-{item:02d}_part-phase_GRE"
    )
    nm_DIS3D_mag_echo_GRE = create_key(
        "{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_acq-NM_rec-DIS3D_run-{item:02d}_echo_part-mag_GRE"
    )
    nm_DIS3D_phase_echo_GRE = create_key(
        "{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_acq-NM_rec-DIS3D_run-{item:02d}_echo_part-mag_GRE"
    )

    fmap_diff = create_key(
        "{bids_subject_session_dir}/fmap/{bids_subject_session_prefix}_phasediff"
    )
    fmap_magnitude = create_key(
        "{bids_subject_session_dir}/fmap/{bids_subject_session_prefix}_magnitude"
    )

    info = {
        bold_ap: [],
        bold_ap_sbref: [],
        bold_pa: [],
        bold_pa_sbref: [],
        dwi_ap: [],
        dwi_pa: [],
        fmap_diff: [],
        fmap_magnitude: [],
        inv1_mp2rage: [],
        t1map: [],
        t1w: [],
        uni_mp2rage: [],
        inv2_mp2rage: [],
        DIS2D_inv1_mp2rage: [],
        DIS2D_t1map: [],
        DIS2D_t1w: [],
        DIS2D_inv2_mp2rage: [],
        DIS2D_uni_mp2rage: [],
        DIS3D_inv1_mp2rage: [],
        DIS3D_t1map: [],
        DIS3D_t1w: [],
        DIS3D_inv2_mp2rage: [],
        DIS3D_uni_mp2rage: [],
        nm_comb_echo_GRE: [],
        nm_DIS2D_comb_echo_GRE: [],
        nm_DIS3D_comb_echo_GRE: [],
        nm_mag_echo_GRE: [],
        nm_DIS2D_mag_echo_GRE: [],
        nm_DIS3D_mag_echo_GRE: [],
        nm_phase_echo_GRE: [],
        nm_DIS2D_phase_echo_GRE: [],
        nm_DIS3D_phase_echo_GRE: [],
    }

    for idx, s in enumerate(seqinfo):
        # mp2rage
        if "mp2rage" in s.series_description.lower() and (
            not "memp2rage" in s.series_description.lower()
        ):
            if "INV1" in (s.series_description).strip():
                if "DIS2D" in (s.image_type[3].strip()):
                    info[DIS2D_inv1_mp2rage].append({"item": s.series_id})
                if "DIS3D" in (s.image_type[3].strip()):
                    info[DIS3D_inv1_mp2rage].append({"item": s.series_id})
                if "ND" in (s.image_type[3].strip()):
                    info[inv1_mp2rage].append({"item": s.series_id})
            if "T1_Images" in (s.series_description).strip():
                if "DIS2D" in (s.image_type[3].strip()):
                    info[DIS2D_t1map].append({"item": s.series_id})
                if "DIS3D" in (s.image_type[3].strip()):
                    info[DIS3D_t1map].append({"item": s.series_id})
                if "ND" in (s.image_type[3].strip()):
                    info[t1map].append({"item": s.series_id})
            if "UNI-DEN" in (s.series_description).strip():
                if "ND" in (s.image_type[3].strip()):
                    info[t1w].append({"item": s.series_id})
                elif "DIS2D" in (s.image_type[4].strip()):
                    info[DIS2D_t1w].append({"item": s.series_id})
                elif "DIS3D" in (s.image_type[4].strip()):
                    info[DIS3D_t1w].append({"item": s.series_id})
            if "UNI_Images" in (s.series_description).strip():
                if "DIS2D" in s.image_type:
                    info[DIS2D_uni_mp2rage].append({"item": s.series_id})
                if "DIS3D" in s.image_type:
                    info[DIS3D_uni_mp2rage].append({"item": s.series_id})
                if "ND" in s.image_type:
                    info[uni_mp2rage].append({"item": s.series_id})
            if "_INV2" in (s.series_description).strip():
                if "DIS2D" in (s.image_type[3].strip()):
                    info[DIS2D_inv2_mp2rage].append({"item": s.series_id})
                if "DIS3D" in (s.image_type[3].strip()):
                    info[DIS3D_inv2_mp2rage].append({"item": s.series_id})
                if "ND" in (s.image_type[3].strip()):
                    info[inv2_mp2rage].append({"item": s.series_id})

        # rs func (incl opp phase enc)
        if len(s.image_type) > 2:
            if ("DIFFUSION" in s.image_type[2].strip()) and (
                "ORIGINAL" in s.image_type[0].strip()
            ):
                if "PA" in (s.series_description).strip():
                    info[dwi_pa].append({"item": s.series_id, "dir": "PA"})
                elif "AP" in (s.series_description).strip():
                    info[dwi_ap].append({"item": s.series_id, "dir": "AP"})

            elif "bold" in (s.series_description).strip():

                if "AP" in (s.series_description).strip():
                    if s.dim4 == 1 and "SBRef" in (s.series_description).strip():
                        info[bold_ap_sbref].append({"item": s.series_id})
                    elif s.dim4 > 1:
                        info[bold_ap].append({"item": s.series_id})
                elif "PA" in (s.series_description).strip():
                    if s.dim4 == 1 and "SBRef" in (s.series_description).strip():
                        info[bold_pa_sbref].append({"item": s.series_id})
                    elif s.dim4 > 1:
                        info[bold_pa].append({"item": s.series_id})

        # NM-GRE
        if "NM-GRE" in s.series_description:
            if "CombEcho" in s.series_description:
                # combined echo
                info[nm_comb_echo_GRE].append({"item": s.series_id})
            else:
                if "M" in (s.image_type[2].strip()):
                    if "ND" in (s.image_type[3].strip()):
                        info[nm_mag_echo_GRE].append({"item": s.series_id})
                    if "DIS2D" in (s.image_type[3].strip()):
                        info[nm_DIS2D_mag_echo_GRE].append({"item": s.series_id})
                    if "DIS3D" in (s.image_type[3].strip()):
                        info[nm_DIS3D_mag_echo_GRE].append({"item": s.series_id})

                if "P" in (s.image_type[2].strip()):
                    if "ND" in (s.image_type[3].strip()):
                        info[nm_phase_echo_GRE].append({"item": s.series_id})
                    if "DIS2D" in (s.image_type[3].strip()):
                        info[nm_DIS2D_phase_echo_GRE].append({"item": s.series_id})
                    if "DIS3D" in (s.image_type[3].strip()):
                        info[nm_DIS3D_phase_echo_GRE].append({"item": s.series_id})

    return info
