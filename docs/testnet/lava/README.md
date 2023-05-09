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
peers="37add870e1f40b6b00a55b71d20590b2128fdd3d@88.99.33.248:26656,ba78f0ac713d5e7a0274ef593674dae337aabbee@176.103.222.18:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14456,64df498c92b9ccaf78012229d399aa34a014f087@65.109.122.105:56659,13a9209a4d08803a3becac57de8eb02dd51f8f41@65.109.23.114:19956,bfe21dd5af98aa42d213cd5bd943162a36b0505f@92.243.165.98:26656,3173b2d34ce415ee9a1bf08646d85688bf49e299@5.189.186.222:36656,fe1998168f5336811a79fbcaf2d5d5a69f2f9f63@65.108.81.145:26656,8a117e9a5a7dcbf3963a2d1982aabc92fa5e2a5d@18.220.175.93:26656,5e068fccd370b2f2e5ab4240a304323af6385f1f@172.93.110.154:27656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
