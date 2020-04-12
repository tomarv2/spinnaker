**Spinnaker + Jenkins (In-progress)**
***
![Image description](https://files.gitter.im/tomarv2/NiDO/Screen-Shot-2020-04-10-at-4.48.56-PM.png)

Good starting point: https://www.spinnaker.io/guides/tutorials/codelabs/hello-deployment/
***

To start with I have been using Spinnaker for nearly 3 years.

**Run halyard:**


docker run --rm -d -v /Users/demo/.hal:/root/.hal -v /Users/demo/.kube/config:/root/.kube/config -v /Users/demo/.aws/config:/root/.aws/config --name halyard gcr.io/spinnaker-marketplace/halyard:1.0.0