# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/jackal.png" width="150" alt=""><figcaption></figcaption></figure>

The Jackal Protocol is a fast, scalable, and secure blockchain that empowers  individuals, developers, and enterprises to increase their data privacy and  cybersecurity posture without sacrificing ease of use. This protocol strives  to offer world-class applications to protect the planet's most important data–your data.

**Chain ID**: jackal-1 | **Latest Version Tag**: v1.1.2-hotfix | **Wasm**: ON

Website: [https://jackalprotocol.com](https://jackalprotocol.com)

## Restake

[Restake with kjnodes](https://restake.app/jackal/jklvaloper1tr3wm3mdkz0tda6t7vavqnn7fe2g4un0f67xmt) (every day at 08:00, 20:00)
## Public endpoints

* rpc: [https://jackal.rpc.kjnodes.com](https://jackal.rpc.kjnodes.com)
* api: [https://jackal.api.kjnodes.com](https://jackal.api.kjnodes.com)

## Peering

**state-sync**

```
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@jackal.rpc.kjnodes.com:37656
```

**seed-node**

```
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@jackal.rpc.kjnodes.com:37659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/jackal/addrbook.json > $HOME/.canine/config/addrbook.json
```

**live-peers** (10)
```
peers="c0b6d010bb442ff6511bc6fdde1f319b8a3a3bdc@65.108.127.50:17556,637166728d6103ad4ec9fff97a321a024bff3e58@65.109.94.221:28656,d0313585956c8e7969993c1577f4969739b19bb7@85.10.238.147:26656,4398bd773ac885b7365de3604eb487be10c54563@185.16.38.210:26906,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:37656,173c43436e2287f3660c344a5fd2386da4a61968@65.109.92.241:11126,fc905fe58d36875a833202ce53759d0ae6c11435@141.95.65.26:48656,2a55d2e6cc5fa2dda8a484ab7d00f77f076d237f@141.95.47.216:26656,46d4495643f2579573a61e181a88de3b8f0acc4f@2.139.23.24:36656,0836e6f18a67cc6139e315f024189cb8a84f3121@95.217.0.158:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.canine/config/config.toml
```
