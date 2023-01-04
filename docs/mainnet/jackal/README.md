# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/jackal.png" width="150" alt=""><figcaption></figcaption></figure>

The Jackal Protocol is a fast, scalable, and secure blockchain that empowers  individuals, developers, and enterprises to increase their data privacy and  cybersecurity posture without sacrificing ease of use. This protocol strives  to offer world-class applications to protect the planet's most important data–your data.

**Chain ID**: jackal-1 | **Latest Version Tag**: v1.1.2-hotfix | **Wasm**: ON

[Website](https://jackalprotocol.com) | [Discord](https://discord.com/invite/5GKym3p6rj) | [Twitter](https://twitter.com/Jackal_Protocol)

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
peers="aca915dcd2087459a5d3e400b707ce1932f91401@65.108.229.102:56656,9bcaee1ad957fa75f60a6dd9d8870e53220794a9@104.37.187.214:60756,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:37656,0985977a794b298e7ef990fe344d572c60c453b1@172.105.72.158:26656,72f98b8ac9af924c77f52cdc26a78e7728d4e19d@24.158.14.212:26656,0836e6f18a67cc6139e315f024189cb8a84f3121@95.217.0.158:26656,c2842c76779913e05fa4256e3caab852e1782951@202.61.194.254:60756,7751d16cfa48da0a5bea6f40e9bcc386b4c76c50@51.89.7.184:26638,dd7e72f0a71476e51c0a601a40d6fc02a1ae1a95@65.108.6.45:60856,7574e0ab179fc6cc47ac89284f4641790218540e@18.163.165.245:26626"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.canine/config/config.toml
```
