# layer-debug

Juju base layer to collect debug information.

## What does it do?

This base layer provides a `debug` action, which can be used to collect debug
information of a live unit:

```
$ juju run-action debug-test/0 debug
Action queued with id: 4b26e339-7366-4dc7-80ed-255ac0377020`
```

This produces a .tar.gz file which you can retrieve:

```
$ juju show-action-output 4b26e339-7366-4dc7-80ed-255ac0377020
results:
  command: juju scp debug-test/0:/home/ubuntu/debug-20161110151539.tar.gz .
  message: Archive has been created on unit debug-test/0. Use the juju scp
    command to copy it to your local machine.
  path: /home/ubuntu/debug-20161110151539.tar.gz
status: completed
timing:
  completed: 2016-11-10 15:15:41 +0000 UTC
  enqueued: 2016-11-10 15:15:38 +0000 UTC
  started: 2016-11-10 15:15:40 +0000 UTC

$ juju scp debug-test/0:/home/ubuntu/debug-20161110151539.tar.gz .
```

The archive includes basic information such as systemctl status, Juju logs,
charm unit data, etc. Additional application-specific information may be
included as well.

## How do I include it?

To include the `debug` action in your charm, simply add it to the includes
section of your `layer.yaml`:

```
includes:
  - layer:debug
```

This provides the `debug` action with basic information. That's it!

## Adding application-specific information

When the `debug` action is run, all executable files in the charm's
`debug-scripts/` folder are run, and their output is included in the archive.
You can include application-specific information by creating this folder and
adding your own scripts to it.

> Careful: Make sure script names are unique. If two different layers have a
> script with the same name, and both are included in a charm, then one script
> will override the other.

Both stdout and stderr of debug scripts are captured. Alternatively, the
`DEBUG_SCRIPT_DIR` environment variable points to a directory that the debug
script can add files to.

A few examples can be seen [here](debug-scripts).

If you're writing a Python script, there is also a minimal `debug_script`
library you can import and use. [Example usage](debug-scripts/charm-unitdata)
