<!--------------------------------------------------------------------------------- Description -->
#  pubsub_python : subject
    this is documents of pubsub_python : subject

<!--------------------------------------------------------------------------------- Simple -->
<br><br>

## Simple 
```bash
nats sub hello
nats pub hello "Hi from macOS"
```

<!--------------------------------------------------------------------------------- Group -->
<br><br>

## Group 
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
```bash
# terminal 1
nats sub tasks --queue workers
# terminal 2
nats sub tasks --queue workers
# terminal 3
nats pub tasks "job-1"
nats pub tasks "job-2"
```