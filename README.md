# devops_proj_3

## Steps to setup CI in Jenkins:
1. Install jenkins with docker support.
2. Download plugins: Docker, Docker Pipeline, workspace cleanup, Github plugin
3. Configure Credentials in Jenkins: AWS_ACCESS_KEY_ID (secret text), AWS_SECRET_ACCESS_KEY (secret text), DOCKERHUB_CREDS (username with password)
4. Create a new pipeline and use the jenkins file in this repo to configure the pipeline


## Steps to run the job to check if there are running ec2 instances:
1.Configure env variables to access AWS :AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY . If running on jenkins, configure as secret text
2.Run docker image:
```
docker run --env $AWS_ACCESS_KEY_ID --env $AWS_SECRET_ACCESS_KEY matanmeshi1/devops_proj3:lts
```

