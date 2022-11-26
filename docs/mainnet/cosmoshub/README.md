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
peers="2e6f37cfbc4549c23f4ec48e9de68203858b62fc@51.38.52.99:26656,4d94cc91625530f212d951ca1c18b2e850b8ac6e@88.208.227.114:26656,213857e741833d17275ea559bb2d0342398cec99@35.245.206.45:26656,915a5d104236764e33d5f7fd8d6c946e66766723@34.74.124.82:26656,222385f3ce7f55f9c01c23f2ee340ed9548b18fa@35.222.169.98:26656,bd410d4564f7e0dd9a0eb16a64c337a059e11b80@47.103.35.130:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:34656,c1e437f73b8889b78ea34981e7c349157ad80284@107.135.15.66:26656,3ddcd917b078dc61d2ff6b7281996acde35ad4fb@141.95.202.13:26656,0848802b3a558aa18ba25ba3fbe6aea3486241a1@23.88.72.109:26696"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gaia/config/config.toml
```
