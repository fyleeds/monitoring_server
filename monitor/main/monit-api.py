from flask import Flask, abort, jsonify
import json
import os
import sys
sys.path.append(os.path.abspath('../reports/report'))
# from log_report import logLastReport, logListReports
from get_report import  getReportId
from create_report import  reports_path

sys.path.append(os.path.abspath('../log'))
from logger_config import setup_logger
logger = setup_logger("create_api_logger")



# on crée un ptit objet Flask, nécessaire pour ajouter des routes
app = Flask(__name__)
app.secret_key = b'SECRET_KEY'

# SWAGGER_URL = '/swagger'
# API_URL = '/static/swagger.yaml'  # Location of your swagger file
# SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
#     SWAGGER_URL,
#     API_URL,
#     config={'app_name': "Monit API"}
# )
# app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix=SWAGGER_URL)

# utilisation d'un décorateur Python avec @ pour donc décorer une fonction
# c'est l'ajout de ce décorateur qui permet d'ajouter une route
# c'est dans la doc de Flask, nous on obéit :D
@app.route('/reports', methods=['GET'])
def get_reports():
    keys= []
    values = []
    for file in os.scandir(reports_path):
        file = open(reports_path + file.name)
        if file is not None:
            report= json.load(file)
            values.append(report)
            keys.append(getReportId(file.name))
        file.close()
        reports = dict(zip(keys, values))
        logger.info("reports sent to API :  %s", reports)
    if reports is not None:
        return jsonify(reports)
    else:
        abort(404)


@app.route('/reports/<input_report_id>', methods=['GET'])
def get_reportById(input_report_id=None):
    if input_report_id is not None:
        for report_name in [file.name for file in os.scandir(reports_path)]:
            report_id = getReportId(report_name)
            if report_id == input_report_id:
                report_name_found = report_name
                break        
        if report_name_found is not None:
            file = open(reports_path + report_name_found)
            report = json.load(file)
            file.close()
        else:
            abort(404)

        if report is not None:
            logger.info("report %s sent to API :  %s", input_report_id, report)
            return jsonify(report)
        else:
            # la ptite 404 clean quand on demande une ressource qui n'existe pas
            abort(404)
    else:
        abort(404)

if __name__ == '__main__':
    logger.info("API started")
    try:
        app.run(host='0.0.0.0', port=5000)
    except Exception as e:
        logger.error("Error while starting API : %s", e)
    logger.info("API stopped")