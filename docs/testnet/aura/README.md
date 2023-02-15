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

**live-peers** (10)
```bash
peers="94f09cc1e0d2357c8c8423589c42dc7721387a60@176.9.44.113:26686,7cad1bcb2ad777dba21840832341f2ce14bae1a5@5.75.174.126:26656,e874935eee84c8313dbb52ba497aed2d8d1f1245@65.108.237.231:27656,e7d497959ae94823a70fc4c1c7fe2bc31b2ead57@135.181.143.48:28656,b2394ad608075aa405cdf4ab55e36376d93f7b1d@65.108.206.118:56656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:17656,7812205773ac30f3d47200ac2391c79896c60135@54.254.220.113:26656,3d6b07bdb11754c8c8512525dac109d8bdee3857@65.21.53.39:7656,b130852645cc3d7925cfccd14d97425a2260e7ec@65.109.82.106:19656,0770c2687cc34d59ca62270960d3ffcad6e42cf8@65.108.233.44:21656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.aura/config/config.toml
```
