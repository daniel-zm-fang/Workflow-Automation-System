# Workflow Automation System

This project implements a flexible **workflow automation system**, similar to **Zapier**. It demonstrates how to build a system that can automate multi-step workflows triggered by events like receiving an email.

## How It Works

1. **Triggers**: The system starts with a trigger (e.g., receiving an email).
2. **Actions**: It then executes a series of actions (e.g., extracting data from PDFs, sending emails).
3. **Workflow**: Triggers and actions are combined into a workflow.
4. **API**: The system exposes an API to run workflows using HTTP requests.

## Setup and Running

1. Clone the repository:

   ```bash
   git clone https://github.com/daniel-zm-fang/Workflow-Automation-System.git
   cd workflow-automation-system
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   python run.py
   ```

## Usage & Examples

To run a workflow, send a POST request to that workflow's endpoint with the necessary configuration.

Two example workflows can be found in the `demo_1.py` and `demo_2.py`:

To run them (make sure you execute `python run.py` first):

```bash
python demo_1.py

python demo_2.py
```

## Extending the System

To add new triggers or actions:

1. Create new Trigger or Action classes inheriting from `BaseTrigger` or `BaseAction`.
2. Mix and match Triggers and Actions, package them in a Workflow classto create new workflows.
3. Instantiate new endpoints in the `routes.py` file.

## Note

This is an MVP demonstration. Inputs and outputs of triggers and actions are mocked.

## Challenges & Next Steps

- How can we make it easy for users to create workflows without technical knowledge?
  
   A: visual workflow builder: Create a drag-and-drop interface where users can visually connect triggers and actions. Also, offer a library of common pre-built workflows.

- How do we handle long-running workflows?

   A: Users should use **persistent** workflows, which is already supported. In production, we can save the state of a workflow in a database to allow recovery from failures.

- How can we make the system scalable to handle thousands of workflows running concurrently?

   A: Use horizontal scaling techniques with Kubernetes. each pod is a complete instance of application, capable of handling any workflow.Also use load balancers to distribute workflow executions across multiple servers. Microservice architecture is not suitable here. For example, if a critical service like trigger service goes down, all workflows can not be executed.

- How do we manage and update the integrations as third-party APIs change?

   A: We can maintain different versions of integrations to support both old and new API versions. Automated testing can be used to quickly identify issues when APIs change.

- How do we ensure the security of user credentials for various services?

   A: Use strong encryption for storing user credentials and sensitive data, both in transit and in storage. Where possible, use OAuth 2.0 instead of storing raw credentials.
