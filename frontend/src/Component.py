import os


class Component:
    def __init__(self):
        self.patient_list = os.listdir('/home/wyjang/IdeaProjects/cbnuh/data')
        self.patient = ''
        self.pat_hx = ''
        self.pat_pt = ''
        self.patient_path = "/home/wyjang/IdeaProjects/cbnuh/frontend/tmp"
        self.project_path = "/home/wyjang/IdeaProjects/cbnuh/frontend/tmp"
        self.try_path = "/home/wyjang/IdeaProjects/cbnuh/frontend/tmp"
        self.MRI_img_path = "/home/wyjang/project/prostate0017/MR_T2_dicom_raw"
        self.CT_img_path = "/home/wyjang/IdeaProjects/cbnuh/frontend/tmp"
        self.sCT_img_path = "/home/wyjang/IdeaProjects/cbnuh/frontend/tmp"
        self.mri_temp_path_frontend_jpg = "/home/wyjang/IdeaProjects/cbnuh/frontend/tmp/mri.jpg"
        self.sct_temp_path_frontend_jpg = "/home/wyjang/IdeaProjects/cbnuh/frontend/tmp/sct.jpg"
        self.eh_temp_path_frontend_jpg = "/home/wyjang/IdeaProjects/cbnuh/frontend/tmp/emri.jpg"
        self.esct_temp_path_frontend_jpg = "/home/wyjang/IdeaProjects/cbnuh/frontend/tmp/esct.jpg"
        self.temp_path = "/home/wyjang/IdeaProjects/cbnuh/frontend/tmp"

