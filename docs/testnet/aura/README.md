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
peers="914d435a0c6376fb367ae5d13a6f963b709d964b@142.132.223.189:26656,a8f02c61ae74b646c323ac5c98a1eae6a4770141@116.202.112.175:26656,64fdaa6da59901793beda215679ac2a6549b46b4@144.91.122.166:26656,b8125bee4bc07c591dfa0e292d18a800d28fabef@65.21.139.244:26656,3d6b07bdb11754c8c8512525dac109d8bdee3857@65.21.53.39:56656,5d869eb132e188b848875cc169edb3614d6bb620@144.76.27.79:26656,5fa2ce7aef7fe5f5b338f3f1dc1ffd2f58fcf120@18.219.32.49:26656,2e1407476ad3566eb11ac92ad1df4782c7ba83dd@18.143.61.108:26656,465b0a11c7ec9433f64758e0613361ebb4a5ce6e@213.133.102.206:20356,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:17656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.aura/config/config.toml
```
