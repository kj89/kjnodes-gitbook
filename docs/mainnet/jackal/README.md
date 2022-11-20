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
peers="ee2ef67b49cbc7b4af7ff0b7321870a5d9ae69a5@65.108.138.80:17556,8d59eb5f7ad207e59c06620f6e9e7b6760b56211@65.108.75.107:18656,dbbd1e102b9d0cde827cd272205fa3a2886a6b2c@5.9.147.22:21656,ecb163fca7436befa3a5694a7d558e89d3f04b2c@65.109.29.150:17656,1f30e644ddd8edf310cbd9be4ac07b604eed581e@66.85.143.242:26676,aca915dcd2087459a5d3e400b707ce1932f91401@65.108.229.102:56656,0faa7f1099de2e02deebe09fcb52863056333265@144.202.72.17:26616,399068f8371dce4ae5d7cd7da2c965e765e68f4b@65.108.238.102:17556,c2842c76779913e05fa4256e3caab852e1782951@202.61.194.254:60756,3de470ce92bece46919f05141d5935e6143b9afa@88.198.34.226:11126,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:37656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.canine/config/config.toml
```
