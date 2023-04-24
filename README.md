# Cloud Native Monitoring

## Pre-requisites
- [Install python](https://www.python.org/downloads/) ```>=``` 3.11 
- [Install docker](https://www.docker.com/products/docker-desktop/)
- [Install Kubectl](https://kubernetes.io/docs/tasks/tools/)
- [Vscode](https://code.visualstudio.com/) or any IDE of choice

## Step by step process
  - First and formost if you don't have a aws credentials create one
    - Create a root user
    - Create an IAM user
        - Login as an IAM user
        - Create the access_key and 
        - Add a programmatical access key token and align it with required permissions
            - If aws cli is not installed, then install it through the [link](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
            - Permission required: AWS ECR related permission (assuming that a permission group is created and then that permission is assigned to the IAM user). Check the created credentials are working as expected and add the credentials created to aws cli by using. [Reference](https://docs.aws.amazon.com/cli/latest/reference/configure/index.html)
                ```
                aws configure
                ```
    - Install pip - [reference](https://pip.pypa.io/en/stable/installation/)
        ```
        python -m ensurepip --upgrade
        ```
    - Install pipenv - [reference](https://pypi.org/project/pipenv/)
        ```
        pip install pipenv
        ```
    - Install all the requirements (assuming that requirements.txt is in project root directory)
        ```
        pipenv install -r requirements.txt
        ```
    

            
            