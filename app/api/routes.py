from flask import Blueprint, request, jsonify
from datetime import timedelta
from app.trigger.email_trigger import EmailTrigger
from app.trigger.scheduled_trigger import ScheduledTrigger
from app.action.extract_pdf_data import ExtractPDFDataAction
from app.action.send_email import SendEmailAction
from app.action.dummy_action import DummyAction
from app.workflow.one_off import OneOffWorkflow
from app.workflow.persistent import PersistentWorkflow

api = Blueprint("api", __name__)

workflows = {}


@api.route("/run_one_off_pdf_email_workflow", methods=["POST"])
def run_one_off_pdf_email_workflow():
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

    workflow = OneOffWorkflow(
        "One-off Insurance Application Workflow",
        email_trigger,
        [extract_pdf_data, send_email],
    )

    results = workflow.run()
    return jsonify(results)


@api.route("/start_persistent_pdf_email_workflow", methods=["POST"])
def start_persistent_pdf_email_workflow():
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

    workflow = PersistentWorkflow(
        "Persistent Insurance Application Workflow",
        email_trigger,
        [extract_pdf_data, send_email],
        check_interval=10.0,  # Check for new emails every 10 seconds
    )

    workflow_id = f"pdf_email_{len(workflows) + 1}"
    workflows[workflow_id] = workflow
    workflow.run()

    return jsonify({"status": "Workflow started", "workflow_id": workflow_id})


@api.route("/start_persistent_scheduled_dummy_workflow", methods=["POST"])
def start_persistent_scheduled_dummy_workflow():
    trigger = ScheduledTrigger("Dummy Scheduled Trigger", timedelta(seconds=10))
    dummy_action = DummyAction("Dummy Action")

    workflow = PersistentWorkflow(
        "Persistent Dummy Scheduled Workflow",
        trigger,
        [dummy_action],
        check_interval=1.0,  # Check trigger condition every second
    )

    workflow_id = f"scheduled_dummy_{len(workflows) + 1}"
    workflows[workflow_id] = workflow
    workflow.run()

    return jsonify({"status": "Workflow started", "workflow_id": workflow_id})


@api.route("/stop_workflow/<workflow_id>", methods=["POST"])
def stop_workflow(workflow_id):
    if workflow_id in workflows:
        workflows[workflow_id].stop()
        del workflows[workflow_id]
        return jsonify({"status": f"Workflow {workflow_id} stopped"})
    else:
        return jsonify({"status": f"Workflow {workflow_id} not found"}), 404


@api.route("/list_workflows", methods=["GET"])
def list_workflows():
    workflow_list = [
        {"id": workflow_id, "name": workflow.name, "type": type(workflow).__name__}
        for workflow_id, workflow in workflows.items()
    ]
    return jsonify({"workflows": workflow_list})


@api.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "healthy"}), 200
