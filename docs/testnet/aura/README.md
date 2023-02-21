# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/aura.png" width="150" alt=""><figcaption></figcaption></figure>

The Aura Network protocol allows users to mint, rate, track data,  or trade NFT for the goal of constructing a strong platform to  support all trading assets on the crypto market in a simpler and easier way

**Chain ID**: euphoria-2 | **Latest Version Tag**: euphoria_v0.4.2 | **Wasm**: ON

[Website](https://aura.network) | [Discord](https://discord.gg/hpvF5QcWRf) | [Twitter](https://twitter.com/AuraNetworkHQ)




## Chain explorer
[https://explorer.kjnodes.com/aura-testnet](https://explorer.kjnodes.com/aura-testnet)

## Public endpoints

* api: [https://aura-testnet.api.kjnodes.com](https://aura-testnet.api.kjnodes.com)
* rpc: [https://aura-testnet.rpc.kjnodes.com](https://aura-testnet.rpc.kjnodes.com)
* grpc: [https://aura-testnet.grpc.kjnodes.com](https://aura-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@aura-testnet.rpc.kjnodes.com:17656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@aura-testnet.rpc.kjnodes.com:17659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/aura-testnet/addrbook.json > $HOME/.aura/config/addrbook.json
```

**live-peers** (10)
```bash
peers="94f09cc1e0d2357c8c8423589c42dc7721387a60@176.9.44.113:26686,003686d978739de9988cbfcc6e120c2db41f87b5@65.109.30.12:46656,b2394ad608075aa405cdf4ab55e36376d93f7b1d@65.108.206.118:56656,7bc01325a59434dffaeef624c1c5f5f7b9fc826b@135.181.215.116:27656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:17656,5b2758dfcbcbc19b9a0ee04c09008b67c98cd7d9@162.244.35.40:24656,b130852645cc3d7925cfccd14d97425a2260e7ec@65.109.82.106:19656,bfef15bb8b4cbc4fb777aa33e75e6064cc1ba5bf@185.144.99.14:26656,7812205773ac30f3d47200ac2391c79896c60135@54.254.220.113:26656,fdcc8f1ca406213d79947c5f38920a085ed90c0f@144.202.72.17:26676"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.aura/config/config.toml
```
