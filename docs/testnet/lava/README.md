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
peers="147cf727f179eccbd29de3ebf5899c1f4a93f6de@46.38.235.53:26656,ed780f77754e8c4657b145144f0f95225d43bb03@65.108.224.156:27656,5c107bb2b72c930a5ab3406a1f7c7345b7229b49@148.251.11.99:11656,433be6210ad6350bebebad68ec50d3e0d90cb305@217.13.223.167:60856,3177033dfc8a88c0b1a4500e2812c74f41e9a32b@94.130.236.21:26656,14ae45e7f2ff7491cfa686a8fcac7cc095bc38ff@213.239.217.52:39656,697750a8171090e8547c1749ff05c88c080f6350@131.153.158.137:26656,f68c57ca955420779773f9320a6b7710c2b29f73@188.191.36.222:26656,24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,bee277da0e5b235e0a7e38ea90d8547924370dbe@65.108.227.112:13656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
