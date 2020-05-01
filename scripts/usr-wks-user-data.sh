#!/bin/bash

install_maven()
{
  sudo wget http://repos.fedorapeople.org/repos/dchen/apache-maven/epel-apache-maven.repo -O /etc/yum.repos.d/epel-apache-maven.repo
  sudo sed -i s/\$releasever/6/g /etc/yum.repos.d/epel-apache-maven.repo
  sudo yum install -y apache-maven
  mvn --version
}

install_jdk()
{
 sudo yum install java-1.8.0-openjdk-devel -y
}

install_ffmpeg()
{
   mkdir -p /data/0
   cd /data/0
   git clone git@github.com:FFmpeg/FFmpeg.git
   sudo yum install -y nasm yasm
   ./configure
   make
   sudo make install
}

install_jdk
install_maven

install_ffmpeg