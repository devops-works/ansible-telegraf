import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.fixture()
def AnsibleGetVar(Ansible, var):
    return Ansible("debug", "msg={{ %s }}" % var)["msg"]


# def test_telegraf_runs(host):
#     tg = host.process.filter("comm=telegraf")
#     assert tg


# def test_telegraf_is_enabled(host):
#     tg = host.service("telegraf")
#     assert tg.is_running
#     assert tg.is_enabled
