import helpers
import requests

baseUrl = "https://raw.githubusercontent.com/"
grabPath = "ryan-bell-gea/onboarding.v1/main/README.md"
urls = []

#hit the GH repo and download the contents as a list of strings, each string being one line of the README
contentsList = requests.get(baseUrl+grabPath).text.splitlines()

#pull urls from each line and split filename from url, download each and place in User's Downloads/Onboarding/
for url in contentsList:
    if url.startswith("source"):
        url = url.split("=")[1]
        name = url.rsplit('/',1)[-1]
        pack = (name, url)
        urls.append(pack)

#hit each link from the GH README and download the file
for x in urls:
    helpers.url_response(x)

helpers.git_install()
helpers.java_install()
helpers.set_env("JAVA_HOME")
helpers.maven_install()
helpers.set_env("MAVEN_HOME")