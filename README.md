# Create your vantage6 algorithm template

## What does this repository contain

This repository contains template code from which new vantage6 algorithms can be
created. By answering a number of questions, a personalized template will be
created that allows the algorithm developer to focus on the algorithm rather
than on the infrastructure around it.

The template generator used in the background is
[copier](https://github.com/copier-org/copier).

## How to create an algorithm

You can create your own vantage6 algorithm template by running

``` bash
v6 algorithm create
```

and this will start a questionnaire to help you personalize your algorithm.
Be sure that your vantage6 version is at least 4.1.0 - the command is only
available from that version onwards.

Alternatively, you can also run it outside of the vantage6 CLI:

```bash
copier copy https://github.com/vantage6/v6-algorithm-template /path/to/my/new/algorithm
```

## Updating an algorithm

*You can also do this when you have already implemented your algorithm!*

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
copier copy https://github.com/vantage6/v6-algorithm-template /path/to/my/new/algorithm
```

## Developer instructions

To release a new version of the template generator, a new tag has to be added
with the semantic versioning format (e.g. `1.2.3`). `Copier` does not use the
latest on a certain main branch, but requires these tags to find the most recent
version of the template. So to release a new version, do:

```bash
git tag x.y.z
git push origin x.y.z
```

Note that we therefore do not follow the vantage6 way of defining tags with a
`version/` prefix - this does not conform to the `copier` standard.
