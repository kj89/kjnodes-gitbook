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

**live-peers** (10)
```bash
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14456,47385d0a7051109de5342e3b27890c4a4b9e0763@65.108.72.233:16656,4c50601b49951a90204e72371e9efb453092f824@194.61.28.72:26656,57d64cbf5a16820aa9a0582335705f37dde4c18b@190.15.217.229:26656,b16eb3c538b9a460612a4cea37c2657f15579126@65.109.30.90:11656,230648adf4aa55029c72ec5d7bc1be59529acf34@37.120.171.159:26656,bb8c8cea499a1fa7e97922b5a9882c2360c6575a@176.103.222.21:26656,433be6210ad6350bebebad68ec50d3e0d90cb305@217.13.223.167:60856,b1806dfabc9bb5fb721b3f82628a3fb23a2ad786@65.109.65.248:30656,653bb90f4e8a1db9dbbeadd7bd5ae7fd1e1bb7e6@65.108.101.4:23356"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
