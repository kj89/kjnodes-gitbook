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

**live-peers** (17)
```bash
peers="dd7e72f0a71476e51c0a601a40d6fc02a1ae1a95@65.108.6.45:60856,db9c7d34cd04e155b3eed730f68fc9315245cf5c@65.108.124.219:30656,588e509e3a8c1dc4ba938779bf569cd9f6f0f4be@212.23.222.109:26256,55df88ae25223565af42ccd6b3b558b8e70bba31@213.239.216.252:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:37656,11c23c5341d0ac69f9ebb3be9afa7fe0e134ece0@94.79.54.137:28656,e272f855eb99975dbd23bfc52dce9ff9661596ff@65.109.60.54:37656,c0b6d010bb442ff6511bc6fdde1f319b8a3a3bdc@65.108.127.50:17556,5745d29dd5b49009f405e21913a474a23f1e40ec@131.153.57.226:43656,ebc272824924ea1a27ea3183dd0b9ba713494f83@95.214.52.139:26906,26b6255375a592c3b0664bd474a6975f468c3785@88.99.164.158:11126,6e7d2937b3d29952cf83058b81fad4a1ec3b88e8@195.3.223.204:10756,a79da224ad9d4501dbf1d547986ebec55d56b951@135.181.128.114:17556,9bcaee1ad957fa75f60a6dd9d8870e53220794a9@104.37.187.214:60756,a4a4168d22313a9d34e5e6c208e053292096864d@66.85.149.162:43656,4bfc9e0f762e952b76daee87e9ffd081d2974f75@188.217.162.92:26656,6852add4eaa027707a6000c78ea9e7cde81b058f@18.118.26.4:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.canine/config/config.toml
```
