# apache-airflow-tutorial

In case you want to install Apache airflow manualy. This might be your way.

First make sure, that you have your python installed.

### Python3 installation
# apt update
# apt install software-properties-common
# add-apt-repository ppa:deadsnakes/ppa
# apt install python3.8

If you have done that, check the version, and you are good to continue with the next step

### pip installation
# apt install python3-pip

Once you have do that, let's move to the next step
This step is essential, not doing that will bring you a lot of trouble as it has brought to me

### Setting the home directory for the apache airflow to operate in
# export AIRFLOW_HOME=~/airflow/

After having set the directory, you are all set to install the apache airflow itself:

### Setting up Apache Overflow
# pip3 install apache-airflow

The installation process will also bring this stuff with it:
airflow-webserver.pid -  web server running file, remember where it lives
airflow.cfg - file that holds the Airflow configurations, take care
airflow.db - the initial( SQLite database)
unittests.cfg
webserver_config.py

You're almost set, now move to the airflow home directory and create the folder, that will hold your DAGs
### Making the DAGs (tasks) folder
# mkdir dags

*DAG folder path can also be set in the airflow.cfg via the dags_folder parameter

### Enjoy

If you have done everything well, you might now want to test the installation by running the folowing comands:
# systemctl start airflow-webserver - this will run the web-server you will be interacting with
# systemctl start airflow-scheduler - the Airflow Scheduler

