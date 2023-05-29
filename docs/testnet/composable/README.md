# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/composable.png" alt=""><figcaption></figcaption></figure>

The complete infrastructure for cross-chain smart  contracts, applications, and modular functionality.

**Chain ID**: banksy-testnet-3 | **Latest Version Tag**: v2.3.5 | **Wasm**: OFF

[Website](https://www.composable.finance) | [Discord](https://discord.gg/composable) | [Twitter](https://twitter.com/ComposableFin)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/composable-testnet](https://explorer.kjnodes.com/composable-testnet)

## Public endpoints

* api: [https://composable-testnet.api.kjnodes.com](https://composable-testnet.api.kjnodes.com)
* rpc: [https://composable-testnet.rpc.kjnodes.com](https://composable-testnet.rpc.kjnodes.com)
* grpc: composable-testnet.grpc.kjnodes.com:15990

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@composable-testnet.rpc.kjnodes.com:15956
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@composable-testnet.rpc.kjnodes.com:15959
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/composable-testnet/addrbook.json > $HOME/.banksy/config/addrbook.json
```

**live-peers** (9)
```bash
peers="4d3873e7d858f2cb710fea20c88445ef97d3ae60@37.27.17.146:19656,b2a5b6c11e7d71c2a43d88a73b9dcff3352f4302@57.128.86.7:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15956,df49f4fee2fe62bc0ca8c27ee0dbae3f0abec98f@46.38.232.86:24656,99004e3251209542b30c7502a7c35b1d574cd3ae@195.3.221.16:26656,de2410e83b86e74a4569e0c120846b67c204f5bc@65.108.226.183:22256,02ea9a908729d6c7a846a535a63fd47131c59b88@65.109.60.19:36656,33d01ca326bb21c3e02c6f05b9cb530eea93c39d@65.109.23.237:30536,764fed363ddaa588c5bfaa43d5ef3177738bbc23@167.114.172.204:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.banksy/config/config.toml
```
