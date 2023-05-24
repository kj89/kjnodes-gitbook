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
peers="e268a2ce255d51a93e6ec89ee73c233bbaec70f4@49.12.185.46:26656,a5e61061417d9d4b51bbfa2a66042cfce7047f5d@195.201.197.4:14656,47385d0a7051109de5342e3b27890c4a4b9e0763@65.108.72.233:16656,14ae45e7f2ff7491cfa686a8fcac7cc095bc38ff@213.239.217.52:39656,4634ca7cefe997035440df1095915ed255e81296@49.12.189.98:26656,433be6210ad6350bebebad68ec50d3e0d90cb305@217.13.223.167:60856,697750a8171090e8547c1749ff05c88c080f6350@131.153.158.137:26656,897d44b1cb6633539cf51261f6629a9d5664eb9b@159.69.72.247:11656,daf1720b75cd6f200daac9c453910257e20e6e52@161.97.74.88:26256,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14456"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
