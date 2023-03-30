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

**live-peers** (36)
```bash
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,bb8c8cea499a1fa7e97922b5a9882c2360c6575a@176.103.222.21:26656,6ba3b6ec03839afffa64c83e18ff80a681f4968d@65.108.194.40:21756,013f0163d37428ed99eacd8ee84059da5c243981@5.161.132.217:26656,ed780f77754e8c4657b145144f0f95225d43bb03@65.108.224.156:27656,5bdbd9a68d212ec341c781cc553043486ce5b8ee@31.220.76.135:26656,9057ee9d3d9b3c42c184dc89a7b2a07026b81a45@31.220.76.131:26656,c36a4007590af64d3e0a6b4736812ca6f6219561@65.108.9.164:23556,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,57474bd0977b3ed65cf23086b6d1d92bf00d50d0@207.180.236.122:31656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,0d6983bcd192c0b4a0f61e6d849c152704e2f017@91.107.148.5:26656,1f704611e8aa4a53504fac1b80eb55c876dae8bd@65.108.13.154:30656,14ae45e7f2ff7491cfa686a8fcac7cc095bc38ff@213.239.217.52:39656,5a469a75fb05eddf2d79fb17063cc59e84d0821a@207.180.236.115:34656,d6a116d2aed64bd2f383b894e38f2a62232e44b7@116.202.161.165:36656,6b1d0465b3e2a32b5328e59eb75c38d88233b56f@80.82.215.19:60656,07c557b393b235a7b004a4a32831e54092dc24a0@91.107.147.250:26656,15480dd0fcccdf317d11993ff4c5d0098bc48a47@78.46.106.75:11656,c40a7bc3c7aee0428273c0bfa75fcb14bf0f44c4@65.109.90.171:30656,c32d101819cedf78ea986e6d832e2306fb6d0649@185.248.24.224:16656,d9703df8c0e5eef6c0766217d611a13ed6ee8d95@88.99.33.248:26656,71fb615c968e6ea9458d065d71d47dd1bb10d11e@185.205.246.203:36656,7efe22c915d7bf814df232f74466142b3099fa34@185.169.252.65:26656,64df498c92b9ccaf78012229d399aa34a014f087@65.109.122.105:56659,b1806dfabc9bb5fb721b3f82628a3fb23a2ad786@65.109.65.248:30656,e38146de8800082110878c0521fd3ee5f93b70d6@194.163.177.203:26656,5e068fccd370b2f2e5ab4240a304323af6385f1f@172.93.110.154:27656,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,0adbe1e790b58d19cc53a9839059a95d7d5d7aba@65.109.70.23:19956,433be6210ad6350bebebad68ec50d3e0d90cb305@217.13.223.167:60856,6b7bfa6f0297b231f40a9284d45282af93320315@65.109.116.50:28656,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:27066,9d5802ec3e10fbac150850ffdfa50f324e804b95@95.214.55.62:35656,377370216f2c003b9d00118ec5373ed21f13aab3@185.16.39.19:35656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
