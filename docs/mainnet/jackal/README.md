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
peers="c2842c76779913e05fa4256e3caab852e1782951@202.61.194.254:60756,ea35106e43dcec1e5c66319272da48df3dce7723@57.128.144.233:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:37656,2ec46ff04ebfafc19f505feaaf00943c15bb2757@185.16.38.149:26656,173c43436e2287f3660c344a5fd2386da4a61968@65.109.92.241:11126,b8b29fe5391749ca1425e60212a944e24ac4a03e@135.181.139.115:31656,7574e0ab179fc6cc47ac89284f4641790218540e@18.163.165.245:26626,519f2b648a2a8794ac33b195f39b6d836e09f8f2@131.153.154.13:26656,dd7e72f0a71476e51c0a601a40d6fc02a1ae1a95@65.108.6.45:60856,fc905fe58d36875a833202ce53759d0ae6c11435@141.95.65.26:48656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.canine/config/config.toml
```
