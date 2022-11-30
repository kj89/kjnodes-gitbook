# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/cosmoshub.png" width="150" alt=""><figcaption></figcaption></figure>

The Cosmos Hub is the blockchain protocol underlying an  increasingly large number of blockchains built on the  Cosmos Network, allowing them to communicate with each other.

**Chain ID**: cosmoshub-4 | **Latest Version Tag**: v7.1.0 | **Wasm**: OFF

Website: [https://hub.cosmos.network](https://hub.cosmos.network)


## Public endpoints

* rpc: [https://cosmoshub.rpc.kjnodes.com](https://cosmoshub.rpc.kjnodes.com)
* api: [https://cosmoshub.api.kjnodes.com](https://cosmoshub.api.kjnodes.com)

## Peering

**state-sync**

```
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@cosmoshub.rpc.kjnodes.com:34656
```

**seed-node**

```
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@cosmoshub.rpc.kjnodes.com:34659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/cosmoshub/addrbook.json > $HOME/.gaia/config/addrbook.json
```

**live-peers** (10)
```
peers="1da54d20c7339713f1d6d28dd2117087dd33d0ca@154.53.32.78:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:34656,dd53fa5cfb6a604feb80860d47506d0dd84baa12@142.132.210.234:26656,89c643c1f8bee0eaa680a304eb067905df986643@95.217.122.233:26656,2240ec8c6271ab9a7e8ccf108f78a43c2521d3e6@34.125.189.191:26656,52a6b8f416ba3ed2aafa72e35df28ee4c3ee547b@5.9.108.156:36656,d5cdd27a0aae56776f6fba0b7ba0ee66aeba534a@88.198.11.139:26656,29826fe1aa7aa136b00e513f8043fe91aa92c88c@138.201.63.38:26656,efe3df8397cbb8f070200184fa9f32ef9d790e41@139.180.185.11:26956,44741f1e7a0fd0c66aedaba458ad9b517bc23d3f@54.248.188.49:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gaia/config/config.toml
```
