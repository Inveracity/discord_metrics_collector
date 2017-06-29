# -*- mode: ruby -*-
# vi: set ft=ruby :
Vagrant.configure("2") do |config|
  config.vm.define "master" do |dev|
    dev.vm.box = "ubuntu/xenial64"
    dev.vm.host_name = "master"
    dev.vm.network :private_network, ip: "192.168.56.2"
    config.vm.network "forwarded_port", guest: 14480, host: 14480
    config.vm.network "forwarded_port", guest: 3000, host: 3000
    config.vm.provider :virtualbox do |vb|
        vb.customize ["modifyvm", :id, "--memory", "2048"]
        vb.customize ["modifyvm", :id, "--ioapic", "on"]
        vb.customize ["modifyvm", :id, "--cpus", "2"]
        vb.linked_clone = true
    config.vm.synced_folder ".", "/vagrant",
        type: "virtualbox",
        mount_options: ["dmode=775,fmode=775"]
    end
    config.vm.provision "shell", path: "bootstrap-vagrant.sh"
  end
end


