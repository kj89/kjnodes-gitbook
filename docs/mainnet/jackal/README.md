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
peers="399068f8371dce4ae5d7cd7da2c965e765e68f4b@65.108.238.102:17556,c0b6d010bb442ff6511bc6fdde1f319b8a3a3bdc@65.108.127.50:17556,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:37656,e5a142be860ee9b2f5c71d813e39fceb12cbd218@78.46.78.83:26686,4398bd773ac885b7365de3604eb487be10c54563@185.16.38.210:26906,e258f57604c59fc02d07b9669ae64f00bb45a20c@162.205.240.139:37656,039a1c4f438c1ecc2dd901e7316d16fdafadfdab@104.193.254.36:27656,68205c025ec65bf4d4183691d19d15b0a72221ec@65.108.42.185:26656,1f30e644ddd8edf310cbd9be4ac07b604eed581e@66.85.143.242:26676,8c6eae80747ae0a45befcece5170d23f432a2fb1@51.89.224.199:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.canine/config/config.toml
```
