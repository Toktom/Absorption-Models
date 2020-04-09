# PyAbsorp
This is a package developed to be use to find the _Sound Absorption Coefficient_ through some implemented models, like  _Biot-Allard_, _Johnson-Champoux_ and others.

## Dependencies
**PyAbsorp** runs under Linux, Windows and MacOS, a **Python 3.8.2** installation is needed with the latest **Numpy**, **Scipy**. 
_Matplotlib is recommended, but not necessary._

## Implemented Models
- **Delany-Bazley** (with **Miki** and **Allard-Champoux** variation)
- **Biot-Allard**
- **Johnson-Champoux** (with **Allard** and **Lafarge** variation)
- **Rayleigh**

## How to Install
1. First make sure that you have the package [*setuptools*](https://pypi.org/project/setuptools/) installed.
2. Second make sure that you have the latest version of [Numpy](https://pypi.org/project/numpy/) and [Scipy](https://pypi.org/project/scipy/), as mentioned above.
3. Install through pip, by using the following command:
    ``` pip install git+https://github.com/Toktom/PyAbsorp ```
    
## Future Objectives
- [ ] Code validation
- [ ] Implement Pride variation to the Johnson-Champoux model.
- [ ] Implement models to the perforated plates situation.
- [ ] Theoretical review of the implemented models.
- [ ] English review

## How to contribute

For more details, read the [_CONTRIBUTING_](https://github.com/Toktom/PyAbsorp/blob/master/CONTRIBUTING.md) file.

### License
This project is under **MIT License**.
Check the license [here](https://github.com/Toktom/PyAbsorp/blob/master/LICENSE).

### Authors
- [**Michael Markus Ackermann**](https://github.com/Toktom)