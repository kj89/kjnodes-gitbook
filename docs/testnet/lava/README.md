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
peers="24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,14ae45e7f2ff7491cfa686a8fcac7cc095bc38ff@213.239.217.52:39656,b294ab07592bb93a85b099fb684dd96a98e12ba9@178.63.102.172:23356,47385d0a7051109de5342e3b27890c4a4b9e0763@65.108.72.233:16656,ef1b3374ca00c338de50d51fc41ca317488156eb@207.244.245.41:26656,5e068fccd370b2f2e5ab4240a304323af6385f1f@172.93.110.154:27656,c55e0f1c1916bfa35127ca194263fe65c75c2995@38.242.251.1:26656,b16eb3c538b9a460612a4cea37c2657f15579126@65.109.30.90:11656,433be6210ad6350bebebad68ec50d3e0d90cb305@217.13.223.167:60856,d64aa8f4d864daac54639cd1fdebbf4c464ba4f1@5.75.235.206:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
