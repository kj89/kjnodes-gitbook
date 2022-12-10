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
peers="c0b6d010bb442ff6511bc6fdde1f319b8a3a3bdc@65.108.127.50:17556,5a4d1a83c877dd5db378ef5f897824273c2d4beb@141.95.72.198:36656,0faa7f1099de2e02deebe09fcb52863056333265@144.202.72.17:26616,1f30e644ddd8edf310cbd9be4ac07b604eed581e@66.85.143.242:26676,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:37656,8d59eb5f7ad207e59c06620f6e9e7b6760b56211@65.108.75.107:18656,e258f57604c59fc02d07b9669ae64f00bb45a20c@162.205.240.139:37656,ea35106e43dcec1e5c66319272da48df3dce7723@57.128.144.233:26656,2a55d2e6cc5fa2dda8a484ab7d00f77f076d237f@141.95.47.216:26656,399068f8371dce4ae5d7cd7da2c965e765e68f4b@65.108.238.102:17556"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.canine/config/config.toml
```
