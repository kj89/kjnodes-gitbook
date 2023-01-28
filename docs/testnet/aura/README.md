# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/aura.png" width="150" alt=""><figcaption></figcaption></figure>

The Aura Network protocol allows users to mint, rate, track data,  or trade NFT for the goal of constructing a strong platform to  support all trading assets on the crypto market in a simpler and easier way

**Chain ID**: euphoria-2 | **Latest Version Tag**: euphoria_v0.4.2 | **Wasm**: ON

[Website](https://aura.network) | [Discord](https://discord.gg/hpvF5QcWRf) | [Twitter](https://twitter.com/AuraNetworkHQ)


## Chain explorer
[https://explorer.kjnodes.com/aura-testnet](https://explorer.kjnodes.com/aura-testnet)

## Public endpoints

* api: [https://aura-testnet.api.kjnodes.com](https://aura-testnet.api.kjnodes.com)
* rpc: [https://aura-testnet.rpc.kjnodes.com](https://aura-testnet.rpc.kjnodes.com)
* grpc: [https://aura-testnet.grpc.kjnodes.com](https://aura-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@aura-testnet.rpc.kjnodes.com:17656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@aura-testnet.rpc.kjnodes.com:17659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/aura-testnet/addrbook.json > $HOME/.aura/config/addrbook.json
```

**live-peers** (9)
```bash
peers="7cad1bcb2ad777dba21840832341f2ce14bae1a5@5.75.174.126:26656,e7d497959ae94823a70fc4c1c7fe2bc31b2ead57@135.181.143.48:28656,b2394ad608075aa405cdf4ab55e36376d93f7b1d@65.108.206.118:56656,b130852645cc3d7925cfccd14d97425a2260e7ec@65.109.82.106:19656,b91ee5c72905bc49beed2720bb882c923c68fbc9@65.108.142.47:21656,fdcc8f1ca406213d79947c5f38920a085ed90c0f@144.202.72.17:26676,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:17656,0770c2687cc34d59ca62270960d3ffcad6e42cf8@65.108.233.44:21656,6ef01ca6714aa8127d1b21b5339909ca6319dae0@144.76.97.251:26776"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.aura/config/config.toml
```
