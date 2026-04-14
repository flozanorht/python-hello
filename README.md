Minimal Containerfiles for a "Hello, world" Python application, using different base images.

The application returns the version of its Python runtime and its Flask framework as a JSON response.

During the build, reference the specific version of the Containerfile you want, for example to use [Hummingbird](https://hummingbird-project.io/) builder and runtime images:

````
$ podman build -t flask-app -f Containerfile.hummingbird
````

Then run the resulting container:

````
$ podman run -d -p 127.0.0.1:5000:5000 --name my-flask-app flask-app
````

And test it:

````
$ curl http://127.0.0.1:5000
{
  "flask_version": "3.1.3",
  "python_version": "3.12.13"
}
````

To build using [Calunga libraries](https://github.com/calungaproject/index/blob/main/docs/getting_started.md), copy the `pip.conf.orig` file to `pip.conf` and edit it to include a valid username and password for accessing the Red Hat registry. Then reference the file as a container secret:

````
$ podman build -t flask-app --secret id=pip.conf,src=pip.conf -f Containerfile.calunga
````

You can use a [free Red Hat Developers subscription](https://developers.redhat.com/articles/faqs-no-cost-red-hat-enterprise-linux), and it is recommended that you create a [service account](https://access.redhat.com/terms-based-registry/accounts) instead of using your Red Hat customer portal login.

Some containerfiles, for example the one using UBI with S2I, may require a login to the Red Hat terms-based registry, For this, you can use your Red Hat customer portal login (from a free Red Developer subscription) or a registry service account:

````
$ podman login registry.redhat.io
Username: <your Red Hat login or service account name>
Password: <your Red Hat password or service account token>
````

All containerfiles are hardcoded to use Python 3.12 because this is the version available on all kinds of base images, but they should work with newer Python releases, if available. I assume the reader will be able to make the necessary changes.

I didn't include logic, such as build args, to enable changing Python versions without making edits to the containerfiles to privilege simplicity and legibility of the code.

I'm not using a "production ready" setup, for example by using gunicorn, becasue it is not available yet from the Calunga index.
