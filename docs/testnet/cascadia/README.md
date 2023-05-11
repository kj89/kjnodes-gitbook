# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/cascadia.png" alt=""><figcaption></figcaption></figure>

Cascadia is a layer-1 blockchain built to explore the  nature of incentives on network effects, starting  with ve-tokenomics.

**Chain ID**: cascadia_6102-1 | **Latest Version Tag**: v0.1.2 | **Wasm**: OFF

[Website](https://www.cascadia.foundation) | [Discord](https://discord.gg/cascadia) | [Twitter](https://twitter.com/CascadiaSystems)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/cascadia-testnet](https://explorer.kjnodes.com/cascadia-testnet)

## Public endpoints

* api: [https://cascadia-testnet.api.kjnodes.com](https://cascadia-testnet.api.kjnodes.com)
* rpc: [https://cascadia-testnet.rpc.kjnodes.com](https://cascadia-testnet.rpc.kjnodes.com)
* grpc: cascadia-testnet.grpc.kjnodes.com:15590

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@cascadia-testnet.rpc.kjnodes.com:15556
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@cascadia-testnet.rpc.kjnodes.com:15559
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/cascadia-testnet/addrbook.json > $HOME/.cascadiad/config/addrbook.json
```

**live-peers** (10)
```bash
peers="275dc82c6fbea56c9c0b5098d5156a939a8698a0@178.63.102.172:25556,8d00e22ed928ca4e409816f7d6fdd2c9faaf3b8f@167.235.31.186:22656,e0dcea0df3c5e31458ba855358b08cc804ddb287@144.91.122.14:26656,5d563f5d882904f89b929fde2d1cf2342c8cba7c@185.209.223.64:36656,77f241dc899638b011dd7448ca7897879cb590e4@195.3.220.22:11656,f78611ffa950efd9ddb4ed8f7bd8327c289ba377@65.109.108.150:46656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15556,b08c31354f72aabc769abc8bfd0a8ee7cd0201e5@38.242.238.112:26656,5f1bcdfe67b0cd55ed12a06454206c7f1ab4b35b@95.216.160.203:26656,fcac681e16636bc1185194e31d0ff9b27d7f1275@85.239.233.241:55656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
