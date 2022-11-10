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
peers="d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:37656,fc905fe58d36875a833202ce53759d0ae6c11435@141.95.65.26:48656,4398bd773ac885b7365de3604eb487be10c54563@185.16.38.210:26906,dbec14a10d43c25d77ee9987a985652fa4e6344a@131.153.59.6:26656,68eb09cb9c5a2b136e8c693a48bcb26d9108062f@157.90.2.254:26656,433e26fb4d2533d81a2016a7c9ba768dd6ad2177@65.108.194.26:60756,ea35106e43dcec1e5c66319272da48df3dce7723@57.128.144.233:26656,0faa7f1099de2e02deebe09fcb52863056333265@144.202.72.17:26616,77e2a9fae692906f7fb4d9769675c1e23abf4eaa@138.201.132.55:37656,399068f8371dce4ae5d7cd7da2c965e765e68f4b@65.108.238.102:17556"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.canine/config/config.toml
```
