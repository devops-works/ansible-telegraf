# -*- mode: ruby -*-
Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/xenial64"
  # config.vm.network "forwarded_port", guest: 80, host: 8080
  config.vm.provider "virtualbox" do |v|
    v.name   = "ansible-telegraf"
    v.memory = 1024
  end

  config.vm.provision "shell", :inline => "sudo apt-get update && sudo apt-get -y upgrade"
  config.vm.provision "shell",
    :path => "tests/specs.sh",
    :upload_path => "/home/vagrant/specs",
    # change role name below
    :args => "--install ansible-telegraf"
end
