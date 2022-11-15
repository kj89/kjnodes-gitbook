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
peers="399068f8371dce4ae5d7cd7da2c965e765e68f4b@65.108.238.102:17556,c0b6d010bb442ff6511bc6fdde1f319b8a3a3bdc@65.108.127.50:17556,108652f503665772ad024d9d2129a9f4fa9ffe9b@176.9.98.24:30536,ea35106e43dcec1e5c66319272da48df3dce7723@57.128.144.233:26656,0faa7f1099de2e02deebe09fcb52863056333265@144.202.72.17:26616,0b8bbc839c20b07ac5999bca7d905d53274c5f2d@24.158.14.214:36656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:37656,a2afb42b65da7013eca54778ce01dfb877c2a82a@154.12.227.132:37656,aa0749284ff68c721c5cd6539c7fd04f8063f2a5@65.108.105.25:11656,f42498ca4d9e62f95115f04ae18fa5ec1c1487f1@65.108.141.109:18656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.canine/config/config.toml
```
