from flask import Blueprint, request, jsonify
from app.workflow.workflow import Workflow
from app.trigger.email_trigger import EmailTrigger
from app.action.extract_pdf_data import ExtractPDFDataAction
from app.action.send_email import SendEmailAction
from app.workflow.workflow import Workflow

api = Blueprint("api", __name__)


@api.route("/run_workflow", methods=["POST"])
def run_workflow():
    data = request.json
    email_trigger = EmailTrigger(
        "Insurance Application Email",
        data["imap_server"],
        data["email_address"],
        data["email_password"],
    )

    extract_pdf_data = ExtractPDFDataAction("Extract PDF Data", data["company"])
    send_email = SendEmailAction(
        "Send Summary Email",
        data["smtp_server"],
        data["email_address"],
        data["email_password"],
    )

    insurance_workflow = Workflow(
        "Insurance Application Workflow", email_trigger, [extract_pdf_data, send_email]
    )

    results = insurance_workflow.run()
    return jsonify(results)


@api.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "healthy"}), 200
