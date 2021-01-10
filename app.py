from flask import Flask
from flask import request, jsonify, redirect
from tempfile import TemporaryFile
import myprosody as mysp
import logging
from werkzeug.utils import secure_filename
import os
from timming import Timer
from flask.helpers import make_response
app = Flask(__name__)
app.config["DEBUG"] = True
logging.basicConfig(level=logging.DEBUG)

UPLOAD_FOLDER = '/Users/wtoledo/Documents/wt/toefl/myprosody/myprosody/dataset/audioToCheck'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['AUDIO_FILES'] = '/Users/wtoledo/Documents/wt/toefl/myprosody/myprosody'

ALLOWED_EXTENSIONS = {'wav'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=["GET"])
def home():
    return 'TOEFL Speaking checker'


@app.route('/verification/audio', methods=['POST'])
def verification():
    logging.info("audio verification")
    logging.info("params")
    req = request.form
    uploaded_file = request.files['audio_file']
    audio_file = uploaded_file
    file = audio_file
    file_ext = os.path.splitext(file.filename)[1]

    logging.info(f"filename {file.filename} ")

    logging.info(f"file ext {file_ext}")

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    p = file.filename.partition('.')[0]
    c = app.config['AUDIO_FILES']

    sound=app.config['UPLOAD_FOLDER']+"/"+secure_filename(file.filename)
    logging.info(f"sound to check {sound}")
    t=Timer()
    # t.start()
    # logging.info("overview")
    # overview = mysp.mysptotal(p, c)
    # logging.info(overview)
    # t.stop()

    # logging.info("gender")
    # t.start()
    # gender = mysp.myspgend(p, c)
    # logging.info(gender)
    # t.stop()

    # logging.info("syllabe")
    # t.start()
    # syllabe = mysp.myspsyl(p, c)
    # logging.info(syllabe)
    # t.stop()

    # logging.info("filters and pauses")
    # t.start()
    # pause = mysp.mysppaus(p, c)
    # logging.info(pause)
    # t.stop()

    # logging.info("rate of the speech")
    # t.start()
    # speech_rate = mysp.myspsr(p, c)
    # logging.info(speech_rate)
    # t.stop()

    # logging.info("articulation speed")
    # t.start()
    # articulation_speed = mysp.myspatc(p, c)
    # logging.info(articulation_speed)
    # t.stop()

    # logging.info("speaking time")
    # t.start()
    # speaking_time = mysp.myspst(p, c)
    # logging.info(speaking_time)
    # t.stop()

    # logging.info("speaking duration")
    # t.start()
    # total_speaking_duration = mysp.myspod(p, c)
    # logging.info(total_speaking_duration)
    # t.stop()

    # logging.info("balance")
    # t.start()
    # balance = mysp.myspbala(p, c)
    # logging.info(balance)
    # t.stop()

    # logging.info("freq_dist_mean")
    # t.start()
    # freq_dist_mean = mysp.myspf0mean(p, c)
    # logging.info(freq_dist_mean)
    # t.stop()

    # logging.info("freq_dist_sd")
    # t.start()
    # freq_dist_sd = mysp.myspf0sd(p, c)
    # logging.info(freq_dist_sd)
    # t.stop()

    # logging.info("freq_dist_median")
    # t.start()
    # freq_dist_median = mysp.myspf0med(p, c)
    # logging.info(freq_dist_median)
    # t.stop()

    # logging.info("freq_dist_minimun")
    # t.start()
    # freq_dist_minimun = mysp.myspf0min(p, c)
    # logging.info(freq_dist_minimun)
    # t.stop()

    # logging.info("freq_dist_max")
    # t.start()
    # freq_dist_max = mysp.myspf0max(p, c)
    # logging.info(freq_dist_max)
    # t.stop()

    # logging.info("quantile_25th")
    # t.start()
    # quantile_25th = mysp.myspf0q25(p, c)
    # logging.info(quantile_25th)
    # t.stop()

    # logging.info("quantile_75th")
    # t.start()
    # quantile_75th = mysp.myspf0q75(p, c)
    # logging.info(quantile_75th)
    # t.stop()

    # logging.info("pronuntiation_probability_score")
    # t.start()
    # pronuntiation_probability_score = mysp.mysppron(p, c)
    # logging.info(pronuntiation_probability_score)
    # t.stop()

    logging.info("native_comparation")
    t.start()
    native_comparation = mysp.myprosody(p, c,sound)
    logging.info(native_comparation)
    t.stop()

    logging.info("spoken_lang_proeficiency_level")
    t.start()
    spoken_lang_proeficiency_level = mysp.mysplev(p, c,sound)
    logging.info(spoken_lang_proeficiency_level)
    t.stop()
    data={}
    # data = jsonify(
    #     {"overview": str(overview),
    #      "gender": gender,
    #      "syllabe": syllabe,
    #      "pause": pause,
    #      "speech_rate": speech_rate,
    #      "articulation_speed": articulation_speed,
    #      "speaking_time": speaking_time,
    #      "total_speaking_duration": total_speaking_duration,
    #      "balance": balance,
    #      "freq_dist_mean": freq_dist_mean,
    #      "freq_dist_sd": freq_dist_sd,
    #      "freq_dist_median": freq_dist_median,
    #      "freq_dist_minimum": freq_dist_minimun,
    #      "freq_dist_max": freq_dist_max,
    #      "quantile_25th": quantile_25th,
    #      "quantile_75th": quantile_75th,
    #      "pronuntiation_probability_score": pronuntiation_probability_score,
    #      "native_comparation": native_comparation,
    #      "spoken_lang_proeficiency_level": spoken_lang_proeficiency_level
    #      }
    # )

    logging.info(f"data  {data}")
    response = make_response(data,
                             401,
                             )
    response.headers["Content-Type"] = "application/json"
    return response


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404 <p>The resource could not be found.</p></h1>", 404


app.run()
