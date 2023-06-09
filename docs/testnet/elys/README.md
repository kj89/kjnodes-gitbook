# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/elys.png" alt=""><figcaption></figcaption></figure>

Elys is a fast layer 1 blockchain powered by the Cosmos-SDK.  It is the first, and only, decentralized suite of financial  applications in the Cosmos ecosystem that has built-in native  bridging capabilities for optimal user experience and value  capture, and native margin trading capabilities that are  powered by liquidity pools & liquidity providers.

**Chain ID**: elystestnet-1 | **Latest Version Tag**: v0.6.0 | **Wasm**: OFF

[Website](https://elys.network) | [Discord](https://discord.gg/R9Gr6Vh7vC) | [Twitter](https://twitter.com/elys_network)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/elys-testnet](https://explorer.kjnodes.com/elys-testnet)

## Public endpoints

* api: [https://elys-testnet.api.kjnodes.com](https://elys-testnet.api.kjnodes.com)
* rpc: [https://elys-testnet.rpc.kjnodes.com](https://elys-testnet.rpc.kjnodes.com)
* grpc: elys-testnet.grpc.kjnodes.com:15390

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@elys-testnet.rpc.kjnodes.com:15356
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@elys-testnet.rpc.kjnodes.com:15359
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/elys-testnet/addrbook.json > $HOME/.elys/config/addrbook.json
```

**live-peers** (10)
```bash
peers="fed5ba77a69a4e75f44588f794999e9ca0c6b440@45.67.217.22:21956,98143b5dca162ba726536d07a6af6500d3e6fe1e@65.108.200.40:38656,8cc16cba9ccb2e1a555acb29bf53a9198ecae7ce@209.126.2.211:53656,8d9845f7ef934ade824981b9145a26f00192b575@45.79.24.206:26656,136f2c639937adc6a06fe9b004da19087ddba466@88.198.242.163:26656,fc5a323a8c57393e84902e832a75f15bd0b898b2@84.46.242.124:53656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15356,01aaf7bce61622ab4f2f6cedbc57fa3aa5d3cf3c@167.235.1.101:26676,8851667ffc0b35d3a993fce617fd7a1a736729ad@65.21.126.180:30656,701a382e03978c54f1176145460125516b6a4672@3.144.113.232:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.elys/config/config.toml
```
