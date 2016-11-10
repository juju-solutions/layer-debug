# layer-sos

Juju base layer for gathering debug information.

## What does it do?

This base layer provides an `sos` action, which can be used to gather debug
information of a live unit:

```
$ juju run-action sos-test/0 sos
Action queued with id: 4b26e339-7366-4dc7-80ed-255ac0377020`
```

This produces a .tar.gz file which you can retrieve:

```
$ juju show-action-output 4b26e339-7366-4dc7-80ed-255ac0377020
results:
  command: juju scp sos-test/0:/home/ubuntu/sos-20161110151539.tar.gz .
  path: /home/ubuntu/sos-20161110151539.tar.gz
status: completed
timing:
  completed: 2016-11-10 15:15:41 +0000 UTC
  enqueued: 2016-11-10 15:15:38 +0000 UTC
  started: 2016-11-10 15:15:40 +0000 UTC

$ juju scp sos-test/0:/home/ubuntu/sos-20161110151539.tar.gz .
```

The archive includes basic information such as systemctl status, Juju logs,
charm unit data, etc. Additional application-specific information may be
included as well.

## How do I include it?

To include the `sos` action in your charm, simply add it to the includes
section of your `layer.yaml`:

```
includes:
  - layer:sos
```

This provides the `sos` action with basic information. That's it!

## Adding application-specific information

When the `sos` action is run, all executable files in the charm's
`sos-scripts/` folder are run, and their output is included in the archive.
You can include application-specific information by creating this folder and
adding your own scripts to to it.

Both stdout and stderr of SOS scripts are captured. Alternatively, the
`SOS_SCRIPT_DIR` environment variable points to a directory that the SOS script
can add files to.

A few examples can be seen [here](sos-scripts).

If you're writing a Python script, there is also a minimal `sos_script` library
you can import and use. [Example usage](sos-scripts/charm-unitdata)
