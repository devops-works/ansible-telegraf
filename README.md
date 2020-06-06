ansible-telegraf role
======================

Installs [telegraf](https://github.com/influxdata/telegraf) on ubuntu
14.04 and up.

Requires Ansible 2.5+.

See
[defaults/main.yml](https://github.com/leucos/ansible-telegraf/blob/master/defaults/main.yml)
for supported variables.

## Variables

- `telegraf_enabled`: whether to install telegraf or not
- `telegraf_autoping`: whether to enable ping module and ping all inventory
  hosts from each host
- `telegraf_install_latest`: if set to `true`, will always attempt to
  install latest version
- `telegraf_agent_debug`: debug mode
- `telegraf_agent_hostname` hostname to use when reporting (default: inventory_hostname)
- `telegraf_agent_interval`: collecting interval
- `telegraf_agent_flush_interval`: reporting interval
- `telegraf_agent_flush_jitter`: jitter the flush interval by a random amount. This is primarily to avoid large write spikes for users running a large number of telegraf instances. ie, a jitter of 5s and flush_interval 10s means flushes will happen every 10-15s.
- `telegraf_agent_round_interval`: rounds collection interval to 'interval' ie, if interval="10s" then always collect on :00, :10, :20, etc.
- `telegraf_tags`: additional tags to add (dict)
- `telegraf_output_influxdb`: influxdb servers

## Inputs

Telegraf inputs are specified this way:

```
telegraf_inputs:
  cpu:
    percpu: "true"
    totalcpu: "true"
    drop: ["cpu_time"]
  disk: {}
  mem: {}
  swap: {}
  system: {}
```

You can use `_input_name` variable if you key is not reflecting an input
name. This is handy when you need several inputs with the same name (e.g. several CloudWatch inputs for different namespaces for instance). For instance:

```

telegraf_inputs:
  cloudwatch_efs:
    _input_name: cloudwatch
    namespace: "AWS/EFS"
  cloudwatch_rds:
    _input_name: cloudwatch
    namespace: "AWS/RDS"
  cloudwatch_elb:
    _input_name: cloudwatch
    namespace: "AWS/ELB"
  cpu:
    percpu: "true"
    totalcpu: "true"
    drop: ["cpu_time"]
  disk: {}
  ...
```


Run `vagrant up && vagrant ssh -c specs` to run specs (and play with telegraf).

Michel Blanc <mb@mbnet.fr>
