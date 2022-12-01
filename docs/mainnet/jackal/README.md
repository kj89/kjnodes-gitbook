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
peers="c2842c76779913e05fa4256e3caab852e1782951@202.61.194.254:60756,f7b5bc8e8eb8a954f9c36ac7c06ff7b9b847c785@167.86.82.140:46656,0faa7f1099de2e02deebe09fcb52863056333265@144.202.72.17:26616,e258f57604c59fc02d07b9669ae64f00bb45a20c@162.205.240.139:37656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:37656,dd7e72f0a71476e51c0a601a40d6fc02a1ae1a95@65.108.6.45:60856,0985977a794b298e7ef990fe344d572c60c453b1@172.105.72.158:26656,05ab6d764ff112666275376b3f664fc3b19d3bc3@195.201.165.123:11126,2a55d2e6cc5fa2dda8a484ab7d00f77f076d237f@141.95.47.216:26656,fc905fe58d36875a833202ce53759d0ae6c11435@141.95.65.26:48656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.canine/config/config.toml
```
