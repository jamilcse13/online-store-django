## configure virtual environment
- install pipenv: pip3 install pipenv
- then run *pipenv shell* for install virtual env
- now we can install any package inside the virtual env:
    - ex: pipenv install pytest
- we can follow up which packages are installed by using:
    - pip3 freeze

- [django-cors-headers](https://github.com/adamchainz/django-cors-headers)
    - Here we have used *django-cors-headers* for retrict our api access
    - for this we need to add some codes and extensions in project's settings.py
    - allowing hosts will be declared at ALLOWED_HOSTS

- media:
    - we added *media* directory at the root of the project and setup settings and urls
    - here we stored images, audios, videos and each type of media files

#### some key point:
- [CORS](https://www.educative.io/edpresso/how-cors-cross-origin-resource-sharing-works) (Cross-Origin Resource Sharing)
    - This allows in-browser requests to your Django application from other origins.
