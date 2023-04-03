# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/aura.png" width="150" alt=""><figcaption></figcaption></figure>

The Aura Network protocol allows users to mint, rate, track data,  or trade NFT for the goal of constructing a strong platform to  support all trading assets on the crypto market in a simpler and easier way

**Chain ID**: euphoria-2 | **Latest Version Tag**: euphoria_v0.4.4 | **Wasm**: ON

[Website](https://aura.network) | [Discord](https://discord.gg/hpvF5QcWRf) | [Twitter](https://twitter.com/AuraNetworkHQ)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/aura-testnet](https://explorer.kjnodes.com/aura-testnet)

## Public endpoints

* api: [https://aura-testnet.api.kjnodes.com](https://aura-testnet.api.kjnodes.com)
* rpc: [https://aura-testnet.rpc.kjnodes.com](https://aura-testnet.rpc.kjnodes.com)
* grpc: aura-testnet.grpc.kjnodes.com:17090

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

**live-peers** (16)
```bash
peers="1e9b7325e120a3d511eec20a3199c2218343fcd3@65.108.105.99:28656,b130852645cc3d7925cfccd14d97425a2260e7ec@65.109.82.106:19656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:17656,7812205773ac30f3d47200ac2391c79896c60135@54.254.220.113:26656,e3dbeeeb2dea9912610b92a436dfe3cb831a94e4@65.108.195.29:36126,c53157159e7cea010b86e44786831f792d852e1f@65.108.76.44:11023,b2394ad608075aa405cdf4ab55e36376d93f7b1d@65.108.206.118:56656,9df9e8307e3e671c9bcd1a23f0b73b45f2b8003d@65.109.88.251:35656,fb3d13cb2e8ad1a1cae7dc1f21c62411007df9f8@85.10.193.246:33656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.57:26966,fdcc8f1ca406213d79947c5f38920a085ed90c0f@144.202.72.17:26676,7bc01325a59434dffaeef624c1c5f5f7b9fc826b@135.181.215.116:27656,0770c2687cc34d59ca62270960d3ffcad6e42cf8@65.108.233.44:21656,2216fb37f6fe5f22b84586e15fd0d25f41458531@116.96.44.135:26656,402173d6f0715cd152a8df8e5db198811ced5603@38.242.206.189:26656,2e1407476ad3566eb11ac92ad1df4782c7ba83dd@18.143.61.108:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.aura/config/config.toml
```
