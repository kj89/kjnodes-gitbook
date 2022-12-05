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
peers="2a55d2e6cc5fa2dda8a484ab7d00f77f076d237f@141.95.47.216:26656,f6aaf53be76e005f83376ceca6d26d30ac93d42c@46.4.81.204:33656,c2842c76779913e05fa4256e3caab852e1782951@202.61.194.254:60756,289c3e984194ac2ccaa74e201147010648e90970@195.3.223.108:26656,dbec14a10d43c25d77ee9987a985652fa4e6344a@131.153.59.6:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:37656,83d66a37202785b09aee4e3ae1b50d2ddfbf860c@162.19.89.8:10856,5a4d1a83c877dd5db378ef5f897824273c2d4beb@141.95.72.198:36656,1f30e644ddd8edf310cbd9be4ac07b604eed581e@66.85.143.242:26676,4118b172fc2a45e0335c59641fd7c2e5e5e2c53c@65.108.238.203:28656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.canine/config/config.toml
```
