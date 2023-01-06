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

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@jackal.rpc.kjnodes.com:37656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@jackal.rpc.kjnodes.com:37659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/jackal/addrbook.json > $HOME/.canine/config/addrbook.json
```

**live-peers** (10)
```bash
peers="68205c025ec65bf4d4183691d19d15b0a72221ec@65.108.42.185:26656,0985977a794b298e7ef990fe344d572c60c453b1@172.105.72.158:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:37656,588e509e3a8c1dc4ba938779bf569cd9f6f0f4be@212.23.222.109:26256,9bcaee1ad957fa75f60a6dd9d8870e53220794a9@104.37.187.214:60756,0b8bbc839c20b07ac5999bca7d905d53274c5f2d@24.158.14.214:36656,72f98b8ac9af924c77f52cdc26a78e7728d4e19d@24.158.14.212:26656,4398bd773ac885b7365de3604eb487be10c54563@185.16.38.210:26906,7574e0ab179fc6cc47ac89284f4641790218540e@18.163.165.245:26626,8d59eb5f7ad207e59c06620f6e9e7b6760b56211@65.108.75.107:18656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.canine/config/config.toml
```
