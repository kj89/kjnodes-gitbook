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
peers="e08efc0b0e15e4d8eacf0f4ed5e52f6e9bdc312d@144.76.97.251:36156,a77da5b3ce86a5226bae6e7b87964dd4efe8fe46@65.21.170.3:31656,83d66a37202785b09aee4e3ae1b50d2ddfbf860c@162.19.89.8:10856,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:37656,6852add4eaa027707a6000c78ea9e7cde81b058f@18.118.26.4:26656,ed0ac0ebe8464781a1bd4934701e36f0f3538548@24.158.14.212:26656,0841db0ae5e5443905837e196d2e1ffd31f2e480@131.153.202.81:36656,e272f855eb99975dbd23bfc52dce9ff9661596ff@65.109.60.54:37656,dbec14a10d43c25d77ee9987a985652fa4e6344a@131.153.59.6:26656,a2afb42b65da7013eca54778ce01dfb877c2a82a@154.12.227.132:37656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.canine/config/config.toml
```
