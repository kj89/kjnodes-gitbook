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
peers="c0b6d010bb442ff6511bc6fdde1f319b8a3a3bdc@65.108.127.50:17556,0e095a81f6e9633f321c405fcd8524457cba49ee@144.76.17.48:10856,68eb09cb9c5a2b136e8c693a48bcb26d9108062f@157.90.2.254:26656,0faa7f1099de2e02deebe09fcb52863056333265@144.202.72.17:26616,0b8bbc839c20b07ac5999bca7d905d53274c5f2d@24.158.14.214:36656,dbec14a10d43c25d77ee9987a985652fa4e6344a@131.153.59.6:26656,8d59eb5f7ad207e59c06620f6e9e7b6760b56211@65.108.75.107:18656,fe470c3822748792d4b9d1512ba5cc51c5ce4443@185.180.222.181:46656,a13b5c78c65b785f4189a7873015c47217f2c83c@65.108.13.185:27565,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:37656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.canine/config/config.toml
```
