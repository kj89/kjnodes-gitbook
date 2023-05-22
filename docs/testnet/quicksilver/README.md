# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/quicksilver.png" alt=""><figcaption></figcaption></figure>

Quicksilver is a permissionless, sovereign Cosmos SDK zone providing liquid staking for the entire Cosmos Ecosystem.

**Chain ID**: innuendo-5 | **Latest Version Tag**: v1.4.0-rc10.2 | **Wasm**: OFF

[Website](https://quicksilver.zone) | [Discord](https://discord.gg/quicksilverprotocol) | [Twitter](https://twitter.com/quicksilverzone)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/quicksilver-testnet](https://explorer.kjnodes.com/quicksilver-testnet)

## Public endpoints

* api: [https://quicksilver-testnet.api.kjnodes.com](https://quicksilver-testnet.api.kjnodes.com)
* rpc: [https://quicksilver-testnet.rpc.kjnodes.com](https://quicksilver-testnet.rpc.kjnodes.com)
* grpc: quicksilver-testnet.grpc.kjnodes.com:11190

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@quicksilver-testnet.rpc.kjnodes.com:11156
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@quicksilver-testnet.rpc.kjnodes.com:11159
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/quicksilver-testnet/addrbook.json > $HOME/.quicksilverd/config/addrbook.json
```

**live-peers** (9)
```bash
peers="af8cfa944802a9bd510fc3407950a15e8be86c31@213.239.217.52:30656,25410bff2fb7312d24c11b1e990507e5e3aa40b7@135.125.5.31:48656,74abcb5243d4ffc43de6ad1a288d8e50adcd467e@65.109.80.176:20656,e25a748120c9608c1d2a70fafa75178d862b3463@178.18.254.211:10656,796e72ffc343c187cd5e8397c0c09c0671d228e0@185.16.39.51:26656,9a60250367f370dc7395c7a5b0d503cec544188f@65.108.230.113:20026,78acdbabc08231765444b3143a222d433a5157e1@142.132.205.94:15651,7781c28c240e85474425040f744b501d99120d1d@195.201.108.152:11656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:11156"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quicksilverd/config/config.toml
```
