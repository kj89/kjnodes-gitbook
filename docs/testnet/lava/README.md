# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/lava.png" alt=""><figcaption></figcaption></figure>

Lava powers a trustless market for RPC data access. The protocol  governs over peer to peer and private Provider-Application pairings,  ensuring high quality RPC service while creating consensus around data served.

**Chain ID**: lava-testnet-1 | **Latest Version Tag**: v0.12.1 | **Wasm**: OFF

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
peers="ed780f77754e8c4657b145144f0f95225d43bb03@65.108.224.156:27656,47385d0a7051109de5342e3b27890c4a4b9e0763@65.108.72.233:16656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14456,5585de73ef537dcbbe8ae04392ccea3a112cc6e6@65.109.85.170:49656,230648adf4aa55029c72ec5d7bc1be59529acf34@37.120.171.159:26656,257856431ef33f9fbfe6c119fdf3820035891d0c@38.242.197.140:26656,433be6210ad6350bebebad68ec50d3e0d90cb305@217.13.223.167:60856,8b154033143fdedf4835dfc7b030c7d781bfd54e@195.201.219.227:26656,13a9209a4d08803a3becac57de8eb02dd51f8f41@65.109.23.114:19956,40046fe63bdaa9efde27707b0d3de0bf84fedf80@86.111.48.158:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
