# Workflow Automation System

This project implements a flexible **workflow automation system**, similar to **Zapier**, with a focus on insurance application processing. It demonstrates how to build a system that can automate multi-step workflows triggered by events like receiving an email.

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
