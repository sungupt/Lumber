
import pickle
import numpy as np 
import json
# loading model



__model = None
def get_predict_result(pelvic_incidence,pelvic_tilt,lumbar_lordosis_angle,sacral_slope,pelvic_radius,degree_spondylolisthesis,pelvic_slope,Direct_tilt,thoracic_slope,cervical_tilt,sacrum_angle,scoliosis_slope):
    
    input = np.array([pelvic_incidence,pelvic_tilt,lumbar_lordosis_angle,sacral_slope,pelvic_radius,degree_spondylolisthesis,pelvic_slope,Direct_tilt,thoracic_slope,cervical_tilt,sacrum_angle,scoliosis_slope])
    result = __model.predict([input])[0]    
    if 0 == int(result):
        return "  Normal"
    else:
        return "  Abnormal"

def load_save_artifacts():
    global __model
    with open("C:/Lumber_Project/Lumber/server/artifacts/LowerBackPain.pickle",'rb') as f:
        __model = pickle.load(f)
    print("loading saved artifacts .... done")
    
if __name__ == '__main__':
    load_save_artifacts()
    result=get_predict_result(0.155897,0.521747,0.115281,0.109938,0.628095,0.185433	,0.851662,0.124589,0.909809,0.243829,0.091337,0.7707860)
    print(result)
    
    
    