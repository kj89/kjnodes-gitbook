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

**live-peers** (21)
```bash
peers="24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,beaedffb147f5908523589c212c971c292fef46c@65.108.226.101:28656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,25da069c4dca143029ddae47bf2b7de69c2a8678@65.108.9.164:21156,6ba3b6ec03839afffa64c83e18ff80a681f4968d@65.108.194.40:21756,ba78f0ac713d5e7a0274ef593674dae337aabbee@176.103.222.18:26656,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,1a18bdd0c259d604cda023a5e03eba2a25f5c045@94.19.249.187:27656,125935f63c123b6891b014ffc071fbf781270771@23.88.74.54:11656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,e3c92ba5f1ebd8bec0ab9431eb183ed9864eca87@65.108.231.238:46656,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,ed780f77754e8c4657b145144f0f95225d43bb03@65.108.224.156:27656,47385d0a7051109de5342e3b27890c4a4b9e0763@65.108.72.233:16656,942ca9d454ff241806e40e466533bf4ad1235eaa@46.4.53.208:36656,112fba64a7e5e27b0cf8f02c634334c957891abf@75.119.146.244:28656,0516c4d11552b334a683bdb4410fa22ef7e3f8ba@65.21.239.60:11656,d6a116d2aed64bd2f383b894e38f2a62232e44b7@116.202.161.165:36656,a2afdc48785be73f208af349e78d632b5556cc01@5.75.226.151:26656,fd8ea335ddad4a793d9dbbd9b3b70ec99d6a3331@161.97.139.208:26656,14ae45e7f2ff7491cfa686a8fcac7cc095bc38ff@213.239.217.52:39656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
