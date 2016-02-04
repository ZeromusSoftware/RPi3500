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


# /!\ PROBLEME
#Tester l'installation de java

#command -v java -version
#if $? == 0; then
# /!\ PROBLEME

#Prepare Hadood User Account and Group

sudo addgroup hadoop
sudo adduser --ingroup hadoop hduser
sudo adduser hduser sudo
su hduser
mkdir ~/.ssh
ssh-keygen -t rsa -P ""
cat ~/.ssh/id_rsa.pub > ~/.ssh/authorized_keys


#Verify that hduser can login to SSH

su hduser
ssh localhost


# Download and install Hadoop

cd ~/
wget http://apache.mirrors.spacedump.net/hadoop/core/hadoop-1.2.1/hadoop-1.2.1.tar.gz
sudo mkdir /opt
sudo tar -xvzf hadoop-1.2.1.tar.gz -C /opt/
cd /opt
sudo mv hadoop-1.2.1 hadoop
sudo chown -R hduser:hadoop hadoop

echo 'export JAVA_HOME=$(readlink -f /usr/bin/java | sed "s:bin/java::")' >> /etc/bash.bashrc
echo 'export HADOOP_INSTALL=/opt/hadoop' >> /etc/bash.bashrc
echo -n'export PATH=$PATH:$HADOOP_INSTALL/bin' >> /etc/bash.bashrc


#Verify hadoop executable is accessible outside

exit
su hduser
hadoop version


#Configure Hadoop environment variables

sed -i 's\#export JAVA_HOME=$(readlink -f /usr/bin/java | sed "s:bin/java::")\export JAVA_HOME=$(readlink -f /usr/bin/java | sed "s:bin/java::")\g' /opt/hadoop/conf/hadoop-env.sh

sed -i 's\#export HADOOP_HEAPSIZE=250\export HADOOP_HEAPSIZE=250\g' /opt/hadoop/conf/hadoop-env.sh

sed -i 's\export HADOOP_DATANODE_OPTS="-Dcom.sun.management.jmxremote $HADOOP_DATANODE_OPTSi"\export HADOOP_DATANODE_OPTS="-Dcom.sun.management.jmxremote $HADOOP_DATANODE_OPTSi -client"\g' /opt/hadoop/conf/hadoop-env.sh


#Configure Hadoop

sed -i 's|<configuration>|<configuration>\n<property>\n<name>hadoop.tmp.dir</name>\n<value>/hdfs/tmp</value>\n</property>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://localhost:54310</value>\n</property>|g' /opt/hadoop/conf/core-site.xml

sed -i 's|<configuration>|<configuration>\n<property>\n<name>mapred.job.tracker</name>\n<value>localhost:54311</value>\n</property>|g' /opt/hadoop/conf/mapred-site.xml

sed -i 's|<configuration>|<configuration>\n<property>\n<name>dfs.replication</name>\n<value>1</value>\n</property>|g' /opt/hadoop/conf/hdfs-site.xml


#Create HDFS file system

sudo mkdir -p /hdfs/tmp
sudo chown hduser:hadoop /hdfs/tmp
sudo chmod 750 /hdfs/tmp
hadoop namenode -format

su hduser


#Start services

/opt/hadoop/bin/start-dfs.sh
/opt/hadoop/bin/start-mapred.sh


#Run the jps command to checkl that all services started as supposed to

jps


exit 0;
