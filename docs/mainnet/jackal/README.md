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
peers="fc905fe58d36875a833202ce53759d0ae6c11435@141.95.65.26:48656,5a4d1a83c877dd5db378ef5f897824273c2d4beb@141.95.72.198:36656,0b8bbc839c20b07ac5999bca7d905d53274c5f2d@24.158.14.214:36656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:37656,a2afb42b65da7013eca54778ce01dfb877c2a82a@154.12.227.132:37656,4398bd773ac885b7365de3604eb487be10c54563@185.16.38.210:26906,e08efc0b0e15e4d8eacf0f4ed5e52f6e9bdc312d@144.76.97.251:36156,dbec14a10d43c25d77ee9987a985652fa4e6344a@131.153.59.6:26656,1f30e644ddd8edf310cbd9be4ac07b604eed581e@66.85.143.242:26676,9bcaee1ad957fa75f60a6dd9d8870e53220794a9@104.37.187.214:60756"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.canine/config/config.toml
```
