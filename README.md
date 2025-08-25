<!--------------------------------------------------------------------------------- Description -->
# pubsub_python
    this is documents of pubsub_python

<!--------------------------------------------------------------------------------- Resource -->
<br><br>

## Resource  

Web

    Web        : https://nats.io/
    Github     : https://github.com/nats-io

<!--------------------------------------------------------------------------------- Install -->
<br><br>

## Install 

Mac
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install rust
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
echo $HOME/.cargo/env >> $HOME/.zshrc
```

Linux
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install build-essential pkg-config libssl-dev -y
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
rustc --version
cargo --version
rustup update
```

Windows
```bash
```

IDE
```bash
Vs-Code
Rust Extension Pack
```

<!--------------------------------------------------------------------------------- Structure -->
<br><br>

## Structure 

NATS Server
Publisher
Subscriber
Subject
Message

<!--------------------------------------------------------------------------------- Subscriber -->
<br><br>

## Subscriber 

Simple Subscription
Queue Group Subscription
Wildcard Subscription

<!--------------------------------------------------------------------------------- Message -->
<br><br>

## Message 
At-most-once
At-least-once



<!--------------------------------------------------------------------------------- Modules -->
<br><br>

## Modules 

JetStream



<!--------------------------------------------------------------------------------- Note -->
<br><br>

## Note 

Authentication
Encryption
Grouping
Log
