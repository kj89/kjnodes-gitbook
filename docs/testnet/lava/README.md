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

**live-peers** (38)
```bash
peers="24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,0d6983bcd192c0b4a0f61e6d849c152704e2f017@91.107.148.5:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:27066,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,149f9f017344ce9cebb637baa7cab57a28f3a8c3@86.111.48.159:26656,3f6d9698d9a5d9fe17afa5968ea652fae478b32f@185.250.37.239:32656,c36a4007590af64d3e0a6b4736812ca6f6219561@65.108.9.164:23556,e3c92ba5f1ebd8bec0ab9431eb183ed9864eca87@65.108.231.238:46656,0a78dd75926983ba06de451480673487ffa1bcc1@199.175.98.106:26656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,653bb90f4e8a1db9dbbeadd7bd5ae7fd1e1bb7e6@65.108.101.4:23356,8cd81b9119e4aa45fe549dd12543de862457c989@38.242.155.47:26656,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,d1730b774b7c1d52dd9f6ae874a56de958aa147e@65.109.15.19:26656,8a20f8f798c5073f0867812e691f54b5cd0dd65d@109.123.242.188:26656,9d5802ec3e10fbac150850ffdfa50f324e804b95@95.214.55.62:35656,5ab0449599aabcf90f664003c2ef1510ecd33b1b@65.21.203.204:11656,5f04e56cabc20ab2e94b03022f024a310dfdf840@85.10.198.169:11656,67ba50d49201090cb09c4d03be2c8db50be2f437@95.217.167.118:26656,bf7aef75c35725f89f31c12197100a1dd91b3174@146.190.47.103:26656,f0501090b870f7796dfdd1f1f5479aec2baecfe8@88.198.52.89:11656,b7274e1274815e898fd52e4724c934820571fb5e@142.132.191.94:16656,a20e24a251c9e6325a7c1e05d6a479bcd9c721ac@168.119.52.60:26656,b36a39d183383fa068f0db145b179bf8455a06f4@38.242.159.214:26656,7adc61737172235479b405f61477a02be635fb21@62.171.188.69:26656,ef6e9620807e7e4614fd8e02722f8075ec277544@199.175.98.122:26656,7e851a5714dff9276bd5a73b4d5c64bab6b1faca@135.181.16.252:33656,5676c8606f23471e220f8bf7317498a61bb93194@65.21.134.202:26686,dd01ee232917a1af8bf917b9b5fadd5b5b127d99@65.108.133.101:26656,4e96723af8feb8a515573a7b9391e7bf7d562480@194.163.162.155:26656,1f704611e8aa4a53504fac1b80eb55c876dae8bd@65.108.13.154:30656,0efa60456219f5b7847ee21439aa8662c0a8e1b6@65.21.195.40:26656,c13b120d588c86008dc4ea5e3633b93c01831124@80.79.5.171:31656,6b7bfa6f0297b231f40a9284d45282af93320315@65.109.116.50:28656,a2afdc48785be73f208af349e78d632b5556cc01@5.75.226.151:26656,370ae92bd28701e0c1d8dc912ccf0d40fe0db3d5@157.90.245.166:26656,ab924e7944c332bd1b52c8733e262bbdd33cb5ac@116.202.165.53:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
