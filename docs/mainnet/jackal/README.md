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
peers="399068f8371dce4ae5d7cd7da2c965e765e68f4b@65.108.238.102:17556,d0313585956c8e7969993c1577f4969739b19bb7@85.10.238.147:26656,2ec46ff04ebfafc19f505feaaf00943c15bb2757@185.16.38.149:26656,e258f57604c59fc02d07b9669ae64f00bb45a20c@162.205.240.139:37656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:37656,bc6ce122e5809b06dcf90742ee40091f3ee6bcee@142.132.248.253:42656,83d66a37202785b09aee4e3ae1b50d2ddfbf860c@162.19.89.8:10856,5a4d1a83c877dd5db378ef5f897824273c2d4beb@141.95.72.198:36656,0b8bbc839c20b07ac5999bca7d905d53274c5f2d@24.158.14.214:36656,173c43436e2287f3660c344a5fd2386da4a61968@65.109.92.241:11126"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.canine/config/config.toml
```
