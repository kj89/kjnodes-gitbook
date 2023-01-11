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

**live-peers** (16)
```bash
peers="26b6255375a592c3b0664bd474a6975f468c3785@88.99.164.158:11126,dd7e72f0a71476e51c0a601a40d6fc02a1ae1a95@65.108.6.45:60856,d0313585956c8e7969993c1577f4969739b19bb7@85.10.238.147:26656,170397e75ca2b0f4e9f3b1bb5d0d23f9b10f01c7@46.4.53.94:30565,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:37656,11c23c5341d0ac69f9ebb3be9afa7fe0e134ece0@94.79.54.137:28656,e272f855eb99975dbd23bfc52dce9ff9661596ff@65.109.60.54:37656,bc6ce122e5809b06dcf90742ee40091f3ee6bcee@142.132.248.253:42656,0faa7f1099de2e02deebe09fcb52863056333265@144.202.72.17:26616,ebc272824924ea1a27ea3183dd0b9ba713494f83@95.214.52.139:26906,4398bd773ac885b7365de3604eb487be10c54563@185.16.38.210:26906,0836e6f18a67cc6139e315f024189cb8a84f3121@95.217.0.158:26656,637166728d6103ad4ec9fff97a321a024bff3e58@65.109.94.221:28656,4bfc9e0f762e952b76daee87e9ffd081d2974f75@188.217.162.92:26656,a79da224ad9d4501dbf1d547986ebec55d56b951@135.181.128.114:17556,0841db0ae5e5443905837e196d2e1ffd31f2e480@131.153.202.81:36656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.canine/config/config.toml
```
