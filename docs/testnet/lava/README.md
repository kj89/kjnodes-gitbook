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

**live-peers** (11)
```bash
peers="ed780f77754e8c4657b145144f0f95225d43bb03@65.108.224.156:27656,40046fe63bdaa9efde27707b0d3de0bf84fedf80@86.111.48.158:26656,b294ab07592bb93a85b099fb684dd96a98e12ba9@178.63.102.172:23356,433be6210ad6350bebebad68ec50d3e0d90cb305@217.13.223.167:60856,1fd86f6ba06ef4b189276f97f70fea04161019db@144.76.176.154:11656,3456c9ba0df46cbb526717d73fa51ff0ed9a53a1@95.216.14.58:60756,276c73534246fb9ec48d5c72ebd62c42e2f96462@157.90.17.150:26656,d796c20b5bdb8f1633c2a13afbf12314a77b668c@91.107.148.113:26656,2c419186cd96b59fe8b3307c54c27d6805414aba@65.108.8.28:60756,47385d0a7051109de5342e3b27890c4a4b9e0763@65.108.72.233:16656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14456"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
