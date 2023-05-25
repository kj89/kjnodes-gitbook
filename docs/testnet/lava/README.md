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
peers="47385d0a7051109de5342e3b27890c4a4b9e0763@65.108.72.233:16656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14456,897d44b1cb6633539cf51261f6629a9d5664eb9b@159.69.72.247:11656,64df498c92b9ccaf78012229d399aa34a014f087@65.109.122.105:56659,1f704611e8aa4a53504fac1b80eb55c876dae8bd@65.108.13.154:30656,ef38861694f07881410c1b1c5852c72050831d68@95.214.55.74:26656,1ec38451f3e45535ceba905d1442310c69aaf93e@217.76.61.37:26656,5e068fccd370b2f2e5ab4240a304323af6385f1f@172.93.110.154:27656,433be6210ad6350bebebad68ec50d3e0d90cb305@217.13.223.167:60856,257856431ef33f9fbfe6c119fdf3820035891d0c@38.242.197.140:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
