# instahack-flask
A flask app which asks you the url of the instagram picture and returns the picture which you can download and share. It works only for public accounts. Private accounts doesn't get affected.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
You need to have various python libraries, few important are
* python3 (everything is in python3, my default python verison is 3.6.7 and my deafult pip is pi3)
* a virtual environment (detailed in the *Installing* part)
* Flask (framework)
* requests and bs4 (modules)

### Installing
1. First of all you need to setup your virtual environment. (setup and activate)
```
pyvenv-3.6 ihenv
```
Install the python virtual environment setup using this command `sudo apt install python3.6-venv`
```
source ihenv/bin/activate
```
2. Install all the dependencies, python modules 
```
pip3 install -r requirements
```
3. Run the python app
```python3 app.py
```
Now, the app should be running on the localhost, browse to to the link where your app is running. (most probably, http://127.0.0.1:5000/)

## Running the tests
1. Once the site is running live. Give your desired instagram picture url and click on *Submit* button. It will return the high quality original picture.

### And coding style tests
1. If you are using any other module for implementing any new features, please install the modules in the virtual environment and update it in the requirements.txt by using the below command.
```
pip freeze > requirements.txt
```

## Built With
* [Flask](http://flask.pocoo.org/docs/1.0/) - Web framework used for backend.
* [Bootstrap](http://getbootstrap.com/docs/4.1/getting-started/introduction/) - Web framework used for frontend.

## Contributing
If you are really interested in contributing to the please follow the below steps and rules.
1. Fork the project. (Give a star :star: to the repo before you fork :P)*
2. Clone it.
```
git clone https://github.com/<username>/instahack-flask/
```
3. Look for any issues clicking the issues tab. Go through it and assign take one. Make sure you get assigned or atleast say that you are gonna work on it.
4. Always create a new branch and work on the feature or bug. Check this if you are not that familiar with branching, [Git Branching](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)
5. Please follow the template created for raising issues or sending pull requests.

## Authors
* **Venu Vardhan** - *Initial work* - [vchrombie](https://github.com/vchrombie)

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments
* References: [How to Download Instagram Photos](https://www.digitaltrends.com/social-media/how-to-download-instagram-photos/). Tried to automate one of the methods using python.