#!/bin/bash

BIDS_DIR=$AUTOBIDS_DATA/Peters/tle3T_phase2_Ex7T/bids
SUBJ_EXPR=*_Ex_{subject}  #search string for patientname


HEURISTIC=cfmm_base.py

#DCM2BIDS_PIPELINE=$AUTOBIDS_DIR/pipelines/heudiconv_bids
#PRE_BIDS_PIPELINE=$AUTOBIDS_DIR/pipelines/tuneup_bids
POST_BIDS_PIPELINE=$AUTOBIDS_DIR/pipelines/correct7T

GLOBUS_BIDS_ENDPOINT=a2ce3026-4d42-11e8-8fe0-0a6d4e044368
EMAIL_NOTIFICATION=alik@robarts.ca,mgaed@uwo.ca


TAR2BIDS_IMG=`shub-cache docker://khanlab/tar2bids:v0.0.3d
