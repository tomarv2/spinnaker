**Spinnaker + Jenkins (In-progress)**
***
![Image description](https://files.gitter.im/tomarv2/NiDO/Screen-Shot-2020-04-10-at-4.48.56-PM.png)

Good starting point: https://www.spinnaker.io/guides/tutorials/codelabs/hello-deployment/
***

**Run halyard:**


docker run --rm -d -v /Users/vtomar/.hal:/root/.hal -v /Users/vtomar/.kube/config:/root/.kube/config -v /Users/vtomar/.aws/config:/root/.aws/config --name halyard gcr.io/spinnaker-marketplace/halyard:1.0.0