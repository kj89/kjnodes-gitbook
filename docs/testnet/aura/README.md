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

**live-peers** (22)
```bash
peers="94f09cc1e0d2357c8c8423589c42dc7721387a60@176.9.44.113:26686,fb3d13cb2e8ad1a1cae7dc1f21c62411007df9f8@85.10.193.246:33656,f758144073cd69baabcb1ff04d1d1f0f1200f728@85.10.200.221:29656,b130852645cc3d7925cfccd14d97425a2260e7ec@65.109.82.106:19656,9df9e8307e3e671c9bcd1a23f0b73b45f2b8003d@65.109.88.251:35656,e7d497959ae94823a70fc4c1c7fe2bc31b2ead57@135.181.143.48:28656,3d6b07bdb11754c8c8512525dac109d8bdee3857@65.21.53.39:7656,b2394ad608075aa405cdf4ab55e36376d93f7b1d@65.108.206.118:56656,0770c2687cc34d59ca62270960d3ffcad6e42cf8@65.108.233.44:21656,241bd90cceab3ca7d5d4bcf79bca22c6255ec94b@135.148.233.0:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:17656,7812205773ac30f3d47200ac2391c79896c60135@54.254.220.113:26656,6ef01ca6714aa8127d1b21b5339909ca6319dae0@144.76.97.251:26776,7cad1bcb2ad777dba21840832341f2ce14bae1a5@5.75.174.126:26656,e3dbeeeb2dea9912610b92a436dfe3cb831a94e4@65.108.195.29:36126,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.57:26966,a9e04c4648aa4b47b03949104f3d31263510c929@65.108.78.101:17656,c53157159e7cea010b86e44786831f792d852e1f@65.108.76.44:11023,fdcc8f1ca406213d79947c5f38920a085ed90c0f@144.202.72.17:26676,2e1407476ad3566eb11ac92ad1df4782c7ba83dd@18.143.61.108:26656,bbb958be20d917718c62a59ff01e58c200848674@3.237.196.11:26656,7bc01325a59434dffaeef624c1c5f5f7b9fc826b@135.181.215.116:27656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.aura/config/config.toml
```
