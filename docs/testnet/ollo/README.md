# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/ollo.png" alt=""><figcaption></figcaption></figure>

OLLO is a sovereign L1 chain built on the Cosmos network providing  next-gen trading tools & sustainable tokenomics.

**Chain ID**: ollo-testnet-1 | **Latest Version Tag**: v0.0.1 | **Wasm**: OFF

[Website](https://www.ollostation.zone) | [Discord](https://discord.com/invite/GxBqZ9mSSm) | [Twitter](https://twitter.com/OLLOStation)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/ollo-testnet](https://explorer.kjnodes.com/ollo-testnet)

## Public endpoints

* api: [https://ollo-testnet.api.kjnodes.com](https://ollo-testnet.api.kjnodes.com)
* rpc: [https://ollo-testnet.rpc.kjnodes.com](https://ollo-testnet.rpc.kjnodes.com)
* grpc: ollo-testnet.grpc.kjnodes.com:13290

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@ollo-testnet.rpc.kjnodes.com:13256
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@ollo-testnet.rpc.kjnodes.com:13259
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/ollo-testnet/addrbook.json > $HOME/.ollo/config/addrbook.json
```

**live-peers** (10)
```bash
peers="d14b740968d24aa5c31ade7dbda2b1204c40f24c@65.109.52.156:46656,0bee9e500e51465917506b47691a8fb032100da9@94.130.200.168:32656,90ad9622ac54023fe4ee9824d77b5d3e3c25c245@162.55.234.70:54956,da8d3ca8e1c147f0037b1c43ad3de7174f5ec1b7@209.145.59.224:26656,dd577d8f2e997d7e70495640aff124ddb70d1a21@95.217.192.222:26656,42beefd08b5f8580177d1506220db3a548090262@65.108.195.29:26116,799dff05af5d30477f44c816753ff89104b2b8b5@116.202.227.117:32656,d6c5ff021b091a1fd93b9f811cf7fca0d31e8510@65.108.238.61:46656,7349272f712e713a957bf5349930e3439e98b518@167.235.27.69:20656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13256"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ollo/config/config.toml
```
