
[![Downloads](https://pepy.tech/badge/ratemyprofessorapi)](https://pepy.tech/project/ratemyprofessorapi)
[![Supported Versions](https://img.shields.io/pypi/pyversions/ratemyprofessorapi.svg)](https://pypi.org/project/ratemyprofessorapi)

# RateMyProfessorAPI


## Setup
**Please note that this has only been tested on Python 3.9.1. If this doesn't work for older versions, open up an Issue.**
**This project requires Python 3.5 or above. This WILL NOT WORK on Python 3.4 or lower.**

Install the package using the following command:
```
python -m pip install RateMyProfessorAPI 
```

To update the package, use the following command:
```
python -m pip install RateMyProfessorAPI --upgrade
```

To use the package in your program, please import the package:
```py
import ratemyprofessor
```

## Uninstallation
To uninstall the package, use the following command:
```
python -m pip uninstall RateMyProfessorAPI
```

## Usage
To retrieve a list of professors, you have to first specify the school:
```python
ratemyprofessor.get_school_by_name("School Name")
```
This will return `None` if no school is found corresponding with that name. 
Alternatively, to search for multiple schools, use
```python
ratemyprofessor.get_schools_by_name("School Name")
```
This will return a list of `School`s.

Using the `School` object obtained from the previous commands, you can use that to find the professor:
```python
ratemyprofessor.get_professor_by_school_and_name(school, "Professor Name") 
```
where school refers to a `School` object.
Alternatively, to search for multiple professors, use
```python
ratemyprofessor.get_professor_by_schools_and_name(school, "Professor Name") 
```
This will return a list of `Professor`s.

## Documentation
I am currently working on documentation but as of now there is no documentation yet. Sorry!

## Example
```python
import ratemyprofessor

professor = ratemyprofessor.get_professor_by_school_and_name(
    ratemyprofessor.get_school_by_name("Case Western Reserve University"), "Connamacher")
if professor is not None:
    print("%sworks in the %s Department of %s." % (professor.name, professor.department, professor.school.name))
    print("Rating: %s / 5.0" % professor.rating)
    print("Difficulty: %s / 5.0" % professor.difficulty)
    print("Total Ratings: %s" % professor.num_ratings)
    if professor.would_take_again is not None:
        print(("Would Take Again: %s" % round(professor.would_take_again, 1)) + '%')
    else:
        print("Would Take Again: N/A")

```

**Output:**
```
Harold Connamacher works in the Computer Science Department of Case Western Reserve University.
Rating: 4.7 / 5.0
Difficulty: 3.8 / 5.0
Total Ratings: 102
Would Take Again: 86.2%
```
See `examples` for more examples.

## Acknowledgements and License
This can be seen as a continuation of the [RateMyProfessorPyAPI](https://pypi.org/project/RateMyProfessorPyAPI/) project that can also be found on GitHub [here](https://github.com/remiliacn/RateMyProfessorPy).
This serves as an inspiration for this project.
This project is also licensed under the [Apache 2.0 License](http://www.apache.org/licenses/LICENSE-2.0). See LICENSE for more details.
