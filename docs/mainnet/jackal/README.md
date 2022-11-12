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
peers="aa0749284ff68c721c5cd6539c7fd04f8063f2a5@65.108.105.25:11656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:37656,bc6ce122e5809b06dcf90742ee40091f3ee6bcee@142.132.248.253:42656,d0313585956c8e7969993c1577f4969739b19bb7@85.10.238.147:26656,5a4d1a83c877dd5db378ef5f897824273c2d4beb@141.95.72.198:36656,0faa7f1099de2e02deebe09fcb52863056333265@144.202.72.17:26616,1f30e644ddd8edf310cbd9be4ac07b604eed581e@66.85.143.242:26676,c0b6d010bb442ff6511bc6fdde1f319b8a3a3bdc@65.108.127.50:17556,dc579f845ae894cdbe3ab19f1b52387f3d5b681d@23.88.69.167:27211,f90a64a0a3f3c0480360e0fe5dd0f806d7741558@207.244.127.5:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.canine/config/config.toml
```
