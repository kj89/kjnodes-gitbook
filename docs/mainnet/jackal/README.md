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
peers="108652f503665772ad024d9d2129a9f4fa9ffe9b@176.9.98.24:30536,f7b5bc8e8eb8a954f9c36ac7c06ff7b9b847c785@167.86.82.140:46656,f90a64a0a3f3c0480360e0fe5dd0f806d7741558@207.244.127.5:26656,dbec14a10d43c25d77ee9987a985652fa4e6344a@131.153.59.6:26656,1f30e644ddd8edf310cbd9be4ac07b604eed581e@66.85.143.242:26676,e98ed884751f26b98bc32d4469efd53b3507129f@15.235.114.194:10756,c0b6d010bb442ff6511bc6fdde1f319b8a3a3bdc@65.108.127.50:17556,0e095a81f6e9633f321c405fcd8524457cba49ee@144.76.17.48:10856,399068f8371dce4ae5d7cd7da2c965e765e68f4b@65.108.238.102:17556,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:37656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.canine/config/config.toml
```
