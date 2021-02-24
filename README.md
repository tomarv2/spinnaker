<p align="center">
    <a href="https://www.apache.org/licenses/LICENSE-2.0" alt="license">
        <img src="https://img.shields.io/github/license/tomarv2/spinnaker" /></a>
    <a href="https://github.com/tomarv2/spinnaker/tags" alt="GitHub tag">
        <img src="https://img.shields.io/github/v/tag/tomarv2/spinnaker" /></a>
    <a href="https://stackoverflow.com/users/6679867/tomarv2" alt="Stack Exchange reputation">
        <img src="https://img.shields.io/stackexchange/stackoverflow/r/6679867"></a>
    <a href="https://discord.gg/XH975bzN" alt="chat on Discord">
        <img src="https://img.shields.io/discord/813961944443912223?logo=discord"></a>
    <a href="https://twitter.com/intent/follow?screen_name=varuntomar2019" alt="follow on Twitter">
        <img src="https://img.shields.io/twitter/follow/varuntomar2019?style=social&logo=twitter"></a>
</p>

#Spinnaker + Jenkins

***
![Image description](https://files.gitter.im/tomarv2/NiDO/Screen-Shot-2020-04-10-at-4.48.56-PM.png)

Good starting point: https://www.spinnaker.io/guides/tutorials/codelabs/hello-deployment/
***

**Run halyard:**


docker run --rm -d -v /Users/demo/.hal:/root/.hal -v /Users/demo/.kube/config:/root/.kube/config -v /Users/demo/.aws/config:/root/.aws/config --name halyard gcr.io/spinnaker-marketplace/halyard:1.0.0