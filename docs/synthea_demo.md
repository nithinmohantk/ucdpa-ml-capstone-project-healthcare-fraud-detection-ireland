

```powershell
╭─   NithinMohan  D:  Workspace  hacks  synthea   master    ?8 ~10                       44.4s   14:15:44 
╰─ $  ./run_synthea -p 1000 "County Galway" Tuam --exporter.baseDirectory="./output_galway_tuam/"
ARG = -p
ARG = 1000
ARG = "County Galway"
ARG = Tuam
ARG = --exporter.baseDirectory
ARG = ./output_galway_tuam/
ARG =
syntheaArgs =  '-p','1000','County Galway','Tuam','--exporter.baseDirectory','./output_galway_tuam/',
WARNING: A restricted method in java.lang.System has been called
WARNING: java.lang.System::load has been called by net.rubygrapefruit.platform.internal.NativeLibraryLoader in an unnamed module (file:/C:/Users/nithinmohan/.gradle/wrapper/dists/gradle-8.2.1-bin/5hap6b9n41hkg4jeh2au2pllh/gradle-8.2.1/lib/native-platform-0.22-milestone-24.jar)
WARNING: Use --enable-native-access=ALL-UNNAMED to avoid a warning for callers in this module
WARNING: Restricted methods will be blocked in a future release unless native access is enabled


> Task :run
SLF4J: No SLF4J providers were found.
SLF4J: Defaulting to no-operation (NOP) logger implementation
SLF4J: See http://www.slf4j.org/codes.html#noProviders for further details.
Scanned 88 modules and 152 submodules.
Loading submodule modules\allergies\allergy_panel.json
Loading submodule modules\allergies\drug_allergy_incidence.json
Loading submodule modules\allergies\environmental_allergy_incidence.json
Loading submodule modules\allergies\food_allergy_incidence.json
Loading submodule modules\allergies\immunotherapy.json
Loading submodule modules\allergies\outgrow_env_allergies.json
Loading submodule modules\allergies\outgrow_food_allergies.json
Loading submodule modules\allergies\severe_allergic_reaction.json
Loading submodule modules\anemia\anemia_sub.json
Loading submodule modules\breast_cancer\chemotherapy_breast.json
Loading submodule modules\breast_cancer\hormone_diagnosis.json
Loading submodule modules\breast_cancer\hormonetherapy_breast.json
Loading submodule modules\breast_cancer\surgery_therapy_breast.json
Loading submodule modules\breast_cancer\tnm_diagnosis.json
Loading submodule modules\contraceptives\clear_contraceptive.json
Loading submodule modules\contraceptives\female_sterilization.json
Loading submodule modules\contraceptives\implant_contraceptive.json
Loading submodule modules\contraceptives\injectable_contraceptive.json
Loading submodule modules\contraceptives\intrauterine_device.json
Loading submodule modules\contraceptives\male_sterilization.json
Loading submodule modules\contraceptives\oral_contraceptive.json
Loading submodule modules\contraceptives\patch_contraceptive.json
Loading submodule modules\contraceptives\ring_contraceptive.json
Loading submodule modules\covid19\admission.json
Loading submodule modules\covid19\determine_risk.json
Loading Lookup Table: covid-19-severity-outcomes.csv
Loading Lookup Table: covid-19-survival-outcomes.csv
Loading submodule modules\covid19\diagnose_bacterial_infection.json
Loading submodule modules\covid19\diagnose_blood_clot.json
Loading submodule modules\covid19\end_outcomes.json
Loading submodule modules\covid19\end_symptoms.json
Loading submodule modules\covid19\infection.json
Loading submodule modules\covid19\measurements_daily.json
Loading submodule modules\covid19\measurements_frequent.json
Loading submodule modules\covid19\measurements_vitals.json
Loading submodule modules\covid19\medications.json
Loading submodule modules\covid19\nonsurvivor_lab_values.json
Loading submodule modules\covid19\outcomes.json
Loading submodule modules\covid19\supplies_hospitalization.json
Loading submodule modules\covid19\supplies_icu.json
Loading submodule modules\covid19\supplies_intubation.json
Loading submodule modules\covid19\survivor_lab_values.json
Loading submodule modules\covid19\symptoms.json
Loading submodule modules\covid19\treat_blood_clot.json
Loading submodule modules\dermatitis\early_moderate_eczema_obs.json
Loading submodule modules\dermatitis\early_severe_eczema_obs.json
Loading submodule modules\dermatitis\mid_moderate_eczema_obs.json
Loading submodule modules\dermatitis\mid_severe_eczema_obs.json
Loading submodule modules\dermatitis\moderate_cd_obs.json
Loading submodule modules\dermatitis\severe_cd_obs.json
Loading submodule modules\dme\wheelchair.json
Loading submodule modules\dme\wheelchair_end.json
Loading submodule modules\encounter\anxiety_screening.json
Loading submodule modules\encounter\depression_screening.json
Loading submodule modules\encounter\fall_risk_screening.json
Loading submodule modules\encounter\hark_screening.json
Loading submodule modules\encounter\hospital_basic_labs.json
Loading submodule modules\encounter\sdoh_hrsn.json
Loading submodule modules\encounter\substance_use_screening.json
Loading submodule modules\encounter\vitals.json
Loading submodule modules\heart\acs_anticoagulant.json
Loading submodule modules\heart\acs_antiplatelet.json
Loading submodule modules\heart\acs_arrival_medications.json
Loading submodule modules\heart\acs_discharge_meds.json
Loading submodule modules\heart\avrr\antithrombotic.json
Loading submodule modules\heart\avrr\avrr_referral.json
Loading submodule modules\heart\avrr\intraop_meds_blood.json
Loading submodule modules\heart\avrr\outcomes.json
Loading submodule modules\heart\avrr\preoperative.json
Loading submodule modules\heart\avrr\savrr_operation.json
Loading submodule modules\heart\avrr\savrr_postop.json
Loading submodule modules\heart\avrr\sequence.json
Loading submodule modules\heart\cabg\cabg_referral.json
Loading submodule modules\heart\cabg\details.json
Loading Lookup Table: cabg_details_operative_approach.csv
Loading Lookup Table: cabg_details_num_grafts.csv
Loading Lookup Table: cabg_details_num_art_cond.csv
Loading submodule modules\heart\cabg\icu_meds_devices.json
Loading submodule modules\heart\cabg\labs_common.json
Loading submodule modules\heart\cabg\operation.json
Loading submodule modules\heart\cabg\or_intraop.json
Loading submodule modules\heart\cabg\or_labs_meds.json
Loading submodule modules\heart\cabg\outcomes.json
Loading submodule modules\heart\cabg\postop.json
Loading submodule modules\heart\cabg\postop_blood.json
Loading submodule modules\heart\cabg\preoperative.json
Loading submodule modules\heart\cabg_sequence.json
Loading submodule modules\heart\cardiac_labs.json
Loading submodule modules\heart\chf_lab_work.json
Loading submodule modules\heart\chf_lvad.json
Loading submodule modules\heart\chf_meds.json
Loading submodule modules\heart\chf_meds_hfmef.json
Loading submodule modules\heart\chf_meds_hfref_nyha2.json
Loading submodule modules\heart\chf_meds_hfref_nyha3.json
Loading submodule modules\heart\chf_meds_hfref_nyha4.json
Loading submodule modules\heart\chf_nyha_panel.json
Loading submodule modules\heart\chf_transplant.json
Loading submodule modules\heart\nsteacs_pathway.json
Loading submodule modules\heart\operative_status.json
Loading submodule modules\heart\or_blood.json
Loading Lookup Table: or_blood_anemia_check.csv
Loading Lookup Table: or_blood_platelet_check.csv
Loading Lookup Table: or_blood_plasma_check.csv
Loading submodule modules\heart\savrepair\operative_status.json
Loading submodule modules\heart\savreplace\operative_status.json
Loading submodule modules\heart\stemi_fibrinolytic.json
Loading submodule modules\heart\stemi_pathway.json
Loading submodule modules\heart\tavr\alt_access.json
Loading submodule modules\heart\tavr\operation.json
Loading submodule modules\heart\tavr\operative_status.json
Loading submodule modules\heart\tavr\outcomes.json
Loading submodule modules\heart\tavr\postop.json
Loading submodule modules\heart\vhd_risks.json
Loading submodule modules\hiv\art_sequence.json
Loading submodule modules\hiv\art_sequence_1987_1994.json
Loading submodule modules\hiv\art_sequence_1995_1996.json
Loading submodule modules\hiv\art_sequence_1997_2002.json
Loading submodule modules\hiv\art_sequence_2003_2005.json
Loading submodule modules\hiv\art_sequence_2006_2014.json
Loading submodule modules\hiv\art_sequence_2015.json
Loading submodule modules\hiv\hiv_baseline.json
Loading submodule modules\hiv\hiv_cd4.json
Loading Lookup Table: hiv_stage.csv
Loading submodule modules\hiv\hiv_oi_prophylaxis.json
Loading submodule modules\hiv\hiv_screening.json
Loading submodule modules\hiv\hiv_viral_load.json
Loading submodule modules\hiv\stop_all_art_meds.json
Loading submodule modules\injuries\broken_jaw.json
Loading submodule modules\lung_cancer\lung_cancer_probabilities.json
Loading submodule modules\medications\ace_arb.json
Loading Lookup Table: ace_arb_ingredient_distribution.csv
Loading Lookup Table: ace_arb_amlodipine_benazepril_product_distribution.csv
Loading Lookup Table: ace_arb_benazepril_product_distribution.csv
Loading Lookup Table: ace_arb_benazepril_hydrochlorothiazide_product_distribution.csv
Loading Lookup Table: ace_arb_enalapril_product_distribution.csv
Loading Lookup Table: ace_arb_hydrochlorothiazide_lisinopril_product_distribution.csv
Loading Lookup Table: ace_arb_hydrochlorothiazide_losartan_product_distribution.csv
Loading Lookup Table: ace_arb_hydrochlorothiazide_valsartan_product_distribution.csv
Loading Lookup Table: ace_arb_irbesartan_product_distribution.csv
Loading Lookup Table: ace_arb_lisinopril_product_distribution.csv
Loading Lookup Table: ace_arb_losartan_product_distribution.csv
Loading Lookup Table: ace_arb_quinapril_product_distribution.csv
Loading Lookup Table: ace_arb_ramipril_product_distribution.csv
Loading Lookup Table: ace_arb_sacubitril_valsartan_product_distribution.csv
Loading Lookup Table: ace_arb_telmisartan_product_distribution.csv
Loading Lookup Table: ace_arb_valsartan_product_distribution.csv
Loading submodule modules\medications\beta_blocker.json
Loading Lookup Table: beta_blocker_ingredient_distribution.csv
Loading Lookup Table: beta_blocker_atenolol_product_distribution.csv
Loading Lookup Table: beta_blocker_bisoprolol_product_distribution.csv
Loading Lookup Table: beta_blocker_bisoprolol_hydrochlorothiazide_product_distribution.csv
Loading Lookup Table: beta_blocker_carvedilol_product_distribution.csv
Loading Lookup Table: beta_blocker_labetalol_product_distribution.csv
Loading Lookup Table: beta_blocker_metoprolol_product_distribution.csv
Loading Lookup Table: beta_blocker_nebivolol_product_distribution.csv
Loading Lookup Table: beta_blocker_propranolol_product_distribution.csv
Loading submodule modules\medications\ear_infection_antibiotic.json
Loading submodule modules\medications\emergency_inhaler.json
Loading Lookup Table: emergency_inhaler_ingredient_distribution.csv
Loading Lookup Table: emergency_inhaler_albuterol_product_distribution.csv
Loading Lookup Table: emergency_inhaler_levalbuterol_product_distribution.csv
Loading submodule modules\medications\hypertension_medication.json
Loading submodule modules\medications\maintenance_inhaler.json
Loading Lookup Table: maintenance_inhaler_ingredient_distribution.csv
Loading Lookup Table: maintenance_inhaler_beclomethasone_product_distribution.csv
Loading Lookup Table: maintenance_inhaler_budesonide_product_distribution.csv
Loading Lookup Table: maintenance_inhaler_fluticasone_product_distribution.csv
Loading Lookup Table: maintenance_inhaler_mometasone_product_distribution.csv
Loading submodule modules\medications\moderate_opioid_pain_reliever.json
Loading submodule modules\medications\otc_antihistamine.json
Loading submodule modules\medications\otc_pain_reliever.json
Loading submodule modules\medications\statin.json
Loading Lookup Table: statin_ingredient_distribution.csv
Loading Lookup Table: statin_atorvastatin_product_distribution.csv
Loading Lookup Table: statin_ezetimibe_simvastatin_product_distribution.csv
Loading Lookup Table: statin_lovastatin_product_distribution.csv
Loading Lookup Table: statin_pitavastatin_product_distribution.csv
Loading Lookup Table: statin_pravastatin_product_distribution.csv
Loading Lookup Table: statin_rosuvastatin_product_distribution.csv
Loading Lookup Table: statin_simvastatin_product_distribution.csv
Loading submodule modules\medications\strong_opioid_pain_reliever.json
Loading submodule modules\metabolic_syndrome\amputations.json
Loading submodule modules\metabolic_syndrome\dme_supplies.json
Loading submodule modules\metabolic_syndrome\eye_conditions.json
Loading submodule modules\metabolic_syndrome\kidney_conditions.json
Loading submodule modules\metabolic_syndrome\medications.json
Loading submodule modules\snf\skilled_nursing_facility.json
Loading submodule modules\surgery\general_anesthesia.json
Loading submodule modules\total_joint_replacement\functional_status_assessments.json
Loading submodule modules\uti\abx_tx.json
Loading submodule modules\uti\ambulatory_eval.json
Loading submodule modules\uti\ambulatory_path.json
Loading submodule modules\uti\ed_bundle.json
Loading submodule modules\uti\ed_eval.json
Loading submodule modules\uti\ed_path.json
Loading submodule modules\uti\gu_pregnancy_check.json
Loading submodule modules\uti\hpi.json
Loading submodule modules\uti\lab_follow_up.json
Loading submodule modules\uti\labs.json
Loading submodule modules\uti\telemed_path.json
Loading submodule modules\veterans\veteran_suicide_probabilities.json
Loading submodule modules\weight_loss\mend_week.json
Loading module modules\acute_myeloid_leukemia.json
Loading Lookup Table: AML.csv
Loading module modules\allergic_rhinitis.json
Loading module modules\allergies.json
Loading module modules\anemia___unknown_etiology.json
Loading module modules\appendicitis.json
Loading module modules\asthma.json
Loading module modules\atopy.json
Loading module modules\atrial_fibrillation.json
Loading module modules\attention_deficit_disorder.json
Loading module modules\bone_marrow_transplant.json
Loading module modules\breast_cancer.json
Loading module modules\bronchitis.json
Loading module modules\cerebral_palsy.json
Loading module modules\chronic_kidney_disease.json
Loading module modules\colorectal_cancer.json
Loading module modules\congestive_heart_failure.json
Loading module modules\contraceptive_maintenance.json
Loading module modules\contraceptives.json
Loading module modules\copd.json
Loading module modules\covid19.json
Loading Lookup Table: covid19_prob.csv
Loading module modules\cystic_fibrosis.json
Loading module modules\dementia.json
Loading module modules\dental_and_oral_examination.json
Loading module modules\dentures.json
Loading module modules\dermatitis.json
Loading module modules\dialysis.json
Loading module modules\ear_infections.json
Loading module modules\epilepsy.json
Loading module modules\female_reproduction.json
Loading module modules\fibromyalgia.json
Loading module modules\food_allergies.json
Loading module modules\gallstones.json
Loading module modules\gout.json
Loading module modules\hiv_care.json
Loading Lookup Table: hiv_care.csv
Loading module modules\hiv_diagnosis.json
Loading Lookup Table: hiv_mortality_later.csv
Loading Lookup Table: hiv_mortality_early.csv
Loading Lookup Table: hiv_mortality_very_early.csv
Loading Lookup Table: hiv_diagnosis_early.csv
Loading Lookup Table: hiv_diagnosis_later.csv
Loading module modules\home_health_treatment.json
Loading module modules\home_hospice_snf.json
Loading module modules\homelessness.json
Loading module modules\hospice_treatment.json
Loading module modules\hypertension.json
Loading module modules\hypothyroidism.json
Loading module modules\injuries.json
Loading module modules\kidney_transplant.json
Loading module modules\lung_cancer.json
Loading module modules\lupus.json
Loading module modules\mTBI.json
Loading module modules\med_rec.json
Loading module modules\mend_program.json
Loading module modules\metabolic_syndrome_care.json
Loading module modules\metabolic_syndrome_disease.json
Loading module modules\myocardial_infarction.json
Loading module modules\opioid_addiction.json
Loading module modules\osteoarthritis.json
Loading module modules\osteoporosis.json
Loading module modules\pregnancy.json
Loading module modules\prescribing_opioids_for_chronic_pain_and_treatment_of_oud.json
Loading module modules\rheumatoid_arthritis.json
Loading module modules\self_harm.json
Loading module modules\sepsis.json
Loading module modules\sexual_activity.json
Loading module modules\sinusitis.json
Loading module modules\sleep_apnea.json
Loading module modules\sore_throat.json
Loading module modules\spina_bifida.json
Loading module modules\stable_ischemic_heart_disease.json
Loading module modules\stroke.json
Loading module modules\total_joint_replacement.json
Loading module modules\trigger_bone_marrow_transplant.json
Loading module modules\urinary_tract_infections.json
Loading Lookup Table: uti.csv
Loading Lookup Table: uti_recurrence.csv
Loading module modules\veteran.json
Loading module modules\veteran_hyperlipidemia.json
Loading module modules\veteran_lung_cancer.json
Loading module modules\veteran_mdd.json
Loading module modules\veteran_prostate_cancer.json
Loading module modules\veteran_ptsd.json
Loading module modules\veteran_self_harm.json
Loading module modules\veteran_substance_abuse_conditions.json
Loading module modules\veteran_substance_abuse_treatment.json
Loading module modules\vhd_aortic.json
Loading Lookup Table: vhd_as.csv
Loading Lookup Table: vhd_ar.csv
Loading module modules\vhd_mitral.json
Loading Lookup Table: vhd_mr.csv
Loading Lookup Table: vhd_ms.csv
Loading module modules\vhd_pulmonic.json
Loading Lookup Table: vhd_ps.csv
Loading Lookup Table: vhd_pr.csv
Loading module modules\vhd_tricuspid.json
Loading Lookup Table: vhd_tr.csv
Loading Lookup Table: vhd_ts.csv
Loading module modules\wellness_encounters.json
Running with options:
Population: 1000
Seed: 1763561819514
Provider Seed:1763561819514
Reference Time: 1763561819514
Location: Tuam, County Galway
Min Age: 0
Max Age: 140
20 -- Henriette328 Purdy2 (6 y/o F) Tuam, County Galway  (9243)
10 -- Traci329 Hettinger594 (2 y/o F) Tuam, County Galway  (4539)
19 -- Geralyn932 Rippin620 (15 y/o F) Tuam, County Galway  (20563)
16 -- Erika442 Adams676 (5 y/o F) Tuam, County Galway  (7377)
13 -- Scottie437 Rowe323 (15 y/o M) Tuam, County Galway  (21240)
14 -- Jenette717 Vandervort697 (29 y/o F) Tuam, County Galway  (41068)
1 -- Justa309 Abernathy524 (12 y/o F) Tuam, County Galway  (16912)
9 -- Phuong301 Bechtelar572 (9 y/o F) Tuam, County Galway  (12866)
11 -- Crystal2 Kling921 (18 y/o F) Tuam, County Galway  (26315)
4 -- Izetta651 Fay398 (19 y/o F) Tuam, County Galway  (26562)
3 -- Pasquale620 O'Conner199 (20 y/o M) Tuam, County Galway  (28045)
6 -- Krissy321 Britta584 Runte676 (28 y/o F) Tuam, County Galway  (41845)
17 -- Monty345 Rath779 (41 y/o M) Tuam, County Galway  (59350)
18 -- Nidia145 Kattie846 Schamberger479 (65 y/o F) Tuam, County Galway  (96556)
12 -- Petra678 Wehner319 (73 y/o F) Tuam, County Galway DECEASED (103867)
8 -- Alfredo17 Balistreri607 (35 y/o M) Tuam, County Galway  (49005)
5 -- Tressa150 Britney439 Schiller186 (51 y/o F) Tuam, County Galway  (75284)
15 -- Alysha630 Ziemann98 (50 y/o F) Tuam, County Galway DECEASED (73829)
2 -- Magaly973 Bartell116 (65 y/o F) Tuam, County Galway  (98102)
7 -- Robert854 Wisozk929 (67 y/o M) Tuam, County Galway  (94914)
21 -- Erica194 Schultz619 (22 y/o F) Tuam, County Galway  (32554)
29 -- Zenaida56 Sawayn19 (4 y/o F) Tuam, County Galway  (6416)
31 -- Robin66 Larkin917 (0 y/o F) Tuam, County Galway  (831)
22 -- Lola232 Dickens475 (57 y/o F) Tuam, County Galway  (84593)
24 -- Shyla233 Lockman863 (64 y/o F) Tuam, County Galway  (95612)
26 -- Kristina583 Swaniawski813 (22 y/o F) Tuam, County Galway  (31844)
23 -- Micha632 Parker433 (70 y/o F) Tuam, County Galway  (99687)
32 -- Altagracia629 Krajcik437 (13 y/o F) Tuam, County Galway  (18346)
28 -- Luanne915 Zieme486 (36 y/o F) Tuam, County Galway  (53209)
35 -- German382 Kemmer137 (14 y/o M) Tuam, County Galway  (19600)
41 -- Jennifer579 Stroman228 (1 y/o F) Tuam, County Galway  (2985)
12 -- Reda120 Thersa321 Cartwright189 (78 y/o F) Tuam, County Galway  (114630)
27 -- Elvis145 Tremblay80 (53 y/o M) Tuam, County Galway  (74820)
40 -- Jess275 Eichmann909 (49 y/o M) Tuam, County Galway  (68636)
50 -- Sanda877 Lebsack687 (1 y/o F) Tuam, County Galway  (2811)
38 -- Candice681 Conn188 (19 y/o F) Tuam, County Galway  (28851)
36 -- Felica690 Sean831 Moen819 (50 y/o F) Tuam, County Galway  (71149)
49 -- Shelly431 Wyman904 (14 y/o F) Tuam, County Galway  (20337)
42 -- Damien170 Homenick806 (20 y/o M) Tuam, County Galway  (28808)
30 -- Cherise743 Anderson154 (42 y/o F) Tuam, County Galway  (60288)
44 -- Chelsea317 Bobbie849 Kuvalis369 (63 y/o F) Tuam, County Galway  (92125)
43 -- Lavera253 Ninfa662 Ullrich385 (61 y/o F) Tuam, County Galway DECEASED (120841)
52 -- Zachary28 Flatley871 (26 y/o M) Tuam, County Galway  (38405)
37 -- Benny518 Jacobson885 (52 y/o M) Tuam, County Galway DECEASED (74769)
47 -- Ivan258 Koepp521 (47 y/o M) Tuam, County Galway  (65523)
34 -- Lorene243 Dorethea38 DuBuque211 (65 y/o F) Tuam, County Galway  (100395)
33 -- Carmel816 Lucilla742 Stark857 (46 y/o F) Tuam, County Galway  (69134)
48 -- Geoffrey157 Harber290 (41 y/o M) Tuam, County Galway  (58472)
46 -- Willian804 Schaefer657 (31 y/o M) Tuam, County Galway  (47485)
53 -- Prince887 Daugherty69 (51 y/o M) Tuam, County Galway  (70415)
54 -- Mardell937 Alta896 Pfeffer420 (40 y/o F) Tuam, County Galway DECEASED (59231)
51 -- Gregory545 Rogahn59 (61 y/o M) Tuam, County Galway  (85676)
60 -- Joette227 Parisian75 (1 y/o F) Tuam, County Galway  (2468)
56 -- Forrest301 Spinka232 (44 y/o M) Tuam, County Galway DECEASED (62875)
65 -- Vickie113 Christiansen251 (2 y/o F) Tuam, County Galway  (3465)
39 -- Adela471 Beverly445 Kautzer186 (59 y/o F) Tuam, County Galway  (86872)
66 -- Pat3 Reichert620 (8 y/o M) Tuam, County Galway  (11632)
45 -- Erick204 Luettgen772 (70 y/o M) Tuam, County Galway  (102551)
55 -- Matt836 Batz141 (63 y/o M) Tuam, County Galway  (90953)
58 -- Dudley365 Bogisich202 (31 y/o M) Tuam, County Galway  (45996)
61 -- Barbera53 Kuvalis369 (48 y/o F) Tuam, County Galway  (72781)
15 -- Elyse324 Upton904 (72 y/o F) Tuam, County Galway  (105870)
57 -- Robyn562 Torphy630 (44 y/o F) Tuam, County Galway  (62859)
63 -- Erlinda993 Pagac496 (43 y/o F) Tuam, County Galway  (61339)
69 -- Julee121 Olson653 (6 y/o F) Tuam, County Galway  (9381)
64 -- Ezra452 Ullrich385 (21 y/o M) Tuam, County Galway  (29631)
62 -- Lovie151 Nobuko304 Collier206 (32 y/o F) Tuam, County Galway  (45693)
67 -- Abraham100 Reilly981 (60 y/o M) Tuam, County Galway  (86698)
54 -- Erlinda993 Shanika235 O'Hara248 (52 y/o F) Tuam, County Galway  (77198)
56 -- Connie24 Paucek755 (58 y/o M) Tuam, County Galway  (85166)
25 -- Despina962 Zoe32 Weissnat378 (101 y/o F) Tuam, County Galway DECEASED (212731)
73 -- Cheree978 Wilderman619 (35 y/o F) Tuam, County Galway  (52336)
71 -- Steven797 Leda374 Davis923 (36 y/o F) Tuam, County Galway  (53870)
79 -- Roman389 Bogisich202 (0 y/o M) Tuam, County Galway  (1232)
59 -- Adelina682 Kiara978 Heathcote539 (67 y/o F) Tuam, County Galway DECEASED (98746)
81 -- Odell776 Becker968 (3 y/o M) Tuam, County Galway  (5699)
68 -- Jimmy858 Bergstrom287 (50 y/o M) Tuam, County Galway  (69057)
72 -- Malissa448 Tessa832 Donnelly343 (42 y/o F) Tuam, County Galway  (69421)
80 -- Burt293 Gulgowski816 (16 y/o M) Tuam, County Galway  (23197)
85 -- Talitha643 Thiel172 (2 y/o F) Tuam, County Galway  (3602)
74 -- Gino587 Goyette777 (57 y/o M) Tuam, County Galway  (79324)
37 -- Bret7 Littel644 (54 y/o M) Tuam, County Galway  (75519)
75 -- Tracy345 Ryan260 (33 y/o M) Tuam, County Galway  (46292)
70 -- King743 Heathcote539 (65 y/o M) Tuam, County Galway  (92587)
77 -- Chung121 Beahan375 (38 y/o M) Tuam, County Galway  (54950)
86 -- Lionel365 Streich926 (6 y/o M) Tuam, County Galway  (9142)
88 -- Tyron580 Oberbrunner298 (12 y/o M) Tuam, County Galway  (17254)
90 -- Muriel394 Connelly992 (5 y/o F) Tuam, County Galway  (8210)
83 -- Danika134 Lida218 Collins926 (36 y/o F) Tuam, County Galway  (54553)
84 -- Hilton264 Walter473 (50 y/o M) Tuam, County Galway  (71627)
93 -- Devorah937 Ernser583 (6 y/o F) Tuam, County Galway  (9605)
82 -- Normand813 Lockman863 (49 y/o M) Tuam, County Galway DECEASED (69758)
78 -- Kenda873 Thompson596 (68 y/o F) Tuam, County Galway  (97955)
76 -- Ima629 Stefania815 Collier206 (63 y/o F) Tuam, County Galway  (92869)
87 -- Beaulah36 Leola603 Kulas532 (30 y/o F) Tuam, County Galway  (45944)
96 -- Latashia561 Greenholt190 (12 y/o F) Tuam, County Galway  (17456)
92 -- Emelina469 Gleichner915 (14 y/o F) Tuam, County Galway  (20051)
91 -- Bessie423 Schinner682 (19 y/o F) Tuam, County Galway  (26781)
97 -- Gonzalo160 Monahan736 (20 y/o M) Tuam, County Galway  (28414)
95 -- Treasa448 Brekke496 (28 y/o F) Tuam, County Galway  (40729)
94 -- Charlott617 Robin66 Parisian75 (35 y/o F) Tuam, County Galway  (53164)
89 -- Edgardo196 Murazik203 (60 y/o M) Tuam, County Galway  (84440)
106 -- Myriam433 Nolan344 (1 y/o F) Tuam, County Galway  (2555)
99 -- Jenine75 Rolfson709 (33 y/o F) Tuam, County Galway  (46878)
102 -- Miquel905 O'Conner199 (27 y/o M) Tuam, County Galway  (38648)
98 -- Luis923 Blanda868 (56 y/o M) Tuam, County Galway  (78807)
101 -- Nilsa143 Chi716 Gleichner915 (56 y/o F) Tuam, County Galway  (86406)
112 -- Sammy219 Brakus656 (30 y/o M) Tuam, County Galway DECEASED (44527)
104 -- Mark765 Marietta439 Purdy2 (51 y/o F) Tuam, County Galway  (72837)
100 -- Genie948 Fahey393 (55 y/o F) Tuam, County Galway  (80698)
82 -- Cletus494 Weimann465 (52 y/o M) Tuam, County Galway  (74627)
109 -- Daisey627 Refugia211 Welch179 (28 y/o F) Tuam, County Galway  (43056)
107 -- Maximo817 Sporer811 (53 y/o M) Tuam, County Galway  (74348)
116 -- Terese90 Rice937 (20 y/o F) Tuam, County Galway  (29711)
114 -- Ludie599 Ronald408 Gutkowski940 (36 y/o F) Tuam, County Galway  (51310)
108 -- Emmanuel930 Tromp100 (58 y/o M) Tuam, County Galway  (87218)
105 -- Randy380 Cartwright189 (59 y/o M) Tuam, County Galway  (84368)
115 -- Harry448 Erdman779 (49 y/o M) Tuam, County Galway  (69168)
59 -- Stacia109 Hills818 (85 y/o F) Tuam, County Galway DECEASED (135786)
43 -- Lakeesha370 Oberbrunner298 (64 y/o F) Tuam, County Galway DECEASED (96059)
111 -- Joshua658 Hirthe744 (60 y/o M) Tuam, County Galway  (86633)
113 -- Nita296 Sylvia544 Koepp521 (57 y/o F) Tuam, County Galway  (81354)
118 -- Benito209 Heathcote539 (7 y/o M) Tuam, County Galway DECEASED (10754)
120 -- Mui729 Pollich983 (11 y/o F) Tuam, County Galway  (15224)
103 -- Shayla126 Vernia453 Parisian75 (71 y/o F) Tuam, County Galway  (139126)
119 -- Refugio197 Bahringer146 (14 y/o M) Tuam, County Galway  (19476)
110 -- Dodie685 Carole948 Hegmann834 (70 y/o F) Tuam, County Galway  (105798)
123 -- Quinn173 Kertzmann286 (11 y/o M) Tuam, County Galway  (15156)
122 -- Florida645 Waters156 (18 y/o F) Tuam, County Galway  (26136)
126 -- Rudolf736 Goodwin327 (9 y/o M) Tuam, County Galway DECEASED (12964)
124 -- Hisako109 Schimmel440 (17 y/o F) Tuam, County Galway  (24085)
121 -- Joaquin141 Wiza601 (34 y/o M) Tuam, County Galway  (47647)
117 -- Jerome176 Kirlin939 (41 y/o M) Tuam, County Galway  (62818)
130 -- Edward499 Gislason620 (17 y/o F) Tuam, County Galway  (24018)
131 -- Marisol435 Herzog843 (16 y/o F) Tuam, County Galway  (22835)
128 -- Dorie139 Jacqueline49 Pouros728 (28 y/o F) Tuam, County Galway  (40564)
126 -- Salvatore257 Reilly981 (9 y/o M) Tuam, County Galway  (13928)
133 -- Debbi640 Erdman779 (4 y/o F) Tuam, County Galway  (6503)
129 -- Mirna233 Kerluke267 (16 y/o F) Tuam, County Galway  (22962)
127 -- Marcelo725 Reilly981 (42 y/o M) Tuam, County Galway  (60461)
134 -- Rosamaria757 Romaguera67 (6 y/o F) Tuam, County Galway  (9531)
136 -- Kalyn451 Schmitt836 (6 y/o F) Tuam, County Galway  (8929)
112 -- Alvaro283 Spinka232 (52 y/o M) Tuam, County Galway  (75566)
135 -- Alfonso758 Crooks415 (19 y/o M) Tuam, County Galway  (27732)
137 -- Pierre431 Schiller186 (14 y/o M) Tuam, County Galway  (20569)
118 -- Raphael767 Crona259 (68 y/o M) Tuam, County Galway  (96666)
139 -- Angelo118 Batz141 (32 y/o M) Tuam, County Galway  (45540)
142 -- Gerard367 Maggio310 (14 y/o M) Tuam, County Galway  (20373)
125 -- Reynaldo722 Cassin499 (54 y/o M) Tuam, County Galway DECEASED (78578)
143 -- Joey457 Berge125 (12 y/o M) Tuam, County Galway  (17108)
138 -- Hermelinda327 Marylynn944 Parisian75 (47 y/o F) Tuam, County Galway  (69119)
150 -- Allan198 Gutmann970 (4 y/o M) Tuam, County Galway  (6184)
43 -- Gretta175 Johnette525 Doyle959 (64 y/o F) Tuam, County Galway  (119162)
145 -- Ardell826 MacGyver246 (16 y/o F) Tuam, County Galway  (22539)
132 -- Concepcion673 Stracke611 (75 y/o F) Tuam, County Galway DECEASED (119543)
147 -- Herschel574 Bartell116 (19 y/o M) Tuam, County Galway  (27371)
151 -- Breanna581 Wunsch504 (13 y/o F) Tuam, County Galway  (20746)
141 -- Roxanne257 Jerry654 Hirthe744 (54 y/o F) Tuam, County Galway  (79576)
146 -- Floretta117 Lindy582 Predovic534 (55 y/o F) Tuam, County Galway  (79482)
144 -- Eda506 Daphine453 Osinski784 (46 y/o F) Tuam, County Galway  (65482)
148 -- Evan94 VonRueden376 (59 y/o M) Tuam, County Galway  (85667)
160 -- Greg949 Lang846 (0 y/o M) Tuam, County Galway  (736)
162 -- Maryalice613 Bernier607 (2 y/o F) Tuam, County Galway  (3704)
153 -- Augustus49 Bogan287 (52 y/o M) Tuam, County Galway DECEASED (95806)
154 -- Rosenda12 Lewis216 Tromp100 (59 y/o F) Tuam, County Galway  (87301)
157 -- Marcelo725 Kuhic920 (38 y/o M) Tuam, County Galway  (52670)
155 -- Larry532 Veum823 (33 y/o M) Tuam, County Galway  (46035)
156 -- Sherryl893 Bernier607 (46 y/o F) Tuam, County Galway  (72394)
140 -- Carmelo33 Heller342 (62 y/o M) Tuam, County Galway  (95705)
164 -- Daniella68 Stoltenberg489 (35 y/o F) Tuam, County Galway  (52434)
167 -- Nelson403 Hessel84 (3 y/o M) Tuam, County Galway  (5478)
158 -- Kyla51 Angella518 Koelpin146 (41 y/o F) Tuam, County Galway  (60404)
159 -- Rhett759 Mueller846 (63 y/o M) Tuam, County Galway  (89211)
149 -- Ed239 Ankunding277 (87 y/o M) Tuam, County Galway  (158724)
163 -- Nathan164 Murray856 (63 y/o M) Tuam, County Galway  (91803)
165 -- Noreen211 Jacobi462 (51 y/o F) Tuam, County Galway  (74015)
168 -- Odis959 Deckow585 (29 y/o M) Tuam, County Galway  (41201)
166 -- Augustus49 Schmitt836 (59 y/o M) Tuam, County Galway  (81847)
25 -- Londa304 Stacee229 Stehr398 (94 y/o F) Tuam, County Galway DECEASED (140685)
152 -- Gayle448 MacGyver246 (69 y/o M) Tuam, County Galway DECEASED (100296)
161 -- Rodrigo242 Kuvalis369 (54 y/o M) Tuam, County Galway  (75007)
172 -- Huey641 Zieme486 (18 y/o M) Tuam, County Galway  (24957)
177 -- Dewitt635 Franecki195 (3 y/o M) Tuam, County Galway  (4750)
178 -- Meta661 Dooley940 (2 y/o F) Tuam, County Galway  (3584)
179 -- Shella455 Cummings51 (7 y/o F) Tuam, County Galway  (10558)
174 -- Anh979 Kihn564 (34 y/o F) Tuam, County Galway  (48653)
173 -- Edmundo94 Greenfelder433 (51 y/o M) Tuam, County Galway  (71606)
125 -- Duncan491 Vandervort697 (72 y/o M) Tuam, County Galway DECEASED (111164)
132 -- Soon875 Wilkinson796 (78 y/o F) Tuam, County Galway  (114970)
180 -- Telma919 Gleichner915 (23 y/o F) Tuam, County Galway  (33286)
181 -- Gil594 Schaefer657 (53 y/o M) Tuam, County Galway  (85215)
182 -- Janise4 Carroll471 (16 y/o F) Tuam, County Galway  (21806)
175 -- Anjelica989 Abshire638 (61 y/o F) Tuam, County Galway  (89263)
171 -- Hobert364 Monahan736 (67 y/o M) Tuam, County Galway  (96033)
187 -- Javier97 Haley279 (15 y/o M) Tuam, County Galway  (21433)
176 -- Burl285 Schimmel440 (65 y/o M) Tuam, County Galway DECEASED (98030)
184 -- Livia401 Honey275 Paucek755 (73 y/o F) Tuam, County Galway  (107024)
185 -- Lavona767 Penney623 Kutch271 (56 y/o F) Tuam, County Galway  (85544)
170 -- Clora637 Lucy743 Turner526 (61 y/o F) Tuam, County Galway  (90126)
190 -- Blossom971 Kunde533 (12 y/o F) Tuam, County Galway  (16874)
186 -- Gavin481 Cole117 (39 y/o M) Tuam, County Galway  (53309)
169 -- Calandra120 Flossie205 Kozey370 (74 y/o F) Tuam, County Galway  (139752)
59 -- Mercy752 Barabara924 Cremin516 (93 y/o F) Tuam, County Galway  (144535)
188 -- Keena534 Dooley940 (46 y/o F) Tuam, County Galway  (64467)
192 -- Pura348 Numbers230 Mueller846 (58 y/o F) Tuam, County Galway  (84804)
194 -- Madlyn383 Kulas532 (20 y/o F) Tuam, County Galway  (28092)
183 -- Sanjuanita786 Leonida214 Bogisich202 (66 y/o F) Tuam, County Galway  (96465)
195 -- Tyrell880 Spencer878 (18 y/o M) Tuam, County Galway  (26201)
152 -- Oliver401 O'Keefe54 (72 y/o M) Tuam, County Galway DECEASED (103008)
193 -- Coleman27 Murphy561 (62 y/o M) Tuam, County Galway  (87241)
191 -- Eliseo499 Beahan375 (79 y/o M) Tuam, County Galway DECEASED (122369)
197 -- Raul814 Bartoletti50 (32 y/o M) Tuam, County Galway  (45714)
204 -- Allen322 O'Conner199 (6 y/o M) Tuam, County Galway  (8644)
201 -- Margit604 Heaney114 (17 y/o F) Tuam, County Galway  (23446)
199 -- Page791 Nobuko304 Bogisich202 (43 y/o F) Tuam, County Galway  (65474)
205 -- Sarita454 Ankunding277 (17 y/o F) Tuam, County Galway  (24550)
200 -- Maximo817 Hyatt152 (45 y/o M) Tuam, County Galway  (66495)
203 -- Federico589 Konopelski743 (31 y/o M) Tuam, County Galway  (45764)
207 -- Love546 Mertz280 (20 y/o F) Tuam, County Galway  (29207)
198 -- Lacy523 Harris789 (54 y/o M) Tuam, County Galway  (79913)
202 -- Manuela585 Susie661 Kihn564 (39 y/o F) Tuam, County Galway  (55967)
196 -- Rita460 Shields502 (41 y/o F) Tuam, County Galway  (61643)
208 -- Wes853 Koepp521 (5 y/o M) Tuam, County Galway  (8044)
125 -- Chadwick722 Cartwright189 (47 y/o M) Tuam, County Galway DECEASED (65403)
206 -- Ruben688 Jones311 (55 y/o M) Tuam, County Galway  (79401)
212 -- Keiko299 Ankunding277 (26 y/o F) Tuam, County Galway  (37802)
216 -- Tarsha65 Jakubowski832 (9 y/o F) Tuam, County Galway  (12897)
176 -- Daron260 Mante251 (74 y/o M) Tuam, County Galway  (108553)
217 -- Hai304 Rowe323 (17 y/o M) Tuam, County Galway  (23369)
153 -- Noe500 Farrell962 (53 y/o M) Tuam, County Galway  (74031)
152 -- Gary33 Sanford861 (73 y/o M) Tuam, County Galway  (105983)
219 -- Lucila204 Keeling57 (2 y/o F) Tuam, County Galway  (3951)
209 -- Jerome176 Kessler503 (64 y/o M) Tuam, County Galway  (95908)
220 -- Jarrett354 Paucek755 (2 y/o M) Tuam, County Galway  (3676)
213 -- Ardis509 Goodwin327 (43 y/o F) Tuam, County Galway  (63432)
214 -- Miguel815 Friesen796 (56 y/o M) Tuam, County Galway  (82789)
211 -- Mel236 Kshlerin58 (34 y/o M) Tuam, County Galway  (47851)
215 -- Willian804 Kautzer186 (76 y/o M) Tuam, County Galway  (107104)
189 -- Corrina72 Brittni468 Goldner995 (101 y/o F) Tuam, County Galway  (151869)
218 -- Chad48 Pacocha935 (40 y/o M) Tuam, County Galway  (55727)
230 -- Chad48 Tillman293 (13 y/o M) Tuam, County Galway  (19476)
229 -- King743 Cormier289 (35 y/o M) Tuam, County Galway  (50753)
210 -- Eric487 Olson653 (51 y/o M) Tuam, County Galway  (77644)
25 -- Jason347 Lehner980 (101 y/o F) Tuam, County Galway  (191429)
222 -- Rey54 Douglas31 (67 y/o M) Tuam, County Galway  (97329)
228 -- Beaulah36 Kerluke267 (34 y/o F) Tuam, County Galway  (47606)
224 -- Elton404 Graham902 (56 y/o M) Tuam, County Galway  (81712)
227 -- Liz413 Kling921 (63 y/o F) Tuam, County Galway  (91150)
226 -- Tessie155 Block661 (43 y/o F) Tuam, County Galway DECEASED (63886)
223 -- Van763 Azzie965 Larson43 (66 y/o F) Tuam, County Galway  (96102)
221 -- Denny560 Hayes766 (77 y/o M) Tuam, County Galway  (111680)
234 -- Pat3 Baumbach677 (9 y/o M) Tuam, County Galway  (13743)
191 -- Marcelo725 Rosenbaum794 (87 y/o M) Tuam, County Galway  (128339)
238 -- Anisa442 Krajcik437 (8 y/o F) Tuam, County Galway  (11993)
231 -- Golden321 Ferry570 (47 y/o F) Tuam, County Galway  (67263)
225 -- Milo271 Lubowitz58 (78 y/o M) Tuam, County Galway  (118858)
236 -- Altha90 Considine820 (22 y/o F) Tuam, County Galway  (32105)
242 -- Conchita9 Carter549 (4 y/o F) Tuam, County Galway  (7270)
237 -- Lona294 Violette536 Stehr398 (29 y/o F) Tuam, County Galway  (42812)
241 -- Cyril535 Zboncak558 (14 y/o M) Tuam, County Galway  (19418)
239 -- Theresia791 Bode78 (22 y/o F) Tuam, County Galway  (30655)
247 -- Lyndon118 Gutkowski940 (15 y/o M) Tuam, County Galway  (20729)
246 -- Trevor374 Gerlach374 (15 y/o M) Tuam, County Galway  (21372)
245 -- Andres25 Predovic534 (20 y/o M) Tuam, County Galway  (28697)
233 -- Kindra525 Carlyn477 Kiehn525 (49 y/o F) Tuam, County Galway  (86578)
232 -- Amos720 Ratke343 (67 y/o M) Tuam, County Galway  (93384)
243 -- Hayley136 Blanda868 (23 y/o F) Tuam, County Galway  (34484)
252 -- Marvella276 Kling921 (9 y/o F) Tuam, County Galway  (12910)
240 -- Rene434 Kuhn96 (55 y/o M) Tuam, County Galway  (77210)
251 -- Ken316 Koss676 (21 y/o M) Tuam, County Galway DECEASED (29460)
125 -- Jesus702 Mayert710 (74 y/o M) Tuam, County Galway  (108635)
244 -- Ramiro608 Schmidt332 (42 y/o M) Tuam, County Galway  (59802)
235 -- Bryant814 Kozey370 (63 y/o M) Tuam, County Galway  (93912)
250 -- Wilbur107 Johnson679 (40 y/o M) Tuam, County Galway  (58495)
248 -- Vickie113 Toshiko149 Bosco882 (43 y/o F) Tuam, County Galway  (64138)
251 -- Antoine384 Haag279 (24 y/o M) Tuam, County Galway  (35524)
255 -- Janis361 Sanford861 (38 y/o F) Tuam, County Galway  (55434)
253 -- Greg949 Bartoletti50 (61 y/o M) Tuam, County Galway  (88088)
249 -- Shantay950 Nicola388 Jast432 (48 y/o F) Tuam, County Galway  (68392)
259 -- Heath320 Cummings51 (35 y/o M) Tuam, County Galway  (50261)
263 -- Caroline183 Rice937 (22 y/o F) Tuam, County Galway  (31564)
254 -- Tommye961 Muriel394 Cormier289 (55 y/o F) Tuam, County Galway  (82446)
265 -- Tyrell880 Macejkovic424 (3 y/o M) Tuam, County Galway  (5227)
264 -- Brett333 Schmitt836 (11 y/o M) Tuam, County Galway  (15814)
256 -- Iva908 Danica886 Ullrich385 (61 y/o F) Tuam, County Galway  (93534)
257 -- Reita211 Mayert710 (58 y/o F) Tuam, County Galway DECEASED (86336)
266 -- Jena102 Breitenberg711 (18 y/o F) Tuam, County Galway  (26517)
272 -- Bill567 Ondricka197 (15 y/o M) Tuam, County Galway  (21867)
226 -- Patty600 Drema139 Murray856 (79 y/o F) Tuam, County Galway  (114761)
262 -- Rolanda823 Shannon293 Gleason633 (37 y/o F) Tuam, County Galway  (54128)
258 -- Marion502 Oberbrunner298 (68 y/o M) Tuam, County Galway  (98379)
269 -- Jacinto644 Klocko335 (17 y/o M) Tuam, County Galway  (23655)
261 -- Cherly215 Bayer639 (52 y/o F) Tuam, County Galway  (74674)
260 -- Kiyoko456 Kozey370 (53 y/o F) Tuam, County Galway  (76751)
274 -- Ima629 Gislason620 (13 y/o F) Tuam, County Galway  (18599)
270 -- Sherron201 Dickinson688 (22 y/o F) Tuam, County Galway  (31998)
267 -- Harriett813 Kimbery217 Reynolds644 (53 y/o F) Tuam, County Galway  (80050)
280 -- Colby655 Gerhold939 (14 y/o M) Tuam, County Galway  (19671)
277 -- Fausto876 Hodkiewicz467 (19 y/o M) Tuam, County Galway  (28097)
281 -- Milagro117 Dickens475 (7 y/o F) Tuam, County Galway  (10370)
271 -- Reuben327 Hane680 (55 y/o M) Tuam, County Galway  (76048)
276 -- Nickolas58 Zulauf375 (52 y/o M) Tuam, County Galway DECEASED (74713)
278 -- Euna523 Ward668 (35 y/o F) Tuam, County Galway  (50469)
282 -- Brandon214 Carroll471 (17 y/o F) Tuam, County Galway  (24287)
268 -- Hyun970 Gretta175 Boyle917 (74 y/o F) Tuam, County Galway  (111883)
283 -- Garrett899 O'Kon634 (22 y/o M) Tuam, County Galway  (31637)
287 -- Dan465 Hilll811 (7 y/o M) Tuam, County Galway  (10478)
286 -- Merrill415 Hansen121 (12 y/o M) Tuam, County Galway DECEASED (16918)
279 -- Johanne551 Mariko625 Streich926 (44 y/o F) Tuam, County Galway  (95252)
273 -- Suzann567 Moore224 (68 y/o F) Tuam, County Galway  (97114)
257 -- Bella510 Jacobs452 (27 y/o F) Tuam, County Galway DECEASED (39185)
285 -- Myra819 Danna372 Thompson596 (38 y/o F) Tuam, County Galway  (57626)
290 -- Dominick530 Abshire638 (17 y/o M) Tuam, County Galway  (24382)
275 -- Barrett790 Quitzon246 (58 y/o M) Tuam, County Galway  (88163)
292 -- Valentin929 Leannon79 (37 y/o M) Tuam, County Galway  (55476)
284 -- Rocco842 Jones311 (52 y/o M) Tuam, County Galway  (74549)
296 -- Shu104 Gutkowski940 (25 y/o F) Tuam, County Galway  (37512)
289 -- Denise470 Stamm704 (44 y/o F) Tuam, County Galway  (63691)
297 -- Emanuel231 Hoppe518 (12 y/o M) Tuam, County Galway  (17242)
301 -- Blanca837 Grant908 (11 y/o F) Tuam, County Galway  (15902)
305 -- Elisabeth967 Kuhlman484 (1 y/o F) Tuam, County Galway  (1788)
303 -- Verdie59 Ernser583 (10 y/o F) Tuam, County Galway  (13913)
294 -- Marco578 Reichert620 (73 y/o M) Tuam, County Galway  (105937)
276 -- Tyrell880 Hauck852 (73 y/o M) Tuam, County Galway  (105786)
309 -- Armando772 Cormier289 (8 y/o M) Tuam, County Galway  (10733)
306 -- Antonio44 Wunsch504 (12 y/o M) Tuam, County Galway  (17112)
293 -- Corrina72 Ivonne773 Labadie908 (65 y/o F) Tuam, County Galway  (97368)
291 -- Francisca486 Simonis280 (49 y/o F) Tuam, County Galway  (71495)
288 -- Ahmad985 Hane680 (54 y/o M) Tuam, County Galway  (79118)
302 -- Ezra452 Spinka232 (44 y/o M) Tuam, County Galway  (63871)
312 -- Cheri871 Jacobi462 (18 y/o F) Tuam, County Galway  (26085)
299 -- Tiara667 Janelle257 Will178 (80 y/o F) Tuam, County Galway  (119033)
304 -- Junior695 Kessler503 (55 y/o M) Tuam, County Galway  (76168)
317 -- Carlee848 O'Reilly797 (0 y/o F) Tuam, County Galway  (1309)
286 -- Ty725 Jacobs452 (46 y/o M) Tuam, County Galway  (63893)
307 -- Burl285 Johnston597 (46 y/o M) Tuam, County Galway  (63913)
257 -- Wanda961 Langosh790 (79 y/o F) Tuam, County Galway  (118570)
313 -- Tanner110 Lindgren255 (15 y/o M) Tuam, County Galway  (22346)
316 -- Debbra216 Sanford861 (2 y/o F) Tuam, County Galway  (4017)
300 -- Emeline473 Pamelia915 Hand679 (46 y/o F) Tuam, County Galway  (67944)
298 -- Dania217 Shaun461 Hoeger474 (50 y/o F) Tuam, County Galway  (76738)
295 -- Ellamae709 Christinia886 Kihn564 (71 y/o F) Tuam, County Galway  (108084)
315 -- Lynwood354 Gusikowski974 (35 y/o M) Tuam, County Galway  (49592)
320 -- Santina680 Moen819 (17 y/o F) Tuam, County Galway  (24929)
322 -- Rupert654 Bradtke547 (16 y/o M) Tuam, County Galway  (22706)
308 -- Noreen211 Regan713 Kunde533 (71 y/o F) Tuam, County Galway  (105318)
311 -- Cecil300 Turcotte120 (71 y/o M) Tuam, County Galway  (101636)
326 -- Zenia843 Swift555 (5 y/o F) Tuam, County Galway  (7771)
328 -- Joye57 Zboncak558 (11 y/o F) Tuam, County Galway  (15776)
323 -- Nichole96 Sharee66 Senger904 (29 y/o F) Tuam, County Galway  (41936)
310 -- Donald774 Homenick806 (72 y/o M) Tuam, County Galway  (103114)
314 -- Frances376 Sporer811 (46 y/o M) Tuam, County Galway  (71848)
319 -- Mario764 Fadel536 (48 y/o M) Tuam, County Galway  (72187)
329 -- Arden380 Jenkins714 (26 y/o M) Tuam, County Galway  (37261)
324 -- Argentina169 Dayle885 Lockman863 (38 y/o F) Tuam, County Galway  (55642)
336 -- Peter292 Herzog843 (2 y/o M) Tuam, County Galway  (4441)
339 -- Tressie547 Bahringer146 (3 y/o F) Tuam, County Galway  (5578)
332 -- Sabra779 Purdy2 (8 y/o F) Tuam, County Galway  (12933)
338 -- Madelyn308 Abernathy524 (4 y/o F) Tuam, County Galway  (18264)
337 -- Marylouise236 Schaden604 (9 y/o F) Tuam, County Galway  (13837)
321 -- Rueben647 Stark857 (55 y/o M) Tuam, County Galway  (77373)
333 -- Brigette230 Paulina892 Hilll811 (39 y/o F) Tuam, County Galway  (58342)
344 -- Steve819 Cummings51 (2 y/o M) Tuam, County Galway  (3865)
345 -- Clyde817 Morar593 (9 y/o M) Tuam, County Galway  (13205)
341 -- Milan77 Hackett68 (25 y/o M) Tuam, County Galway  (35446)
334 -- Carter549 Ledner144 (56 y/o M) Tuam, County Galway  (78056)
330 -- Jung484 Rippin620 (74 y/o F) Tuam, County Galway  (106828)
325 -- Gilbert263 Schuppe920 (59 y/o M) Tuam, County Galway  (83231)
318 -- Andy346 Spinka232 (73 y/o M) Tuam, County Galway  (103764)
335 -- Daryl568 Leannon79 (51 y/o M) Tuam, County Galway DECEASED (76725)
327 -- Samira471 Leeanna836 Carroll471 (75 y/o F) Tuam, County Galway  (117653)
350 -- Douglas31 Conroy74 (14 y/o M) Tuam, County Galway  (19378)
331 -- Alphonso102 Lemke654 (46 y/o M) Tuam, County Galway  (70330)
342 -- Mary779 Feil794 (49 y/o M) Tuam, County Galway  (67783)
347 -- Francis500 Emard19 (39 y/o M) Tuam, County Galway  (53758)
349 -- Tonya123 Boyle917 (18 y/o F) Tuam, County Galway  (27506)
355 -- Mariella503 Johnston597 (15 y/o F) Tuam, County Galway  (22031)
340 -- Mariano761 McDermott739 (50 y/o M) Tuam, County Galway DECEASED (71826)
351 -- Awilda854 Schneider199 (41 y/o F) Tuam, County Galway  (60283)
343 -- Eloisa55 Lieselotte680 Schowalter414 (56 y/o F) Tuam, County Galway  (113159)
352 -- Alesia841 Lawana430 Effertz744 (36 y/o F) Tuam, County Galway  (51510)
356 -- Carlton317 Rodriguez71 (41 y/o M) Tuam, County Galway  (57915)
357 -- Inez706 Debbi640 Cummerata161 (31 y/o F) Tuam, County Galway  (44397)
363 -- Marylin690 Crona259 (14 y/o F) Tuam, County Galway  (20500)
359 -- Benita195 Joanie498 Hansen121 (42 y/o F) Tuam, County Galway  (58902)
348 -- Bernie827 Ebert178 (53 y/o M) Tuam, County Galway DECEASED (77395)
365 -- Jordon466 Krajcik437 (7 y/o M) Tuam, County Galway  (11001)
364 -- Alfonzo975 Stracke611 (27 y/o M) Tuam, County Galway  (37705)
360 -- Werner409 Hilpert278 (31 y/o M) Tuam, County Galway  (42695)
361 -- Stefan297 Schiller186 (39 y/o M) Tuam, County Galway  (53471)
346 -- Rhea34 Thea616 Fadel536 (68 y/o F) Tuam, County Galway  (97853)
358 -- Junior695 Gutkowski940 (68 y/o M) Tuam, County Galway  (100290)
353 -- Duane703 McClure239 (78 y/o M) Tuam, County Galway  (142729)
354 -- Ezekiel373 Feest103 (60 y/o M) Tuam, County Galway  (87928)
367 -- Rachell479 Marlena558 Kuvalis369 (38 y/o F) Tuam, County Galway  (56253)
375 -- Zelma45 Fay398 (15 y/o F) Tuam, County Galway  (22529)
373 -- Nathanial472 Bartoletti50 (29 y/o M) Tuam, County Galway  (40122)
335 -- Ronald408 Kautzer186 (59 y/o M) Tuam, County Galway  (84963)
374 -- Elijah719 Reinger292 (32 y/o M) Tuam, County Galway  (46537)
372 -- Delores12 Kiley170 Huel628 (37 y/o F) Tuam, County Galway DECEASED (54059)
340 -- Ernesto186 Schmitt836 (57 y/o M) Tuam, County Galway DECEASED (81362)
381 -- Deedee112 Howell947 (0 y/o F) Tuam, County Galway  (1138)
366 -- Glenda787 Vernie449 Wintheiser220 (67 y/o F) Tuam, County Galway  (114054)
370 -- Hai304 Wunsch504 (65 y/o M) Tuam, County Galway  (95062)
371 -- Demetria799 Ariana988 Berge125 (62 y/o F) Tuam, County Galway  (87819)
380 -- Lanita675 Jerde200 (17 y/o F) Tuam, County Galway  (24431)
368 -- Donny470 White193 (68 y/o M) Tuam, County Galway  (143653)
377 -- Morgan564 Hettinger594 (34 y/o M) Tuam, County Galway  (47593)
362 -- August363 Gorczany269 (76 y/o M) Tuam, County Galway  (112688)
369 -- Cleo27 Benita195 Wintheiser220 (59 y/o F) Tuam, County Galway  (91263)
378 -- Ryan260 Bernier607 (44 y/o M) Tuam, County Galway  (61936)
376 -- Arminda86 Nell215 Ernser583 (63 y/o F) Tuam, County Galway  (95041)
388 -- Dianna917 Carroll471 (7 y/o F) Tuam, County Galway  (9818)
348 -- Caleb651 Greenholt190 (55 y/o M) Tuam, County Galway  (82198)
379 -- Jazmine498 Crysta430 Wiegand701 (57 y/o F) Tuam, County Galway DECEASED (85189)
382 -- Nelson403 Weimann465 (34 y/o M) Tuam, County Galway  (48085)
386 -- Elenor843 Arcelia945 Feest103 (52 y/o F) Tuam, County Galway  (74955)
389 -- Jerrie417 Hoppe518 (27 y/o F) Tuam, County Galway  (38158)
384 -- Evelia928 Will178 (77 y/o F) Tuam, County Galway  (110995)
385 -- Gaylord332 Kuhlman484 (58 y/o M) Tuam, County Galway DECEASED (136428)
390 -- Noe500 Klocko335 (35 y/o M) Tuam, County Galway  (49962)
392 -- Norbert530 Ullrich385 (32 y/o M) Tuam, County Galway  (45183)
383 -- Deetta949 Missy373 Lehner980 (80 y/o F) Tuam, County Galway  (119519)
387 -- Elease461 Hui924 Corkery305 (82 y/o F) Tuam, County Galway  (124093)
393 -- Trinidad33 Hyatt152 (35 y/o F) Tuam, County Galway DECEASED (51987)
372 -- Jenny686 Breann988 Ward668 (53 y/o F) Tuam, County Galway  (78570)
340 -- Rogelio17 Konopelski743 (49 y/o M) Tuam, County Galway DECEASED (70552)
397 -- Milford485 Mayer370 (31 y/o M) Tuam, County Galway  (44607)
379 -- Cori307 Narcisa997 Schaden604 (52 y/o F) Tuam, County Galway DECEASED (74429)
400 -- Lou594 Graham902 (32 y/o M) Tuam, County Galway  (44430)
404 -- Bernardine460 Hickle134 (18 y/o F) Tuam, County Galway  (25970)
391 -- Elene949 Mildred587 Kuphal363 (65 y/o F) Tuam, County Galway DECEASED (120142)
396 -- Kathi607 Fritsch593 (48 y/o F) Tuam, County Galway  (68193)
395 -- Morris740 Raynor401 (54 y/o M) Tuam, County Galway  (84385)
398 -- Herta650 O'Keefe54 (44 y/o F) Tuam, County Galway  (64189)
402 -- Terrance440 Wyman904 (41 y/o M) Tuam, County Galway  (56639)
401 -- Micheal721 McCullough561 (31 y/o M) Tuam, County Galway  (43346)
403 -- Carrol931 Franecki195 (43 y/o M) Tuam, County Galway  (59043)
408 -- Joseph689 Wisozk929 (5 y/o M) Tuam, County Galway  (8735)
394 -- Francisco472 Thiel172 (76 y/o M) Tuam, County Galway  (111144)
399 -- Johnie961 Rempel203 (63 y/o M) Tuam, County Galway DECEASED (90637)
413 -- Wilson960 Emard19 (4 y/o M) Tuam, County Galway  (6998)
409 -- Scottie437 Wiza601 (36 y/o M) Tuam, County Galway  (51691)
405 -- Hans694 Pfeffer420 (47 y/o M) Tuam, County Galway DECEASED (67015)
407 -- Caroline183 Birgit199 Weimann465 (35 y/o F) Tuam, County Galway  (53479)
415 -- Santos184 Watsica258 (17 y/o M) Tuam, County Galway  (24150)
410 -- Aleen595 Dietrich576 (29 y/o F) Tuam, County Galway  (41341)
420 -- Teodoro374 Goyette777 (8 y/o M) Tuam, County Galway  (11873)
379 -- Lyndia317 Martina386 Douglas31 (72 y/o F) Tuam, County Galway  (105994)
411 -- Fairy757 Shanelle862 Rempel203 (32 y/o F) Tuam, County Galway  (50295)
417 -- Fabian647 Funk324 (26 y/o M) Tuam, County Galway  (39407)
419 -- Lena684 Cruickshank494 (22 y/o F) Tuam, County Galway  (30973)
416 -- Stanford577 Weimann465 (65 y/o M) Tuam, County Galway  (92616)
414 -- Randi364 Marta91 Hudson301 (48 y/o F) Tuam, County Galway  (66792)
340 -- Brooks264 Pouros728 (64 y/o M) Tuam, County Galway  (95780)
418 -- Reynaldo722 Cartwright189 (49 y/o M) Tuam, County Galway DECEASED (73566)
421 -- Steve819 Bosco882 (38 y/o M) Tuam, County Galway DECEASED (54736)
412 -- Cyril535 Miller503 (58 y/o M) Tuam, County Galway  (84552)
405 -- Steven797 Koss676 (55 y/o M) Tuam, County Galway DECEASED (77312)
393 -- Jamika47 Adams676 (83 y/o F) Tuam, County Galway  (122716)
399 -- Harrison106 Bergstrom287 (67 y/o M) Tuam, County Galway  (100251)
427 -- Kenisha791 Collier206 (12 y/o F) Tuam, County Galway  (17033)
424 -- Tawnya388 Emard19 (44 y/o F) Tuam, County Galway  (62755)
430 -- Pura348 Welch179 (5 y/o F) Tuam, County Galway  (7938)
406 -- Wilburn655 Corwin846 (83 y/o M) Tuam, County Galway DECEASED (180691)
423 -- Lowell343 Bins636 (74 y/o M) Tuam, County Galway  (105498)
422 -- Francis500 Von197 (66 y/o M) Tuam, County Galway  (94025)
429 -- Bethanie176 Ullrich385 (51 y/o F) Tuam, County Galway  (73275)
421 -- Delmer311 Mann644 (34 y/o M) Tuam, County Galway DECEASED (51055)
426 -- Trudy596 Fritsch593 (45 y/o F) Tuam, County Galway  (65636)
431 -- Serina556 Marquardt819 (54 y/o F) Tuam, County Galway  (81205)
428 -- Mohammed454 Hermiston71 (63 y/o M) Tuam, County Galway  (90003)
433 -- Gwyn381 Ziemann98 (39 y/o F) Tuam, County Galway  (56201)
434 -- Migdalia164 Kuphal363 (19 y/o F) Tuam, County Galway  (26727)
418 -- Ellsworth48 Watsica258 (69 y/o M) Tuam, County Galway DECEASED (97962)
425 -- Kristeen693 Mariann762 Reinger292 (88 y/o F) Tuam, County Galway DECEASED (130307)
440 -- Elly836 Smith67 (15 y/o F) Tuam, County Galway  (21723)
437 -- Malinda718 Ora550 Mraz590 (39 y/o F) Tuam, County Galway  (55783)
446 -- Dawn804 Ryan260 (5 y/o F) Tuam, County Galway  (8589)
432 -- Johnsie484 Elia719 Runte676 (48 y/o F) Tuam, County Galway  (71692)
439 -- Zachary28 Upton904 (44 y/o M) Tuam, County Galway  (63636)
436 -- Carletta836 Littel644 (54 y/o F) Tuam, County Galway  (79437)
438 -- Kip442 Olson653 (67 y/o M) Tuam, County Galway  (95255)
421 -- Osvaldo336 Muller251 (42 y/o M) Tuam, County Galway  (61126)
448 -- Rossana121 Hand679 (3 y/o F) Tuam, County Galway  (5233)
405 -- Harley673 Hintz995 (73 y/o M) Tuam, County Galway DECEASED (134199)
391 -- Detra426 Moira454 Parker433 (77 y/o F) Tuam, County Galway  (110729)
444 -- Buena501 Weber641 (22 y/o F) Tuam, County Galway  (31354)
441 -- Jack927 Pfannerstill264 (51 y/o M) Tuam, County Galway  (72988)
445 -- Carmelo33 Champlin946 (40 y/o M) Tuam, County Galway  (57814)
443 -- Rick943 Batz141 (40 y/o M) Tuam, County Galway  (56497)
450 -- Antonietta855 Kreiger457 (16 y/o F) Tuam, County Galway  (23644)
442 -- Shawnna218 Joelle163 Weimann465 (60 y/o F) Tuam, County Galway  (87120)
458 -- Jewel43 Schneider199 (2 y/o M) Tuam, County Galway DECEASED (3303)
451 -- Rod343 Becker968 (31 y/o M) Tuam, County Galway  (44160)
418 -- Silas208 Kling921 (74 y/o M) Tuam, County Galway  (114332)
458 -- Sandy901 Herman763 (9 y/o M) Tuam, County Galway  (12475)
453 -- Ira784 Ratke343 (30 y/o M) Tuam, County Galway  (41656)
460 -- Stevie682 Hermiston71 (15 y/o F) Tuam, County Galway  (21102)
456 -- Sharice315 Hodkiewicz467 (27 y/o F) Tuam, County Galway  (38408)
457 -- Booker670 Mertz280 (27 y/o M) Tuam, County Galway  (40214)
447 -- Salvador46 Hilpert278 (82 y/o M) Tuam, County Galway DECEASED (119108)
455 -- Terica746 Torp761 (39 y/o F) Tuam, County Galway  (56554)
435 -- Taylor21 Blanda868 (110 y/o M) Tuam, County Galway  (156921)
449 -- Tressie547 Schiller186 (76 y/o F) Tuam, County Galway  (111837)
452 -- Jonathan639 Botsford977 (68 y/o M) Tuam, County Galway  (98850)
466 -- Randal152 Hoppe518 (4 y/o M) Tuam, County Galway  (6767)
454 -- Cory323 Stroman228 (60 y/o M) Tuam, County Galway  (88398)
465 -- Dotty422 Hettinger594 (20 y/o F) Tuam, County Galway  (29123)
425 -- Jerlene697 Beverly445 Schaden604 (97 y/o F) Tuam, County Galway  (142856)
463 -- Classie132 Lind531 (28 y/o F) Tuam, County Galway  (40936)
459 -- Marcel580 Goldner995 (70 y/o M) Tuam, County Galway  (99383)
472 -- Frederic454 Mosciski958 (3 y/o M) Tuam, County Galway  (4981)
473 -- Belle514 Carter549 (6 y/o F) Tuam, County Galway  (9596)
461 -- Lowell343 Hickle134 (59 y/o M) Tuam, County Galway  (82849)
406 -- Billy698 Blick895 (82 y/o M) Tuam, County Galway DECEASED (117733)
469 -- Aaron697 Bode78 (41 y/o M) Tuam, County Galway  (57800)
467 -- Kendall673 McClure239 (53 y/o M) Tuam, County Galway DECEASED (78337)
464 -- Kristina583 Trinh357 Ondricka197 (40 y/o F) Tuam, County Galway  (57999)
462 -- Todd315 Fisher429 (73 y/o M) Tuam, County Galway  (124975)
478 -- Filiberto722 Huels583 (20 y/o M) Tuam, County Galway  (28316)
480 -- Clementine778 Lynch190 (12 y/o F) Tuam, County Galway  (17299)
471 -- Marguerita493 Lea264 Kshlerin58 (43 y/o F) Tuam, County Galway DECEASED (92179)
476 -- Roberto515 Leffler128 (36 y/o M) Tuam, County Galway  (53716)
483 -- Myrtie622 Dickens475 (7 y/o F) Tuam, County Galway  (9988)
470 -- Johnathon489 Sporer811 (51 y/o M) Tuam, County Galway  (76301)
468 -- Gary33 Alida395 Barton704 (53 y/o F) Tuam, County Galway  (79722)
486 -- Donn979 Cruickshank494 (3 y/o M) Tuam, County Galway  (5558)
477 -- Jack927 Aimee901 Bechtelar572 (54 y/o F) Tuam, County Galway  (78551)
487 -- Houston994 Kautzer186 (4 y/o M) Tuam, County Galway  (6816)
481 -- Emmitt44 Bashirian201 (58 y/o M) Tuam, County Galway  (83104)
474 -- Andreas188 Altenwerth646 (81 y/o M) Tuam, County Galway  (116637)
475 -- Joe656 Kohler843 (59 y/o M) Tuam, County Galway  (85720)
479 -- Casie505 Gertha313 Reinger292 (51 y/o F) Tuam, County Galway  (73782)
490 -- Johnny786 Raynor401 (15 y/o M) Tuam, County Galway  (21101)
447 -- Shirley182 Hamill307 (62 y/o M) Tuam, County Galway DECEASED (112163)
485 -- Shantay950 Valrie435 Tremblay80 (53 y/o F) Tuam, County Galway  (75597)
385 -- Lamont867 Lakin515 (66 y/o M) Tuam, County Galway  (97603)
467 -- Scottie437 Gorczany269 (54 y/o M) Tuam, County Galway DECEASED (76752)
492 -- Tommie457 Glover433 (2 y/o F) Tuam, County Galway  (4150)
496 -- Antione404 Mraz590 (3 y/o M) Tuam, County Galway  (5216)
484 -- Lincoln623 West559 (58 y/o M) Tuam, County Galway  (83552)
495 -- Rory188 King743 (4 y/o F) Tuam, County Galway  (6418)
489 -- Janet238 Jenkins714 (51 y/o F) Tuam, County Galway  (75362)
493 -- Owen89 DuBuque211 (16 y/o M) Tuam, County Galway  (23477)
497 -- Josh874 Legros616 (11 y/o M) Tuam, County Galway  (15361)
482 -- Kurt412 Welch179 (57 y/o M) Tuam, County Galway DECEASED (86906)
498 -- Joseph689 Olson653 (12 y/o F) Tuam, County Galway  (16728)
494 -- Cleotilde229 Mistie167 Reichert620 (45 y/o F) Tuam, County Galway  (63288)
506 -- Nancee600 Ratke343 (0 y/o F) Tuam, County Galway  (650)
488 -- Adriene242 Gisela897 Paucek755 (74 y/o F) Tuam, County Galway  (109430)
491 -- Jean712 Jacobi462 (56 y/o M) Tuam, County Galway  (81477)
503 -- Donald774 Howell947 (39 y/o M) Tuam, County Galway  (61655)
502 -- Demetrius568 Krystin400 Cruickshank494 (44 y/o F) Tuam, County Galway  (61474)
507 -- Albert312 Wiza601 (28 y/o F) Tuam, County Galway  (42745)
504 -- Hubert238 Russel238 (23 y/o M) Tuam, County Galway  (33160)
508 -- Leonila462 Micki733 Casper496 (39 y/o F) Tuam, County Galway  (55151)
501 -- Kirby843 Skiles927 (22 y/o M) Tuam, County Galway  (31261)
406 -- Rudolf736 Rodriguez71 (84 y/o M) Tuam, County Galway DECEASED (126761)
500 -- Edna186 Schimmel440 (31 y/o F) Tuam, County Galway  (45496)
509 -- Rudolph554 Schmidt332 (54 y/o M) Tuam, County Galway  (75960)
510 -- Herminia75 Reginia455 Bernier607 (29 y/o F) Tuam, County Galway DECEASED (43814)
499 -- Merrill415 Mohr916 (43 y/o M) Tuam, County Galway  (65611)
467 -- Nicolas769 Pfeffer420 (80 y/o M) Tuam, County Galway  (117375)
505 -- Kristeen693 Jacobi462 (76 y/o F) Tuam, County Galway  (118187)
513 -- Randolph418 Corwin846 (34 y/o M) Tuam, County Galway  (47332)
405 -- Ervin886 Bergstrom287 (44 y/o M) Tuam, County Galway DECEASED (63832)
518 -- Dionna991 Langworth352 (16 y/o F) Tuam, County Galway  (24509)
512 -- Cory323 Ankunding277 (51 y/o M) Tuam, County Galway  (98344)
515 -- Craig656 Willms744 (33 y/o M) Tuam, County Galway  (45216)
516 -- Maurice742 Weber641 (51 y/o M) Tuam, County Galway  (73665)
524 -- Richard937 Hahn503 (24 y/o M) Tuam, County Galway  (32947)
522 -- Lucas404 Labadie908 (18 y/o M) Tuam, County Galway  (25539)
511 -- Leon728 Nicolas769 (78 y/o M) Tuam, County Galway  (113532)
525 -- Dusty207 Yundt842 (2 y/o F) Tuam, County Galway  (3524)
517 -- Alfreda3 Rasheeda241 Kling921 (55 y/o F) Tuam, County Galway  (77357)
519 -- Damien170 Heidenreich818 (39 y/o M) Tuam, County Galway  (55773)
523 -- Eliseo499 Boyer713 (51 y/o M) Tuam, County Galway  (72899)
514 -- Evelina828 O'Conner199 (61 y/o F) Tuam, County Galway  (87080)
520 -- Neda956 Jast432 (74 y/o F) Tuam, County Galway  (108077)
510 -- Yuonne878 Nana422 Kautzer186 (33 y/o F) Tuam, County Galway  (47614)
521 -- Cherlyn665 Considine820 (61 y/o F) Tuam, County Galway  (89015)
529 -- Chase54 Gutmann970 (27 y/o M) Tuam, County Galway  (39327)
482 -- Sebastian508 Tremblay80 (64 y/o M) Tuam, County Galway  (96426)
526 -- Raphael767 Jast432 (58 y/o M) Tuam, County Galway  (82623)
536 -- Lonnie913 Schulist381 (10 y/o M) Tuam, County Galway  (14533)
528 -- Bert917 Runte676 (58 y/o M) Tuam, County Galway  (82445)
533 -- Malcolm243 Pollich983 (41 y/o M) Tuam, County Galway  (57072)
527 -- Dorthea49 Kylee806 Hodkiewicz467 (53 y/o F) Tuam, County Galway  (77895)
539 -- Russell422 Wiegand701 (16 y/o M) Tuam, County Galway DECEASED (23662)
532 -- Vance413 Stanton715 (56 y/o M) Tuam, County Galway  (77494)
537 -- Tyron580 Legros616 (14 y/o M) Tuam, County Galway  (20361)
405 -- Brian582 MacGyver246 (82 y/o M) Tuam, County Galway  (118483)
531 -- Gilberto712 Daniel959 (60 y/o M) Tuam, County Galway  (84195)
534 -- Dwayne786 Kozey370 (65 y/o M) Tuam, County Galway DECEASED (95179)
542 -- Jewel43 Russel238 (44 y/o M) Tuam, County Galway  (61935)
543 -- Gilberto712 Rippin620 (46 y/o M) Tuam, County Galway  (63272)
538 -- Colleen54 Leonia336 Gutkowski940 (65 y/o F) Tuam, County Galway  (93822)
471 -- Pam996 Chong355 Kertzmann286 (48 y/o F) Tuam, County Galway  (68858)
539 -- Cordell41 Feil794 (45 y/o M) Tuam, County Galway  (66443)
549 -- Kenton313 Lehner980 (6 y/o M) Tuam, County Galway  (9072)
544 -- Nelly786 Cummerata161 (51 y/o F) Tuam, County Galway  (75054)
541 -- Nelle766 Fay398 (72 y/o F) Tuam, County Galway  (105926)
530 -- Melissia267 Temple691 O'Hara248 (72 y/o F) Tuam, County Galway  (107842)
406 -- Toney527 Spinka232 (64 y/o M) Tuam, County Galway DECEASED (124726)
547 -- Lillian593 Serena400 McClure239 (32 y/o F) Tuam, County Galway  (46982)
545 -- Vernie449 Alexa171 Wisozk929 (51 y/o F) Tuam, County Galway  (79806)
535 -- Demetria799 Cummings51 (67 y/o F) Tuam, County Galway  (97674)
555 -- Reggie481 Wyman904 (12 y/o M) Tuam, County Galway  (18018)
550 -- Leonel449 Lynch190 (56 y/o M) Tuam, County Galway  (79520)
552 -- Jackeline690 Daniel959 (41 y/o F) Tuam, County Galway DECEASED (58910)
548 -- Erminia669 Talitha643 Collins926 (59 y/o F) Tuam, County Galway  (88211)
540 -- Dori98 Vivien121 Thompson596 (62 y/o F) Tuam, County Galway  (92750)
559 -- Orville751 Bergnaum523 (2 y/o M) Tuam, County Galway  (3664)
546 -- Delmar187 Schmitt836 (53 y/o M) Tuam, County Galway  (74720)
553 -- Thea616 Latanya388 Wunsch504 (47 y/o F) Tuam, County Galway  (69150)
560 -- Filomena215 Koepp521 (12 y/o F) Tuam, County Galway  (17067)
557 -- Jacalyn740 Wintheiser220 (47 y/o F) Tuam, County Galway  (68690)
554 -- Kristofer887 Predovic534 (38 y/o M) Tuam, County Galway  (52633)
558 -- Duncan491 Spencer878 (47 y/o M) Tuam, County Galway  (65742)
534 -- Phil587 Hahn503 (72 y/o M) Tuam, County Galway  (101115)
565 -- Clay913 Tromp100 (18 y/o M) Tuam, County Galway  (25475)
570 -- Neomi684 Blanda868 (4 y/o F) Tuam, County Galway  (5874)
571 -- Trinidad33 Huels583 (8 y/o M) Tuam, County Galway  (11971)
556 -- Edison640 Wilderman619 (63 y/o M) Tuam, County Galway  (113145)
562 -- Vince741 Veum823 (42 y/o M) Tuam, County Galway  (57673)
551 -- Hoa730 Dibbert990 (70 y/o F) Tuam, County Galway  (104586)
561 -- Arianne988 Gayle448 Boyer713 (44 y/o F) Tuam, County Galway  (64790)
567 -- Shanice479 Maire384 Trantow673 (31 y/o F) Tuam, County Galway  (49227)
566 -- Von197 Leffler128 (49 y/o M) Tuam, County Galway  (68023)
563 -- Lucius907 Bauch723 (42 y/o M) Tuam, County Galway  (85002)
568 -- Patrina117 Nanette893 Strosin214 (40 y/o F) Tuam, County Galway  (56790)
569 -- Annie941 Hyon784 Considine820 (42 y/o F) Tuam, County Galway  (63766)
576 -- Jasmin506 Bailey598 (38 y/o F) Tuam, County Galway  (57796)
564 -- Twila243 Lynda214 Rowe323 (47 y/o F) Tuam, County Galway  (108586)
574 -- Wilson960 Grant908 (44 y/o M) Tuam, County Galway  (66581)
580 -- Esther279 Jakubowski832 (28 y/o F) Tuam, County Galway  (41366)
447 -- Demarcus108 Hoppe518 (93 y/o M) Tuam, County Galway DECEASED (276066)
552 -- Alaine226 Pollich983 (100 y/o F) Tuam, County Galway  (145620)
585 -- Evon528 Fisher429 (0 y/o F) Tuam, County Galway  (1358)
578 -- Alonzo487 Gleichner915 (55 y/o M) Tuam, County Galway  (77326)
575 -- Edie35 Fritsch593 (70 y/o F) Tuam, County Galway DECEASED (107172)
584 -- Necole468 Dietrich576 (14 y/o F) Tuam, County Galway  (19808)
582 -- Howard613 Runolfsdottir785 (35 y/o M) Tuam, County Galway  (49667)
573 -- Delbert384 Hackett68 (93 y/o M) Tuam, County Galway  (134110)
589 -- Deeanna316 Barton704 (13 y/o F) Tuam, County Galway DECEASED (18991)
583 -- Emmanuel930 Kshlerin58 (41 y/o M) Tuam, County Galway  (57151)
587 -- Randal152 Lesch175 (30 y/o M) Tuam, County Galway  (41044)
572 -- Newton741 Lang846 (61 y/o M) Tuam, County Galway  (89599)
577 -- Walton167 Flatley871 (77 y/o M) Tuam, County Galway  (110098)
586 -- Eryn994 Kessler503 (45 y/o F) Tuam, County Galway  (64731)
596 -- Theo630 Grant908 (4 y/o M) Tuam, County Galway  (6060)
591 -- Porter490 Marks830 (20 y/o M) Tuam, County Galway  (28739)
595 -- Angel97 Schmeler639 (18 y/o M) Tuam, County Galway  (25928)
594 -- Jann271 VonRueden376 (36 y/o F) Tuam, County Galway  (50335)
589 -- Ghislaine112 Parker433 (13 y/o F) Tuam, County Galway  (19934)
588 -- Alfonso758 Treutel973 (59 y/o M) Tuam, County Galway  (93247)
599 -- Berry486 Lesch175 (14 y/o M) Tuam, County Galway  (20774)
592 -- Quentin28 Russel238 (47 y/o M) Tuam, County Galway  (65150)
590 -- Jordan900 Rath779 (59 y/o M) Tuam, County Galway DECEASED (88711)
593 -- Tammy740 Cruickshank494 (42 y/o F) Tuam, County Galway  (62449)
600 -- Colby655 Erdman779 (48 y/o M) Tuam, County Galway  (68831)
603 -- Laurena366 Jackelyn13 Crona259 (31 y/o F) Tuam, County Galway  (45704)
597 -- Sean831 Oberbrunner298 (72 y/o M) Tuam, County Galway DECEASED (104237)
581 -- Kirsten270 Durgan499 (102 y/o F) Tuam, County Galway  (147288)
602 -- Rosita520 Ashly243 Hayes766 (69 y/o F) Tuam, County Galway  (98156)
606 -- Josef103 Hand679 (50 y/o M) Tuam, County Galway  (72766)
608 -- Morton637 Hintz995 (33 y/o M) Tuam, County Galway  (49141)
598 -- Cathryn51 Mindi87 Walker122 (77 y/o F) Tuam, County Galway  (154987)
575 -- Charis952 Muller251 (75 y/o F) Tuam, County Galway  (109657)
613 -- Roscoe437 Nolan344 (0 y/o M) Tuam, County Galway  (1733)
579 -- Alex454 Osinski784 (100 y/o M) Tuam, County Galway  (192021)
615 -- Idell650 Jacobs452 (0 y/o F) Tuam, County Galway  (1363)
609 -- Carol737 Berge125 (31 y/o M) Tuam, County Galway  (44118)
601 -- Andres25 Ferry570 (61 y/o M) Tuam, County Galway  (86826)
611 -- Talisha682 Ernestine645 Fisher429 (49 y/o F) Tuam, County Galway  (73933)
607 -- Noah480 Runolfsdottir785 (50 y/o M) Tuam, County Galway  (69907)
604 -- Les282 Smitham825 (52 y/o M) Tuam, County Galway  (76570)
612 -- Shonna561 Cruickshank494 (39 y/o F) Tuam, County Galway  (56875)
616 -- Trey250 Littel644 (25 y/o M) Tuam, County Galway  (34698)
610 -- Macy314 Alise864 Torp761 (53 y/o F) Tuam, County Galway  (84073)
620 -- Bruce167 Williamson769 (12 y/o M) Tuam, County Galway  (17542)
622 -- Everett935 Kunze215 (8 y/o M) Tuam, County Galway  (12006)
614 -- Alex454 Dorothea248 Kling921 (64 y/o F) Tuam, County Galway  (98471)
617 -- Fermin479 Kling921 (37 y/o M) Tuam, County Galway  (54883)
605 -- Art115 Wehner319 (71 y/o M) Tuam, County Galway  (111313)
618 -- Magnolia736 Karlyn611 Bogisich202 (59 y/o F) Tuam, County Galway  (86183)
597 -- Rudolph554 Wilkinson796 (77 y/o M) Tuam, County Galway  (112562)
619 -- Lindsay928 Hessel84 (53 y/o M) Tuam, County Galway  (76188)
629 -- Porfirio146 Adams676 (11 y/o M) Tuam, County Galway  (15296)
628 -- Chaya236 Legros616 (25 y/o F) Tuam, County Galway  (35658)
624 -- Kirby843 Pfeffer420 (40 y/o M) Tuam, County Galway  (56700)
590 -- Eugenio846 Mertz280 (80 y/o M) Tuam, County Galway  (209418)
631 -- Deloras136 Kertzmann286 (14 y/o F) Tuam, County Galway  (19494)
627 -- Porsche32 Leila837 Sauer652 (32 y/o F) Tuam, County Galway  (47760)
632 -- Gretchen912 Greenholt190 (18 y/o F) Tuam, County Galway  (25873)
636 -- Katharina121 Strosin214 (11 y/o F) Tuam, County Galway  (16093)
634 -- Cyril535 Howe413 (12 y/o M) Tuam, County Galway  (17353)
621 -- Hal307 Waters156 (74 y/o M) Tuam, County Galway DECEASED (107679)
625 -- Johnathon489 Mohr916 (54 y/o M) Tuam, County Galway  (79154)
641 -- Enoch803 Rohan584 (8 y/o M) Tuam, County Galway  (11446)
623 -- Barney639 Corkery305 (73 y/o M) Tuam, County Galway  (132760)
626 -- Lang846 Annamarie398 King743 (63 y/o F) Tuam, County Galway  (89882)
630 -- Jules135 Harris789 (63 y/o M) Tuam, County Galway  (91742)
639 -- Dick869 Stracke611 (19 y/o M) Tuam, County Galway  (27586)
642 -- Lonna614 Arlena205 Konopelski743 (37 y/o F) Tuam, County Galway  (57341)
645 -- Yasuko490 Pfannerstill264 (14 y/o F) Tuam, County Galway  (19768)
635 -- Charley358 Kshlerin58 (76 y/o M) Tuam, County Galway  (108168)
633 -- Maryland870 Schamberger479 (75 y/o F) Tuam, County Galway  (108397)
644 -- Shantell717 Lane844 Schmidt332 (31 y/o F) Tuam, County Galway  (44439)
637 -- Tenisha328 Krista314 Stark857 (75 y/o F) Tuam, County Galway  (110173)
640 -- Ali918 McClure239 (51 y/o M) Tuam, County Galway  (76466)
651 -- Leonardo412 Upton904 (1 y/o M) Tuam, County Galway  (2444)
652 -- Ezequiel972 Terry864 (4 y/o M) Tuam, County Galway  (6191)
638 -- Keila316 Nelle766 Heidenreich818 (47 y/o F) Tuam, County Galway  (68783)
647 -- Alverta45 Susann104 Cole117 (42 y/o F) Tuam, County Galway  (59195)
650 -- Nicholle822 Bahringer146 (17 y/o F) Tuam, County Galway  (24485)
643 -- Ramiro608 Hammes673 (69 y/o M) Tuam, County Galway  (102124)
660 -- Fredric73 Jast432 (0 y/o M) Tuam, County Galway  (1091)
648 -- Clifford177 Klein929 (22 y/o M) Tuam, County Galway  (31177)
656 -- Stacey209 Abernathy524 (9 y/o F) Tuam, County Galway  (13236)
659 -- Petronila724 Bruen238 (10 y/o F) Tuam, County Galway  (13576)
658 -- Huey641 Hintz995 (8 y/o M) Tuam, County Galway  (11824)
662 -- Verdie59 Gutkowski940 (2 y/o F) Tuam, County Galway  (3472)
657 -- Gayle448 Gleason633 (14 y/o F) Tuam, County Galway  (20224)
649 -- Casey401 Lashawn862 Kautzer186 (37 y/o F) Tuam, County Galway  (56640)
646 -- Shante445 Tajuana20 Mayert710 (33 y/o F) Tuam, County Galway  (48070)
661 -- Colby655 Glover433 (15 y/o M) Tuam, County Galway  (21306)
653 -- Myron933 Schuppe920 (40 y/o M) Tuam, County Galway  (55896)
406 -- Edwardo860 Ortiz186 (84 y/o M) Tuam, County Galway  (119697)
670 -- Teisha100 Wuckert783 (5 y/o F) Tuam, County Galway  (7300)
654 -- Major265 Hilll811 (31 y/o M) Tuam, County Galway  (50572)
666 -- Jaleesa813 Santina680 Hilpert278 (30 y/o F) Tuam, County Galway DECEASED (44885)
663 -- Guadalupe206 Schmidt332 (34 y/o M) Tuam, County Galway  (49439)
655 -- Muoi890 Carmelia328 Crooks415 (64 y/o F) Tuam, County Galway  (92191)
668 -- Stephan15 Rogahn59 (37 y/o M) Tuam, County Galway  (52788)
664 -- Berry486 Hickle134 (67 y/o M) Tuam, County Galway  (98918)
678 -- Wes853 Jaskolski867 (1 y/o M) Tuam, County Galway  (2049)
669 -- Alda400 Stracke611 (49 y/o F) Tuam, County Galway  (72440)
677 -- Allen322 Connelly992 (13 y/o M) Tuam, County Galway  (18979)
674 -- Sheryll569 Champlin946 (43 y/o F) Tuam, County Galway  (61921)
672 -- Mariella503 Rachael540 Osinski784 (48 y/o F) Tuam, County Galway  (72340)
665 -- Francine922 Sueann178 Schuppe920 (63 y/o F) Tuam, County Galway  (102008)
671 -- Mavis612 Donnette259 Hodkiewicz467 (42 y/o F) Tuam, County Galway  (59445)
667 -- Randee35 Goldner995 (53 y/o F) Tuam, County Galway  (76308)
676 -- Lana840 Darline247 Deckow585 (39 y/o F) Tuam, County Galway  (55959)
682 -- Denisha680 Lemke654 (12 y/o F) Tuam, County Galway  (17145)
666 -- Daina567 Hanna456 Buckridge80 (38 y/o F) Tuam, County Galway  (57734)
675 -- Donnie175 Keeling57 (68 y/o M) Tuam, County Galway  (98298)
690 -- Merissa718 Ziemann98 (12 y/o F) Tuam, County Galway  (18483)
692 -- Kiyoko456 Brekke496 (4 y/o F) Tuam, County Galway  (6992)
679 -- Shena75 Barton704 (69 y/o F) Tuam, County Galway  (105410)
685 -- Stepanie29 Angelena945 Witting912 (40 y/o F) Tuam, County Galway  (58801)
683 -- Pasquale620 Monahan736 (58 y/o M) Tuam, County Galway  (92740)
684 -- Josef103 Kris249 (55 y/o M) Tuam, County Galway DECEASED (80452)
694 -- Georgene966 Swaniawski813 (1 y/o F) Tuam, County Galway  (2870)
673 -- Tobias236 Bode78 (69 y/o M) Tuam, County Galway DECEASED (115363)
681 -- Kyle55 Koss676 (68 y/o F) Tuam, County Galway  (97414)
680 -- Phillis443 Luettgen772 (84 y/o F) Tuam, County Galway DECEASED (126020)
687 -- Leigh689 Murray856 (56 y/o M) Tuam, County Galway  (82400)
693 -- Tracy345 Pollich983 (18 y/o M) Tuam, County Galway  (26017)
688 -- Rodrigo242 Kautzer186 (45 y/o M) Tuam, County Galway  (65979)
686 -- Brad867 McLaughlin530 (44 y/o M) Tuam, County Galway DECEASED (64846)
689 -- Talisha682 Kala987 Toy286 (69 y/o F) Tuam, County Galway  (98564)
695 -- Elias404 Cassin499 (29 y/o M) Tuam, County Galway DECEASED (41300)
691 -- Carissa540 Celestina960 Mitchell808 (49 y/o F) Tuam, County Galway  (72205)
698 -- Carman694 Weimann465 (4 y/o F) Tuam, County Galway  (7026)
699 -- Isaac321 Brakus656 (15 y/o M) Tuam, County Galway  (20940)
704 -- Frankie174 Anderson154 (1 y/o M) Tuam, County Galway  (3229)
447 -- Brenton674 Pollich983 (77 y/o M) Tuam, County Galway DECEASED (112231)
706 -- Akiko835 Padberg411 (11 y/o F) Tuam, County Galway  (15105)
621 -- Homer307 Walker122 (108 y/o M) Tuam, County Galway  (225430)
707 -- Jesse626 Bogan287 (17 y/o M) Tuam, County Galway  (25710)
697 -- Jerry654 Hayes766 (39 y/o F) Tuam, County Galway  (54929)
710 -- Marcos263 West559 (0 y/o M) Tuam, County Galway  (451)
711 -- Sang383 Casper496 (3 y/o M) Tuam, County Galway  (5040)
702 -- Brittany443 Kihn564 (40 y/o F) Tuam, County Galway  (57409)
686 -- Felipe97 Von197 (19 y/o M) Tuam, County Galway DECEASED (27323)
705 -- Jude172 Johnson679 (37 y/o M) Tuam, County Galway  (52581)
703 -- Terry864 Hane680 (54 y/o M) Tuam, County Galway  (76577)
701 -- Delbert384 Lueilwitz711 (50 y/o M) Tuam, County Galway  (70176)
695 -- Thomas756 Lindgren255 (50 y/o M) Tuam, County Galway  (71982)
684 -- Dean966 Quigley282 (34 y/o M) Tuam, County Galway DECEASED (48113)
712 -- Jessica140 Sanford861 (25 y/o F) Tuam, County Galway  (34864)
680 -- Matilde468 Nona876 Goyette777 (60 y/o F) Tuam, County Galway DECEASED (85142)
696 -- Cruz300 Reynolds644 (69 y/o F) Tuam, County Galway  (100030)
720 -- Edwardo860 McClure239 (8 y/o M) Tuam, County Galway  (11815)
709 -- Wayne846 Olson653 (62 y/o M) Tuam, County Galway  (91791)
719 -- Dillon740 Grant908 (26 y/o M) Tuam, County Galway  (37793)
708 -- Lindsy319 Kelly223 Hammes673 (50 y/o F) Tuam, County Galway  (70360)
718 -- Dewayne363 Kuhn96 (24 y/o M) Tuam, County Galway  (34948)
713 -- Hue920 Arlette667 Hayes766 (51 y/o F) Tuam, County Galway  (76353)
723 -- Diego848 Romaguera67 (11 y/o M) Tuam, County Galway  (16575)
715 -- Derick144 Tremblay80 (42 y/o M) Tuam, County Galway  (57738)
722 -- Toney527 Schaden604 (25 y/o M) Tuam, County Galway  (35854)
714 -- Humberto482 Robel940 (67 y/o M) Tuam, County Galway  (94422)
716 -- Angela104 Dianne921 Lemke654 (69 y/o F) Tuam, County Galway  (99639)
727 -- Burl285 Schuppe920 (16 y/o M) Tuam, County Galway  (22337)
717 -- Vito638 Hodkiewicz467 (54 y/o M) Tuam, County Galway  (78842)
729 -- Ariel183 Roob72 (2 y/o M) Tuam, County Galway DECEASED (3990)
700 -- Rashad361 Daugherty69 (93 y/o M) Tuam, County Galway  (209030)
725 -- Roni48 Gerry91 Brakus656 (32 y/o F) Tuam, County Galway  (46853)
447 -- Donte636 Towne435 (87 y/o M) Tuam, County Galway DECEASED (129643)
684 -- Leopoldo762 Bashirian201 (65 y/o M) Tuam, County Galway  (94440)
732 -- Roosevelt595 Hansen121 (5 y/o M) Tuam, County Galway  (7437)
721 -- Britni406 Theresa98 Goldner995 (68 y/o F) Tuam, County Galway  (95584)
734 -- Nita296 Harris789 (17 y/o F) Tuam, County Galway  (23961)
728 -- Cleo27 Leannon79 (35 y/o M) Tuam, County Galway  (48934)
735 -- Tiara667 Shirly501 Hoppe518 (29 y/o F) Tuam, County Galway DECEASED (42574)
739 -- Freddie621 Johnston597 (3 y/o M) Tuam, County Galway DECEASED (4690)
743 -- Gregorio366 Hintz995 (3 y/o M) Tuam, County Galway  (5194)
736 -- Kelsi424 Jeannie478 McKenzie376 (38 y/o F) Tuam, County Galway  (54224)
730 -- Cristen212 Linda558 DuBuque211 (56 y/o F) Tuam, County Galway  (80164)
726 -- Bruno518 Ruecker817 (48 y/o M) Tuam, County Galway  (70733)
733 -- Roosevelt595 Douglas31 (37 y/o M) Tuam, County Galway  (51686)
724 -- Adam631 Hahn503 (74 y/o M) Tuam, County Galway  (104838)
740 -- Teisha100 Sima34 Ryan260 (35 y/o F) Tuam, County Galway  (49197)
680 -- Aleshia311 Berge125 (89 y/o F) Tuam, County Galway  (139522)
741 -- Justine412 Lemke654 (35 y/o F) Tuam, County Galway  (51490)
742 -- Danna372 Robena997 Tillman293 (36 y/o F) Tuam, County Galway  (52028)
731 -- Dusty207 Little434 (68 y/o M) Tuam, County Galway DECEASED (124281)
737 -- Phyliss206 Lebsack687 (56 y/o F) Tuam, County Galway  (80222)
744 -- Mao115 Fairy757 Bednar518 (49 y/o F) Tuam, County Galway DECEASED (71172)
751 -- Broderick767 Daniel959 (4 y/o M) Tuam, County Galway  (6064)
738 -- Odis959 Tromp100 (35 y/o M) Tuam, County Galway  (51641)
735 -- Renda520 Freida957 Volkman526 (43 y/o F) Tuam, County Galway  (62735)
752 -- Steve819 Casper496 (13 y/o M) Tuam, County Galway  (18693)
686 -- Jordon466 Rice937 (82 y/o M) Tuam, County Galway  (159743)
745 -- Lindsay928 Miller503 (54 y/o M) Tuam, County Galway  (74860)
673 -- Nick779 Beier427 (70 y/o M) Tuam, County Galway  (127119)
750 -- Shad704 Kulas532 (15 y/o M) Tuam, County Galway  (21945)
749 -- Adelina682 Chanelle850 Zulauf375 (40 y/o F) Tuam, County Galway  (60269)
753 -- Fred155 Hudson301 (28 y/o M) Tuam, County Galway  (39862)
746 -- Adina377 Bergstrom287 (27 y/o F) Tuam, County Galway  (40569)
739 -- Gregorio366 Rogahn59 (46 y/o M) Tuam, County Galway  (64076)
748 -- Omer483 Reilly981 (68 y/o M) Tuam, County Galway DECEASED (99111)
747 -- Angele108 Saturnina961 Stanton715 (58 y/o F) Tuam, County Galway  (109295)
755 -- Shawnna218 Hayes766 (19 y/o F) Tuam, County Galway  (27176)
758 -- Jamison785 Altenwerth646 (3 y/o M) Tuam, County Galway  (4829)
754 -- Marcelo725 Casper496 (35 y/o M) Tuam, County Galway  (50472)
762 -- Jayna69 Schiller186 (0 y/o F) Tuam, County Galway  (567)
757 -- Deetta949 Cronin387 (11 y/o F) Tuam, County Galway  (16151)
729 -- Nick779 Lemke654 (70 y/o M) Tuam, County Galway  (125491)
766 -- Trevor374 McCullough561 (0 y/o M) Tuam, County Galway  (1167)
765 -- Racheal820 Schiller186 (5 y/o F) Tuam, County Galway  (9803)
763 -- Reggie481 Wisozk929 (16 y/o M) Tuam, County Galway  (23257)
744 -- Merrie964 Kathlyn335 Runolfsdottir785 (59 y/o F) Tuam, County Galway  (86953)
772 -- Alysia661 Stoltenberg489 (6 y/o F) Tuam, County Galway  (9320)
756 -- Mikki421 Larkin917 (69 y/o F) Tuam, County Galway  (102812)
764 -- Leanna255 Bernier607 (28 y/o F) Tuam, County Galway  (41395)
760 -- Kraig824 Abshire638 (51 y/o M) Tuam, County Galway  (75055)
447 -- Gordon377 McClure239 (88 y/o M) Tuam, County Galway DECEASED (132457)
759 -- Abdul218 Jaskolski867 (74 y/o M) Tuam, County Galway  (105859)
768 -- Janelle257 Camilla89 Reinger292 (45 y/o F) Tuam, County Galway  (66578)
761 -- Gerard367 Carroll471 (65 y/o M) Tuam, County Galway  (100879)
769 -- Richie600 Schimmel440 (55 y/o M) Tuam, County Galway  (77432)
748 -- Brendon298 Cremin516 (69 y/o M) Tuam, County Galway  (100590)
775 -- Vince741 Cruickshank494 (33 y/o M) Tuam, County Galway  (45711)
771 -- Kanisha187 Zona368 Pfannerstill264 (41 y/o F) Tuam, County Galway  (58850)
774 -- Luanne915 Sirena316 Reynolds644 (46 y/o F) Tuam, County Galway  (66707)
780 -- Ryan260 Kihn564 (10 y/o M) Tuam, County Galway  (14360)
767 -- Renaldo199 Metz686 (76 y/o M) Tuam, County Galway DECEASED (138855)
778 -- Kent912 Anderson154 (40 y/o M) Tuam, County Galway  (57996)
770 -- Phil587 Schowalter414 (87 y/o M) Tuam, County Galway  (127635)
785 -- Delcie812 Deckow585 (10 y/o F) Tuam, County Galway  (14015)
779 -- Nguyet780 Oretha285 Boehm581 (42 y/o F) Tuam, County Galway  (62899)
773 -- Toshia520 Ha329 Hirthe744 (83 y/o F) Tuam, County Galway  (150855)
777 -- Fritz267 McCullough561 (59 y/o M) Tuam, County Galway DECEASED (83496)
784 -- Kandi717 Kassulke119 (37 y/o F) Tuam, County Galway  (53429)
781 -- Adrianna470 Ozell178 Hahn503 (46 y/o F) Tuam, County Galway DECEASED (68649)
782 -- Derick144 Berge125 (50 y/o M) Tuam, County Galway  (70139)
791 -- January966 Ziemann98 (1 y/o F) Tuam, County Galway  (2149)
789 -- Bobbie849 Hagenes547 (20 y/o F) Tuam, County Galway  (28369)
776 -- Alaina222 Bashirian201 (65 y/o F) Tuam, County Galway  (93452)
793 -- Verdell500 Prohaska837 (2 y/o F) Tuam, County Galway DECEASED (3674)
787 -- Natividad796 Sherilyn598 McCullough561 (42 y/o F) Tuam, County Galway  (62276)
786 -- Berta524 Will178 (47 y/o F) Tuam, County Galway  (70234)
795 -- Matilde468 Turner526 (4 y/o F) Tuam, County Galway  (6125)
783 -- Carl856 Hansen121 (53 y/o M) Tuam, County Galway  (113384)
790 -- Celestine956 Reichert620 (59 y/o F) Tuam, County Galway  (86392)
788 -- Magali989 Corrin41 Gutkowski940 (50 y/o F) Tuam, County Galway  (81378)
792 -- Rory188 Lesch175 (37 y/o M) Tuam, County Galway  (56911)
794 -- Raymundo71 Corkery305 (56 y/o M) Tuam, County Galway  (83630)
731 -- Eliseo499 VonRueden376 (79 y/o M) Tuam, County Galway  (182142)
801 -- Isaiah615 Walter473 (2 y/o M) Tuam, County Galway DECEASED (3977)
797 -- Jesus702 Corkery305 (11 y/o M) Tuam, County Galway  (15800)
447 -- King743 Hansen121 (85 y/o M) Tuam, County Galway DECEASED (137109)
793 -- Debbi640 Pamella8 Mosciski958 (39 y/o F) Tuam, County Galway DECEASED (55244)
805 -- Aleisha941 Lowe577 (3 y/o F) Tuam, County Galway  (5097)
777 -- Columbus656 Rempel203 (84 y/o M) Tuam, County Galway  (123433)
800 -- Logan497 Thiel172 (58 y/o F) Tuam, County Galway  (83814)
799 -- Rashad361 Cummings51 (56 y/o M) Tuam, County Galway  (78295)
806 -- Jordan900 Hoppe518 (23 y/o M) Tuam, County Galway  (31765)
804 -- Cinda869 Thersa321 Zieme486 (48 y/o F) Tuam, County Galway  (69789)
781 -- Sherrill767 Fran41 Koepp521 (54 y/o F) Tuam, County Galway  (78011)
807 -- Israel728 Abshire638 (37 y/o M) Tuam, County Galway  (52170)
802 -- Etha376 Deonna907 O'Kon634 (52 y/o F) Tuam, County Galway  (78898)
798 -- Mabelle762 Willena258 Little434 (77 y/o F) Tuam, County Galway  (113373)
796 -- Lesa839 Adrian111 Hegmann834 (60 y/o F) Tuam, County Galway  (115438)
810 -- Ida350 Cole117 (6 y/o F) Tuam, County Galway  (9715)
809 -- Delmar187 Toy286 (31 y/o M) Tuam, County Galway  (43711)
803 -- Britta584 Lauri399 Dare640 (72 y/o F) Tuam, County Galway DECEASED (105370)
801 -- Bud153 Spencer878 (63 y/o M) Tuam, County Galway  (100931)
812 -- Leo278 Kerluke267 (36 y/o M) Tuam, County Galway  (50316)
815 -- Marshall526 Cummings51 (22 y/o F) Tuam, County Galway  (30776)
816 -- Heriberto162 Fadel536 (15 y/o M) Tuam, County Galway  (22062)
808 -- Antonia30 Muller251 (61 y/o M) Tuam, County Galway  (87056)
819 -- Tamra871 Littel644 (4 y/o F) Tuam, County Galway  (6649)
813 -- Renata373 Idella49 Langworth352 (48 y/o F) Tuam, County Galway  (68269)
818 -- David908 Luettgen772 (44 y/o M) Tuam, County Galway  (62015)
814 -- Hermila490 Koch169 (52 y/o F) Tuam, County Galway  (75783)
820 -- Korey682 Bahringer146 (19 y/o M) Tuam, County Galway  (27713)
793 -- Nicole384 Suzy993 Emmerich580 (76 y/o F) Tuam, County Galway  (114554)
821 -- Chris95 Conn188 (41 y/o M) Tuam, County Galway  (58495)
811 -- Boris111 Breitenberg711 (68 y/o M) Tuam, County Galway  (96913)
817 -- Jeanice469 Hermann103 (47 y/o F) Tuam, County Galway  (71721)
827 -- Genny123 Wilderman619 (19 y/o F) Tuam, County Galway  (26842)
823 -- Rosy219 Jestine4 Bergnaum523 (46 y/o F) Tuam, County Galway  (67207)
831 -- Kiera822 Schultz619 (1 y/o F) Tuam, County Galway  (2668)
830 -- Ozzie259 Streich926 (16 y/o M) Tuam, County Galway  (22458)
828 -- Wilford267 Koelpin146 (44 y/o M) Tuam, County Galway  (61392)
834 -- Georgette866 Paucek755 (0 y/o F) Tuam, County Galway  (433)
833 -- Earle679 Hyatt152 (5 y/o M) Tuam, County Galway  (8073)
826 -- Trudie215 Von197 (65 y/o F) Tuam, County Galway  (93990)
835 -- Mike230 Bahringer146 (4 y/o F) Tuam, County Galway  (6315)
822 -- Cecelia952 Torp761 (65 y/o F) Tuam, County Galway  (94811)
824 -- Pansy803 Crona259 (52 y/o F) Tuam, County Galway DECEASED (124494)
829 -- Carlos172 Jerde200 (43 y/o M) Tuam, County Galway  (59841)
837 -- Ernest565 Eichmann909 (18 y/o M) Tuam, County Galway  (26781)
839 -- Halina47 Stokes453 (20 y/o F) Tuam, County Galway  (28699)
825 -- Dino214 Jacobson885 (68 y/o M) Tuam, County Galway DECEASED (114086)
841 -- Hugo693 Breitenberg711 (30 y/o M) Tuam, County Galway  (45722)
845 -- Ellen406 Runolfsson901 (8 y/o F) Tuam, County Galway  (12151)
840 -- Vena594 Mirtha993 Miller503 (36 y/o F) Tuam, County Galway  (53528)
844 -- Hollis7 Kuhic920 (27 y/o F) Tuam, County Galway  (38572)
849 -- Gale827 Larkin917 (2 y/o M) Tuam, County Galway  (3600)
847 -- Alphonse92 Stehr398 (15 y/o M) Tuam, County Galway  (21459)
842 -- Alita891 Man114 Ratke343 (36 y/o F) Tuam, County Galway DECEASED (50433)
848 -- Darwin703 Cronin387 (25 y/o M) Tuam, County Galway DECEASED (36562)
851 -- Daniela614 Runolfsson901 (15 y/o F) Tuam, County Galway DECEASED (21972)
842 -- Anita473 Satterfield305 (8 y/o F) Tuam, County Galway DECEASED (12684)
832 -- Bunny174 Carola944 Effertz744 (104 y/o F) Tuam, County Galway  (150103)
843 -- Bret7 Homenick806 (60 y/o M) Tuam, County Galway DECEASED (128744)
836 -- Dalia295 Letty680 Hagenes547 (75 y/o F) Tuam, County Galway DECEASED (112215)
856 -- Moises22 Kuphal363 (20 y/o M) Tuam, County Galway  (27697)
838 -- Brian582 Osinski784 (71 y/o M) Tuam, County Galway  (143698)
850 -- Theo630 Cummings51 (71 y/o M) Tuam, County Galway  (105295)
447 -- Harlan808 Welch179 (76 y/o M) Tuam, County Galway DECEASED (172442)
852 -- Kim439 Abernathy524 (64 y/o M) Tuam, County Galway DECEASED (94181)
857 -- Avery919 Glover433 (10 y/o M) Tuam, County Galway  (14332)
855 -- Winford225 Balistreri607 (58 y/o M) Tuam, County Galway  (84482)
848 -- Isaac321 Nicolas769 (38 y/o M) Tuam, County Galway  (54800)
854 -- Lucio648 Mueller846 (50 y/o M) Tuam, County Galway  (69488)
767 -- Kurtis994 Barrows492 (84 y/o M) Tuam, County Galway DECEASED (249732)
846 -- Kate239 Angelika194 Anderson154 (85 y/o F) Tuam, County Galway DECEASED (122651)
851 -- Vernia453 Earlean804 Dare640 (33 y/o F) Tuam, County Galway  (49268)
859 -- Myrtie622 Langworth352 (26 y/o F) Tuam, County Galway  (39028)
858 -- Rashad361 Buckridge80 (55 y/o M) Tuam, County Galway  (78277)
853 -- Galen747 Heaney114 (73 y/o M) Tuam, County Galway DECEASED (129489)
864 -- Jamey282 Mitchell808 (19 y/o M) Tuam, County Galway  (26332)
861 -- Grayce293 Hyatt152 (20 y/o F) Tuam, County Galway  (28715)
862 -- Forest317 Kozey370 (32 y/o M) Tuam, County Galway  (44726)
860 -- Norris589 Brekke496 (43 y/o M) Tuam, County Galway  (59318)
863 -- Gonzalo160 Eichmann909 (43 y/o M) Tuam, County Galway  (61452)
803 -- Coralie787 McKenzie376 (101 y/o F) Tuam, County Galway  (357254)
870 -- Leigh689 Towne435 (16 y/o M) Tuam, County Galway  (22691)
852 -- Troy560 Wyman904 (64 y/o M) Tuam, County Galway  (101823)
836 -- Shiela18 Cathi439 Wisoky380 (50 y/o F) Tuam, County Galway DECEASED (75498)
865 -- Jamaal34 Runolfsdottir785 (58 y/o M) Tuam, County Galway  (82782)
866 -- Leslee214 Annie941 Hilll811 (58 y/o F) Tuam, County Galway  (84602)
871 -- Marylee823 Lavonda853 Hagenes547 (36 y/o F) Tuam, County Galway  (52674)
842 -- Glayds212 Heaney114 (65 y/o F) Tuam, County Galway  (101553)
867 -- Claretta294 Carolin818 Hills818 (69 y/o F) Tuam, County Galway  (99876)
869 -- Brendon298 Gutmann970 (66 y/o M) Tuam, County Galway  (96940)
868 -- Terisa250 Rempel203 (64 y/o F) Tuam, County Galway  (95631)
873 -- Emilio417 Corwin846 (50 y/o M) Tuam, County Galway  (68558)
Waiting for threads to finish... java.util.concurrent.ThreadPoolExecutor@73c31181[Shutting down, pool size = 20, active threads = 20, queued tasks = 123, completed tasks = 857]
872 -- Shelby741 Adelle43 Grimes165 (60 y/o F) Tuam, County Galway  (85866)
879 -- Justin359 Franecki195 (10 y/o M) Tuam, County Galway  (13688)
846 -- Charita800 Wan724 Klein929 (85 y/o F) Tuam, County Galway  (121299)
882 -- Ernestina649 Reinger292 (5 y/o F) Tuam, County Galway  (7792)
883 -- Ashlea10 Hills818 (6 y/o F) Tuam, County Galway  (9076)
880 -- Douglas31 VonRueden376 (24 y/o M) Tuam, County Galway  (32887)
878 -- Shane235 Lehner980 (42 y/o M) Tuam, County Galway  (58250)
876 -- Lenita591 Krystle484 Johnson679 (53 y/o F) Tuam, County Galway  (81188)
874 -- Seema671 Sol312 Wisoky380 (57 y/o F) Tuam, County Galway  (88638)
875 -- Clint766 Daugherty69 (78 y/o M) Tuam, County Galway  (117313)
881 -- Daniel959 Schuster709 (26 y/o F) Tuam, County Galway  (39143)
888 -- Tierra831 Dibbert990 (10 y/o F) Tuam, County Galway  (16777)
889 -- Michiko564 Emard19 (9 y/o F) Tuam, County Galway  (13878)
877 -- Tyron580 Stark857 (58 y/o M) Tuam, County Galway  (80845)
884 -- Ben667 Heathcote539 (34 y/o M) Tuam, County Galway  (48717)
886 -- Oren284 Borer986 (31 y/o M) Tuam, County Galway  (45109)
891 -- Trenton748 Morar593 (4 y/o M) Tuam, County Galway  (6207)
885 -- Buck819 Davis923 (54 y/o M) Tuam, County Galway  (76296)
887 -- Nadine465 Huels583 (45 y/o F) Tuam, County Galway  (65629)
895 -- Cary869 Lemke654 (8 y/o M) Tuam, County Galway  (11328)
897 -- Vera718 Shanahan202 (0 y/o F) Tuam, County Galway DECEASED (1497)
890 -- Kanesha23 Dickinson688 (51 y/o F) Tuam, County Galway  (73496)
836 -- Criselda629 Rutherford999 (73 y/o F) Tuam, County Galway DECEASED (113798)
902 -- Eddie505 Hyatt152 (3 y/o F) Tuam, County Galway  (5832)
893 -- Cleveland582 Witting912 (33 y/o M) Tuam, County Galway  (45971)
892 -- Whitley172 Stokes453 (44 y/o F) Tuam, County Galway  (67027)
896 -- Marco578 Schaefer657 (42 y/o M) Tuam, County Galway  (60100)
894 -- Dale454 Macejkovic424 (31 y/o M) Tuam, County Galway  (43098)
906 -- Lita714 West559 (5 y/o F) Tuam, County Galway  (7305)
898 -- Keri25 Kutch271 (39 y/o F) Tuam, County Galway  (56038)
907 -- Lecia978 Ernser583 (5 y/o F) Tuam, County Galway  (7661)
909 -- Arlette667 Kuvalis369 (4 y/o F) Tuam, County Galway  (6805)
910 -- Karole140 Barrows492 (13 y/o F) Tuam, County Galway  (17751)
905 -- Perry780 Zana914 Simonis280 (41 y/o F) Tuam, County Galway  (58181)
900 -- Jed345 Douglas31 (67 y/o M) Tuam, County Galway  (116775)
903 -- Joanna347 Treutel973 (54 y/o F) Tuam, County Galway  (78871)
824 -- Lanelle105 Lowe577 (30 y/o F) Tuam, County Galway DECEASED (43167)
913 -- Elton404 Pagac496 (37 y/o M) Tuam, County Galway DECEASED (53998)
901 -- Oren284 Bogan287 (93 y/o M) Tuam, County Galway DECEASED (138291)
916 -- Brock407 Tremblay80 (3 y/o M) Tuam, County Galway  (5814)
904 -- Trinity427 Leanna255 Little434 (54 y/o F) Tuam, County Galway  (78463)
897 -- Launa267 Erline657 Jaskolski867 (74 y/o F) Tuam, County Galway  (108218)
914 -- Mohamed943 Lindgren255 (55 y/o M) Tuam, County Galway  (77066)
908 -- Loise968 Eura647 Leffler128 (72 y/o F) Tuam, County Galway  (107618)
911 -- Noel608 Franecki195 (63 y/o M) Tuam, County Galway  (90952)
899 -- Lon587 Sporer811 (73 y/o M) Tuam, County Galway  (109781)
912 -- Ardelle563 Kenna183 Bergnaum523 (37 y/o F) Tuam, County Galway  (54249)
915 -- Kirk871 McCullough561 (61 y/o M) Tuam, County Galway  (88671)
919 -- Muoi890 Morissette863 (11 y/o F) Tuam, County Galway  (16239)
917 -- Kamilah729 Schuster709 (61 y/o F) Tuam, County Galway  (89159)
921 -- Jerome176 Wunsch504 (15 y/o M) Tuam, County Galway  (21518)
922 -- Clemencia569 Kuphal363 (21 y/o F) Tuam, County Galway  (30078)
824 -- Caroline183 Caterina17 Wintheiser220 (41 y/o F) Tuam, County Galway DECEASED (58835)
913 -- Laurence43 Jenkins714 (48 y/o M) Tuam, County Galway DECEASED (73542)
924 -- Cathrine584 Schoen8 (10 y/o F) Tuam, County Galway  (15542)
925 -- Bradley693 Christiansen251 (6 y/o M) Tuam, County Galway  (9252)
923 -- Nigel915 Walter473 (13 y/o M) Tuam, County Galway  (18167)
920 -- Chastity705 Janella261 Cassin499 (57 y/o F) Tuam, County Galway  (82095)
843 -- Malcom15 Daniel959 (73 y/o M) Tuam, County Galway  (162606)
926 -- Lanny564 Schimmel440 (38 y/o M) Tuam, County Galway  (52723)
918 -- Setsuko288 Boyle917 (83 y/o F) Tuam, County Galway  (125397)
932 -- Guadalupe206 Collins926 (5 y/o M) Tuam, County Galway  (8005)
933 -- Josh874 Konopelski743 (1 y/o M) Tuam, County Galway  (1865)
931 -- Vinita997 Fadel536 (16 y/o F) Tuam, County Galway  (22987)
936 -- Kathe603 Adams676 (5 y/o F) Tuam, County Galway  (7527)
937 -- Fawn386 Kozey370 (6 y/o F) Tuam, County Galway  (9720)
836 -- Kerrie266 Lili474 Mertz280 (78 y/o F) Tuam, County Galway  (114145)
901 -- Junior695 Kling921 (90 y/o M) Tuam, County Galway DECEASED (130331)
825 -- Arden380 VonRueden376 (86 y/o M) Tuam, County Galway DECEASED (260640)
935 -- Pamelia915 O'Keefe54 (33 y/o F) Tuam, County Galway  (47240)
938 -- Brain142 Larkin917 (14 y/o M) Tuam, County Galway  (19195)
939 -- Lorenza655 Kertzmann286 (22 y/o F) Tuam, County Galway  (31602)
928 -- Winter723 Shelby741 Klein929 (51 y/o F) Tuam, County Galway DECEASED (74886)
934 -- Refugia211 Latonia966 Gaylord332 (60 y/o F) Tuam, County Galway DECEASED (84592)
940 -- Karma832 Yajaira121 Quitzon246 (32 y/o F) Tuam, County Galway  (45169)
930 -- Marty115 Torp761 (45 y/o M) Tuam, County Galway  (63063)
927 -- Liliana922 O'Kon634 (66 y/o F) Tuam, County Galway  (94065)
929 -- Jayna69 Raguel228 Kovacek682 (68 y/o F) Tuam, County Galway  (104186)
913 -- Neville893 Corkery305 (65 y/o M) Tuam, County Galway  (112079)
945 -- Jerald662 Labadie908 (29 y/o M) Tuam, County Galway  (40302)
942 -- Graig740 Goodwin327 (50 y/o M) Tuam, County Galway  (71416)
943 -- Maryanna659 Fidela881 Will178 (35 y/o F) Tuam, County Galway  (52753)
944 -- Terra840 Gabriele201 Hartmann983 (38 y/o F) Tuam, County Galway  (57276)
824 -- Crystle668 Heaney114 (77 y/o F) Tuam, County Galway  (115780)
447 -- Hilton264 Heller342 (55 y/o M) Tuam, County Galway DECEASED (76297)
941 -- Maida946 Wilkinson796 (69 y/o F) Tuam, County Galway  (102944)
946 -- Verline727 Helga481 Wyman904 (56 y/o F) Tuam, County Galway  (84001)
947 -- Merle11 Olson653 (29 y/o M) Tuam, County Galway  (42378)
948 -- Johnathon489 Shields502 (35 y/o M) Tuam, County Galway  (52552)
934 -- Delia459 Shan714 Schiller186 (69 y/o F) Tuam, County Galway  (99770)
853 -- Lupe126 Spencer878 (54 y/o M) Tuam, County Galway DECEASED (102359)
951 -- Rob341 Barrows492 (32 y/o M) Tuam, County Galway  (46542)
950 -- Miyoko154 Lesa839 Wiza601 (63 y/o F) Tuam, County Galway  (92713)
928 -- Kristal814 Mosciski958 (62 y/o F) Tuam, County Galway DECEASED (91545)
955 -- Jenna662 Abernathy524 (20 y/o F) Tuam, County Galway  (28781)
952 -- Eugenie836 Shiela18 Mosciski958 (48 y/o F) Tuam, County Galway  (68783)
954 -- Tod265 Boehm581 (36 y/o M) Tuam, County Galway  (53979)
957 -- Hong136 Barrows492 (58 y/o M) Tuam, County Galway  (80999)
960 -- Marshall526 Sauer652 (13 y/o M) Tuam, County Galway  (18577)
767 -- Mickey576 Davis923 (88 y/o M) Tuam, County Galway DECEASED (163294)
958 -- Santina680 Rozella39 Ortiz186 (59 y/o F) Tuam, County Galway  (86744)
956 -- Iliana226 Pacocha935 (64 y/o F) Tuam, County Galway  (91747)
959 -- Alberto639 Pouros728 (50 y/o M) Tuam, County Galway  (70436)
964 -- Hedwig986 Vandervort697 (10 y/o F) Tuam, County Galway  (14461)
953 -- Lonnie913 Beer512 (67 y/o M) Tuam, County Galway DECEASED (93032)
966 -- Kevin729 Wintheiser220 (13 y/o M) Tuam, County Galway  (18141)
962 -- Bradley693 Skiles927 (36 y/o M) Tuam, County Galway  (50723)
965 -- Yong583 Weimann465 (15 y/o F) Tuam, County Galway  (21553)
961 -- Candra395 Considine820 (49 y/o F) Tuam, County Galway  (73929)
971 -- Edra310 McGlynn426 (5 y/o F) Tuam, County Galway  (7989)
949 -- Thanh759 Edna186 Feeney44 (67 y/o F) Tuam, County Galway  (166586)
974 -- Rhiannon677 Beahan375 (1 y/o F) Tuam, County Galway  (2169)
447 -- Darwin703 Dietrich576 (77 y/o M) Tuam, County Galway DECEASED (172857)
972 -- Beata187 Schowalter414 (8 y/o F) Tuam, County Galway  (12194)
970 -- Harry448 Schneider199 (17 y/o M) Tuam, County Galway  (25022)
975 -- Monte325 Dickens475 (12 y/o M) Tuam, County Galway  (17487)
963 -- Aron520 Barton704 (50 y/o M) Tuam, County Galway  (77972)
901 -- Vince741 Mosciski958 (91 y/o M) Tuam, County Galway DECEASED (272229)
969 -- Omer483 Crona259 (41 y/o M) Tuam, County Galway  (57174)
976 -- Georgene966 Bayer639 (26 y/o F) Tuam, County Galway  (38162)
980 -- Corrinne176 Herman763 (1 y/o F) Tuam, County Galway  (2850)
973 -- Arlinda565 Laurette750 Farrell962 (41 y/o F) Tuam, County Galway  (61608)
967 -- Enda486 Wendolyn786 Erdman779 (65 y/o F) Tuam, County Galway  (96540)
978 -- Jalisa590 Jenelle653 Baumbach677 (45 y/o F) Tuam, County Galway DECEASED (66059)
981 -- Louise871 Yost751 (17 y/o F) Tuam, County Galway  (24025)
979 -- Emmett200 Halvorson124 (33 y/o M) Tuam, County Galway  (49401)
982 -- Orval846 Nitzsche158 (33 y/o M) Tuam, County Galway  (46011)
983 -- Gerry91 Rolfson709 (18 y/o M) Tuam, County Galway  (26219)
928 -- Erline657 Walsh511 (58 y/o F) Tuam, County Galway DECEASED (88984)
988 -- France571 Kris249 (4 y/o F) Tuam, County Galway  (7147)
985 -- Noel608 Crooks415 (39 y/o M) Tuam, County Galway  (57388)
968 -- Barbie211 Hyon784 Monahan736 (83 y/o F) Tuam, County Galway  (121451)
977 -- Janiece99 Kiana854 Borer986 (67 y/o F) Tuam, County Galway  (107183)
953 -- Billy698 Wiza601 (64 y/o M) Tuam, County Galway DECEASED (91729)
853 -- Asa127 Ryan260 (63 y/o M) Tuam, County Galway DECEASED (88554)
986 -- Shawanda667 Nyla424 Grady603 (61 y/o F) Tuam, County Galway  (87535)
992 -- Nathalie366 Schulist381 (8 y/o F) Tuam, County Galway  (11641)
991 -- Shirley182 Rogahn59 (35 y/o M) Tuam, County Galway  (49021)
978 -- Raeann749 Bev675 Gerlach374 (62 y/o F) Tuam, County Galway  (92791)
987 -- Jarod376 Pollich983 (70 y/o M) Tuam, County Galway  (102301)
984 -- Zena758 Koch169 (65 y/o F) Tuam, County Galway DECEASED (136737)
989 -- Zackary401 Runolfsdottir785 (73 y/o M) Tuam, County Galway  (107183)
993 -- Shawn523 Mills423 (34 y/o M) Tuam, County Galway  (49838)
990 -- Micheal721 Kuhlman484 (46 y/o F) Tuam, County Galway DECEASED (69509)
997 -- Tasia358 Romaguera67 (12 y/o F) Tuam, County Galway  (16737)
996 -- Tuyet839 Pollich983 (7 y/o F) Tuam, County Galway  (9985)
953 -- Kerry175 Lebsack687 (18 y/o M) Tuam, County Galway DECEASED (25532)
994 -- Palmer257 Kemmer137 (29 y/o M) Tuam, County Galway DECEASED (43240)
999 -- Garrett899 Auer97 (37 y/o M) Tuam, County Galway  (51699)
998 -- Beula159 Bahringer146 (31 y/o F) Tuam, County Galway  (43922)
995 -- Anton902 Ritchie586 (66 y/o M) Tuam, County Galway  (93264)
1000 -- Carson894 Armstrong51 (63 y/o M) Tuam, County Galway DECEASED (113258)
928 -- Mertie42 Miller503 (73 y/o F) Tuam, County Galway  (108528)
853 -- Ron353 Cole117 (63 y/o M) Tuam, County Galway DECEASED (126588)
994 -- Darius626 Torphy630 (41 y/o M) Tuam, County Galway  (59372)
990 -- Christinia886 Margeret29 Simonis280 (72 y/o F) Tuam, County Galway  (104795)
953 -- Merlin721 Bergstrom287 (74 y/o M) Tuam, County Galway DECEASED (154293)
767 -- Warren653 Weimann465 (17 y/o M) Tuam, County Galway DECEASED (24443)
984 -- Glynis780 Nannie905 Roberts511 (66 y/o F) Tuam, County Galway  (98780)
901 -- Theron432 Howe413 (99 y/o M) Tuam, County Galway  (213718)
1000 -- Rayford811 Schowalter414 (55 y/o M) Tuam, County Galway DECEASED (79682)
767 -- Miles206 O'Keefe54 (82 y/o M) Tuam, County Galway DECEASED (124698)
853 -- Brendon298 Nitzsche158 (77 y/o M) Tuam, County Galway  (110829)
447 -- Pedro316 Wiegand701 (90 y/o M) Tuam, County Galway DECEASED (196050)
1000 -- Brooks264 Moore224 (73 y/o M) Tuam, County Galway DECEASED (105983)
767 -- Carlo647 Effertz744 (102 y/o M) Tuam, County Galway DECEASED (278668)
1000 -- Ross213 Considine820 (92 y/o M) Tuam, County Galway  (176205)
825 -- Frankie174 Ratke343 (74 y/o M) Tuam, County Galway DECEASED (162796)
953 -- Mike230 Williamson769 (79 y/o M) Tuam, County Galway DECEASED (152395)
767 -- Curtis94 Schulist381 (55 y/o M) Tuam, County Galway DECEASED (82570)
447 -- Reed154 Kilback373 (19 y/o M) Tuam, County Galway DECEASED (27251)
767 -- Alonso270 Barrows492 (51 y/o M) Tuam, County Galway DECEASED (70624)
953 -- Valentin929 Kertzmann286 (50 y/o M) Tuam, County Galway DECEASED (68839)
953 -- Paul232 Kuhic920 (2 y/o M) Tuam, County Galway DECEASED (3331)
447 -- Laverne101 Durgan499 (68 y/o M) Tuam, County Galway DECEASED (100863)
825 -- Elton404 Bosco882 (80 y/o M) Tuam, County Galway DECEASED (118516)
767 -- Bret7 Bogisich202 (97 y/o M) Tuam, County Galway DECEASED (185234)
953 -- Monty345 Upton904 (85 y/o M) Tuam, County Galway DECEASED (122488)
447 -- Rayford811 Fahey393 (55 y/o M) Tuam, County Galway DECEASED (80379)
825 -- Wyatt967 Hansen121 (87 y/o M) Tuam, County Galway  (126169)
447 -- Kirby843 Lubowitz58 (85 y/o M) Tuam, County Galway  (124162)
953 -- Zack583 Crona259 (107 y/o M) Tuam, County Galway  (169065)
767 -- Eric487 Deckow585 (66 y/o M) Tuam, County Galway DECEASED (94455)
767 -- Harold594 Mayer370 (45 y/o M) Tuam, County Galway DECEASED (63014)
767 -- Colby655 Bartoletti50 (87 y/o M) Tuam, County Galway  (130877)
Records: total=1161, alive=1000, dead=161
RNG=1000
Clinician RNG=96

Deprecated Gradle features were used in this build, making it incompatible with Gradle 9.0.

You can use '--warning-mode all' to show the individual deprecation warnings and determine if they come from your own scripts or plugins.

For more on this, please refer to https://docs.gradle.org/8.2.1/userguide/command_line_interface.html#sec:command_line_warnings in the Gradle documentation.

BUILD SUCCESSFUL in 49s
4 actionable tasks: 2 executed, 2 up-to-date
```