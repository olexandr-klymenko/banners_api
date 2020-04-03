

Updated solution for Ubuntu 18.04

    echo "deb http://packages.couchbase.com/ubuntu bionic bionic/main" | sudo tee /etc/apt/sources.list.d/couchbase.list
    wget -O- http://packages.couchbase.com/ubuntu/couchbase.key | sudo apt-key add -
    sudo apt-get update
    sudo apt-get install libcouchbase2-libevent libcouchbase-dev

