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
peers="fb3d13cb2e8ad1a1cae7dc1f21c62411007df9f8@85.10.193.246:33656,d74774b137ce78a61ccbe9c30ff8ec8cb969247d@89.58.59.10:26656,1e9b7325e120a3d511eec20a3199c2218343fcd3@65.108.105.99:28656,b2394ad608075aa405cdf4ab55e36376d93f7b1d@65.108.206.118:56656,94f09cc1e0d2357c8c8423589c42dc7721387a60@176.9.44.113:26686,855b0ff76f5a80ab7f322e818263835d009de052@46.4.5.45:21756,7cad1bcb2ad777dba21840832341f2ce14bae1a5@5.75.174.126:26656,b130852645cc3d7925cfccd14d97425a2260e7ec@65.109.82.106:19656,9df9e8307e3e671c9bcd1a23f0b73b45f2b8003d@65.109.88.251:35656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:11756"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.aura/config/config.toml
```
