# Create your vantage6 algorithm template

## What does this repository contain?

This repository contains template code from which new vantage6 algorithms can be
created. By answering a number of questions, a personalized template will be
created that allows the algorithm developer to focus on the algorithm rather
than on the infrastructure around it.

The template generator used in the background is
[copier](https://github.com/copier-org/copier).

## How to create your own algorithm?

You can create your own vantage6 algorithm template by running

```bash
v6 algorithm create
```

and this will start a questionnaire to help you personalize your algorithm.
Be sure that your vantage6 version is at least 4.1.0 - the command is only
available from that version onwards.

Alternatively, you can also run it outside of the vantage6 CLI:

```bash
# install required dependencies in your python environment
pip install copier pyyaml

# Create a new algorithm template
copier copy https://github.com/vantage6/v6-algorithm-template /path/to/my/new/algorithm
```

After creating the template, follow the checklist in the README to complete your
algorithm!

## Updating an algorithm

_You can also do this when you have already implemented your algorithm!_

This algorithm template generator may be updated for several reasons: it is
extended with new questions to personalize your template further, it contains
a bug, the vantage6 algorithm structure is updated, etc. In such cases, you
should update your algorithm. You can do so with

```bash
v6 algorithm update
```

which will take the latest version of this repository and use it to update the
algorithm code.

You can also use the copier CLI:

```bash
# install required dependencies in your python environment
pip install copier pyyaml

# Update an existing algorithm
copier copy https://github.com/vantage6/v6-algorithm-template /path/to/my/new/algorithm
```

## Developer instructions

### Release new version

To release a new version of the template generator, a new tag has to be added
with the semantic versioning format (e.g. `1.2.3`). Copier does not use the
latest on a certain main branch, but requires these tags to find the most recent
version of the template. So to release a new version, do:

```bash
git tag x.y.z
git push origin x.y.z
```

Note that we therefore do not follow the vantage6 way of defining tags with a
`version/` prefix - this does not conform to the `copier` standard.

### Developing new version

When developing a new version of the template generator, you can test it by

```bash
copier copy --trust --vcs-ref=HEAD . /path/to/my/new/algorithm
```

The `--vcs-ref=HEAD` flag will ensure that local changes are taken into account
when generating the template. This is useful when developing new features because then
it is not necessary to commit changes to test them.

Also note the `--defaults` option to fill out the same answers to the questions as in
the previous iteration, and the `-w` to overwrite files from last time without asking
confirmation.

```bash
copier copy --vcs-ref=HEAD -w --defaults --trust . /path/to/my/new/algorithm
```
