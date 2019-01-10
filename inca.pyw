import sys
import clr
sys.path.append("C:\ETAS\INCA7.2\cebra")
clr.AddReference("incacom")
from de.etas.cebra.toolAPI.Inca import *
from de.etas.cebra.toolAPI.Common import *
a=Inca(True)
myDB=a.GetCurrentDataBase()
print a.APIVersion()
print a.GetApplicationLanguage()
print a.GetDataBasePath()
print a.GetETASLogFilePath()
print a.GetLicenseManager()
print a.GetPollingCycleTimeTS()
print a.GetRecordingFileFormatsInternal()
print a.GetOpenedExperiment()
print a.GetOpenedExperimentView()
##print dir(myDB)
##b=myDB.BrowseItem("Experiment_Dura_XCP_New")[0].OpenExperiment()
b=a.GetOpenedExperiment()
##c=b.GetAllMeasureElements()
##print d=c[1].GetValue()
##print d.Label()
##f=b.GetAllCalibrationElements()
##c=(i.Label for i in b.GetAllMeasureElements())
c=myDB.BrowseItem("Experiment_Dura_XCP_New")[0]
d=c.GetParentFolder()
print d.GetName()
#u'eM18_Beta2_Dev_Orig'
for i in d.GetAllDataBaseItems():
    print i.GetName()
    
##  Cal
##CVTC_SV51-04_CMX_EPT_V1.2_20180729 HCU
##CVTC_SV51-04_CMX_EPT_V1.2_20180729 PEU
##CVTC_SV51-04_CMX_PT_V1.2_20180729 HCU
##EP_PT_CAN_V1.1
##Experiment_Dura_XCP_1218
##Experiment_Dura_XCP_backup
##Experiment_Dura_XCP_New
##Experiment_Dura_XCP_New_1218
##NewExp_PEU
##PATAC_Customer_180827
##Workspace
##Workspace_All
##Workspace_PEU
##Workspace_XCP_TCU  
f=d.GetAllSubFolders()
e=b.GetHardwareConfiguration()
g=c.GetName()
