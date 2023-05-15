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
peers="37add870e1f40b6b00a55b71d20590b2128fdd3d@88.99.33.248:26656,24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,95c59c9236f2e1c1c9ee35c6a9cd1b9f2fdc362e@213.239.215.115:29956,147cf727f179eccbd29de3ebf5899c1f4a93f6de@46.38.235.53:26656,8b154033143fdedf4835dfc7b030c7d781bfd54e@195.201.219.227:26656,bfe21dd5af98aa42d213cd5bd943162a36b0505f@92.243.165.98:26656,47385d0a7051109de5342e3b27890c4a4b9e0763@65.108.72.233:16656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14456,ac7cefeff026e1c616035a49f3b00c78da63c2e9@18.215.128.248:26656,8a117e9a5a7dcbf3963a2d1982aabc92fa5e2a5d@18.220.175.93:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
