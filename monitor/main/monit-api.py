from flask import Flask, abort, jsonify
import json
import os
import sys
sys.path.append(os.path.abspath('../reports/report'))
# from log_report import logLastReport, logListReports
from get_report import  getReportId
from create_report import  report_path, reports_path
# on crée un ptit objet Flask, nécessaire pour ajouter des routes
app = Flask(__name__)
app.secret_key = b'SECRET_KEY'

# utilisation d'un décorateur Python avec @ pour donc décorer une fonction
# c'est l'ajout de ce décorateur qui permet d'ajouter une route
# c'est dans la doc de Flask, nous on obéit :D
@app.route('/reports', methods=['GET'])
def get_reports():
    reports_id = []
    for report_name in [file.name for file in os.scandir(reports_path)]:
        report_id = getReportId(report_name)
        reports_id.append( {
            "id": report_id,
        })
    if reports_id is not None:
        return jsonify(reports_id)
    else:
        abort(404)


@app.route('/reports/<input_report_id>', methods=['GET'])
def get_reportById(input_report_id=None):
    if input_report_id is not None:
        for report_name in [file.name for file in os.scandir(reports_path)]:
            report_id = getReportId(report_name)
            if report_id == input_report_id:
                report_name_found = report_name
        if report_name_found is not None:
            file = open(report_path + report_name_found)
            report = json.load(file)
            file.close()
        else:
            abort(404)

        if report is not None:
            return jsonify(report)
        else:
            # la ptite 404 clean quand on demande une ressource qui n'existe pas
            abort(404)
    else:
        abort(404)

if __name__ == '__main__':
    app.run(host='37.44.247.226', port=80, debug=True)