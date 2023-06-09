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
peers="799dff05af5d30477f44c816753ff89104b2b8b5@116.202.227.117:32656,ab89596768849d679ed11a9e1848224760a278cc@83.171.248.175:32656,d14b740968d24aa5c31ade7dbda2b1204c40f24c@65.109.52.156:46656,dd577d8f2e997d7e70495640aff124ddb70d1a21@95.217.192.222:26656,2f5965450c9c831266959632fba2c1533b8f676d@38.242.248.2:26656,d94c9bf688c921319bf3747e41cc6bafd589ffde@65.21.134.243:26677,e53eedfc4c5c4487e1fba7f3b97de6aadfca8cea@5.161.179.64:26656,e3d1fbe11462a128f14ebc10f7e8bd59823f09e2@161.97.152.215:26656,69d2c02f413bea1376f5398646f0c2ce0f82d62e@141.94.73.93:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13256"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ollo/config/config.toml
```
