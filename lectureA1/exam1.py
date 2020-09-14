import geo1001_2020_master.lectureA1.plotPWIDSdata
import numpy as np

WD_mean = np.mean(geo1001_2020_master.lectureA1.plotPWIDSdata.WD)
WD_var = np.var(geo1001_2020_master.lectureA1.plotPWIDSdata.WD)
WD_std = np.std(geo1001_2020_master.lectureA1.plotPWIDSdata.WD)
WS_mean = np.mean(geo1001_2020_master.lectureA1.plotPWIDSdata.WS)
WS_var = np.var(geo1001_2020_master.lectureA1.plotPWIDSdata.WS)
WS_std = np.std(geo1001_2020_master.lectureA1.plotPWIDSdata.WS)

print(
      WD_mean, WD_var, WD_std,
      WS_mean, WS_var, WS_std,
      sep='\n'
      )
