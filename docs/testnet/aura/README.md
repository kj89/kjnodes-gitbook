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
peers="465b0a11c7ec9433f64758e0613361ebb4a5ce6e@213.133.102.206:20356,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:17656,b8125bee4bc07c591dfa0e292d18a800d28fabef@65.21.139.244:26656,2e1407476ad3566eb11ac92ad1df4782c7ba83dd@18.143.61.108:26656,3d6b07bdb11754c8c8512525dac109d8bdee3857@65.21.53.39:56656,ca62e050be3c2e688c367e373523ded011dec278@135.181.5.47:20356,e874935eee84c8313dbb52ba497aed2d8d1f1245@65.108.237.231:27656,fdcc8f1ca406213d79947c5f38920a085ed90c0f@144.202.72.17:26636,a8f02c61ae74b646c323ac5c98a1eae6a4770141@116.202.112.175:26656,ffb60d24d8a5ffc510bee9787995f64e21ed458c@13.229.97.101:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.aura/config/config.toml
```
