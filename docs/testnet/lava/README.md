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
peers="24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,3be826c2d20009f17d067833a2adfd679b19394d@65.21.170.3:34656,6ba3b6ec03839afffa64c83e18ff80a681f4968d@65.108.194.40:21756,d1772004f29d81f4c7cbb62ea71d2f230643abfb@65.108.150.175:24003,5a469a75fb05eddf2d79fb17063cc59e84d0821a@207.180.236.115:34656,7adc61737172235479b405f61477a02be635fb21@62.171.188.69:26656,14ae45e7f2ff7491cfa686a8fcac7cc095bc38ff@213.239.217.52:39656,f9af0186eec9a88a5a657deb9a7deff34c05d99f@86.111.48.156:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:27066,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,bfe21dd5af98aa42d213cd5bd943162a36b0505f@92.243.165.98:26656,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,dfa93668152cb6b3a822c987f9c22110a1c2f314@178.18.255.221:26656,194ad0ab2f1003e123085300b0ca16d57e223be8@94.190.90.38:7060,22c51515eea1df09dc872dc8843efb7fc73770b1@199.175.98.102:26656,6b1d0465b3e2a32b5328e59eb75c38d88233b56f@80.82.215.19:60656,20c13bd0d972acba5588493fb528b558a0317013@38.242.133.203:26656,6171a52cf0ffc1706409d2dcec56c1db81c86aae@176.103.222.17:26656,d64aa8f4d864daac54639cd1fdebbf4c464ba4f1@5.75.235.206:26656,0e9062ed560ce78eba346f1d73ae3ca9eeea5985@142.132.248.253:24656,bb8c8cea499a1fa7e97922b5a9882c2360c6575a@176.103.222.21:26656,c32d101819cedf78ea986e6d832e2306fb6d0649@185.248.24.224:16656,29095bea094a78e3396f32535fa3fc6df9484f66@65.109.139.182:20656,0df9cc98fd8e88920efd02425292813108e14a45@185.202.238.214:26656,1a18bdd0c259d604cda023a5e03eba2a25f5c045@94.19.249.187:27656,74a979f0df53ef6f2ba9ab77c0c9fc5ba9c2bdc5@213.239.215.59:29456,47385d0a7051109de5342e3b27890c4a4b9e0763@65.108.72.233:16656,230648adf4aa55029c72ec5d7bc1be59529acf34@37.120.171.159:26656,472cd387bb2cc7feb51d7aa489dc920de1eff5d7@185.209.230.222:26656,8b774eabd1b4fbffdf9d14fba3d4a1690c69d0ad@65.109.24.227:30656,74ce58215cecca7a96c946b3cad6bbc282df9fa3@80.76.235.194:7064,c13b120d588c86008dc4ea5e3633b93c01831124@80.79.5.171:31656,fcd5a8f4aebc4c7100573914b7974a35cd389963@5.9.69.253:20656,bc2e99e6004bb0b87c72ca10f20cd1617edf70fe@141.94.73.93:56656,7546454d0cd3075d6cd73b0384ed1d9413ca477c@93.100.232.183:38656,31550f0ec97d7148b2dae0de2a02240f88d1cfcf@85.114.134.219:12656,a2afdc48785be73f208af349e78d632b5556cc01@5.75.226.151:26656,6b7bfa6f0297b231f40a9284d45282af93320315@65.109.116.50:28656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
