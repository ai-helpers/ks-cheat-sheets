# Kownledge Sharing - AWS

---

## Table of Contents (ToC)

- [Kownledge Sharing - AWS](#kownledge-sharing---aws)
  - [Table of Contents (ToC)](#table-of-contents-toc)
  - [AWS Command-Line Interface (CLI)](#aws-command-line-interface-cli)
    - [MacOS](#macos)
    - [Linux](#linux)
    - [Configuration for the AWS CLI](#configuration-for-the-aws-cli)
  - [AWSume Command-Line Utility](#awsume-command-line-utility)
    - [Installation](#installation)
    - [Configuration](#configuration)
    - [Usage](#usage)
  - [SAML-to-AWS (`saml2aws`) Command-Line Utility](#saml-to-aws-saml2aws-command-line-utility)
    - [MacOS](#macos-1)
    - [Linux](#linux-1)
  - [Configuration for SAML-to-AWS](#configuration-for-saml-to-aws)
  - [Additional AWS SSO Setup and Configuration](#additional-aws-sso-setup-and-configuration)
    - [Install Required Packages](#install-required-packages)
    - [Update Your Shell Configuration](#update-your-shell-configuration)
    - [Verify Your AWS SSO Configuration](#verify-your-aws-sso-configuration)
    - [Finalize AWSume Configuration](#finalize-awsume-configuration)
    - [Configure AWS SSO Login and Profiles](#configure-aws-sso-login-and-profiles)
  - [References](#references)
    - [AWS Inference - Blog links](#aws-inference---blog-links)
    - [AWS Courses (free)](#aws-courses-free)

---

## AWS Command-Line Interface (CLI)

The AWS CLI enables you to interact with AWS services from your terminal. Below are the installation and configuration instructions for macOS and Linux.

### MacOS

Install the AWS CLI using Homebrew:

```bash
brew install awscli
```
### Linux

Install the AWS CLI by downloading and installing the ready-to-use AWS tar-ball:

```bash
mkdir -p ~/tmp/awscliv2 && \
  curl -Ls https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip \
       -o ~/tmp/awscliv2/awscliv2.zip && \
  pushd ~/tmp/awscliv2 && \
  unzip -qq awscliv2.zip && \
  rm -f awscliv2.zip
sudo ./aws/install  # use --update if necessary
popd && \
rm -rf ~/tmp/awscliv2

# Verify installation
aws --version
```

Expected output:
```bash
aws-cli/2.13.33 Python/3.11.6 Linux/4.18.0-521.el8.x86_64 exe/x86_64.centos.8 prompt/off
```

### Configuration for the AWS CLI
1. **Configure Credentials and Setting**
Run the following command to set up your AWS credentials and configuration files:

```bash
aws configure
```

When prompted, provide:
- AWS Access Key ID: Aaaaaaa
- AWS Secret Access Key: xxxxxxxx
- Default region name: eu-west-1
- Default output format: json

2. **Verify Your Configuration**

Check the caller identity to ensure the credentials are working correctly:

```bash
 aws sts get-caller-identity

{
    "UserId":  "012345678901",
    "Account": "012345678901",
    "Arn": "arn:aws:iam::440510661531:root"
}
_EOF
```

3. **Working with s3**

```bash
# List the content of a public S3 bucket:
aws s3 ls --human --summarize s3://demand-forecast/
# List the content of another S3 bucket recursively:
aws s3 ls --human --summarize --recursive s3://turnover-forecast/
```

4. **Configuration Files**

The AWS CLI creates two configuration files in the `~/.aws/` directory: `config` and `credentials`.

```bash
ls -lFh ~/.aws/

total 8.0K
-rw------- 1 user group  44 Nov  9 15:39 config
-rw------- 1 user group 116 Nov  9 15:39 credentials
_EOF
```

5. **Adding Additional Profiles**

To add another profile (e.g., `demand-forecast`), append the following to your `~/.aws/credentials` file:
```bash
cat >> ~/.aws/credentials << _EOF

[demand-forecast]
aws_access_key_id = Aaaaaaa
aws_secret_access_key = xxxxxxxx
_EOF
```

## AWSume Command-Line Utility
[AWSume](https://github.com/trek10inc/awsume) is a Python-based tool that helps you manage AWS roles and profiles seamlessly.

### Installation

Install AWSume using Python's pip:
```bash
python -mpip install -U awsume
```

Reset your shell to load the new configuration:
```bash
exec bash 
# or exec zsh if you're using zsh
```

### Configuration

Configure AWSume to set up aliases and autocompletion:

```bash
awsume-configure
```

This process sets up:

Aliases in your shell profile (e.g., ~/.bash_profile or ~/.zshenv)
Autocomplete scripts for easier command-line use
Reset your shell again after configuration:

```bash
exec bash  # or exec zsh
```

### Usage

Assume a role/profile from your AWS credentials:

For the default profile:

```bash
awsume default
aws sts get-caller-identity
```

For a ```demand-forecast``` profile:

```bash
awsume demand-forecast
aws sts get-caller-identity
```

## SAML-to-AWS (`saml2aws`) Command-Line Utility
In environments where SAML is used for authentication, the [saml2aws](https://github.com/Versent/saml2aws) utility enables you to authenticate via SAML without needing to use a web browser.

### MacOS
Install `saml2aws` using Homebrew:

```bash
brew install saml2aws
```

### Linux
Install `saml2aws` using the latest tar-ball:

```bash
SAML2AWS_VER=$(curl -Ls https://api.github.com/repos/Versent/saml2aws/releases/latest | grep 'tag_name' | cut -d'v' -f2 | cut -d'"' -f1) && \
curl -Ls \
     https://github.com/Versent/saml2aws/releases/download/v${SAML2AWS_VER}/saml2aws_${SAML2AWS_VER}_linux_amd64.tar.gz -o saml2aws.tar.gz && \
tar zxf saml2aws.tar.gz && rm -f saml2aws.tar.gz README.md LICENSE.md
sudo mv -f saml2aws /usr/local/bin/ && sudo chmod 775 /usr/local/bin/saml2aws
```

## Configuration for SAML-to-AWS
Create the configuration file for saml2aws if it does not already exist:

```bash
saml2aws configure
```

During configuration, you will be prompted for details such as:
- Provider: (e.g., Ping)
- AWS Profile: (e.g., saml)
- URL: (e.g., https://idp.example.com)
- Username: (e.g., USERID)

This creates the `~/.saml2aws` configuration file.

## Additional AWS SSO Setup and Configuration

For environments using AWS SSO and for enhanced profile management, you can install and configure additional tools like `aws-sso-util`.

### Install Required Packages

Install both `awsume` and `aws-sso-util`:

```bash
python -mpip install -U awsume aws-sso-util
```

### Update Your Shell Configuration
Add the following environment variables to your ~/.bashrc (or the relevant shell configuration file):

```bash
export AWS_DEFAULT_SSO_START_URL="https://idp.example.com"
export AWS_DEFAULT_SSO_REGION="eu-west-1"
```

Reload your shell configuration:

```bash
source ~/.bashrc
```

### Verify Your AWS SSO Configuration
Check your configuration with:

```bash
aws-sso-util check
```

You should see output confirming your settings (refer to screenshots such as image-20240304-111829.png for an example).

### Finalize AWSume Configuration

Finalize AWSume's setup by running:

```bash
awsume-configure
```

Then reload your shell again:

```bash
source ~/.bashrc
```

Refer to screenshots like `image-20240304-114639.png` for expected output.

  > Note:
  If you encounter an error such as “Module not found” for setuptools when running awsume-configure, do the following:

  1. **Activate the pipx virtual environment for AWSume:**
  ```bash
  source /path/to/venv/bin/activate
  ```

  2. **Install setuptools:**
  ```bash
  pip install setuptools
  ```

### Configure AWS SSO Login and Profiles
1. **Log In to AWS SSO**

Use the AWS SSO start URL to log in:

```bash
aws-sso-util login https://idp.example.com eu-west-1
```

Your web browser will open to complete the authentication process.

2. **Automatically Populate AWS Profiles**

Populate your AWS configuration with SSO profiles:

```bash
aws-sso-util configure populate --region eu-west-1
```

3. **Manually Add Project Profiles**

In your AWS configuration file (`~/.aws/config`), add one profile per project’s role and environment. For example, for the project demand-forecast:

```ini
[profile demand-forecast-pp]
role_session_name = demand-forecast-pp
source_profile = hpc1-pp.AssumeRole
region = eu-west-1
role_arn = arn:aws:iam::123456789998:role/demand-forecast-pp

[profile demand-forecast-pr]
role_session_name = demand-forecast-pr
source_profile = hpc1-pp-prod.AssumeRole
region = eu-west-1
role_arn = arn:aws:iam::123456789999:role/demand-forecast-pr
```

4. **Assume a Role with AWSume**

Now that your profiles are configured, assume the desired role with AWSume. For example, to assume the dsfoperations-infra-pp profile:

```bash
awsume dsfoperations-infra-pp
```

Verify your connection by checking:

```bash
aws sts get-caller-identity
```

The output should reflect the details of the assumed role.

>  Troubleshooting:
  If you encounter an error like aws command not found when running aws sts get-caller-identity, refer to the [AWS CLI installation instructions](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html#getting-started-install-instructions).

---

## References
### AWS Inference - Blog links
- [Blog - SageMaker Inference Highspot page](https://aws.highspot.com/items/671814eaf8e8a0fb2ee30a20?lfrm=shp.0)
- [Blog - Scale down down to zero](https://aws.amazon.com/blogs/machine-learning/unlock-costsavings-with-the-new-scale-down-to-zero-feature-in-amazon-sagemaker-inference/)
- [Blog - Fast Model loader:](https://aws.amazon.com/blogs/machine-learning/introducing-fastmodel-loader-in-sagemaker-inference-accelerate-autoscaling-for-your-large-languagemodels-llms-part-1/)
- [Blog - Container Caching:](https://aws.amazon.com/blogs/machine-learning/supercharge-your-autoscaling-for-generative-ai-inference-introducing-container-caching-in-sagemaker-inference/)
- [Blog - Updated inference optimization toolkit](https://aws.amazon.com/blogs/machinelearning/:amazon-sagemaker-launches-the-updated-inference-optimization-toolkit-forgenerative-ai/)
- [Blog - Deploy hundreds of LoRA adpaters](https://aws.amazon.com/blogs/machine-learning/easilydeploy-and-manage-hundreds-of-lora-adapters-with-sagemaker-efficient-multi-adapterinference/)
- [Blog - Use Bedrock tooling with SageMaker Jumpstart](https://aws.amazon.com/blogs/machinelearning//use-amazon-bedrock-tooling-with-amazon-sagemaker-jumpstart-models/)
- [Blog - G6e support for SageMaker inference](https://aws.amazon.com/blogs/machinelearning/amazon-sagemaker-inference-now-supports-g6e-instances/)

### AWS Courses (free)

- Building Generative AI Applications on Amazon Bedrock: [Link](https://lnkd.in/eM4nRWaW)
- Generative AI Learning Plan for Decision Makers: [Link](https://lnkd.in/ekGRVWys)
- Introduction to Amazon CodeWhisperer: [Link](https://lnkd.in/eZFxyV8a)
- Introduction to Generative AI: [Link](https://lnkd.in/eZFxyV8a)
- Amazon Transcribe - Getting Started: [Link](https://lnkd.in/eZe6KNNd)
- Fundamentals of Prompt Engineering: [Link](https://lnkd.in/e8QgdFz7)
- Building Language Models on AWS: [Link](https://lnkd.in/e6UsvekQ)
- Low-Code Machine Learning on AWS: [Link](https://lnkd.in/eUk-6sf4)
