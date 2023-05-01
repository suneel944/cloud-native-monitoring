# :sparkles: Cloud Native Monitoring :sparkles:

## :ledger: Pre-requisites
- [Install python](https://www.python.org/downloads/) ```>=``` 3.11 
- [Install docker](https://www.docker.com/products/docker-desktop/)
- [Install Kubectl](https://kubernetes.io/docs/tasks/tools/)
- [Install AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
- [Intall K9s](https://k9scli.io/topics/install/)
- [Install act](https://github.com/nektos/act)
- [Vscode](https://code.visualstudio.com/) or any IDE of choice

## :blue_book: Step by step process
  - First and formost if you don't have a aws credentials create one
    - Create a root user
    - Create an IAM user
        - Login as an IAM user
        - Create the access_key and 
        - Add a programmatical access key token and align it with required permissions
            - Permission required: AWS ECR related permission (assuming that a permission group is created and then that permission is assigned to the IAM user). Check the created credentials are working as expected and add the credentials created to aws cli by using. [Reference](https://docs.aws.amazon.com/cli/latest/reference/configure/index.html)
                ```
                aws configure
                ```
        - Navigate to IAM console and select the created IAM and create a role called eksClusterRole. [link](https://docs.aws.amazon.com/eks/latest/userguide/service_IAM_role.html)
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
    - Add AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY to github secrets > actions > new repository secret

## :writing_hand: Running the application locally
 - Build the docker image
    ```
    docker build . -t flask/cloud-native-monitoring:latest
    ```
 - Use the docker compose to start running the container
    ```
    docker compose up
    -OR-
    docker compose up --build
    ```

## :bulb: Fancy running your github action locally
 - Create a file called .secrets in the root directory to mimic the github secrets and store all the secrets
    ```
    AWS_ACCESS_KEY_ID=<iam_key_id>
    AWS_SECRET_ACCESS_KEY=<iam_secret_access_key>
    EKS_CLUSTER_ROLE=<cluster_role_name>
    EKS_NODE_ROLE=<node_role_name>
    ```
 - Once secret file is ready, then you are good to with the execution of the github workflow file locally
   ```
   act --secret-file <relative_path_to_.secrets_file>
   ```
## :camera_flash: Dashboard
![Dashboard snapshot](https://user-images.githubusercontent.com/45133346/235008179-2ab0f442-311b-447d-a6bf-678fbd7a09e7.png)
## :vhs: Demo
https://user-images.githubusercontent.com/45133346/235455621-27d19717-01da-42f1-9fee-15840dd3b53f.mp4
