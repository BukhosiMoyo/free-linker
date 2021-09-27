# This is a free version of linktree.

* its mainly for extending links on your Social Accounts like Instagram, twitter and more

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/BukhosiMoyo/free-linker.git
$ cd free-linker
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ pipenv shell

```

Then install the dependencies:

```sh
(free-linker)$ pip install -r requirements.txt
```
Note the `(free-linker)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `pipenv`, It might also look diffent if you use diffrent virtual environment.

Once `pip` has finished downloading the dependencies make sure you are in the parent project folder:
```sh

(free-linker)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000`.

Here you will be able to view the link projects by clicking project list.
you will be given a list of project and here you can create more or view the
links inside the current projects

If you would like to contribute check the [CONTRIBUTION.md](https://github.com/BukhosiMoyo/free-linker/blob/master/CONTRIBUTION.md)
