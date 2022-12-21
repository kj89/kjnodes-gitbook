# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/aura.png" width="150" alt=""><figcaption></figcaption></figure>

The Aura Network protocol allows users to mint, rate, track data,  or trade NFT for the goal of constructing a strong platform to  support all trading assets on the crypto market in a simpler and easier way

**Chain ID**: euphoria-2 | **Latest Version Tag**: euphoria_v0.4.2 | **Wasm**: ON

[Website](https://aura.network) | [Discord](https://discord.gg/hpvF5QcWRf) | [Twitter](https://twitter.com/AuraNetworkHQ)


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
peers="7cad1bcb2ad777dba21840832341f2ce14bae1a5@5.75.174.126:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:17656,b2394ad608075aa405cdf4ab55e36376d93f7b1d@65.108.206.118:56656,5b2758dfcbcbc19b9a0ee04c09008b67c98cd7d9@162.244.35.40:24656,2e1407476ad3566eb11ac92ad1df4782c7ba83dd@18.143.61.108:26656,3d6b07bdb11754c8c8512525dac109d8bdee3857@65.21.53.39:7656,7812205773ac30f3d47200ac2391c79896c60135@54.254.220.113:26656,e874935eee84c8313dbb52ba497aed2d8d1f1245@65.108.237.231:27656,2694dd6c739393ad7066dc384e41a21b334f5a35@142.132.223.189:26656,003686d978739de9988cbfcc6e120c2db41f87b5@65.109.30.12:46656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.aura/config/config.toml
```
