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
peers="b130852645cc3d7925cfccd14d97425a2260e7ec@65.109.82.106:19656,3d6b07bdb11754c8c8512525dac109d8bdee3857@65.21.53.39:7656,e874935eee84c8313dbb52ba497aed2d8d1f1245@65.108.237.231:27656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:17656,003686d978739de9988cbfcc6e120c2db41f87b5@65.109.30.12:46656,2e1407476ad3566eb11ac92ad1df4782c7ba83dd@18.143.61.108:26656,2694dd6c739393ad7066dc384e41a21b334f5a35@142.132.223.189:26656,7812205773ac30f3d47200ac2391c79896c60135@54.254.220.113:26656,f4047b504d4d5faa47a9044ab48bd29837051d79@5.161.141.144:26656,94f09cc1e0d2357c8c8423589c42dc7721387a60@176.9.44.113:26686"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.aura/config/config.toml
```
