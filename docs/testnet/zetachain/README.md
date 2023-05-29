# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/zetachain.png" alt=""><figcaption></figcaption></figure>

An EVM-compatible L1 blockchain that connects everything:  Build interoperable dApps that span any chain including Bitcoin; access all chains from one place.

**Chain ID**: athens_7001-13 | **Latest Version Tag**: latest | **Wasm**: OFF

[Website](https://www.zetachain.com) | [Discord](https://discord.gg/zetachain) | [Twitter](https://twitter.com/zetablockchain)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/zetachain-testnet](https://explorer.kjnodes.com/zetachain-testnet)

## Public endpoints

* api: [https://zetachain-testnet.api.kjnodes.com](https://zetachain-testnet.api.kjnodes.com)
* rpc: [https://zetachain-testnet.rpc.kjnodes.com](https://zetachain-testnet.rpc.kjnodes.com)
* grpc: zetachain-testnet.grpc.kjnodes.com:16090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@zetachain-testnet.rpc.kjnodes.com:16056
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@zetachain-testnet.rpc.kjnodes.com:16059
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/zetachain-testnet/addrbook.json > $HOME/.zetacored/config/addrbook.json
```

**live-peers** (6)
```bash
peers="a918d08544b5f4e0a9eb20bf91f343eb71b6d5ee@164.90.181.99:26656,24a3a8151ec9ecec0b9ed1ca97accfb1dacc115f@88.218.226.79:26656,038234610497601373b1d27e27251674c6c81df7@3.218.170.198:26656,983972c8d76558b5f0150cd6bffc10ce4f608e4c@65.21.236.163:26656,af58c82b5f4d2268e0b8ca9150190e438c07d90d@34.239.99.239:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:16056"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.zetacored/config/config.toml
```
