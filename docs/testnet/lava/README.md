# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/lava.png" alt=""><figcaption></figcaption></figure>

Lava powers a trustless market for RPC data access. The protocol  governs over peer to peer and private Provider-Application pairings,  ensuring high quality RPC service while creating consensus around data served.

**Chain ID**: lava-testnet-1 | **Latest Version Tag**: v0.11.2 | **Wasm**: OFF

[Website](https://lavanet.xyz) | [Discord](https://discord.com/invite/Tbk5NxTCdA) | [Twitter](https://twitter.com/lavanetxyz)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/lava-testnet](https://explorer.kjnodes.com/lava-testnet)

## Public endpoints

* api: [https://lava-testnet.api.kjnodes.com](https://lava-testnet.api.kjnodes.com)
* rpc: [https://lava-testnet.rpc.kjnodes.com](https://lava-testnet.rpc.kjnodes.com)
* grpc: lava-testnet.grpc.kjnodes.com:14490

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@lava-testnet.rpc.kjnodes.com:14456
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@lava-testnet.rpc.kjnodes.com:14459
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/lava-testnet/addrbook.json > $HOME/.lava/config/addrbook.json
```

**live-peers** (10)
```bash
peers="13a9209a4d08803a3becac57de8eb02dd51f8f41@65.109.23.114:19956,47385d0a7051109de5342e3b27890c4a4b9e0763@65.108.72.233:16656,71f6af45c867266f81d81193013fcb4137351355@194.163.155.84:56656,433be6210ad6350bebebad68ec50d3e0d90cb305@217.13.223.167:60856,d8e81881ced029758f9623179a3c1ecf72aece2e@195.74.86.49:26656,ef38861694f07881410c1b1c5852c72050831d68@95.214.55.74:26656,15480dd0fcccdf317d11993ff4c5d0098bc48a47@78.46.106.75:11656,397056c8cd7e2fce451d4f8e34ef24c0c9ffacba@176.9.44.113:26676,90451ff8f47b8f4b077e95837f112135fea14531@207.180.231.123:31656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14456"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
