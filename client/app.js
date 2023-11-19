function onPredictResult() {
    console.log("predicting result");
    var pelvic_incidence = document.getElementById("pelvic_incidence");
    var pelvic_tilt = document.getElementById("pelvic_tilt");
    var lumbar_lordosis_angle = document.getElementById("lumbar_lordosis_angle");
    var sacral_slope = document.getElementById("sacral_slope");
    var pelvic_radius = document.getElementById("pelvic_radius");
    var degree_spondylolisthesis = document.getElementById("degree_spondylolisthesis");
    var pelvic_slope = document.getElementById("pelvic_slope");
    var Direct_tilt = document.getElementById("Direct_tilt");
    var thoracic_slope = document.getElementById("thoracic_slope");
    var cervical_tilt = document.getElementById("cervical_tilt");
    var sacrum_angle = document.getElementById("sacrum_angle");
    var scoliosis_slope = document.getElementById("scoliosis_slope");
    var output = document.getElementById("result")
    var url = "http://127.0.0.1:5000/predict_result";



    $.post(url, {
            pelvic_incidence: parseFloat(pelvic_incidence.value),
            pelvic_tilt: parseFloat(pelvic_tilt.value),
            lumbar_lordosis_angle: parseFloat(lumbar_lordosis_angle.value),
            sacral_slope: parseFloat(sacral_slope.value),
            pelvic_radius: parseFloat(pelvic_radius.value),
            degree_spondylolisthesis: parseFloat(degree_spondylolisthesis.value),
            pelvic_slope: parseFloat(pelvic_slope.value),
            Direct_tilt: parseFloat(Direct_tilt.value),
            thoracic_slope: parseFloat(thoracic_slope.value),
            cervical_tilt: parseFloat(cervical_tilt.value),
            sacrum_angle: parseFloat(sacrum_angle.value),
            scoliosis_slope: parseFloat(scoliosis_slope.value)
        },
        function(data, status, jqXHR) {
            console.log(data.result);
            output.innerHTML = "<h2> " + "  ----  " + data.result.toString() + "  ----  " + " </h2>";
            console.log(status);
        }, 'json');
}