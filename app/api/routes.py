from flask import Blueprint, request, jsonify
from datetime import timedelta
from app.workflow.workflow import Workflow
from app.trigger.email_trigger import EmailTrigger
from app.trigger.scheduled_trigger import ScheduledTrigger
from app.action.extract_pdf_data import ExtractPDFDataAction
from app.action.send_email import SendEmailAction
from app.action.dummy_action import DummyAction
from app.workflow.workflow import Workflow

api = Blueprint("api", __name__)


@api.route("/extract_pdf_data_from_email_and_send_email", methods=["POST"])
def extract_pdf_data_from_email_and_send_email():
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


@api.route("/run_scheduled_dummy_action_every_ten_second", methods=["POST"])
def run_scheduled_dummy_action_every_ten_second():
    trigger = ScheduledTrigger("Dummy Scheduled Trigger", timedelta(seconds=10))
    dummy_action = DummyAction("Dummy Action")

    dummy_workflow = Workflow("Dummy Scheduled Workflow", trigger, [dummy_action])

    results = dummy_workflow.run()
    return jsonify(results)


@api.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "healthy"}), 200
