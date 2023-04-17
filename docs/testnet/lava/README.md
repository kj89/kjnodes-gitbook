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

**live-peers** (23)
```bash
peers="14ae45e7f2ff7491cfa686a8fcac7cc095bc38ff@213.239.217.52:39656,6ba3b6ec03839afffa64c83e18ff80a681f4968d@65.108.194.40:21756,e3c92ba5f1ebd8bec0ab9431eb183ed9864eca87@65.108.231.238:46656,e5aff8690b3fc34f81c1792d56ba5d182cce68e9@65.109.116.204:21156,1134ffe4fb3e39dba3ebc1e0eede7cc160e8e2d9@42.114.91.170:26656,25da069c4dca143029ddae47bf2b7de69c2a8678@65.108.9.164:21156,92f8e4caaadb2f00c95e03068933f2045a93e910@65.109.65.163:21156,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,704db28ae8082ed936675e8eea9b5a71ba946241@18.212.181.61:26656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,5e068fccd370b2f2e5ab4240a304323af6385f1f@172.93.110.154:27656,15480dd0fcccdf317d11993ff4c5d0098bc48a47@78.46.106.75:11656,f9190a58670c07f8202abfd9b5b14187b18d755b@144.76.97.251:27656,ef38861694f07881410c1b1c5852c72050831d68@95.214.55.74:26656,9057ee9d3d9b3c42c184dc89a7b2a07026b81a45@31.220.76.131:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,fb2b9d41678f3d1c9c0bdef1a87f2037b6b0088a@146.19.24.252:26666,24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,433be6210ad6350bebebad68ec50d3e0d90cb305@217.13.223.167:60856,944389dd08321247c8ad687d904591a3d73d16c6@173.249.38.130:26656,bb8c8cea499a1fa7e97922b5a9882c2360c6575a@176.103.222.21:26656,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,7adc61737172235479b405f61477a02be635fb21@62.171.188.69:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
