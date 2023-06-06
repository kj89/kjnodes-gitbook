# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/composable.png" alt=""><figcaption></figcaption></figure>

The complete infrastructure for cross-chain smart  contracts, applications, and modular functionality.

**Chain ID**: centauri-1 | **Latest Version Tag**: v2.3.5 | **Wasm**: OFF

[Website](https://www.composable.finance) | [Discord](https://discord.gg/composable) | [Twitter](https://twitter.com/ComposableFin)



Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/composable](https://explorer.kjnodes.com/composable)

## Public endpoints

* api: [https://composable.api.kjnodes.com](https://composable.api.kjnodes.com)
* rpc: [https://composable.rpc.kjnodes.com](https://composable.rpc.kjnodes.com)
* grpc: composable.grpc.kjnodes.com:15990

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@composable.rpc.kjnodes.com:15956
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@composable.rpc.kjnodes.com:15959
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/composable/addrbook.json > $HOME/.banksy/config/addrbook.json
```

**live-peers** (10)
```bash
peers="d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:15956,92336725dc7fda1504ea5962bb551f2610126377@65.108.198.118:22256,c6eefdcc5cbe41dd457183c7c3bd7311ddf97638@65.109.116.119:16156,c19bab4c4e5965b1ee079e19337332a2ec3d648d@135.181.79.62:26656,67852a010896f7d28f0bb649f5e05cda44d71875@144.76.40.53:22256,548b18f0288f4c128ef3ff133dcadf004263c363@38.242.230.118:26656,41caa4106f68977e3a5123e56f57934a2d34a1c1@185.248.24.20:26976,0fe72ab099fac951f5a37f51ba895717460a08d0@65.109.53.60:28656,3f72dfcaa83c4922dd6e72bc5b9da7840ef8adaa@57.128.96.155:22256,77975a9a8117248712cdb0b371accfff2a686182@15.235.40.124:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.banksy/config/config.toml
```
