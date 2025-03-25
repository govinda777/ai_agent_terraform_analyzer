# AI Agent Terraform Analyzer

## Overview
The AI Agent Terraform Analyzer is a tool designed to analyze Terraform configurations and streamline infrastructure documentation management. It integrates various components to assess AWS IAM policies, execute Terraform operations, and update documentation to reflect infrastructure changes.

## Architecture
The project is organized as follows:
- **agent/agent_logic.py**: Contains the core logic of the agent, orchestrating the analysis workflows.
- **agent/doc_updater.py**: Responsible for updating documentation based on analysis results.
- **agent/iam_analyzer.py**: Analyzes AWS IAM policies and related configurations.
- **agent/main.py**: The entry point for running the agent.
- **agent/terraform_wrapper.py**: Provides a wrapper for executing Terraform commands and managing Terraform state.

## Usage
1. Install the required dependencies and ensure Python is set up.
2. Configure your environment, including AWS credentials and Terraform configurations.
3. Run the agent using the command:
   ```
   python agent/main.py
   ```
4. The agent will analyze your Terraform files and update documentation accordingly.

## Configuration
- Verify and adjust settings in the Terraform configuration files located in the <code>infra/terraform</code> directory.
- Ensure all necessary environment variables and credentials are properly configured.

## Development and Testing
- Follow coding best practices and refer to existing modules for guidance.
- Run tests located within the <code>infra/tests</code> directory to validate functionality.
- Contributions are welcome—please adhere to the project's coding standards and guidelines.

## Roadmap
- Expand analysis capabilities to support additional cloud providers.
- Enhance logging, error handling, and reporting mechanisms.
- Improve the documentation update process based on user feedback.

## License
Refer to the LICENSE file for licensing details.