# bootsmooth is a Google App Engine boilerplate for Python.

Benefits of using bootsmooth include:

-- Develop Web Apps on App Engine
bootsmooth is a starting point to quickly build your next app on Google's scalable cloud application platform.

-- Built with Python
bootsmooth.py is a Python library which integrates Flask, App Engine, and Pystache in to easy to use modules.

## Getting Started

- Install the App Engine Python SDK. See the README file for directions. You'll need python 2.7 and pip 1.4 or later installed too.

- Clone this repo with

git clone https://github.com/sonofapear/bootsmooth.git

- Install dependencies in the project's lib directory. Note: App Engine can only import libraries from inside your project directory.

cd bootsmooth
pip install -r requirements.txt -t lib

- Run this project locally from the command line:

dev_appserver.py .

- Visit the application http://localhost:8080 in your browser of choice

See the development server documentation for options when running dev_appserver.

For more information, check out the latest development guides at http://www.bootsmooth.com/ or the reference documentation at http://www.bootsmooth.com/reference
