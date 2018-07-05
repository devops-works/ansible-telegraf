ansible-telegraf role
======================

Installs [telegraf](https://github.com/influxdata/telegraf) on ubuntu
14.04 and up.

Requires Ansible 2.5+.

See
[defaults/main.yml](https://github.com/leucos/ansible-telegraf/blob/master/defaults/main.yml)
for supported variables.

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


Run `vagrant up && vagrant ssh -c specs` tu run specs (and play with telegraf).

Michel Blanc <mb@mbnet.fr>
