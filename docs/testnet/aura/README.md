# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/aura.png" alt=""><figcaption></figcaption></figure>

The Aura Network protocol allows users to mint, rate, track data,  or trade NFT for the goal of constructing a strong platform to  support all trading assets on the crypto market in a simpler and easier way

**Chain ID**: euphoria-2 | **Latest Version Tag**: euphoria_v0.5.1 | **Wasm**: ON

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

**live-peers** (26)
```bash
peers="94f09cc1e0d2357c8c8423589c42dc7721387a60@176.9.44.113:26686,6ef01ca6714aa8127d1b21b5339909ca6319dae0@144.76.97.251:26776,d74774b137ce78a61ccbe9c30ff8ec8cb969247d@89.58.59.10:26656,38b49491b5eb8e4edb31e81acbadc42d50047a9e@66.206.2.162:27656,b2394ad608075aa405cdf4ab55e36376d93f7b1d@65.108.206.118:56656,e874935eee84c8313dbb52ba497aed2d8d1f1245@65.108.237.231:27656,e3dbeeeb2dea9912610b92a436dfe3cb831a94e4@65.108.195.29:36126,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:17656,7812205773ac30f3d47200ac2391c79896c60135@54.254.220.113:26656,3152129889968fe62faca92c7dd95bae190c92e5@135.181.142.60:15602,21f7e0a082bb1f156f8efdf6b6d36f505605584b@65.108.192.123:43656,3d6b07bdb11754c8c8512525dac109d8bdee3857@65.21.53.39:7656,fb3d13cb2e8ad1a1cae7dc1f21c62411007df9f8@85.10.193.246:33656,ab2b8330cd137984de0654561a31f461d8433424@88.99.3.158:21756,0770c2687cc34d59ca62270960d3ffcad6e42cf8@65.108.233.44:21656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.57:26966,7cad1bcb2ad777dba21840832341f2ce14bae1a5@5.75.174.126:26656,b9243524f659f2ff56691a4b2919c3060b2bb824@13.214.5.1:26656,241bd90cceab3ca7d5d4bcf79bca22c6255ec94b@135.148.233.0:26656,fdcc8f1ca406213d79947c5f38920a085ed90c0f@136.36.73.232:26676,9df9e8307e3e671c9bcd1a23f0b73b45f2b8003d@65.109.88.251:35656,e4d8765b82baf3f69c0dc6e5e0488705fa3ceddd@95.217.144.107:21756,314e6c8fe910618e7ec56048b30040e734fa41ff@89.117.56.126:25056,705e3c2b2b554586976ed88bb27f68e4c4176a33@13.250.223.114:26656,855b0ff76f5a80ab7f322e818263835d009de052@46.4.5.45:21756,6358ef9523b7c02f7c61ea9ac20521381d2c35c3@58.187.190.96:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.aura/config/config.toml
```
