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

**live-peers** (28)
```bash
peers="035d086cc418352aba9e679e079f17391791ccc6@178.208.252.54:27656,24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,6ba3b6ec03839afffa64c83e18ff80a681f4968d@65.108.194.40:21756,25da069c4dca143029ddae47bf2b7de69c2a8678@65.108.9.164:21156,fd8ea335ddad4a793d9dbbd9b3b70ec99d6a3331@161.97.139.208:26656,4732ed188fbe7603f81d9f4c825397277bb72217@5.75.235.195:26656,d6a116d2aed64bd2f383b894e38f2a62232e44b7@116.202.161.165:36656,a724b94c593241890022e204e0065d8baa67168c@116.202.227.117:44656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,47385d0a7051109de5342e3b27890c4a4b9e0763@65.108.72.233:16656,194ad0ab2f1003e123085300b0ca16d57e223be8@94.190.90.38:7060,b7274e1274815e898fd52e4724c934820571fb5e@142.132.191.94:16656,ce9d3196936a1071c6a95ceb7c5e3c9a3d3512aa@91.225.201.81:26656,34271a6f82d755777a3db02be39e575bf4ebd415@65.109.30.197:28656,9057ee9d3d9b3c42c184dc89a7b2a07026b81a45@31.220.76.131:26656,d46383ede52ee8b12f153c627fa1b8abbf86d84e@95.6.28.8:26656,7adc61737172235479b405f61477a02be635fb21@62.171.188.69:26656,433be6210ad6350bebebad68ec50d3e0d90cb305@217.13.223.167:60856,5a469a75fb05eddf2d79fb17063cc59e84d0821a@207.180.236.115:34656,0322670e17a172f25fec71f274f2bd28d1b7e74f@185.163.64.143:26656,a2afdc48785be73f208af349e78d632b5556cc01@5.75.226.151:26656,e0f25590f8074b4ea70f069f9be332b19f81f344@23.88.70.109:15656,c44a02dba51e23ac06b006fb1285988c89051ce7@85.10.198.171:26556,8b154033143fdedf4835dfc7b030c7d781bfd54e@195.201.219.227:26656,a5c8394322e22b986099484afb543031152c3a5d@176.120.177.123:26656,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
