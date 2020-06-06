### Build & Publish Docker Image
If you want to build your own image, 
replace `joeydebreuk/hellopython` with
your own docker.hub username and project
name `<username>/<imagename>`. Make sure you also change it in k8s/deployment.yaml


1. Build docker file `docker build -t hellopython .`
2. Docker tag it `docker tag hellopython joeydebreuk/hellopython`
3. Push to `docker push joeydebreuk/hellopython`

### Run deployment
`kubectl apply -f k8s`
