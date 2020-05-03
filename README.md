[![wikipediaKnowledge Homepage](https://img.shields.io/badge/wikipediaKnowledge-develop-orange.svg)](https://github.com/davidvelascogarcia/wikipediaKnowledge/tree/develop/programs) [![Latest Release](https://img.shields.io/github/tag/davidvelascogarcia/wikipediaKnowledge.svg?label=Latest%20Release)](https://github.com/davidvelascogarcia/wikipediaKnowledge/tags) [![Build Status](https://travis-ci.org/davidvelascogarcia/wikipediaKnowledge.svg?branch=develop)](https://travis-ci.org/davidvelascogarcia/wikipediaKnowledge)

# Wikipedia Knowledge: wikipediaKnowledge (Python API)

- [Introduction](#introduction)
- [Running Software](#running-software)
- [Requirements](#requirements)
- [Status](#status)
- [Related projects](#related-projects)


## Introduction

`wikipediaKnowledge` module use `wikipedia` API in `python`. This module receive questions to get information with `YARP` port, send request to `Wikipedia` server and publish results with `YARP` port.


## Running Software

`wikipediaKnowledge` requires text like input.
The process to running the program:

1. Execute [programs/wikipediaKnowledge.py](./programs), to start de program.
```python
python wikipediaKnowledge.py
```
2. Connect data source.
```bash
yarp connect /yourport/data:o /wikipediaKnowledge/data:i
```

NOTE:

- Data results are published on `/wikipediaKnowledge/data:o`

## Requirements

`wikipediaKnowledge` requires:

* [Install YARP 2.3.XX+](https://github.com/roboticslab-uc3m/installation-guides/blob/master/install-yarp.md)
* [Install pip](https://github.com/roboticslab-uc3m/installation-guides/blob/master/install-pip.md)
* Install wikipedia:
```bash
pip install wikipedia
```

Tested on: `windows 10`, `ubuntu 14.04`, `ubuntu 16.04`, `ubuntu 18.04`, `lubuntu 18.04` and `raspbian`.

## Status

[![Build Status](https://travis-ci.org/davidvelascogarcia/wikipediaKnowledge.svg?branch=develop)](https://travis-ci.org/davidvelascogarcia/wikipediaKnowledge)

[![Issues](https://img.shields.io/github/issues/davidvelascogarcia/wikipediaKnowledge.svg?label=Issues)](https://github.com/davidvelascogarcia/wikipediaKnowledge/issues)

## Related projects

* [Wikipedia: docs](https://pypi.org/project/wikipedia/)

