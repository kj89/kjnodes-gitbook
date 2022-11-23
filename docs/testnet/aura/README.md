# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/aura.png" width="150" alt=""><figcaption></figcaption></figure>

The Aura Network protocol allows users to mint, rate, track data,  or trade NFT for the goal of constructing a strong platform to  support all trading assets on the crypto market in a simpler and easier way

**Chain ID**: euphoria-1 | **Latest Version Tag**: euphoria_v0.3.3 | **Wasm**: ON

Website: [https://aura.network](https://aura.network)


## Public endpoints

* rpc: [https://aura-testnet.rpc.kjnodes.com](https://aura-testnet.rpc.kjnodes.com)
* api: [https://aura-testnet.api.kjnodes.com](https://aura-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@aura-testnet.rpc.kjnodes.com:17656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@aura-testnet.rpc.kjnodes.com:17659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/aura-testnet/addrbook.json > $HOME/.aura/config/addrbook.json
```

**live-peers** (10)
```
peers="a8f02c61ae74b646c323ac5c98a1eae6a4770141@116.202.112.175:26656,64fdaa6da59901793beda215679ac2a6549b46b4@144.91.122.166:26656,3d6b07bdb11754c8c8512525dac109d8bdee3857@65.21.53.39:56656,fdcc8f1ca406213d79947c5f38920a085ed90c0f@144.202.72.17:26636,7812205773ac30f3d47200ac2391c79896c60135@54.254.220.113:26656,e874935eee84c8313dbb52ba497aed2d8d1f1245@65.108.237.231:27656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:17656,bfa492255ba40d3422f3078bfd6e55696ba005c0@65.108.101.50:60756,1b2b9641ec4c4af89ad9e1d1d4d1b61d60f2b63f@142.132.199.27:20356,c53157159e7cea010b86e44786831f792d852e1f@135.181.72.187:11024"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.aura/config/config.toml
```
