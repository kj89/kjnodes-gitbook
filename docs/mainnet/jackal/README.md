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
peers="b3f167a06a8691d738de5fff2b3ba65053e0787d@65.21.183.76:26656,d39fecbc409541de13fa644d90066d4dabe08262@46.138.245.164:24475,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:37656,dc579f845ae894cdbe3ab19f1b52387f3d5b681d@23.88.69.167:27211,68eb09cb9c5a2b136e8c693a48bcb26d9108062f@157.90.2.254:26656,ae49a9b75f70c0e3e09a2d59c6345053dd71c27f@116.202.227.117:37656,0faa7f1099de2e02deebe09fcb52863056333265@144.202.72.17:26616,f6aaf53be76e005f83376ceca6d26d30ac93d42c@46.4.81.204:33656,6852add4eaa027707a6000c78ea9e7cde81b058f@18.118.26.4:26656,dbec14a10d43c25d77ee9987a985652fa4e6344a@131.153.59.6:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.canine/config/config.toml
```
