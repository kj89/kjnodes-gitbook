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
peers="b7b044df4dc2e709972b79c04d9eb7d921e3b45f@116.202.227.117:53656,3891102c7aaa29dac326b6703ee7030618c92c72@89.58.16.33:26656,fed5ba77a69a4e75f44588f794999e9ca0c6b440@45.67.217.22:21956,78aa6b222ae1f619bef03a9d98cb958dfcccc3a8@46.4.5.45:22056,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15356,3a69f577b14bb5e3829489881cc80841b785e092@116.203.129.0:26656,55b38f49cf89235b7e193b1c9880a8e77316f6a6@167.235.7.34:57656,0ea4e8352215aad85ff33a20a3bf4acf49070662@64.226.117.34:21956,136f2c639937adc6a06fe9b004da19087ddba466@88.198.242.163:26656,dc06b3547cf81c40c931a748679ce22161e5ac43@148.113.6.121:19656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.elys/config/config.toml
```
