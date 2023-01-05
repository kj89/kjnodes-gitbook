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
peers="8d59eb5f7ad207e59c06620f6e9e7b6760b56211@65.108.75.107:18656,637166728d6103ad4ec9fff97a321a024bff3e58@65.109.94.221:28656,2a55d2e6cc5fa2dda8a484ab7d00f77f076d237f@141.95.47.216:26656,bc6ce122e5809b06dcf90742ee40091f3ee6bcee@142.132.248.253:42656,ad41936e5f89b119fdaae25fef0652949770f06e@185.107.57.74:26656,170397e75ca2b0f4e9f3b1bb5d0d23f9b10f01c7@46.4.53.94:30565,72f98b8ac9af924c77f52cdc26a78e7728d4e19d@24.158.14.212:26656,0985977a794b298e7ef990fe344d572c60c453b1@172.105.72.158:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:37656,46d4495643f2579573a61e181a88de3b8f0acc4f@2.139.23.24:36656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.canine/config/config.toml
```
