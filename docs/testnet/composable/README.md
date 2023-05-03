# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/composable.png" alt=""><figcaption></figcaption></figure>

The complete infrastructure for cross-chain smart  contracts, applications, and modular functionality.

**Chain ID**: banksy-testnet-1 | **Latest Version Tag**: v2.2.0 | **Wasm**: ON

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
peers="13c29d1d66d604e8920ba0170276368e4e77f249@88.99.3.158:22256,7ab89f884656a66ca90fd9d44489da3c6ca1fea4@95.217.144.107:22256,c97dd69796a3f55fb00d92358ec34a8185e28212@5.9.79.121:49656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15956,7eabe041d60e63a88591a5c30ca890a9de36119c@3.133.131.224:26656,f23a8daca1f65aeee7ce6f6d47a56542a08538c9@66.45.233.110:26656,067f0f6f1706c4ef7da49b2896f28e194e8be055@96.234.160.22:30456,4775d0152d784b3ddf4f48c2d0ebddf961b52655@43.157.56.21:26656,b960daa0d03d18091906c50dd1312eaa62ca3ce4@136.243.88.91:2530"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.banksy/config/config.toml
```
