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

**live-peers** (40)
```bash
peers="3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,c36a4007590af64d3e0a6b4736812ca6f6219561@65.108.9.164:23556,6ba3b6ec03839afffa64c83e18ff80a681f4968d@65.108.194.40:21756,397056c8cd7e2fce451d4f8e34ef24c0c9ffacba@176.9.44.113:26676,10c4405d04b2a221959de97f69c9a6258676f55d@161.97.79.100:26656,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,013f0163d37428ed99eacd8ee84059da5c243981@5.161.132.217:26656,14ae45e7f2ff7491cfa686a8fcac7cc095bc38ff@213.239.217.52:39656,a0476bc75ad2ade9ce8a6b2cd41ef646d3a2e3ee@85.10.193.246:28656,6b1d0465b3e2a32b5328e59eb75c38d88233b56f@80.82.215.19:60656,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,641426069e0de5daa02877db8c1d6854d7f59464@31.220.72.179:26656,5bdbd9a68d212ec341c781cc553043486ce5b8ee@31.220.76.135:26656,7efe22c915d7bf814df232f74466142b3099fa34@185.169.252.65:26656,32d0eaa31ab8f9c2779ce9272b7a68f3d15a8e6e@213.239.207.175:40656,8cd81b9119e4aa45fe549dd12543de862457c989@38.242.155.47:26656,525696e557db51c4d5f5bca1d7152753c7426c2e@34.192.150.110:26656,ac7cefeff026e1c616035a49f3b00c78da63c2e9@18.215.128.248:26656,d6a116d2aed64bd2f383b894e38f2a62232e44b7@116.202.161.165:36656,5a469a75fb05eddf2d79fb17063cc59e84d0821a@207.180.236.115:34656,c32d101819cedf78ea986e6d832e2306fb6d0649@185.248.24.224:16656,71fb615c968e6ea9458d065d71d47dd1bb10d11e@185.205.246.203:36656,c40a7bc3c7aee0428273c0bfa75fcb14bf0f44c4@65.109.90.171:30656,fb2b9d41678f3d1c9c0bdef1a87f2037b6b0088a@146.19.24.252:26666,d796c20b5bdb8f1633c2a13afbf12314a77b668c@91.107.148.113:26656,433be6210ad6350bebebad68ec50d3e0d90cb305@217.13.223.167:60856,dfa93668152cb6b3a822c987f9c22110a1c2f314@178.18.255.221:26656,35f045092f9c51ab743eec194438b91ecf8ce69e@65.109.116.22:11134,0adbe1e790b58d19cc53a9839059a95d7d5d7aba@65.109.70.23:19956,1a53822aace8a2fded042da7b31cf6824cae4590@195.14.6.2:26656,5e068fccd370b2f2e5ab4240a304323af6385f1f@172.93.110.154:27656,f68c57ca955420779773f9320a6b7710c2b29f73@188.191.36.222:26656,24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,b043a968059a60026988045fdd543c10b2756d6d@79.137.206.77:26656,5f04e56cabc20ab2e94b03022f024a310dfdf840@85.10.198.169:11656,47385d0a7051109de5342e3b27890c4a4b9e0763@65.108.72.233:16656,2e0d035852dcdc9c5c52f74a11bd2da6fb8de64f@185.185.82.30:26656,9057ee9d3d9b3c42c184dc89a7b2a07026b81a45@31.220.76.131:26656,d1730b774b7c1d52dd9f6ae874a56de958aa147e@195.201.76.69:36656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
