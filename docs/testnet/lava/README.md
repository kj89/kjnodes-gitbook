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
peers="257856431ef33f9fbfe6c119fdf3820035891d0c@38.242.197.140:26656,ed780f77754e8c4657b145144f0f95225d43bb03@65.108.224.156:27656,035d086cc418352aba9e679e079f17391791ccc6@178.208.252.54:27656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14456,e1383b216c42acc842193c5ac7321ce6c0d73db0@78.47.37.142:26656,d8e81881ced029758f9623179a3c1ecf72aece2e@195.74.86.49:26656,433be6210ad6350bebebad68ec50d3e0d90cb305@217.13.223.167:60856,24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,9a151159039fd8abce61ddb21e5342605787792b@5.75.228.39:26656,1f704611e8aa4a53504fac1b80eb55c876dae8bd@65.108.13.154:30656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
