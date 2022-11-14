# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/agoric.png" width="150" alt=""><figcaption></figcaption></figure>

Agoric is an interoperable Proof-of-Stake chain in the Cosmos ecosystem.  Agoric JavaScript smart contract platform enables 15M+ developers across the  globe to rapidly build and deploy dapps on-chain.

**Chain ID**: agoric-3 | **Latest Version Tag**: pismoA | **Wasm**: OFF

Website: [https://agoric.com](https://agoric.com)

## Restake

[Restake with kjnodes](https://restake.app/agoric/agoricvaloper1ku5sm2twlsywdrp4wz3kfwgyrtqtp0lpr3nvk8) (every day at 08:00, 20:00)
## Public endpoints

* rpc: [https://agoric.rpc.kjnodes.com](https://agoric.rpc.kjnodes.com)
* api: [https://agoric.api.kjnodes.com](https://agoric.api.kjnodes.com)

## Peering

**state-sync**

```
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@agoric.rpc.kjnodes.com:27656
```

**seed-node**

```
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@agoric.rpc.kjnodes.com:27659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/agoric/addrbook.json > $HOME/.agoric/config/addrbook.json
```

**live-peers** (10)
```
peers="c51a25f0ee9e8305e2c20ca116a4bc840c6fbbd5@65.108.234.23:14456,629c3b0ea094deecb6a31025d01ef6a5ba0beee7@135.181.180.230:26656,3445f4b73fdc63a1bf78c638afb122f69cb0bd4a@157.90.208.234:26656,3704274281d20dc09e7161d80a1e16bcb2de0fbf@185.216.33.154:26656,03c7d68a1433dde6db1acbbdf98712609843cc8f@161.97.187.189:36656,a70c51115e32312ded2ed3ae82a8a06657422753@35.215.32.174:26656,d621aaf4de59956117304abd43d3601c128cc5f7@176.9.34.169:26656,0766444edfd39ba589004830bc73cd65ec606bd6@34.94.183.70:26656,15f63de308337b66d8918ffaa74c6e956991bee9@138.201.120.161:28357,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:27656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.agoric/config/config.toml
```
