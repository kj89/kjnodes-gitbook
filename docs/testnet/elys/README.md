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
peers="b7b044df4dc2e709972b79c04d9eb7d921e3b45f@116.202.227.117:53656,fed5ba77a69a4e75f44588f794999e9ca0c6b440@45.67.217.22:21956,42d3a20613e443087ae5aec1f1e56c0a12cf8455@135.181.60.184:46656,fec2dfd0a7e0e174e90755eb60c750f5ccc43b40@199.175.98.115:53656,8d9845f7ef934ade824981b9145a26f00192b575@45.79.24.206:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15356,d3235fc7392c1f789ce8d3176b44a378a110b99c@195.3.223.26:26656,3a69f577b14bb5e3829489881cc80841b785e092@116.203.129.0:26656,00c65e06302fb35a1064d9aa4e528aaf98925aa8@65.108.105.48:22056,eea369326c859c0167e1085dd7d540c8c8e308fb@95.217.89.202:53656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.elys/config/config.toml
```
