# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/lava.png" width="150" alt=""><figcaption></figcaption></figure>

Lava powers a trustless market for RPC data access. The protocol  governs over peer to peer and private Provider-Application pairings,  ensuring high quality RPC service while creating consensus around data served.

**Chain ID**: lava-testnet-1 | **Latest Version Tag**: v0.7.0 | **Wasm**: OFF

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

**live-peers** (39)
```bash
peers="24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,b7274e1274815e898fd52e4724c934820571fb5e@142.132.191.94:16656,c44a02dba51e23ac06b006fb1285988c89051ce7@85.10.198.171:26556,b591ef22e0c2082eb76dcac5ead95be55d01b695@65.109.178.147:26656,194ad0ab2f1003e123085300b0ca16d57e223be8@94.190.90.38:7060,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,377370216f2c003b9d00118ec5373ed21f13aab3@185.16.39.19:35656,c36a4007590af64d3e0a6b4736812ca6f6219561@65.108.9.164:23556,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:27066,95c59c9236f2e1c1c9ee35c6a9cd1b9f2fdc362e@213.239.215.115:29956,9d5802ec3e10fbac150850ffdfa50f324e804b95@95.214.55.62:35656,0eb2dba8e99f29941edaf58974f469635479562f@154.12.245.39:28656,e77870b8732c952f40813e4e622cc2f108fd0223@154.53.55.153:26656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,14ae45e7f2ff7491cfa686a8fcac7cc095bc38ff@213.239.217.52:39656,20c13bd0d972acba5588493fb528b558a0317013@38.242.133.203:26656,f8b7dbce90a7cd73f008ce65218caad40c0f56c6@167.86.115.153:32656,653bb90f4e8a1db9dbbeadd7bd5ae7fd1e1bb7e6@65.108.101.4:23356,7fb838681ff9855a634c7823de605fb4a5d22eba@65.108.144.202:26656,79fc521d683984e166526e74f88296599baf38c3@5.189.189.235:26656,5a469a75fb05eddf2d79fb17063cc59e84d0821a@207.180.236.115:34656,276c73534246fb9ec48d5c72ebd62c42e2f96462@157.90.17.150:26656,112fba64a7e5e27b0cf8f02c634334c957891abf@75.119.146.244:28656,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,0561fed6e88f2167979e379436529861527d859d@65.109.92.148:61256,92638cc11f41a91cdf86d3e1b21c2396d82bcc4a@95.216.26.91:26656,bb8c8cea499a1fa7e97922b5a9882c2360c6575a@176.103.222.21:26656,5278e834cc67ce1e06ebfc921e37d413a9d40830@65.108.65.36:11656,cb722cc36541920d3907cd67743db5444f53e80b@95.70.184.178:24656,ac99b8d7f3d863baa09cf6378057b78c4f02d029@91.233.173.45:26656,0adbe1e790b58d19cc53a9839059a95d7d5d7aba@65.109.70.23:19956,dd01ee232917a1af8bf917b9b5fadd5b5b127d99@65.108.133.101:26656,4e96723af8feb8a515573a7b9391e7bf7d562480@194.163.162.155:26656,0efa60456219f5b7847ee21439aa8662c0a8e1b6@65.21.195.40:26056,47385d0a7051109de5342e3b27890c4a4b9e0763@65.108.72.233:16656,6b7bfa6f0297b231f40a9284d45282af93320315@65.109.116.50:28656,ade4d8bc8cbe014af6ebdf3cb7b1e9ad36f412c0@176.9.82.221:19956,ab924e7944c332bd1b52c8733e262bbdd33cb5ac@116.202.165.53:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
