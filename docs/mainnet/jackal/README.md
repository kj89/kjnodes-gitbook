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

**live-peers** (11)
```
peers="aa0749284ff68c721c5cd6539c7fd04f8063f2a5@65.108.105.25:11656,68eb09cb9c5a2b136e8c693a48bcb26d9108062f@157.90.2.254:26656,0985977a794b298e7ef990fe344d572c60c453b1@172.105.72.158:26656,0faa7f1099de2e02deebe09fcb52863056333265@144.202.72.17:26616,1f30e644ddd8edf310cbd9be4ac07b604eed581e@66.85.143.242:26676,a79da224ad9d4501dbf1d547986ebec55d56b951@135.181.128.114:17556,399068f8371dce4ae5d7cd7da2c965e765e68f4b@65.108.238.102:17556,dbbd1e102b9d0cde827cd272205fa3a2886a6b2c@5.9.147.22:21656,e08efc0b0e15e4d8eacf0f4ed5e52f6e9bdc312d@144.76.97.251:36156,140e8811d3245e12e42b0b99a68f4b5b900823d3@34.76.87.33:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:37656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.canine/config/config.toml
```
