# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/lava.png" alt=""><figcaption></figcaption></figure>

Lava powers a trustless market for RPC data access. The protocol  governs over peer to peer and private Provider-Application pairings,  ensuring high quality RPC service while creating consensus around data served.

**Chain ID**: lava-testnet-1 | **Latest Version Tag**: v0.12.1-hf | **Wasm**: OFF

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

**live-peers** (11)
```bash
peers="24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,433be6210ad6350bebebad68ec50d3e0d90cb305@217.13.223.167:60856,1dc8db6b9b800deded531bfb56ce12defbc98c74@173.249.46.50:26656,14ae45e7f2ff7491cfa686a8fcac7cc095bc38ff@213.239.217.52:39656,abef1d647b77b701d81ae15e093bf00d29cc56e1@46.4.50.247:13656,47385d0a7051109de5342e3b27890c4a4b9e0763@65.108.72.233:16656,c40a7bc3c7aee0428273c0bfa75fcb14bf0f44c4@65.109.90.171:30656,bfe21dd5af98aa42d213cd5bd943162a36b0505f@92.243.165.98:26656,d8e81881ced029758f9623179a3c1ecf72aece2e@195.74.86.49:26656,bb8c8cea499a1fa7e97922b5a9882c2360c6575a@176.103.222.21:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14456"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
