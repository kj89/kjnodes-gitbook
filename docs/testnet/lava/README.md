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

**live-peers** (24)
```bash
peers="24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,14ae45e7f2ff7491cfa686a8fcac7cc095bc38ff@213.239.217.52:39656,0a528da95ca8025ef4043b6e73f1e789f4102940@176.103.222.22:26656,9057ee9d3d9b3c42c184dc89a7b2a07026b81a45@31.220.76.131:26656,6ba3b6ec03839afffa64c83e18ff80a681f4968d@65.108.194.40:21756,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,25da069c4dca143029ddae47bf2b7de69c2a8678@65.108.9.164:21156,79fc521d683984e166526e74f88296599baf38c3@5.189.189.235:26656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,3f6d9698d9a5d9fe17afa5968ea652fae478b32f@185.250.37.239:32656,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,ef38861694f07881410c1b1c5852c72050831d68@95.214.55.74:26656,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,31478ee0c0521c7cfb3312b86ef490936b5ceb80@65.109.92.240:197,194ad0ab2f1003e123085300b0ca16d57e223be8@94.190.90.38:7060,4bb3bb98ca32b5a0f82d445e60065601bb93a38c@86.111.48.163:26656,4fc42fdf634ef542094c7a44f22e031acea61162@91.77.165.172:27656,5ed48f1abdd16d62f2179af31af3789ac5a42ecc@34.142.220.216:37656,433be6210ad6350bebebad68ec50d3e0d90cb305@217.13.223.167:60856,9df7c85f32839e48af8f490a316990af594d5068@62.210.201.72:26656,14110234a060fc0d9568fb43a32c8b6b0f0f8cc2@65.108.240.151:26656,8d949ac905cf8aa6902a72c8c1fb6bda5a7c4d69@65.108.200.60:21656,b58316584360b072fa08a11df5971a7bec29512f@93.100.234.101:26656,e232ba0d11839944d92b9035ef98445a0fb94c9f@95.214.53.37:12656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
