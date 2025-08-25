<!--------------------------------------------------------------------------------- Description -->
# pubsub_python
    this is documents of pubsub_python

<!--------------------------------------------------------------------------------- Resource -->
<br><br>

## Resource  

Web

    Web        : https://nats.io/
    Github     : https://github.com/nats-io

<!--------------------------------------------------------------------------------- Server -->
<br><br>

## Server 

Install : Mac
```bash
brew install nats-server
brew install nats-io/nats-tools/nats
```

Install : Linux
```bash
```

Tools
```bash
nats-server --version
nats --version
```

<!--------------------------------------------------------------------------------- Structure -->
<br><br>

## Structure 

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

<!--------------------------------------------------------------------------------- Authentication -->
<br><br>

## Authentication 

Authentication

<!--------------------------------------------------------------------------------- Encryption -->
<br><br>

## Encryption 

Encryption


<!--------------------------------------------------------------------------------- Group -->
<br><br>

## Group 
Command-Line
```bash
# terminal 1
nats sub group1.events
# terminal 2
nats sub group2.events
# terminal 3
nats pub group1.events "hello from group1 publisher"
nats pub group2.events "hello from group2 publisher"
```

<!--------------------------------------------------------------------------------- Queue -->
<br><br>

## Queue 
Command-Line
```bash
# terminal 1
nats sub tasks --queue workers
# terminal 2
nats sub tasks --queue workers
# terminal 3
nats pub tasks "job-1"
nats pub tasks "job-2"
```

<!--------------------------------------------------------------------------------- Log -->
<br><br>

## Log 

JetStream

<!--------------------------------------------------------------------------------- Command -->
<br><br>

## Command 
```bash
nats pub hello "Hi from macOS"
nats sub hello
```

<!--------------------------------------------------------------------------------- Note -->
<br><br>

## Note 