# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# extract_statistics.py
# Created on: 2022-04-19 01:03:30.00000
#   (generated by JCT)
# Description: 批量提取tif的像元平均值、最值、标准差等
# ---------------------------------------------------------------------------

import arcpy
year="2018"
file_gen="F:\\result\\"+year+"_"
file_name="result20220406070531.tif"
txt_save_path="C:\\Users\\DELL\\Desktop\\"+year+".TXT"
file_string=""
for month in range(1,13):
    str1=file_gen+str(month)+"\\"+file_name+";"

    file_string=file_string+str1


print(file_string)



# Process: 波段集统计
arcpy.gp.BandCollectionStats_sa(file_string, txt_save_path, "BRIEF")

