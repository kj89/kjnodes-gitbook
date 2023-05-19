# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/elys.png" alt=""><figcaption></figcaption></figure>

Elys is a fast layer 1 blockchain powered by the Cosmos-SDK.  It is the first, and only, decentralized suite of financial  applications in the Cosmos ecosystem that has built-in native  bridging capabilities for optimal user experience and value  capture, and native margin trading capabilities that are  powered by liquidity pools & liquidity providers.

**Chain ID**: elystestnet-1 | **Latest Version Tag**: v0.5.4 | **Wasm**: OFF

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
peers="3a69f577b14bb5e3829489881cc80841b785e092@116.203.129.0:26656,fed5ba77a69a4e75f44588f794999e9ca0c6b440@45.67.217.22:21956,8723618f5dff7ac9b57472f90f2e86a2eb194e0a@71.236.119.108:25656,db03e6915cad62b2646ae72566ed19074a7707b6@95.217.144.107:22056,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15356,1092d9a9508053d6936661ebc5708d0d8d360e3e@193.26.159.34:10656,3f30f68cb08e4dae5dd76c5ce77e6e1a15084346@212.95.51.215:56656,55b38f49cf89235b7e193b1c9880a8e77316f6a6@167.235.7.34:57656,136f2c639937adc6a06fe9b004da19087ddba466@88.198.242.163:26656,89c4d6fa66c4e4517742e564cd6ba1532496fd43@65.108.108.52:32656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.elys/config/config.toml
```
