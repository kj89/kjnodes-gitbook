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
peers="77e2a9fae692906f7fb4d9769675c1e23abf4eaa@138.201.132.55:37656,fc905fe58d36875a833202ce53759d0ae6c11435@141.95.65.26:48656,68eb09cb9c5a2b136e8c693a48bcb26d9108062f@157.90.2.254:26656,6852add4eaa027707a6000c78ea9e7cde81b058f@18.118.26.4:26656,433e26fb4d2533d81a2016a7c9ba768dd6ad2177@65.108.194.26:60756,a13b5c78c65b785f4189a7873015c47217f2c83c@65.108.13.185:27565,b3f167a06a8691d738de5fff2b3ba65053e0787d@65.21.183.76:26656,ad34b284f0abaca967a75db713c622b53d1fb1ef@116.203.75.59:26656,108652f503665772ad024d9d2129a9f4fa9ffe9b@176.9.98.24:30536,8c6eae80747ae0a45befcece5170d23f432a2fb1@51.89.224.199:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.canine/config/config.toml
```
