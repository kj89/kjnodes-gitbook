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
peers="ee2ef67b49cbc7b4af7ff0b7321870a5d9ae69a5@65.108.138.80:17556,05ab6d764ff112666275376b3f664fc3b19d3bc3@195.201.165.123:11126,c2842c76779913e05fa4256e3caab852e1782951@202.61.194.254:60756,2ec46ff04ebfafc19f505feaaf00943c15bb2757@185.16.38.149:26656,0b8bbc839c20b07ac5999bca7d905d53274c5f2d@24.158.14.214:36656,0226d03f05ea1f324d5cf941b1e1ae29e81d9810@141.94.212.224:26656,dd7e72f0a71476e51c0a601a40d6fc02a1ae1a95@65.108.6.45:60856,ad34b284f0abaca967a75db713c622b53d1fb1ef@116.203.75.59:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:37656,f42498ca4d9e62f95115f04ae18fa5ec1c1487f1@65.108.141.109:18656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.canine/config/config.toml
```
