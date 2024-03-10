# Contributing to PiCamera

## Table of Contents

- [Contributing to PiCamera](#contributing-to-picamera)
  - [Table of Contents](#table-of-contents)
  - [Branching strategy](#branching-strategy)
    - [Naming convention](#naming-convention)
    - [Main branch](#main-branch)
    - [Develop branch](#develop-branch)
    - [Feature branches](#feature-branches)
    - [User branches](#user-branches)
  - [Pull Requests](#pull-requests)
  - [Style guides](#style-guides)
    - [Commit messages](#commit-messages)
    - [Python code](#python-code)


## Branching strategy

All branches should adhere to the following heirarchy, branches should be merged into a branch from one of the above levels.

- main
- develop
- feature branches
- user branches

### Naming convention

All branch names should use kebab case. For example, `branch-name`.

### Main branch

The main branch should contain only working code, used for releases of the application.

Developers should never push directly to the main branch. New code should be merged by raising PRs from the develop branch or a hotfix branch.

### Develop branch

The develop branch should be used to contain code for the next version of the application in development. Ideally, code should be working before merged into the develop branch.

Developers should not push directly to the develop branch. New code should be merged by raising PRs from feature or user branches.

The develop branch should not fall behind the main branch.

### Feature branches

Feature branches should be used for the development of new features, bugfixes and documentation.

There are 4 types of feature branch.

| Type          | Purpose                                                                                                                                                           | Naming convention     |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- |
| Feature       | Used to store all changes dedicated to a specific feature or enhancement. Feature branches should be branched from the `develop` branch.                          | `feature/description` |
| Bug fix       | Used to store all changes dedicated to fixing a discovered bug in `develop`. Bug fix branches should be branched from the `develop` branch.                       | `bugfix`              |
| Hot fix       | Used to store all changes dedicated to fixing a bug in the `main` branch, that needs fixing fast. Hot fix branches should be branched from the `main` branch.     | `hotfix/description`  |
| Documentation | Used to store all changes dedicated to improving a section of the repository or software documentation. Documentation branches should be branched from `develop`. | `docs/description`    |

### User branches

Individual users should create branches with the convention `users/username/description`.

For example, John is developing code to add a login form to a web page. The code would be developed under `users/john/login-form`.

Upon completion of the work, a Pull Request should be raised to merge the changes into a feature branch or the develop branch.

> See [Pull Requests](#pull-requests) for more information on raising one.

## Pull Requests

Pull requests should be titled with a brief summary of the changes. The description should explain in more detail the changes made and why.

Pull requests must be approved by at least one other developer. Pull requests must be completed with a merge.

## Style guides

### Commit messages

### Python code
