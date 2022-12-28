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
peers="ee2ef67b49cbc7b4af7ff0b7321870a5d9ae69a5@65.108.138.80:17556,68205c025ec65bf4d4183691d19d15b0a72221ec@65.108.42.185:26656,83d66a37202785b09aee4e3ae1b50d2ddfbf860c@162.19.89.8:10856,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:37656,170397e75ca2b0f4e9f3b1bb5d0d23f9b10f01c7@46.4.53.94:30565,7574e0ab179fc6cc47ac89284f4641790218540e@18.163.165.245:26626,46d4495643f2579573a61e181a88de3b8f0acc4f@2.139.23.24:36656,dbbd1e102b9d0cde827cd272205fa3a2886a6b2c@5.9.147.22:21656,72f98b8ac9af924c77f52cdc26a78e7728d4e19d@24.158.14.212:26656,9bcaee1ad957fa75f60a6dd9d8870e53220794a9@104.37.187.214:60756"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.canine/config/config.toml
```
