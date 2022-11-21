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
peers="222385f3ce7f55f9c01c23f2ee340ed9548b18fa@35.222.169.98:26656,84cc83cd09a974a234a3fdb5bb4fd46fd856f8ec@142.132.135.239:26656,a09ed43e09f773e39855dc5d8b6a220eff4cb947@204.16.241.207:26656,67685d93f2256caa7a2d53e3a104f9e437c3d247@95.216.114.244:26656,1997e68bf205bedeed0c4723786bf03464987dc1@77.87.108.21:26656,993d38129fcb402cb9733a0f6a9798f6d1a8f8ed@15.235.51.48:26656,52a6b8f416ba3ed2aafa72e35df28ee4c3ee547b@5.9.108.156:36656,44741f1e7a0fd0c66aedaba458ad9b517bc23d3f@54.248.188.49:26656,701036e718d0746d1d7055fb0fd1245cf361e0b8@168.119.79.106:26656,1da54d20c7339713f1d6d28dd2117087dd33d0ca@154.53.32.78:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gaia/config/config.toml
```
