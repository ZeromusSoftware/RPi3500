#!/bin/bash
# 0.0.1

sudo su

# Configure Network
interfaces=/etc/network/interfaces
echo " " >> $interfaces
echo "iface eth0 inet static" >> $interfaces
echo "address 192.168.0.110" >> $interfaces
echo "netmask 255.255.255.0" >> $interfaces
echo -n "gateway: 192.168.0.1" >> $interfaces

#Prepare Hadood User Account and Group
sudo addgroup hadoop
sudo adduser --ingroup hadoop hduser
sudo adduser hduser sudo
su hduser
mkdir ~/.ssh
ssh-keygen -t rsa -P ""
cat ~/.ssh/id_rsa.pub > ~/.ssh/authorized_keys


# Download and install Hadoop
cd ~/
wget http://apache.mirrors.spacedump.net/hadoop/core/hadoop-1.2.1/hadoop-1.2.1.tar.gz
sudo mkdir /opt
sudo tar -xvzf hadoop-1.2.1.tar.gz -C /opt/
cd /opt
sudo mv hadoop-1.2.1 hadoop
sudo chown -R hduser:hadoop hadoop

export JAVA_HOME=$(readlink -f /usr/bin/java | sed "s:bin/java::")
export HADOOP_INSTALL=/opt/hadoop
export PATH=$PATH:$HADOOP_INSTALL/bin


## /!\ PROBLEME /!\
# The java implementation to use. Required.
export JAVA_HOME=$(readlink -f /usr/bin/java | sed "s:bin/java::")

# The maximum amount of heap to use, in MB. Default is 1000.
export HADOOP_HEAPSIZE=250

# Command specific options appended to HADOOP_OPTS when specified
export HADOOP_DATANODE_OPTS="-Dcom.sun.management.jmxremote $HADOOP_DATANODE_OPTSi -client"
## /!\ PROBLEME /!\



cd /opt/hadoop/conf/
echo "" >> core-site.xml


echo "" >> mapred-site.xml


echo "" >> hdfs-site.xml


sudo mkdir -p /hdfs/tmp
sudo chown hduser:hadoop /hdfs/tmp
sudo chmod 750 /hdfs/tmp
hadoop namenode -format

/opt/hadoop/bin/start-dfs.sh
/opt/hadoop/bin/start-mapred.sh

jps

exit 0;
