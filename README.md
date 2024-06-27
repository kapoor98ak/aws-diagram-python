# AWS Architecture Diagram Generator

This project uses the `diagrams` package to generate an AWS architecture diagram featuring a cross-region replicated S3 bucket, AWS Secrets Manager, RDS, EC2, and Elastic Beanstalk.

## Prerequisites

1. **Python 3.6+**
2. **pip** (Python package installer)

## Setup

1. **Clone the Repository**

    ```sh
    git clone <your-repo-url>
    cd aws-diagrams
    ```

2. **Install the Required Python Packages**

    ```sh
    pip install diagrams
    ```

3. **Install Graphviz**

    - **macOS:** Install using Homebrew
        ```sh
        brew install graphviz
        ```

    - **Ubuntu:** Install using APT
        ```sh
        sudo apt-get install graphviz
        ```

    - **Windows:** Download the installer from the [Graphviz website](https://graphviz.gitlab.io/download/) and follow the installation instructions.

4. **Verify Graphviz Installation**

    ```sh
    dot -V
    ```

## Running the Script

To generate the architecture diagram, run the following command:

```sh
python3 architecture_diagram.py
```

## Contributions
Feel free to open issues or submit pull requests to enhance the functionality of this project.

## License
This project is licensed under the MIT License.


