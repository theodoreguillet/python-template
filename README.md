# Python project template

## Summary
A basic template repo to use when starting new python project from stratch.

## Requirements
- python 3.8: https://www.python.org/downloads/release/python-380/
- pipenv: `python -m pip install -U pipenv`
- vscode (recommended): https://code.visualstudio.com/

## Getting started
1. Clone the repository
2. Install recommended extensions <br>
Navigate to `Extensions`, filter extensions using `@recommended` filter, click the ☁️ button to install all extensions at once

3. Install the dependencies
```
pipenv install --dev
```
4. Select python interpreter <br>
Ctrl+Shift+P > `Python: Select Interpreter` <br>
Select the path of the virtualenv created by pipenv. To know the path of your virtualenv you can use the command `pipenv --py`

5. Copy `.env.default` to `.env` and fill in the secret environment variables

6. Run the module
```
pipenv run start
```
To debug in vscode, navigate to `Run and Debug` and launch `Python: Module`

## Linting
```
pipenv run lint
```

## Testing
- Type checking
```
pipenv run type-check
```

- Unit testing
```
pipenv run test
```
Tests must be prefixed be `test_` and placed in the `test/` directory <br>
To run and debug tests in vscode, navigate to `Testing`

## Installing packages with pipenv
- Install a dependency
```
pipenv install <package>
```
- Install a dev dependency
```
pipenv install <package> --dev
```
- Show a dependency graph
```
pipenv graph
```
- Remove a dependency
```
pipenv uninstall <package>
```
Installed packages will be automatically added to Pipfile and Pipfile.lock by pipenv, do not use pip to install packages in the virtual environement created by pipenv.
