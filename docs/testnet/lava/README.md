# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/lava.png" alt=""><figcaption></figcaption></figure>

Lava powers a trustless market for RPC data access. The protocol  governs over peer to peer and private Provider-Application pairings,  ensuring high quality RPC service while creating consensus around data served.

**Chain ID**: lava-testnet-1 | **Latest Version Tag**: v0.10.1 | **Wasm**: OFF

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
peers="95c59c9236f2e1c1c9ee35c6a9cd1b9f2fdc362e@213.239.215.115:29956,433be6210ad6350bebebad68ec50d3e0d90cb305@217.13.223.167:60856,64df498c92b9ccaf78012229d399aa34a014f087@65.109.122.105:56659,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14456,8b154033143fdedf4835dfc7b030c7d781bfd54e@195.201.219.227:26656,f0758765ef0350d5cbbdeebf0b8e84f76e21c46d@54.221.204.97:26656,370ae92bd28701e0c1d8dc912ccf0d40fe0db3d5@157.90.245.166:26656,47385d0a7051109de5342e3b27890c4a4b9e0763@65.108.72.233:16656,257856431ef33f9fbfe6c119fdf3820035891d0c@38.242.197.140:26656,1f704611e8aa4a53504fac1b80eb55c876dae8bd@65.108.13.154:30656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
