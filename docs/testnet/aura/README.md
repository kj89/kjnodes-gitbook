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
peers="d74774b137ce78a61ccbe9c30ff8ec8cb969247d@89.58.59.10:26656,bfef15bb8b4cbc4fb777aa33e75e6064cc1ba5bf@185.144.99.14:26656,b2394ad608075aa405cdf4ab55e36376d93f7b1d@65.108.206.118:56656,7812205773ac30f3d47200ac2391c79896c60135@54.254.220.113:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:17656,3152129889968fe62faca92c7dd95bae190c92e5@135.181.142.60:15602,fdcc8f1ca406213d79947c5f38920a085ed90c0f@144.202.72.17:26676,9735c8bb1551d210ea6021f5c7ea3f288ba888df@65.109.38.111:21756,241bd90cceab3ca7d5d4bcf79bca22c6255ec94b@135.148.233.0:26656,b9243524f659f2ff56691a4b2919c3060b2bb824@13.214.5.1:26656,1e9b7325e120a3d511eec20a3199c2218343fcd3@65.108.105.99:28656,38b49491b5eb8e4edb31e81acbadc42d50047a9e@66.206.2.162:27656,ab2b8330cd137984de0654561a31f461d8433424@88.99.3.158:21756,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.57:26966,9df9e8307e3e671c9bcd1a23f0b73b45f2b8003d@65.109.88.251:35656,7cad1bcb2ad777dba21840832341f2ce14bae1a5@5.75.174.126:26656,fb3d13cb2e8ad1a1cae7dc1f21c62411007df9f8@85.10.193.246:33656,e3dbeeeb2dea9912610b92a436dfe3cb831a94e4@65.108.195.29:36126,2e1407476ad3566eb11ac92ad1df4782c7ba83dd@18.143.61.108:26656,b130852645cc3d7925cfccd14d97425a2260e7ec@65.109.82.106:19656,e4d8765b82baf3f69c0dc6e5e0488705fa3ceddd@95.217.144.107:21756,ade4d8bc8cbe014af6ebdf3cb7b1e9ad36f412c0@176.9.82.221:21756"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.aura/config/config.toml
```
