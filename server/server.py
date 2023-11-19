# flask server 

from flask import Flask,render_template,request,jsonify
import util
import json
import pickle
app = Flask(__name__)

@app.route("/hello")
def hello():
    return "<h1> hello</h1>"

@app.route('/predict_result',methods=['post'])
def predict_result():
    pelvic_incidence = float(request.form['pelvic_incidence'])
    pelvic_tilt = float(request.form['pelvic_tilt'])
    lumbar_lordosis_angle = float(request.form['lumbar_lordosis_angle'])
    sacral_slope = float(request.form['sacral_slope'])
    pelvic_radius = float(request.form['pelvic_radius'])
    degree_spondylolisthesis = float(request.form['degree_spondylolisthesis'])
    pelvic_slope = float(request.form['pelvic_slope'])
    Direct_tilt = float(request.form['Direct_tilt'])
    thoracic_slope = float(request.form['thoracic_slope'])
    cervical_tilt = float(request.form['cervical_tilt'])
    sacrum_angle = float(request.form['sacrum_angle'])
    scoliosis_slope = float(request.form['scoliosis_slope'])
    
    response = jsonify({'result':
        util.get_predict_result(pelvic_incidence,pelvic_tilt,lumbar_lordosis_angle,sacral_slope,pelvic_radius,degree_spondylolisthesis,pelvic_slope,Direct_tilt,thoracic_slope,cervical_tilt,sacrum_angle,scoliosis_slope)})
    
    response.headers.add('Access-Control-Allow-Origin','*')
    
    return response
    											
if __name__ == "__main__":
    print("starting flask server")
    util.load_save_artifacts()
    app.run(debug=True)
