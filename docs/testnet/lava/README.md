# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/lava.png" width="150" alt=""><figcaption></figcaption></figure>

Lava powers a trustless market for RPC data access. The protocol  governs over peer to peer and private Provider-Application pairings,  ensuring high quality RPC service while creating consensus around data served.

**Chain ID**: lava-testnet-1 | **Latest Version Tag**: v0.8.1 | **Wasm**: OFF

[Website](https://lavanet.xyz) | [Discord](https://discord.com/invite/Tbk5NxTCdA) | [Twitter](https://twitter.com/lavanetxyz)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/lava-testnet](https://explorer.kjnodes.com/lava-testnet)

## Public endpoints

* api: [https://lava-testnet.api.kjnodes.com](https://lava-testnet.api.kjnodes.com)
* rpc: [https://lava-testnet.rpc.kjnodes.com](https://lava-testnet.rpc.kjnodes.com)
* grpc: lava-testnet.grpc.kjnodes.com:44090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@lava-testnet.rpc.kjnodes.com:44656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@lava-testnet.rpc.kjnodes.com:44659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/lava-testnet/addrbook.json > $HOME/.lava/config/addrbook.json
```

**live-peers** (19)
```bash
peers="14ae45e7f2ff7491cfa686a8fcac7cc095bc38ff@213.239.217.52:39656,c44a02dba51e23ac06b006fb1285988c89051ce7@85.10.198.171:26556,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,25da069c4dca143029ddae47bf2b7de69c2a8678@65.108.9.164:21156,6ba3b6ec03839afffa64c83e18ff80a681f4968d@65.108.194.40:21756,4e0a2772bb3672e54c2ea655c30abdac62191f14@45.84.138.66:18656,0a528da95ca8025ef4043b6e73f1e789f4102940@176.103.222.22:26656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,3f6d9698d9a5d9fe17afa5968ea652fae478b32f@185.250.37.239:32656,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,433be6210ad6350bebebad68ec50d3e0d90cb305@217.13.223.167:60856,5e068fccd370b2f2e5ab4240a304323af6385f1f@172.93.110.154:27656,ef38861694f07881410c1b1c5852c72050831d68@95.214.55.74:26656,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,1f704611e8aa4a53504fac1b80eb55c876dae8bd@65.108.13.154:30656,ade4d8bc8cbe014af6ebdf3cb7b1e9ad36f412c0@176.9.82.221:19956,e232ba0d11839944d92b9035ef98445a0fb94c9f@95.214.53.37:12656,0735c5a841fe98ee0a74de7cef537c03b4c66a1b@45.89.54.153:26656,4732ed188fbe7603f81d9f4c825397277bb72217@5.75.235.195:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
