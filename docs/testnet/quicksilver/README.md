# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/quicksilver.png" alt=""><figcaption></figcaption></figure>

Quicksilver is a permissionless, sovereign Cosmos SDK zone providing liquid staking for the entire Cosmos Ecosystem.

**Chain ID**: rhye-1 | **Latest Version Tag**: v1.4.2-rc7 | **Wasm**: OFF

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
peers="25410bff2fb7312d24c11b1e990507e5e3aa40b7@135.125.5.31:48656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:11156,ee6bae1a6d4a1e07f1e4bc7963cabedc6b73426e@94.130.137.119:26656,ac6068dc650358a0c8f7b774630367ba2c70fa1f@93.190.141.68:21026,d3e80f977fe2ed85029c656e596dbb70b3bd7fee@65.109.95.178:37656,60509a87fc6c97a013de3cdeadf5fd3eab22f896@65.109.23.114:11156,8e14e58b054248a04be96e4a40d6359e93b636ac@65.108.65.94:26656,cd85e8a5ad374c3ee339d6f201a065ae9e911eb4@65.108.226.183:11156,d0d0903d8c2f514c92284341d48aa422d4e37740@78.47.198.121:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quicksilverd/config/config.toml
```
