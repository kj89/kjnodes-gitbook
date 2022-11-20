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
peers="5d869eb132e188b848875cc169edb3614d6bb620@144.76.27.79:26656,e874935eee84c8313dbb52ba497aed2d8d1f1245@65.108.237.231:27656,fdcc8f1ca406213d79947c5f38920a085ed90c0f@144.202.72.17:26636,465b0a11c7ec9433f64758e0613361ebb4a5ce6e@213.133.102.206:20356,2e1407476ad3566eb11ac92ad1df4782c7ba83dd@18.143.61.108:26656,ca62e050be3c2e688c367e373523ded011dec278@135.181.5.47:20356,3d6b07bdb11754c8c8512525dac109d8bdee3857@65.21.53.39:56656,c53157159e7cea010b86e44786831f792d852e1f@135.181.72.187:11024,7812205773ac30f3d47200ac2391c79896c60135@54.254.220.113:26656,64fdaa6da59901793beda215679ac2a6549b46b4@144.91.122.166:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.aura/config/config.toml
```
