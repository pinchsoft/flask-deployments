flask-deployments
=================

Automated, Versioned Deployments for Python Flask Apps

This repo contains the code referenced in [Automated Versioned Deployments for Flask (Or Any Python) Webapps](http://essentialcode.com/2012/01/24/automated-versioned-deployments-for-flask-or-any-python-webapps/, "Automated Versioned Deployments for Flask (Or Any Python) Webapps").

Example usage:

```bash
# Positional arguments
fab upload:demo,1.0.1,0264103894,/home/jread/project

# Named arguments
fab upload:target=demo,version=1.0.1,revision=0264103894,release_dir=/home/jread/project

# combination
fab upload:demo,1.0.1,revision=0264103894,release_dir=/home/jread/project
```
