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
* grpc: aura-testnet.grpc.kjnodes.com:11790

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@aura-testnet.rpc.kjnodes.com:11756
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@aura-testnet.rpc.kjnodes.com:11759
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/aura-testnet/addrbook.json > $HOME/.aura/config/addrbook.json
```

**live-peers** (10)
```bash
peers="b2394ad608075aa405cdf4ab55e36376d93f7b1d@65.108.206.118:56656,9df9e8307e3e671c9bcd1a23f0b73b45f2b8003d@65.109.88.251:35656,855b0ff76f5a80ab7f322e818263835d009de052@46.4.5.45:21756,7cad1bcb2ad777dba21840832341f2ce14bae1a5@5.75.174.126:26656,94f09cc1e0d2357c8c8423589c42dc7721387a60@176.9.44.113:26686,6ef01ca6714aa8127d1b21b5339909ca6319dae0@144.76.97.251:26776,fb3d13cb2e8ad1a1cae7dc1f21c62411007df9f8@85.10.193.246:33656,2e1407476ad3566eb11ac92ad1df4782c7ba83dd@18.143.61.108:26656,e4d8765b82baf3f69c0dc6e5e0488705fa3ceddd@95.217.144.107:21756,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:11756"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.aura/config/config.toml
```
