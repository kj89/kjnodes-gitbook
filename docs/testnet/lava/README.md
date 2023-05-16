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
peers="e268a2ce255d51a93e6ec89ee73c233bbaec70f4@49.12.185.46:26656,5c107bb2b72c930a5ab3406a1f7c7345b7229b49@148.251.11.99:11656,147cf727f179eccbd29de3ebf5899c1f4a93f6de@46.38.235.53:26656,47385d0a7051109de5342e3b27890c4a4b9e0763@65.108.72.233:16656,ed780f77754e8c4657b145144f0f95225d43bb03@65.108.224.156:27656,370ae92bd28701e0c1d8dc912ccf0d40fe0db3d5@157.90.245.166:26656,8a117e9a5a7dcbf3963a2d1982aabc92fa5e2a5d@18.220.175.93:26656,d8e81881ced029758f9623179a3c1ecf72aece2e@195.74.86.49:26656,5d24eb95fa5974af7bb03e370382537251ab6328@95.217.158.66:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14456"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
