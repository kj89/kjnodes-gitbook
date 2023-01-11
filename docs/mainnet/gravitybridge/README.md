# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/gravitybridge.png" width="150" alt=""><figcaption></figcaption></figure>

An open, decentralized bridge that unlocks the power of  interoperability & liquidity between blockchain ecosystems.

**Chain ID**: gravity-bridge-3 | **Latest Version Tag**: v1.8.1 | **Wasm**: OFF

[Website](https://www.gravitybridge.net) | [Discord](https://discord.gg/ARV8dTSjAk) | [Twitter](https://twitter.com/gravity_bridge)

## Restake

[Restake with kjnodes](https://restake.app/gravitybridge/gravityvaloper1nw3uavthnjwsgrrjzav2wdg9m0pw7k4fc7hvlz) (every day at 08:00, 20:00)
## Public endpoints

* rpc: [https://gravitybridge.rpc.kjnodes.com](https://gravitybridge.rpc.kjnodes.com)
* api: [https://gravitybridge.api.kjnodes.com](https://gravitybridge.api.kjnodes.com)

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@gravitybridge.rpc.kjnodes.com:26656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@gravitybridge.rpc.kjnodes.com:26659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/gravitybridge/addrbook.json > $HOME/.gravity/config/addrbook.json
```

**live-peers** (10)
```bash
peers="82bf13b3c0af8cd0ea69c64ff43e61a5b7dbae7f@176.126.87.56:26656,c4385ec685f08dfd635df6d21be9dfbdfdb52896@161.97.182.71:26656,77367b424f624c4f9f423267dd8d4d559b289b62@167.235.9.250:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:26656,c189b7217b037e50b3456440963f91d027a4df5a@65.108.199.222:26656,ca4270ebed73b4d0982450aac16fe08860410fac@142.132.248.138:26626,df243a4c65b436fb4c81bf71b83ce9de865fea5a@213.239.207.165:26656,4e1ea298ef66eec3ec320171f90336a1e4bb13ea@51.81.107.95:10256,0a8487549154b7dd96fd0af1843ecfa62246f816@18.144.134.123:26656,2b107c598194efa2efb04cbd395528900ffb1b1c@65.108.104.113:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gravity/config/config.toml
```
